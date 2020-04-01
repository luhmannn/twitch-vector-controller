import logging
from src.actions.sub import Subscription

class ResponseFilter():
    
    def __init__(self, actionresolver, oauth):
        self.actionresolver = actionresolver
        self.oauth = oauth
    
    async def handle_bad_auth_response(self, response, referer):

        if (response.get('type') == "RESPONSE" and response.get('error') == "ERR_BADAUTH"):
        
            # we assume this is because our token has expired
            # refresh
            newtoken = await self.oauth.refresh_token()
            
            # set new token on this class (already saved in db)
            referer.current_token = newtoken 
            
            # try to subscribe again
            await referer.subscribe_to_topics()
            
        
    async def handle_topic_subscription_response(self, response):
        logging.debug("Inside handle sub response: %s" % response)
        
        _type = response.get('type')
        data = response.get('data')
        
        if data:
            topic = data.get('topic')
            if topic:  
                if (_type == "MESSAGE" and topic.startswith('channel-subscribe-events-v1')):
                    logging.debug("We got a subscriber, will run sub actions now") 
                    
                    message = response.get('data').get('message')
                    name_of_sub = message.get('user_name')
                    months = message.get('cumulative-months')
                    sub_message = message.get('sub_message').get('message')
                    action = message.get('context')
                    
                    action = self.actionresolver.get(action)
                    await action.perform(name_of_sub, months, sub_message)
                    
                    return True
        
        return False
    
    async def handle_topic_channelpoint_response(self, response):
        logging.debug("Inside handle channelpoint response: %s" % response)
        
        _type = response.get('type')
        
        if(_type and _type == "reward-redeemed"):
            
            redemption = response.get('data').get('redemption')
            
            user_input = redemption.get('user_input')
            user_name = redemption.get('user').get('display_name')
            
            reward = redemption.get('reward')            
            
            title = reward.get('title')
            
            channel_point_action = self.actionresolver.get(title)  
            await channel_point_action.perform(user_input)
            
            return True
            
            