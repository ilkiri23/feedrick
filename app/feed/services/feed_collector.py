import typing as t
from functools import partial
from sqlalchemy.orm import Session

from app.db.session import session_scope
from app.bgtask import scheduler
from app.post.services import PostRepository

from .feed_repository import FeedRepository
from .feed_parser import FeedParser

if t.TYPE_CHECKING:
    from ..models import Feed


class FeedCollector:
    def __init__(self, session: Session):
        self.feed_repo = FeedRepository(session)
        self.feed_parser = FeedParser()

    def is_duplicate(self, post: t.Any) -> bool:
        return False

    def detect_duplicates(self, items: list):
        processed_items = []

        for item in items:
            if not self.is_duplicate(item):
                processed_items.append(item)

        return processed_items

    def parse_and_save(self, feed_id: int, feed_url: str):
        with session_scope() as session:
            post_repo = PostRepository(session)
            parsed_data = self.feed_parser.parseURL(feed_url)
            processed_items = detect_duplicates(feed_id, parsed_data.items)

            for item in parsed_data.items:
                if not self.is_duplicate(item, ):
                    processed_items.append(item)

            post_repo.create_many(processed_items)


            post_repo.create_many([{
                'title': item.title,
                'url': item.link,
                'feed_id': feed_id
            } for item in parsed_data.items])

    def start_collecting(self, feed: 'Feed'):
        func = partial(self.parse_and_save, feed.id, feed.url)
        scheduler.add_job(func, 'interval', seconds=feed.refresh_interval*60, id=f'{feed.id}.collecting')
        func()

    def add_feed(self, data: t.Any):
        feed = self.feed_repo.create(data)
        self.start_collecting(feed)
        return feed

    def update_feed(self, feed_id: int, changes: t.Any):
        feed = self.feed_repo.get(feed_id)
        updated_feed = self.feed_repo.update(feed_id, changes)

        if feed.refresh_interval != updated_feed.refresh_interval:
            pass
            # self.restart_collection()
            # func = partial(self.parse_and_save, updated_feed.id, updated_feed.url)
            # scheduler.add_job(func, 'interval', seconds=updated_feed.refresh_interval)
            # func()

    def delete_feed(self, feed_id: int) -> None:
        self.feed_repo.delete(feed_id)

    def delete_feeds_in_folder(self, folder_id: int) -> None:
        deleted_feeds = self.feed_repo.delete_many([('folder_id', '==', folder_id)])
        for feed in deleted_feeds:
            pass
