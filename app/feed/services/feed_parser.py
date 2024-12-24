from dataclasses import dataclass, field
from datetime import datetime
import requests
import feedparser


@dataclass
class ParsedData:
    title: str
    description: str
    url: str

    @dataclass
    class Item:
        id: str
        title: str
        description: str
        link: str
        published_at: datetime
        updated_at: datetime | None = field(default=None)

    items: list[Item]


class FeedParser:
    def parseURL(self, url: str) -> ParsedData:
        response = requests.get(url)
        data = feedparser.parse(response.content)
        return ParsedData(
            title=data.feed.title,
            # description=data.feed.description,
            description='',
            url=data.feed.link,
            items=[ParsedData.Item(
                id=entry.id,
                title=entry.title,
                # description=entry.description,
                description='',
                link=entry.link,
                published_at=datetime.now()
            ) for entry in data.entries]
        )

    
