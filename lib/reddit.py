import links

class SubReddit(links.NamedLink):
    posts = set()

    def __init__(self, url, name):
        links.NamedLink.__init__(self, url, name)
