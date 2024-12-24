import { isNode, isNodeList, isNullOrUndefined } from './utils.js'

function getKeyModifier(event) {
	if (event.code === 'Backspace' || event.code === 'Delete') return 'del'
	if (event.code === 'Escape') return 'esc'
	if (event.code.startsWith('Arrow'))
		return event.code.slice(5).toLowerCase()
	return event.code.toLowerCase()
}

// function getMouseModifier(evt) {
// 	switch (evt.button) {
// 		case 0: return 'left'
// 		case 2: return 'right'
// 		case 1: return 'middle'
// 	}
// }

const mixin = {
	// __saharok__ = [],
	attr(name, value) {
		if (arguments.length === 1) {
			if (isNodeList(this)) return []
			if (isNode(this)) return this.getAttribute(name)
		}

		if (arguments.length > 1) {
			if (isNodeList(this)) this.forEach((el) => this.attr.call(el, name, value))
			if (isNode(this)) {
				if (isNullOrUndefined(value)) this.removeAttribute(name)
				else this.setAttribute(name, value) 
			}
		}

		return this
	},
	attrs(value) {
		if (Array.isArray(value)) {
			if (isNodeList(this)) return []
			if (isNode(this)) return value.map((name) => this.attr(name))
		}

		if (typeof value === 'object') {
			if (isNodeList(this)) this.forEach((el) => this.attrs.call(el, value))
			if (isNode(this)) Object.entries(value).forEach((attr) => this.attr(...attr))
		}

		return this
	},
	styles(value) {
		if (isNodeList(this)) this.forEach((el) => this.styles.call(el, value))
		if (isNode(this)) {
			if (typeof value === 'object') Object.assign(this.style, value)
		}
		return this
	},
	on(name, fn) {
		if (isNodeList(this)) this.forEach((el) => this.on.call(el, name, fn))
		if (isNode(this)) {
			if (Array.isArray(name)) name.forEach((nm) => this.on(nm, fn))
			if (typeof name === 'string') {
				let modifier
				[name, modifier] = name.split('.')
				this.addEventListener(name, (evt) => {
					if (
						(name === 'keydown' || name === 'keyup')
						&& modifier !== undefined
						&& modifier !== getKeyModifier(evt)
					) return
					fn(evt)
				})
			}
		}
		return this
	},
	off(name, fn) {
		if (isNodeList(this)) this.forEach((el) => this.off.call(el, name, fn))
		if (isNode(this)) this.removeEventListener(name, fn)
		return this
	},
	trigger(name, payload) {
		if (isNodeList(this)) this.forEach((el) => this.trigger.call(el, name, payload))
		if (isNode(this)) {
			const event = new CustomEvent(name, { detail: payload, bubbles: true, cancelable: true })
			this.dispatchEvent(event)
		}
		return this
	},
	exec(fn) {
		if (isNodeList(this)) this.forEach(fn)
		if (isNode(this)) fn(this)
		return this
	}
}

function mix(el) {
	if (el.sugared) return el
	if (isNodeList(el)) { el = Array.from(el) }
	Object.assign(el, mixin)
	el.sugared = true
	return el
}

const find = (selector, context = document) => mix(context.querySelector(selector))
const findAll = (selector, context = document) => mix(context.querySelectorAll(selector))
const ready = (fn) => document.addEventListener('DOMContentLoaded', fn)

window.saharok = {
	mix,
	find,
	findAll,
	ready
}


// if (selector instanceof NodeList || Array.isArray(selector)) { nodes = Array.from(selector) }
// 	else if (selector instanceof HTMLElement || selector instanceof SVGElement) { nodes = [selector] }
// 	else if (typeof selector === 'string') { nodes = Array.from(context.querySelectorAll(selector) ?? []) }

