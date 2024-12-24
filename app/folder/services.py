from app.libs.ext.sqlalchemy import BaseRepository
from .models import Folder

class FolderRepository(BaseRepository[Folder]):
    model = Folder
