import logging
import requests

from twython import TwythonStreamer

import settings


class FactStreamer(TwythonStreamer):

    def __init__(self, users, *args, **kwargs):
        self.users = users
        super().__init__(*args, **kwargs)

    @property
    def logger(self):
        return logging.getLogger(str(self))

    def on_success(self, data):
        if 'text' in data:
            tweet = data['text']
            self.logger.info(tweet)
            response = requests.get(
                settings.FACTCHECK_API_URL,
                params=dict(q=tweet, api_key=settings.FACTCHECK_API_KEY),
            )
            try:
                conclusion = response.json()['matches'][0]['conclusion']
                self.logger.info(conclusion)
            except:
                self.logger.warning('Could not get conclusion')

    def on_error(self, status_code, data):
        self.logger.warning(data)

    def __str__(self):
        return '<streamer.FactStreamer(tracking {} ID{})>'.format(
            len(self.users),
            's' if len(self.users) > 1 else '',
        )
