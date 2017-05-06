import logging

from twython import Twython

import settings


log = logging.getLogger(__name__)


def main():

    twitter = Twython(settings.API_KEY, settings.API_SECRET)
    print(twitter.search(q='python'))


if __name__ == '__main__':
    main()
