from twitchio.ext import commands

class Bot(commands.Bot):

    def __init__(self, oauth, env, filter):
        self.oauth = oauth
        
        self.topics = env.get_twitch_topics()
        self.channels = env.get_twitch_channels()
        self.current_token = None
        self.client_id = env.get_twitch_client_id()
        self.irc_token = env.get_twitch_irc_token()
        self.nick = env.get_twitch_nick()
        self.prefix = env.get_twitch_prefix()
        self.filter = filter
        
        super().__init__(
            api_token=self.current_token,
            irc_token=self.irc_token, 
            client_id=self.client_id, 
            nick=self.nick, 
            prefix=self.prefix,
            initial_channels=[self.channels])

    async def event_ready(self):
        self.current_token = await self.oauth.get_token()
        
        try:    
            await self.subscribe_to_topics()
            
            print(f'Ready | {self.nick}')
        except Exception as e:
            print(e)
        
    async def event_raw_pubsub(self, response):        
        # Handle badauth-response
        should_resubscribe = await self.filter.handle_bad_auth_response(response, self)
        
        # Handle subscription topic response
        await self.filter.handle_topic_subscription_response(response)
        
        # Handle channel-point subscription response
        await self.filter.handle_topic_channelpoint_response(response)        
        
        
    async def event_error(self, error: Exception, data=None):
        print(error)

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)
        
    async def subscribe_to_topics(self):
        await super().pubsub_subscribe(self.current_token, self.topics)

    @commands.command(name='vectorsay')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')

