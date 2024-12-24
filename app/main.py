from flask import Flask
from app.libs.ext.htmx.request import HTMXRequest
from app.db.session import session_scope
from app.feed.services.feed_collector import FeedCollector
# from app.feed.services import sync_all_feeds

def create_app():
    app = Flask(__name__, static_folder='static/dist')
    app.request_class = HTMXRequest

    from .reader.routes import bp
    app.register_blueprint(bp)

    # from .post.routes import bp
    # app.register_blueprint(bp)

    # with session_scope() as session:
    #     feed_collector = FeedCollector(session)
    #     feed_collector.start_collecting_for_all()

    return app
