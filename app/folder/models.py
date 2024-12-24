from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, relationship
from app.libs.ext.sqlalchemy import AuditBase

if TYPE_CHECKING:
    from app.feed.models import Feed


class Folder(AuditBase):
    __tablename__ = 'folder'

    name: Mapped[str]

    feeds: Mapped[list['Feed']] = relationship(back_populates='folder')
