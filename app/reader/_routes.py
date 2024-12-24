import itertools
from dataclasses import dataclass
from functools import partial
from flask import Blueprint

from app.db.session import create_session, session_scope
from app.ext.htmx.request import htmx_request
from app.ext.htmx.response import make_htmx_response
from app.feed.services import FeedCollector, FeedRepository
from app.folder.services import FolderRepository
from app.utils import flat_map

from .services import TreeComposer
from . import components as c
from .components import (
    reader_page,
    FeedTree,

    CreateFeedModal,
    UpdateFeedModal,

    CreateFolderModal,
    UpdateFolderModal
)

bp = Blueprint('reader', __name__, url_prefix='/reader')


@bp.get('/feed/<int:feed_id>')
def get_feed_posts(feed_id: int):
    with session_scope() as session:
        tree_composer = TreeComposer(session)
        tree = tree_composer.make_tree()

        feed_repo = FeedRepository(session)
        feed = feed_repo.get(feed_id)

        return make_htmx_response(reader_page(tree, feed.posts))   


# @bp.get('/folder/<int:folder_id>')
# def get_folder_posts(folder_id: int):
#     with session_scope() as session:
#         tree_composer = TreeComposer(session)
#         tree = tree_composer.make_tree()

#         folder_repo = FolderRepository(session)
#         folder = folder_repo.get(folder_id)
#         # a = getattr(folder, name='asdf')
#         # partial(getattr, )
#         # posts = flat_map(partial(getattr, name='posts'), folder.feeds)
#         posts = []

#         return make_htmx_response(reader_page(tree, posts))

@bp.route('/feed/create', methods=['GET', 'POST'])
def create_feed():
    with session_scope() as session:
        if htmx_request.method == 'POST':
            feed_collector = FeedCollector(session)
            feed_collector.add_feed(htmx_request.form)
            return make_htmx_response(trigger='reload-tree')

        folder_repo = FolderRepository(session)
        folders = folder_repo.get_many()
        return make_htmx_response(CreateFeedModal(folders))


@bp.route('/feed/<int:feed_id>/update', methods=['GET', 'POST'])
def update_feed(feed_id: int):
    with session_scope() as session:
        if htmx_request.method == 'POST':
            feed_collector = FeedCollector(session)
            feed_collector.update_feed(feed_id, htmx_request.form)
            return make_htmx_response(trigger='reload-tree')

        # feed = feed_collector.feed
        # folder_repo = FolderRepository(session)
        # folders = folder_repo.get_many()
        return make_htmx_response('')
    # return make_htmx_response(UpdateFeedModal(feed, folders))


@bp.delete('/feed/<int:feed_id>')
def delete_feed(feed_id: int):
    with session_scope() as session:
        feed_collector = FeedCollector(session)
        feed_collector.delete_feed(feed_id)
        return make_htmx_response('')


@bp.route('/folder/create', methods=['GET', 'POST'])
def create_folder():
    pass
    # if htmx_request.method == 'POST':
    #     with session_scope() as session:
    #         folder_repo = FolderRepository(session)
    #         # folder_repo.create(Fol(name='asdf'))
    #         return make_htmx_response(trigger='reload-tree')

    # return make_htmx_response(CreateFolderModal())


@bp.route('/folder/<int:folder_id>/update', methods=['GET', 'POST'])
def update_folder(folder_id: int):
    pass
    # with session_scope() as session:
    #     folder_repo = FolderRepository(session)

    #     if htmx_request.method == 'POST':
    #         folder_repo.update(folder_id, **htmx_request.form)
    #         return make_htmx_response(trigger='reload-tree')

    #     folder = folder_repo.get(folder_id)
    #     return make_htmx_response(UpdateFolderModal(folder))

    # with session_scope() as session:
    #     if htmx_request.method == 'POST':
    #         folder_repo.update(folder_id, **htmx_request.form)
    #         return make_htmx_response(trigger='reload-tree')

    # with transaction_session() as session:
    #     folder_repo = FolderRepository(session)

    #     if htmx_request.method == 'PATCH':
    #         _ = folder_repo.update(folder_id, **htmx_request.form)
    #         return make_htmx_response(trigger='refresh-feeds')

    #     folder = folder_repo.get(folder_id)

    #     return make_htmx_response(UpdateFolderModal(folder))


@bp.delete('/folder/<int:folder_id>')
def delete_folder(folder_id: int):
    with session_scope() as session:
        with_feeds = htmx_request.args.get('with-feeds', 'false') == 'true'
        
        if with_feeds:
            feed_collector = FeedCollector(session)
            feed_collector.delete_feeds_in_folder(folder_id)

        folder_repo = FolderRepository(session)
        folder_repo.delete(folder_id)
        return make_htmx_response(trigger='reload-tree')


@bp.get('/tree')
def get_tree():
    with transaction_session() as session:
        tree_composer = TreeComposer(session)
        tree = tree_composer.make_tree()
        return make_htmx_response(FeedTree(tree))
