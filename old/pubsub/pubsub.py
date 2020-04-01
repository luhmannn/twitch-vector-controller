import websockets
import logging
import asyncio
import json

log = logging.getLogger(__name__)


class Pubsub:
    
    def __init__(self, loop: asyncio.BaseEventLoop):
        self.loop = loop
        self._socket = None
        self._listener = None
    
    
    async def connect(self):
        try:
            log.info('Attempting to connect to websocket')
            self.socket = await websockets.connect('wss://pubsub-edge.twitch.tv')
        except Exception as err:
            log.error('Websocket connetion failed: %s', e)
            
        log.info('Connection established')
        
        self._listener = self.loop.create_task(self.listen())
        
    
    async def listen(self):
        while True:
            try:
                data = json.loads(await self._socket.recv())
                self.loop.create_task(self.)
                

