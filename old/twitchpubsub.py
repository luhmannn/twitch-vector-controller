import websocket
import time
import _thread as thread
import json

class TwitchPubSub():

    def __init__(self, oauth, parserSelector, pubsubActionResolver):
        self.oauth = oauth
        self.parserSelector = parserSelector
        self.actions = pubsubActionResolver
        self.pong_ok = True
        self.last_ping = None
        self.current_loop = None
        self.twitch = None

    def on_message(self, message):
        msg = json.loads(message)
        messageType = msg.get('type')

        parser = self.parserSelector.get_parser(messageType)
        response = parser.parse(message)

        action = self.actions.get(messageType, response)
        if action:
            action.perform(self, twitch)

        print(response.responsetype)

    def on_error(self, message):
        print(message)

    def on_close(self):
        print("** CLOSED **")

    def on_open(self):
        print("Running connection open method")   
        self.current_loop = thread.start_new_thread(self.run, (twitch,))
        thread.start_new_thread(self.keep_alive, (twitch,))
        
    def run(self, *args):
        time.sleep(1)
        
        oauth_token = self.oauth.get_token()        
        payload = {
                    "type": "LISTEN",
                    "nonce": "44h1k13746815ab1r2",
                    "data": {
                        "topics": ["whispers.121074828"],
                        "auth_token": oauth_token

                    }
                }
        
        self.twitch.send(json.dumps(payload))
        
    def keep_alive(self, *args):
        time.sleep(1)
        
        while True:
            
            # If we didn't get a PONG within 10 secs from last ping
            if (not self.pong_ok and time.time() > self.last_ping + 10):
                print ("*** Reconnect ***")
                self.pong_ok = True
                self.connect()
                       
            if (self.last_ping == None or time.time() > self.last_ping + 60*5):
                print ("*** PING ***")
                payload = {
                            "type": "PING"
                        }
                self.twitch.send(json.dumps(payload))
                self.last_ping = time.time()
                self.pong_ok = False
                
        self.last_ping = time.time()

    def connect(self):
        try:
            websocket.enableTrace(True)

            self.twitch = websocket.WebSocketApp("wss://pubsub-edge.twitch.tv",
                                on_message = lambda message: self.on_message(message),
                                on_error = lambda message: self.on_error(message), 
                                on_close = lambda : self.on_close(), 
                                on_open = lambda : self.on_open())

            self.twitch.run_forever()

        except Exception as err:
            print ('Pubsub websocket connection failed: %s', err)

    def register_pong():
        self.last_pong = datetime.now()
        
    def thread_for_ident(ident):
        return threading._active.get(ident)