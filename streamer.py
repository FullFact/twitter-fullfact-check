import logging

from twython import TwythonStreamer


class FactStreamer(TwythonStreamer):

    @property
    def logger(self):
        return logging.getLogger(str(self))

    def on_success(self, data):
        self.logger.info(data)

    def on_error(self, status_code, data):
        self.logger.warning(data)
