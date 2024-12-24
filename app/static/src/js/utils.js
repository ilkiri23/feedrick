export const isNullOrUndefined = (value) => value == null

export const isNode = (value) => (value instanceof HTMLElement || value instanceof SVGElement)

export const isNodeList = (value) => (value instanceof NodeList || Array.isArray(value))


export function throttle(fn, ms) {
	let locked = false
	return (...args) => {
		if (!locked) {
			locked = true
			fn(...args)
			setTimeout(() => { locked = false }, ms)
		}
	}
}


const a = "a[href], area[href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), button:not([disabled]), iframe, object, embed, *[tabindex], *[contenteditable]"
const b = 'a[href]:not([disabled]), button:not([disabled]), textarea:not([disabled]), input[type="text"]:not([disabled]), input[type="radio"]:not([disabled]), input[type="checkbox"]:not([disabled]), select:not([disabled])'

const focusableElementsSelector = `
	a[href]:not([disabled]),
	button:not([disabled]),
	input:not([disabled]),
	select:not([disabled]),
`

export function applyFocusTrap(el) {
	const focusableEls = context.querySelectorAll()

	saharok.mix(el)
		.on('keydown.tab', (ev) => {
			if (ev.shiftKey) {
				
			}
		})
}