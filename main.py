import logging

import settings
import streamer


log = logging.getLogger(__name__)


def main():

    stream = streamer.FactStreamer(
        settings.API_KEY,
        settings.API_SECRET,
        settings.OAUTH_TOKEN,
        settings.OAUTH_TOKEN_SECRET,
    )
    stream.statuses.filter(track='election')


if __name__ == '__main__':
    main()
