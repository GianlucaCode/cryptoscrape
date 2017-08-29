import links
import source
import json, requests, praw
import re
import datetime

INCLUDED_PATH_REDDIT = "sources/reddit/include.txt"
LAST_RUN_PATH_REDDIT = "sources/reddit/.lastrun"

class Reddit(source.Source):
    subreddits = set()
    instance = praw.Reddit("crypto-scrape")

    def __init__(self):
        source.Source.__init__(self, INCLUDED_PATH_REDDIT, LAST_RUN_PATH_REDDIT)
        for sr in self.included:
            self.subreddits.add(self.instance.subreddit(sr))


    def collectMentions(self):
        for sub in self.subreddits:
            for post in sub.new(limit=5):
                time = int(post.created)
                if (time > self.lastRun):
                    print("This post is new since last run.")
