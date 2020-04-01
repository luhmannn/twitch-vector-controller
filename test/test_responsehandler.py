import unittest
from src.responsehandler import ResponseFilter
import aiounittest
import json
from src.actions.actionresolver import ActionResolver
from src.oauth import Oauth
from src.parser.oauthparser import OauthParser
from src.twitchenv import TwitchEnvironment
from src.util.db import DB

class TestResponseHandler(aiounittest.AsyncTestCase):
 
    async def test_sub_response_handling(self):    
        # arrange
        actions = ActionResolver()
        twitchenv = TwitchEnvironment()
        oauthParser = OauthParser()
        db = DB('./vector.db')
        oauth = Oauth(db, twitchenv, oauthParser)
        
        filter = ResponseFilter(actions, oauth)
        
        # example response from https://dev.twitch.tv/docs/pubsub
        response = r"""{
                        "type": "MESSAGE",
                        "data": {
                            "topic": "channel-subscribe-events-v1.44322889",
                            "message": {
                                "user_name": "dallas",
                                "display_name": "dallas",
                                "channel_name": "twitch",
                                "user_id": "44322889",
                                "channel_id": "12826",
                                "time": "2015-12-19T16:39:57-08:00",
                                "sub_plan": "Prime",
                                "sub_plan_name": "Channel Subscription (mr_woodchuck)",
                                "cumulative-months": 9,
                                "streak-months": 3,
                                "context": "sub",
                                "sub_message": {
                                    "message": "A Twitch baby is born! KappaHD",
                                    "emotes": [
                                    {
                                        "start": 23,
                                        "end": 7,
                                        "id": 2867
                                    }]
                                }
                            }
                        }
                        }"""

        # act
        result = await filter.handle_topic_subscription_response(json.loads(response))

        # assert
        self.assertTrue(result)

    async def test_channel_point_handling(self):
        # arrange
        actions = ActionResolver()
        twitchenv = TwitchEnvironment()
        oauthParser = OauthParser()
        db = DB('./vector.db')
        oauth = Oauth(db, twitchenv, oauthParser)
        
        filter = ResponseFilter(actions, oauth)
        
        # example response from https://dev.twitch.tv/docs/pubsub
        response = r"""{
                        "type": "reward-redeemed",
                        "data": {
                            "timestamp": "2019-11-12T01:29:34.98329743Z",
                            "redemption": {
                                "id": "9203c6f0-51b6-4d1d-a9ae-8eafdb0d6d47",
                                "user": {
                                    "id": "30515034",
                                    "login": "davethecust",
                                    "display_name": "davethecust"
                                    },
                                "channel_id": "30515034",
                                "redeemed_at": "2019-12-11T18:52:53.128421623Z",
                                "reward": {
                                    "id": "6ef17bb2-e5ae-432e-8b3f-5ac4dd774668",
                                    "channel_id": "30515034",
                                    "title": "Make Vector Speak",
                                    "prompt": "cleanside's finest \n",
                                    "cost": 10,
                                    "is_user_input_required": true,
                                    "is_sub_only": false,
                                    "image": {
                                        "url_1x": "https://static-cdn.jtvnw.net/custom-reward-images/30515034/6ef17bb2-e5ae-432e-8b3f-5ac4dd774668/7bcd9ca8-da17-42c9-800a-2f08832e5d4b/custom-1.png",
                                        "url_2x": "https://static-cdn.jtvnw.net/custom-reward-images/30515034/6ef17bb2-e5ae-432e-8b3f-5ac4dd774668/7bcd9ca8-da17-42c9-800a-2f08832e5d4b/custom-2.png",
                                        "url_4x": "https://static-cdn.jtvnw.net/custom-reward-images/30515034/6ef17bb2-e5ae-432e-8b3f-5ac4dd774668/7bcd9ca8-da17-42c9-800a-2f08832e5d4b/custom-4.png"
                                    },
                                    "default_image": {
                                        "url_1x": "https://static-cdn.jtvnw.net/custom-reward-images/default-1.png",
                                        "url_2x": "https://static-cdn.jtvnw.net/custom-reward-images/default-2.png",
                                        "url_4x": "https://static-cdn.jtvnw.net/custom-reward-images/default-4.png"
                                    },
                                    "background_color": "#00C7AC",
                                    "is_enabled": true,
                                    "is_paused": false,
                                    "is_in_stock": true,
                                    "max_per_stream": { "is_enabled": false, "max_per_stream": 0 },
                                    "should_redemptions_skip_request_queue": true
                                    },
                                "user_input": "Hello, you are my favourite streamer",
                                "status": "FULFILLED"
                                }
                            }
                        }"""    
        
        # act
        result = await filter.handle_topic_channelpoint_response(json.loads(response))

        # assert
        self.assertTrue(result)