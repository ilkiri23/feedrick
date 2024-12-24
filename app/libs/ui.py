import typing as t
from collections.abc import Iterable, Callable
import operator
import htpy as h
from markupsafe import Markup
from wtforms import Form

type Spacing = t.Literal[1, 2, 3] | None


def stack(
    items: Iterable[h.Node],
    *,
    orientation: t.Literal['horizontal', 'vertical'] = 'horizontal',
    alignment: t.Literal['start', 'center', 'end'] | None = None,
    spacing: Spacing = None,
    **kwargs: h.Attribute
):
    # _class = t.cast(kwargs.pop('_class', ''), h._ClassNames)
    return h.div(
        _class=['vstack', {
            f'vstack--alignment_{alignment}': alignment is not None,
            f'vstack--spacing_{spacing}': spacing is not None,
        }],
        **kwargs
    )[items]


def hstack(
    items: Iterable[h.Node],
    *,
    alignment: t.Literal['start', 'center', 'end'] | None = None,
    spacing: Spacing = None,
    **kwargs: h.Attribute
):
    pass

def button(text: h.Node, **kwargs: h.Attribute):
    type = kwargs.pop('type', 'button')
    return h.button('.button', type=type, **kwargs)[text]


def input(**kwargs: h.Attribute):
    type = kwargs.pop('type', 'text')
    return h.input('.input', type=type, **kwargs)


def select(
    items: list[tuple[str, t.Any]],
    *,
    comparator: Callable[[t.Any, t.Any], bool] = operator.eq,
    **kwargs: h.Attribute
):
    default_value = kwargs.pop('value', items[0] if items else '')
    return h.select(**kwargs)[(
        h.option(
            value=value,
            selected=comparator(default_value, value)
        )[text] for (text, value) in items
    )]


def form_field(label: str | None, control: h.BaseElement):
    return h.label('.form-field')[
        label and h.span('.form-field__label')[label],
        control
    ]

# def radio_group(
#     items: list[tuple[str, t.Any]],
#     *,
#     comparator: Callable[[t.Any, t.Any], bool] = operator.eq,
#     **kwargs: h.Attribute
# ):
#     name = kwargs.pop('name', None)
#     default_value = kwargs.pop('value', items[0] if items else '')
#     return vstack(
#         alignment='start',
#         spacing=1,
#         items=(
#             h.label[
#                 h.input(
#                     type='radio',
#                     name=name,
#                     value=value,
#                     checked=comparator(default_value, value)
    
#                 ), 
#                 text
#             ] for (text, value) in items
#         ),
#         **kwargs
#     )

def wtf_fields(form: Form):
    return [(
        h.div('.form-field')[
            Markup(f"{field.label(class_='form-field__label')}{field}"),
            field.errors and h.ul[(h.li[error] for error in field.errors)]
        ] for field in form
    )]