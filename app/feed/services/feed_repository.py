from app.libs.ext.sqlalchemy import BaseRepository
from ..models import Feed

class FeedRepository(BaseRepository[Feed]):
    model = Feed
