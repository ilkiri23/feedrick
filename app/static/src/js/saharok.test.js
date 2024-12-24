import test from 'tape'
import { JSDOM } from 'jsdom'
import { saharok } from './saharok.js'

const dom = new JSDOM('<!DOCTYPE html><html><body></body></html>')

global.window = dom.window
global.document = dom.window.document
global.Node = dom.window.Node
global.NodeList = dom.window.NodeList
global.HTMLElement = dom.window.HTMLElement
global.SVGElement = dom.window.SVGElement

test('.attr', (t) => {
	t.teardown(() => { document.body.innerHTML = '' })

	t.test('should return value if only `name` is passed', (t) => {
		document.body.innerHTML = '<div role="button" tabindex="0"></div>'
		const div = document.querySelector('div')
		saharok.mix(div)
		t.equal(div.attr('role'), 'button')
		t.equal(div.attr('tabindex'), '0')
		t.end()

		const divs = document.querySelectorAll('div')

		// saharok.mix(divs)
	})

	t.test('should set value to attribute', (t) => {
		document.body.innerHTML = '<div></div>'
		const div = document.querySelector('div')
		saharok.mix(div)
			.attr('role', 'button')
			.attr('tabindex', '0')
		t.equal(div.getAttribute('role'), 'button')
		t.equal(div.getAttribute('tabindex'), '0')
		
		document.body.innerHTML = `<div></div><div></div>`
		const divs = document.querySelectorAll('div')
		saharok.mix(divs)
			.attr('role', 'button')
			.attr('tabindex', '0')
		divs.forEach((div) => {
			t.equal(div.getAttribute('role'), 'button')
			t.equal(div.getAttribute('tabindex'), '0')
		})

		t.end()
	})

	t.test('should remove attribute if passed `value` is null or undefined', (t) => {
		const div = document.createElement('div')
		div.setAttribute('role', 'button')
		div.setAttribute('tabindex', '0')
		saharok.mix(div)
			.attr('role', undefined)
			.attr('tabindex', null)
		t.equal(div.getAttribute('role'), null)
		t.equal(div.getAttribute('tabindex'), null)
		t.end()

		document.body.innerHTML = `
			<div role="button" tabindex="0"></div>
    	<div role="button" tabindex="0"></div>
    `
	})
})

test('.attrs', (t) => {
	t.test('should return values of attributes if passed `value` is array', (t) => {
		const div = document.createElement('div')
		div.setAttribute('role', 'button')
		div.setAttribute('tabindex', '0')
		saharok.mix(div)
		t.deepEqual(div.attrs(['role']), ['button'])
		t.deepEqual(div.attrs(['tabindex']), ['0'])
		t.deepEqual(div.attrs(['role', 'tabindex']), ['button', '0'])
		t.end()
	})

	t.test('should set attribute values if passed `value` is object', (t) => {
		const div = document.createElement('div')
		saharok.mix(div)
			.attrs({
				role: 'button',
				tabindex: '0'
			})
		t.equal(div.getAttribute('role'), 'button')
		t.equal(div.getAttribute('tabindex'), '0')
		t.end()
	})

	t.test('should remove attributes if passed `value` is object with undefined/null values', (t) => {
		const div = document.createElement('div')
		div.setAttribute('role', 'button')
		div.setAttribute('tabindex', '0')
		saharok.mix(div)
			.attrs({
				role: undefined,
				tabindex: null
			})
		t.equal(div.getAttribute('role'), null)
		t.equal(div.getAttribute('tabindex'), null)
		t.end()
	})
})

// test('.styles', (t) => {
// 	t.test('should add styles to elemnt ')
// })

// test('.on', (t) => {
// 	t.test('should add handler to ', (t) => {

// 	})

// 	t.test('should understand key modifier', (t) => {

// 	})
// })

// test('.off', (t) => {
// 	t.test('should remove handler', (t) => {
// 		const fn = t.captureFn(() => {})
// 		const div = document.createElement('div')
// 		div.addEventListener('click', fn)
// 		// div.click()
// 	})
// })
