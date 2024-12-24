import typing as t
import htpy as h
from flask import url_for

import app.libs.ui as ui
from app.feed.models import Feed
from app.folder.models import Folder
from app.post.models import Post

from .models import Tree, Node


def feed_node(node: Node):
    return h.li[
        h.div[
            h.a(
                href=url_for('reader.feed.posts', feed_id=node.id),
                hx_boost='true'
            )[node.name],
            # ui.button(
            #     text='Edit',
            #     hx_get=url_for('reader.update_feed', feed_id=node.id),
            #     hx_target='body',
            #     hx_swap='beforeend'
            # ),
            # ui.button(
            #     text='Unfollow',
            #     hx_delete=url_for('reader.delete_feed', feed_id=node.id),
            #     hx_confirm='Are you sure you want to delete this feed?',
            #     hx_target='closest li',
            #     hx_swap='outerHTML'
            # )
        ]
    ]


# def folder_node(node: Node):
#     children: h.Node = None
#     if node.children:
#         children = h.ul[(
#             feed_node(child) for child in node.children
#         )]

#     return h.li[
#         h.div[
#             h.a(
#                 href=url_for('reader.get_folder_posts', folder_id=node.id),
#                 hx_boost='true'
#             )[node.name],
#             ui.button(
#                 text='Edit',
#                 hx_get=url_for('reader.update_folder', folder_id=node.id),
#                 hx_target='body',
#                 hx_swap='beforeend'
#             ),
#             ui.button(
#                 text='Delete',
#                 hx_delete=url_for('reader.delete_folder', folder_id=node.id),
#                 hx_confirm='Are you sure you want to delete this folder?',
#                 hx_target='closest li',
#                 hx_swap='outerHTML'
#             ),
#             children
#         ]
#     ]


def tree_node(node: Node):
    func = feed_node if node.children is Node else feed_node
    return func(node)


def tree(tree: Tree):
    return h.div(
        '#tree.',
        hx_get=url_for('reader.get_tree'),
        hx_trigger='refresh-feeds from:body, reload-tree from:body',
        hx_select='#tree > ul'
    )[h.ul[(tree_node(node)for node in tree.nodes)]]


# def feeds(tree: Tree):
#     return (
#         h.div[
#                 ui.button(
#                     text='Add folder',
#                     hx_get=url_for('reader.create_folder'),
#                     hx_target='body',
#                     hx_swap='beforeend'
#                 ),
#                 ui.button(
#                     text='Add feed',
#                     hx_get=url_for('reader.create_feed'),
#                     hx_target='body',
#                     hx_swap='beforeend'
#                 ),
#             ],
#             FeedTree(tree),
#         ]
#     )


# def reader_page(tree: Tree, posts: list[Post]):
#     return base_page([
#         feeds(tree),
#         (ui.card(
#             title=post.title,
#             body=[
#                 post.content,
#                 h.a(
#                     '.stretched-link',
#                     href=url_for('post.get_post_content', post_id=post.id),
#                     hx_boost='true'
#                 )
#             ],
#             footer=ui.hstack([
#                 ui.button(
#                     'Mark as Read',
#                     # hx_patch=url_for('mark_post_as_read', post_id=post.id)
#                 ),
#                 ui.button('Favorite')
#             ]),
#         ) for post in posts),
#         h.div('#reader-view')
#         # (post_card(post.title) for post in posts)
#     ])


# def FolderForm(
#     submit_text: str,
#     folder: Folder | None = None,
#     **kwargs: t.Any
# ):
#     return h.form(**kwargs)[
#         TextInput(label='Name', name='name', value=getattr(folder, 'name', ''), required=True),
#         Button(type='submit', text=submit_text)
#     ]


# def CreateFeedModal(folders: list[Folder]):
#     return Modal(
#         open=True,
#         title='Create New Feed',
#         body=FeedForm(
#             folders=folders,
#             submit_text='Create',
#             hx_post=url_for('reader.create_feed'),
#             hx_swap='none'
#         ),
#     )


# def UpdateFeedModal(feed: Feed, folders: list[Folder]):
#     return Modal(
#         open=True,
#         title=f'Update "{feed.name}" Feed',
#         body=FeedForm(
#             feed=feed,
#             folders=folders,
#             submit_text='Update',
#             hx_post=url_for('reader.update_feed', feed_id=feed.id),
#             hx_swap='none'
#         )
#     )


# def CreateFolderModal():
#     return Modal(
#         open=True,
#         title='Create New Folder',
#         body=FolderForm(
#             submit_text='Create',
#             hx_post=url_for('reader.create_folder'),
#         )
#     )


# def UpdateFolderModal(folder: Folder):
#     return Modal(
#         open=True,
#         title=f'Update "{folder.name}" Folder',
#         body=FolderForm(
#             folder=folder,
#             submit_text='Update',
#             hx_patch=url_for('reader.update_folder', folder_id=folder.id)
#         )
#     )


# def reader_toolbar(post):
#     return h.div[
#         ui.hstack(
#             ui.button(
#                 'Back',
#                 hx_get=url_for('reader.get_feed_posts', feed_id=post.feed_id)
#             )
#         )
#     ]
