import csv
import logging

from twython import Twython

import settings
import streamer
from users import screennames_to_ids, User

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def load_example_csv():
    users = {}
    with open('MP_twitter.csv') as infile:
        reader = csv.reader(infile, delimiter=',', quotechar='"')
        for line in reader:
            user, screenname, region = line[0:3]
            users[screenname] = User(user, screenname, region)
    return users


def main():

    twitter = Twython(
        settings.API_KEY,
        settings.API_SECRET,
        settings.OAUTH_TOKEN,
        settings.OAUTH_TOKEN_SECRET,
    )

    users = load_example_csv()

    ids = screennames_to_ids(users.keys(), twitter)

    stream = streamer.FactStreamer(
        users,
        settings.API_KEY,
        settings.API_SECRET,
        settings.OAUTH_TOKEN,
        settings.OAUTH_TOKEN_SECRET,
    )
    log.info('Listening to tweets by {} users'.format(len(ids)))
    stream.statuses.filter(follow=','.join(str(x) for x in ids.values()))


if __name__ == '__main__':
    main()
