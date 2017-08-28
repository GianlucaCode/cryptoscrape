import links
import source
import json, requests, praw

INCLUDED_PATH_REDDIT = "../sources/reddit/include.txt"

class Reddit(source.Source):
    subreddits = set()
    instance = praw.Reddit("crypto-scrape")

    def __init__(self):
        source.Source.__init__(self, INCLUDED_PATH_REDDIT)
        for sr in self.included:
            subreddits.add(self.instance.subreddit(sr))

