from flask import Blueprint

from app.libs.ext.htmx import htmx_request, make_htmx_response
from app.db.session import session_scope

from app.feed.services import FeedCollector, FeedRepository, feed_collector
from app.feed.forms import FeedForm
from app.feed.templates import feed_form, create_feed_modal
from app.folder.services import FolderRepository
from app.utils import flat_map

from ..services import TreeComposer
from .. import components as c
from ..templates import base_page
# from . import components as c
# from .components import (
#     reader_page,
#     FeedTree,

#     CreateFeedModal,
#     UpdateFeedModal,

#     CreateFolderModal,
#     UpdateFolderModal
# )

bp = Blueprint('feed', __name__, url_prefix='/feed')


@bp.get('/<int:feed_id>')
def posts(feed_id: int):
    with session_scope() as session:
        return make_htmx_response(base_page('posts'))
        # if not htmx_request:
        #     tree_composer = TreeComposer(session)
        #     tree = tree_composer.make_tree()

        #     feed_repo = FeedRepository(session)
        #     feed = feed_repo.get(feed_id)
        #     return ''

        # feed_repo = FeedRepository(session)
        # feed = feed_repo.get(feed_id)

        # return make_htmx_response(base_page(''))   


@bp.route('/create', methods=['GET', 'POST'])
def create():
    with session_scope() as session:
        folder_repo = FolderRepository(session)
        folders = folder_repo.get_many()

        form = FeedForm()
        form.set_folders(folders)

        if htmx_request.method == 'POST':
            form.process(htmx_request.form)
            if form.validate():
                feed_collector = FeedCollector(session)
                # feed_collector.subscribe()
                return make_htmx_response(trigger='reload-tree')

        return make_htmx_response(create_feed_modal(form))


@bp.route('/<int:feed_id>/update', methods=['GET', 'POST'])
def update(feed_id: int):
    with session_scope() as session:
        feed_collector = FeedCollector(session)
        form = FeedForm()

        if htmx_request.method == 'POST':
            form.process(htmx_request.form)
            if form.validate():
                feed_collector.update_feed(feed_id, htmx_request.form)
            return make_htmx_response(trigger='reload-tree')

        feed = feed_collector.get_feed(feed_id)
        form.populate_obj(feed)

        with session_scope() as session:
            feed_repo = FeedRepository(session)
            feed = feed_repo.get(feed_id)
            folders = FolderRepository(session).get_many()
            return make_htmx_response(
                update_feed_modal(feed, folders)
            )

    with session_scope() as session:
        form = FeedForm()

        if htmx_request.method == 'POST':

            feed_collector = FeedCollector(session)
            return make_htmx_response(trigger='reload-tree')

        folder_repo = FolderRepository(session)

    # return make_htmx_response(UpdateFeedModal(feed, folders))


# @bp.delete('/<int:feed_id>')
# def delete_feed(feed_id: int):
#     with session_scope(rollback=True, auto_commit=True) as session:
#         feed_collector = FeedCollector(session)
#         feed_collector.delete_feed(feed_id)
#         return make_htmx_response('')
