import { Popover } from './popover.js'
import { Menu } from './menu.js'

class Dropdown extends Popover {
	constructor(trigger, target) {
		super(trigger, target)
		// this.menu = new Menu(target, )
		// this.items = saharok.findAll('[data-dropdown-item]', this.target)
		// this.selectedIndex = -1
		this.#initHandlers()
	}

	#initHandlers() {
		this.trigger
			.on(['keydown.up', 'keydown.down'], () => {
				if (!this.isVisible) this.show()
			})

		this.target
			.on('keydown.tab', (evt) => evt.preventDefault())
			.on('keydown.up', (evt) => console.log('up'))
			.on('keydown.down', (evt) => console.log('down'))
			
		saharok.mix(document.body)
			.on('keydown.up', (evt) => {
				console.log(evt.target)
				console.log('up')
			})
	}

	selectItem(index) {
		this.selectedIndex = index
	}
}

Dropdown.instances = new Map()

export function initDropdowns(context) {
	saharok.findAll('[data-dropdown-target]')
		.exec((el) => {
			const id = el.dataset.dropdownTarget
			const popover = saharok.find(`#${id}`)
			Dropdown.instances.set(id, new Dropdown(el, popover))
		})
}