class Reconnect:

    def __init__(self, oauth):
        self.oauth = oauth

    def perform(self, referer, connection):
        referer.run(connection)