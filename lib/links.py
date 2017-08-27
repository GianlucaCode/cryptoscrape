class Link():
    url = ""

    def __init__(self, url):
        self.url = url

class NamedLink(Link):
    name = ""

    def __init__(self, url, name):
        Link.__init__(self, url)
        self.name = name
