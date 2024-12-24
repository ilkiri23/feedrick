htmx.defineExtension('push-params', {
    onEvent(name, event) {
        if (name === 'htmx:afterRequest') {
            const url = new URL(window.location.href)
            const params = url.searchParams

            Object.entries(event.detail.requestConfig.parameters)
                .forEach(([key, value]) => params.set(key, value))

            history.pushState(history.state, '', url)
        }
    }
})