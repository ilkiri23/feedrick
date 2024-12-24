class Menu {
	constructor(target) {
		this.target = saharok.mix(target)
		this.items = saharok.findAll('[data-menu-item]', target)
		this.currentIndex = -1
	}

	#initHandlers() {
		this.target
			.on('keydown.up', () => selectItem(this.currentIndex - 1))
			.on('keydown.down', () => selectItem(this.currentIndex + 1))
			.on('keydown.tab', (ev) => ev.preventDefault())
	}

	selectItem(index) {
		if (index > (this.items.length - 1) || index < 0) return
		this.items[index].classList.add('selected')
		this.currentIndex = index
	}
}

Menu.instances = new Map()

export function initPopovers(context) {
	saharok.findAll('[role="menu"]', context)
		.exec((menu, index) => {
			// const placement = trigger.dataset.
			Menu.instances.set(index, new Menu(target))
		})
}
