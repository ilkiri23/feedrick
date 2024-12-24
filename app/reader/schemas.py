from pydantic import BaseModel
# from app.ext.pydantic import Ma


class FolderDeleteQuery(BaseModel):
    with_feeds: bool = False