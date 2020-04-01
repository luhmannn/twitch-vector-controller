import logging
from src.celery.tasks import vector_say


class Subscription():
    
    def __init__(self):
        pass
    
    async def perform(self, name, months, message):
        logging.debug('Attempting to perform sub actions with: name=%s - months=%s - message=%s' % (name, months, message))      
        await vector_say.delay(message)      
        return True
                
    