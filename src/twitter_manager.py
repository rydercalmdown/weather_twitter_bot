import os
import twitter
import logging


class TwitterManager():
    """Class for managing twitter posts"""

    def __init__(self):
        """Instantiate twitter manager"""
        self._setup_twitter()

    def _setup_twitter(self):
        """Authenticate to the twitter API"""
        logging.info('Authenticating to twitter')
        self.api = twitter.Api(consumer_key=os.environ['TWITTER_APP_API_KEY'],
                      consumer_secret=os.environ['TWITTER_APP_API_KEY_SECRET'],
                      access_token_key=os.environ['TWITTER_ACCESS_TOKEN'],
                      access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

    def post_to_twitter(self, image, text):
        """Posts the image to twitter with text"""
        logging.info('Sending tweet')
        self.api.PostUpdate(text, media=image)
