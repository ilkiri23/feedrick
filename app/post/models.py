from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship

from app.libs.ext.sqlalchemy import Base

if TYPE_CHECKING:
    from app.feed.models import Feed


class Post(Base):
    __tablename__ = 'post'

    # guid: Mapped[str]
    title: Mapped[str]
    content: Mapped[str | None]
    url: Mapped[str]
    # pub_date: Mapped[datetime]

    feed_id: Mapped[int] = mapped_column(ForeignKey('feed.id', ondelete='CASCADE'))
    
    feed: Mapped['Feed'] = relationship(back_populates='posts')


# class PostContent(Base):
#     __tablename__ = 'post-content'

#     content: Mapped[str]
#     # pub_date: Mapped[datetime]
#     version

#     post_id: Mapped[int] = mapped_column(ForeignKey('post.id', ondelete='CASCADE'))

#     post: Mapped['Post'] = relationship(back_populates='post')