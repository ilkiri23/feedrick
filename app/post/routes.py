from flask import Blueprint
import requests
from readability import Document
from app.db.session import session_scope
from app.ext.htmx.response import make_htmx_response
from .services import PostRepository
from .components import post_content

bp = Blueprint('post', __name__, '/post')


@bp.get('/post/<int:post_id>')
def get_post_content(post_id: int):
    with session_scope() as session:
        post_repo = PostRepository(session)
        post = post_repo.get(post_id)

        if post.content is None:
            response = requests.get(post.link)
            post = post_repo.update(post.id, content=response.text)

        doc = Document(post.content)
        content = doc.summary(html_partial=True)

        return make_htmx_response(post_content(post))
