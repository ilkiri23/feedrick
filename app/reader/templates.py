import htpy as h

def base_page(content: h.Node):
    return h.html[
        h.head[
            h.script(src='https://unpkg.com/htmx.org@2.0.3')
        ],
        h.body[content]
    ]