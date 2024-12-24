import { computePosition, offset } from '@floating-ui/dom';
import { throttle } from './utils.js'

export class Popover {
	constructor(trigger, target) {
		this.isVisible = false
		this.trigger = saharok.mix(trigger).attr('aria-expanded', false)
		this.target = saharok.mix(target).styles({ display: 'none' })
		this.#initHandlers()
	}

	#initHandlers() {
		this.trigger
			.on(['click', 'keydown.enter', 'keydown.space'], () => {
				if (this.isVisible) this.hide()
				else this.show()
			})

		this.target
			.on('keydown.esc', () => this.hide())

		saharok.mix(document.body)
			.on('click', (evt) => {
				if (!this.trigger.contains(evt.target)
					&& !this.target.contains(evt.target))
					this.hide()
			})

		window.addEventListener('resize', throttle(() => this.updatePosition(), 10))
	}

	show() {
		this.isVisible = true
		this.trigger.attr('aria-expanded', true)
		this.target.styles({ display: 'block' }).focus()
		this.updatePosition()
	}

	hide() {
		this.isVisible = false
		this.trigger.attr('aria-expanded', false).focus()
		this.target.styles({ display: 'none' })
	}

	async updatePosition() {
		const { x, y } = await computePosition(this.trigger, this.target, {
			placement: 'bottom-start',
			middleware: [offset(4)]
		})

		this.target.styles({
			left: `${x}px`,
			top: `${y}px`
		})
	}
}

Popover.instances = new Map()

export function initPopovers(context) {
	saharok.findAll('[data-popover-target]', context)
		.exec((trigger) => {
			const id = trigger.dataset.popoverTarget
			// const placement = trigger.dataset.
			const target = document.getElementById(id)
			Popover.instances.set(id, new Popover(trigger, target))
		})
}
