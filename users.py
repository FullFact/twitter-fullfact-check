import collections
import logging

log = logging.getLogger(__name__)


def screennames_to_ids(screennames, client):
    """
    Convert an iterable of screennames to a mapping
    from screennames to Twitter IDs.
    """

    mapping = dict()

    screennames = collections.deque(screennames)

    while screennames:
        chunk = [
            screennames.popleft().strip('@')
            for _ in range(min(10, len(screennames)))
        ]
        response = client.lookup_user(screen_name=','.join(chunk))
        for user in response:
            mapping[user['screen_name']] = user['id']
        log.info('{} user IDs obtained'.format(len(mapping)))

    return mapping


class User:

    def __init__(self, name, screenname, region):
        self.name = name
        self.screenname = screenname
        self.region = region
