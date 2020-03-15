import socket

class Chatbot():

    def __init__(self, host, port, parser, oauth, name, channel, actionresolver):
        self.host = host
        self.port = port
        self.oauth = oauth
        self.name = name
        self.channel = channel
        self.parser = parser
        self.actions = actionresolver
        self.twitch = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.run()

    def run(self):
        self.connect_to_twitch()
        self.authenticate(self.oauth, self.name)
        self.join_channel(self.channel)
        self.recieve_messages()
    
    def connect_to_twitch(self):
        try:
            self.twitch.connect((self.host, self.port))
            print ("Connected to %s:%s" % (self.host, self.port))
        except Exception as err:
            print ("Could not connect to %s:%s" % (self.host, self.port))
            print ( err )

    def authenticate(self, oauth, name):
        try:
            self.twitch.send(('PASS %s\r\n' % oauth).encode('utf-8'))
            self.twitch.send(('NICK %s\r\n' % name).encode('utf-8'))
            self.twitch.send(('USER %s 0 * %s\r\n' % (name,name)).encode('utf-8'))
            print ("Is authenticated")
        except Exception as err:
            print ("Could not authenticate")
            print (err)

    def join_channel(self, channel):
        try:
            self.twitch.send(('JOIN #%s\r\n' % channel).encode('utf-8'))
            print ("Joined channel #%s" % channel)
        except Exception as err:
            print ("Could not join channel %s" % channel)

    def write_in_channel(self, channel, message):
        try:
            self.twitch.send(('PRIVMSG #%s :%s\r\n' % (channel, message)).encode('utf-8'))
        except Exeption as err:
            print ("Could not write in chat")
            print (err)

    def recieve_messages(self):
        while True:
            data = self.twitch.recv(4096).decode()
            self.handle_messages(data)

    def handle_messages(self, data):
        message = self.parser.parse(data)
        if message:       

            command = message['command'][0]
            value = message['command'][1]

            print ('%s - %s' % (command, value))

            action = self.actions.get(command)
            if (action):
                try:
                    action.perform(value)
                except Exception as err:
                    print(err)






    