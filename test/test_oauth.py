import unittest
from src.parser.oauthparser import OauthParser

class TestOauth(unittest.TestCase):
 
    def test_parse_oauth_from_code_request(self):    
        # arrange
        parser = OauthParser()
        response = """{"access_token": "mbg0lge6ry8z030kmrj893f9xal8g5", "refresh_token": "mbg0lge6ry8z030kmrj893f9xal8g5", "expires_in": 23412, "scope": ["channel:read:redemptions chat:read channel_subscriptions whispers:read"], "token_type": "bearer"}"""

        # act
        result = parser.parse_new_oauth_response(response)

        # assert
        self.assertTrue(result.authtoken)
        self.assertTrue(result.refreshtoken)
        