from collections import OrderedDict
from sqlalchemy.orm import Session

from app.feed.services import FeedRepository
from app.folder.services import FolderRepository

from .models import Node, Tree


class TreeComposer:
    def __init__(self, session: Session):
        self.feed_repo = FeedRepository(session)
        self.folder_repo = FolderRepository(session)

    def make_tree(self):
        feeds = self.feed_repo.get_many()
        without_folders: list[Node] = []

        folders = self.folder_repo.get_many()

        folder_dict = OrderedDict([(
            folder.id,
            Node(folder.id, folder.name)
        ) for folder in folders])
        
        for feed in feeds:
            target = without_folders

            if feed.folder_id is not None:
                if folder := folder_dict.get(feed.folder_id):
                    target = folder.children = getattr(folder, 'children', [])

            target.append(Node(id=feed.id, name=feed.name))

        return Tree(nodes=[*folder_dict.values(), *without_folders])

