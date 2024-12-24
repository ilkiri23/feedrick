class Modal {
	constructor(trigger, target) {
		this.isVisible = false
		this.trigger = saharok.mix(trigger)
		this.target = saharok.mix(target)
		this.#initHandlers()
	}

	#initHandlers() {
		this.trigger
			.on(['click', 'keydown.enter', 'keydown.space'], () => {
				if (!this.isVisible) this.show()
			})

		this.target
			.on('keydown.esc', () => this.hide())
	}

	show() {
		this.isVisible = true
		this.target.styles({ display: 'block' }).focus()
		document.body.classList.add('overflow-hidden')
	}

	hide() {
		this.isVisible = false
		this.trigger.focus()
		this.target.styles({ display: 'none' })
		document.body.classList.remove('overflow-hidden')
	}
}

Modal.instances = new Map()

export function initModals(context) {
	saharok.findAll('[data-modal-target]')
		.exec((el) => {
			const id = el.dataset.modalTarget
			const modal = saharok.find(`#${id}}`)
			Modal.instances.set(id, new Modal(el, modal))
		})

	saharok.findAll('[data-modal-hide]')
		.exec((el) => {
			const id = el.dataset.modalTarget
		})
}