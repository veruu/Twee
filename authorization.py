import json
import requests
from rauth import OAuth1Service, OAuth1Session

TWITTER_URL = 'https://api.twitter.com/'


class authorization():
    def __init__(self):
        self.load_keys_and_tokens('.Twee')
        self.twitter = OAuth1Service(
                name='twitter', consumer_key=self.APIkey_secret['APIkey'],
                consumer_secret=self.APIkey_secret['APIsecret'],
                request_token_url=TWITTER_URL + 'oauth/request_token',
                access_token_url=TWITTER_URL + 'oauth/access_token',
                authorize_url=TWITTER_URL + 'oauth/authorize',
                base_url=TWITTER_URL + '1.1/')
        self.session = self.getSession()

    def getSession(self):
        return OAuth1Session(
            self.APIkey_secret['APIkey'], self.APIkey_secret['APIsecret'],
            self.user_access['access_token'],
            self.user_access['access_token_secret'], service=self.twitter)

    def load_keys_and_tokens(self, filename):
        keys_and_tokens = []
        with open(filename, 'r') as f:
            for line in f:
                keys_and_tokens.append(json.loads(line))
        self.APIkey_secret = keys_and_tokens[0]
        self.user_access = keys_and_tokens[1]
