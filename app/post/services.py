from app.libs.ext.sqlalchemy import BaseRepository
from .models import Post

class PostRepository(BaseRepository[Post]):
    model = Post
