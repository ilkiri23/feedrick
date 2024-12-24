from typing import Any, Literal
import json

from werkzeug.datastructures import Headers
from flask import Response

from .headers import HTMXResponseHeader


def _stringify(value: Any):
    return value if isinstance(value, str) else json.dumps(value)


def make_htmx_response(
    content: Any = '',
    # push_url: str | None,
    redirect: str | None = None,
    reswap: Literal[
        'innerHTML',
        'outerHTML',
        'beforebegin',
        'afterbegin',
        'beforeend',
        'afterend',
        'delete',
        'none'
    ] | None = None,
    retarget: str | None = None,
    trigger: str | dict[str, str] | None = None,
    **kwargs: Any
):
    headers: Headers = kwargs.pop('headers', Headers())

    if reswap is not None:
        headers.set(HTMXResponseHeader.RESWAP, reswap)
    if retarget is not None:
        headers.set(HTMXResponseHeader.RETARGET, retarget)
    if trigger is not None:
        headers.set(HTMXResponseHeader.TRIGGER, _stringify(trigger))

    content_type = kwargs.pop('content_type', 'text/html; charset=UTF-8')

    return Response(str(content), headers=headers, content_type=content_type, **kwargs)
