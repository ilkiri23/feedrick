import typing as t
from collections.abc import Callable
from dataclasses import dataclass

P = t.ParamSpec("P")
R = t.TypeVar("R")
C = t.TypeVar("C")


@dataclass
class _ChildrenWrapper(t.Generic[C, R]):
    _component_func: t.Any
    _args: t.Any
    _kwargs: t.Any

    def __getitem__(self, children: C) -> R:
        return self._component_func(children, *self._args, **self._kwargs)  # type: ignore


def with_children(
    component_func: Callable[t.Concatenate[C, P], R],
) -> Callable[P, _ChildrenWrapper[C, R]]:
    def func(*args: P.args, **kwargs: P.kwargs) -> _ChildrenWrapper[C, R]:
        return _ChildrenWrapper(component_func, args, kwargs)
    return func