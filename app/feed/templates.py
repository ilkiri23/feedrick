import typing as t
from flask import url_for
import htpy as h
import app.libs.ui as ui
from .forms import FeedForm 


def feed_form(form: FeedForm, **kwargs: h.Attribute):
    return h.form(**kwargs)[
        h.div[
            *ui.wtf_fields(form),
            ui.button(
                type='submit',
                text='Отправить'
            )
        ]
    ]


def create_feed_modal(form: FeedForm):
    return h.div[
        feed_form(
            form,
            hx_post=url_for('reader.feed.create_feed'),
            hx_swap='none'
        )
    ]
