import zope.publisher.browser


class HelloPage(zope.publisher.browser.BrowserPage):
    def __call__(self):
        return "<html><body><h1>Hello World</h1></body></html>"
