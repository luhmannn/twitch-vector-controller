import os
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
import logging

class Logging():
    
    def __init__(self):
        
        logging.basicConfig(level=logging.DEBUG)
        
        level = int(os.getenv('LOGLEVEL', ''))
        event_level = int(os.getenv('EVENTLEVEL', ''))
        sentry_dsn = os.getenv('SENTRY_DSN', '')
        
        sentry_logging = LoggingIntegration(
            level=level, 
            event_level=event_level 
        )

        sentry_sdk.init(
            dsn=sentry_dsn,
            integrations=[sentry_logging]
        )