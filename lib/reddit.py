import links
import source
import json, requests, praw
import re
import datetime

INCLUDED_PATH_REDDIT = "sources/reddit/include.txt"
LAST_RUN_PATH_REDDIT = "sources/reddit/lastrun.txt"

class Reddit(source.Source):
    subreddits = set()
    instance = praw.Reddit("crypto-scrape")

    def __init__(self):
        source.Source.__init__(self, INCLUDED_PATH_REDDIT, LAST_RUN_PATH_REDDIT)
        for sr in self.included:
            self.subreddits.add(self.instance.subreddit(sr))


    def collectMentions(self):
        self.updateRun()
        for sub in self.subreddits:
            for post in sub.new(limit=5):
                time = post.created
                print(time)
