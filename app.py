import os
from src.oauth import Oauth
from src.util.db import DB
from src.twitchenv import TwitchEnvironment
from src.parser.oauthparser import OauthParser
from src.bot import Bot
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
from src.logging import Logging
from src.actions.actionresolver import ActionResolver
from src.responsehandler import ResponseFilter
from src.celery.tasks import vector_say

if __name__ == "__main__":
    
    # setup logging
    Logging()

    # setup db
    db = DB('./vector.db')
    
    # get env settings
    twitchenv = TwitchEnvironment()
    
    # prepare oauth 
    oauthParser = OauthParser()
    oauth = Oauth(db, twitchenv, oauthParser)
    
    actions = ActionResolver()
    response_filter = ResponseFilter(actions, oauth)
    
    # run the bot
    bot = Bot(oauth, twitchenv, response_filter)
    bot.run()
    
    
    