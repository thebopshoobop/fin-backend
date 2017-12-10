"""Libraries for fetching and parsing feeds concurrently."""

from concurrent.futures import ThreadPoolExecutor

import feedparser

from fin_backend.models import db, Feed


def fetch(feed):
    parsed = feedparser.parse(feed.url, etag=feed.etag, modified=feed.modified)
    return {
        'id': feed.id,
        'etag': parsed.get('etag', ''),
        'modified': parsed.get('modified', ''),
        'entries': parsed.get('entries', [])
    }


def fetch_feeds(feeds):
    try:
        with ThreadPoolExecutor() as executor:
            fetched = executor.map(fetch, feeds, timeout=3)
    except TimeoutError:
        pass

    entries = []
    for response in fetched:
        feed = Feed.query(id=response['id'])
        if ((response['modified'] and feed.modified == response['modified'])
                or (response['etag'] and feed.etag == response['etag'])):
            continue

        feed.modified = response['modified']
        feed.etag = response['etag']
        feed.save()
        db.session.commit()  # probably?

        entries.extend()
