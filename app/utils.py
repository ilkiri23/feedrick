import typing as t
from collections.abc import Iterable, Callable
import re

def to_kebab_case(input: str):
    words = re.sub(r'[-_]', ' ', input).lower().split()
    return '-'.join(words)


def flat_map(func: Callable[..., t.Any], iter: Iterable[t.Any]):
    result: list[t.Any] = []
    for item in iter:
        result.extend(func(item))
    return result
