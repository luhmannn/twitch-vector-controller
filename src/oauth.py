import requests

class Oauth():

    def __init__(self, db, twitchenv, parser):
        self.db = db
        self.twitchenv = twitchenv
        self.parser = parser

    async def get_token(self):
        token = await self.ensureToken()
        return token

    async def refresh_token(self):
        retry_count = await self.get_retry_count()
        if (retry_count < 10):
            print("Oauth: attempting to refresh token")
            refresh_token = await self.get_refresh_token()
            
            try:
                tokenset = await self.refresh_oauth_token(refresh_token, self.twitchenv.get_twitch_client_id(), self.twitchenv.get_twitch_client_secret())
                if (tokenset):
                    
                    await self.reset_retry_count()
                    
                    self.db.set('oauth-token', tokenset.authtoken) 
                    self.db.set('refresh-token', tokenset.refreshtoken)   
                
                    return tokenset.authtoken
                
            except Exception as err:
                await self.increment_retry_count()
                print("Refresh token failed.")
        else:
            print("Too many retries, exiting.")
        
    async def get_retry_count(self):
        retry_count = self.db.get('retry-count')
        if not retry_count:
            retry_count = 0
            self.db.set('retry-count', retry_count)
        return int(retry_count)

    async def reset_retry_count(self):
        self.db.set('retry-count', 0)

    async def increment_retry_count(self):
        retry_count = await self.get_retry_count()
        retry_count += 1
        self.db.set('retry-count', retry_count)

    async def get_refresh_token(self):
        return self.db.get('refresh-token')
    

    async def refresh_oauth_token(self, refresh_token, client_id, client_secret):
        url = 'https://id.twitch.tv/oauth2/token?grant_type=refresh_token&refresh_token=%s&client_id=%s&client_secret=%s' % (refresh_token, client_id, client_secret)
        response = requests.post(url)
        tokenset = self.parser.parse_new_oauth_response(response)
        return tokenset        

    async def get_oauth_token_from_code(self, client_id, client_secret, code):
        url = 'https://id.twitch.tv/oauth2/token?client_id=%s&client_secret=%s&code=%s&grant_type=authorization_code&redirect_uri=http://localhost' % (client_id, client_secret, code)
        response = requests.post(url)
        tokenset = self.parser.parse_new_oauth_response(response)
        return tokenset

    async def ensureToken(self):
        token = self.db.get('oauth-token')
        if not token:
            try:
                tokenset = await self.get_oauth_token_from_code(
                    self.twitchenv.get_twitch_client_id(),
                    self.twitchenv.get_twitch_client_secret(),
                    self.twitchenv.get_twitch_code())

                if (tokenset):
                    self.db.set('oauth-token', tokenset.authtoken) 
                    self.db.set('refresh-token', tokenset.refreshtoken)   
                    return tokenset.authtoken

            except Exception as err:
                print('Could not get token: %s' % err)
                return False
        
        return token
        
