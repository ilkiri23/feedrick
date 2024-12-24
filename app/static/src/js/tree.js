class FolderNode {
  constructor(id, el) {
    this.id = id
    this.el = el
    this.toggleEl = el.querySelector('[data-control="toggle"]')
    // init `_isExpanded` at the same time
    this.isExpanded = el.dataset.folderState === 'expanded'
  }

  get isExpanded() {
    return this._isExpanded
  }

  set isExpanded(value) {
    this._isExpanded = value

    if (value) {
      this.el.dataset.folderState = 'expanded'
      this.el.ariaExpanded = 'true'
      this.toggleEl.textContent = '–'
    } else {
      this.el.dataset.folderState = 'collapsed'
      this.el.ariaExpanded = 'false'
      this.toggleEl.textContent = '+'
    }
  }

  expand() {
    this.isExpanded = true
  }

  collapse() {
    this.isExpanded = false
  }

  toggle() {
    this.isExpanded = !this.isExpanded
  }
}

export class Tree {
  constructor(root) {
    this.root = saharok.mix(root)
    this.folders = new Map()
    this.initHandlers()
  }

  initHandlers() {
    this.root
      .on('fol')
    htmx.on(this.root, 'folder:toggle', (event) => this.toggleFolder(event.detail.folderId))
    htmx.on(this.root, 'folder:delete', (event) => this.deleteFolder(event.detail.folderId))
    htmx.on(this.root, 'htmx:after-swap', () => this.initFolders())
  }

  initFolders() {
    this.folders.clear()
    const els = this.root.querySelectorAll('[data-node-type="folder"]')
    els.forEach((el) => {
      const id = parseInt(el.dataset.folderId)
      this.folders.set(id, new FolderNode(id, el))
    })
  }

  toggleFolder(id) {
    this.folders.get(id).toggle()
    return fetch(`/folder/${id}`, {
      method: 'PATCH',
      headers: { 'Content-type': 'application/json; charset=UTF-8' },
      body: JSON.stringify({ is_expanded: folder.isExpanded })
    })
  }

  deleteFolder(id) {
    this.folders.delete(id)
  }
}
