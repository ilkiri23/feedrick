from flask import Blueprint

from app.libs.ext.htmx import make_htmx_response
from app.db.session import session_scope

from .feed import bp as feed_bp

from ..services import TreeComposer
from ..components import feed_tree

bp = Blueprint('reader', __name__, url_prefix='/reader')
bp.register_blueprint(feed_bp)


@bp.get('')
def page():
    with session_scope() as session:
        tree_composer = TreeComposer(session)
        tree = tree_composer.make_tree()
        return make_htmx_response('')


@bp.get('/tree')
def get_tree():
    with session_scope() as session:
        tree_composer = TreeComposer(session)
        tree = tree_composer.make_tree()
        return make_htmx_response('')