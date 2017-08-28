import links
import source
import praw

INCLUDED_PATH_REDDIT = "../sources/reddit/include.txt"

class Reddit(source.Source):
    subreddits = set()

    def __init__(self):
        source.Source.__init__(self, INCLUDED_PATH_REDDIT)
        for sr in self.included:
            subreddits.add("/r/" + sr)

class SubReddit(links.NamedLink):
    posts = set()

    def __init__(self, url, name):
        links.NamedLink.__init__(self, url, name)

    def updatePosts(self):
        return
