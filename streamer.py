import logging

from twython import TwythonStreamer


class FactStreamer(TwythonStreamer):

    def __init__(self, users, *args, **kwargs):
        self.users = users
        super().__init__(*args, **kwargs)

    @property
    def logger(self):
        return logging.getLogger(str(self))

    def on_success(self, data):
        self.logger.info(data['text'])

    def on_error(self, status_code, data):
        self.logger.warning(data)

    def __str__(self):
        return '<streamer.FactStreamer(tracking {} ID{})>'.format(
            len(self.users),
            's' if self.users > 1 else '',
        )
