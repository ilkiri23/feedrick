class Counter {
	constructor(target, inc, dec) {
		this.target = saharok.mix(target)
		this.inc = saharok.mix(inc)
		this.dec = saharok.mix(dec)
	}

	initHandlers() {
		this.inc.on(['click', 'keydown.enter', 'keydown.space'], () => this.increment())
		this.dec.on(['click', 'keydown.enter', 'keydown.space'], () => this.decrement())
	}

	increment() {

	}
}