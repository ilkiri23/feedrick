from typing import cast
from flask import Request, request

from .headers import HTMXRequestHeader


class HTMXRequest(Request):
    def __bool__(self):
        return self.headers.get(HTMXRequestHeader.REQUEST) == 'true'

    @property
    def boosted(self):
        return self.headers.get(HTMXRequestHeader.BOOSTED) == 'true'

    @property
    def current_url(self):
        return self.headers.get(HTMXRequestHeader.CURRENT_URL)

    @property
    def target(self):
        return self.headers.get(HTMXRequestHeader.TARGET)

    @property
    def trigger(self):
        return self.headers.get(HTMXRequestHeader.TRIGGER)


htmx_request = cast(HTMXRequest, request)