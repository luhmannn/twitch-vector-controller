import asyncio

class PubSubPool:
    
    MAX = 10
    
    def __init__(self, loop: asyncio.BaseEventLoop, base):
        self.loop = loop
        self.base = base
        self.connections = {}
        
        