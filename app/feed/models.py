# pyright: reportImportCycles=false
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.libs.ext.sqlalchemy import AuditBase

if TYPE_CHECKING:
  from app.folder.models import Folder
  from app.post.models import Post


class Feed(AuditBase):
    __tablename__ = 'feed'

    name: Mapped[str]
    url: Mapped[str]
    refresh_interval: Mapped[int] # in minutes
    
    folder_id: Mapped[int | None] = mapped_column(ForeignKey('folder.id'), nullable=True)

    folder: Mapped['Folder'] = relationship(back_populates='feeds')
    posts: Mapped[list['Post']] = relationship(back_populates='feed')
