class ResponseBadAuth:

    def __init__(self, oauth):
        self.oauth = oauth

    def perform(self, referer, connection):
        oauth.refresh_token()
        referer.on_open(referer)