import links
import source.Source as Source
import praw

class Reddit(Source):
    

class SubReddit(links.NamedLink):
    posts = set()

    def __init__(self, url, name):
        links.NamedLink.__init__(self, url, name)

    def updatePosts(self):
        return
