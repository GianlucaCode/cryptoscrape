import links
import source
import json, requests, praw
import datetime

INCLUDED_PATH_REDDIT = "sources/reddit/include.txt"
LAST_RUN_PATH_REDDIT = "sources/reddit/.lastrun"

class Reddit(source.Source):
    subreddits = set()
    instance = praw.Reddit("crypto-scrape")
    srMentions = dict()

    def __init__(self):
        source.Source.__init__(self, INCLUDED_PATH_REDDIT, LAST_RUN_PATH_REDDIT)
        for sr in self.included:
            self.subreddits.add(self.instance.subreddit(sr))
            self.srMentions[sr] = 0

    def collectMentions(self):
        for sub in self.subreddits:
            for post in sub.new(limit=100):
                time = int(post.created)

                if (time > self.lastRun):
                    post.comments.replace_more(limit=0)
                    for crypto in self.cryptos:
                        self.srMentions[sub.display_name] += post.selftext.lower().count(crypto)
                        self.srMentions[sub.display_name] += post.url.lower().count(crypto)
                        for comment in post.comments.list():
                            self.srMentions[sub.display_name] += comment.body.lower().count(crypto)

        # for key, value in self.srMentions.items():
        #     print(key)
        #     print(value)
