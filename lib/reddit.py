import links, source
from simplesql import db
import praw
import time
from textblob import TextBlob

INCLUDED_PATH_REDDIT = "sources/reddit/include.txt"
CRYPTOS_PATH_REDDIT = "sources/reddit/cryptos.txt"

class Reddit(source.Source):
    subreddits = set()
    instance = praw.Reddit("cryptoscrape")
    srMentions = dict()
    data = db.Database("cryptos.db")
    lastRun = 0

    def __init__(self):
        source.Source.__init__(self, INCLUDED_PATH_REDDIT, CRYPTOS_PATH_REDDIT)
        self.setup()
        self.lastRun = 0
        for sr in self.included:
            self.subreddits.add(self.instance.subreddit(sr))
            self.srMentions[sr] = {}
            for crypto in self.cryptos:
                self.srMentions[sr][crypto] = 0

    def collectMentions(self, lim=0):
        for sub in self.subreddits:  
            for post in sub.new(limit=lim):
                postTime = int(post.created)

                if (postTime > self.lastRun):
                    # include all comments
                    post.comments.replace_more(limit = None)

                    for crypto in self.cryptos:
                        self.srMentions[sub.display_name][crypto] += post.url.lower().count(crypto)

                        if (post.selftext.lower().count(crypto) > 0):
                            self.srMentions[sub.display_name][crypto] += post.selftext.lower().count(crypto)
                            selfTextBlob = TextBlob(post.selftext)
                            sentimentScore = selfTextBlob.sentiment.polarity
                            subjectivityScore = selfTextBlob.sentiment.subjectivity
                            self.data.executeSQLFile("lib/sql/insert_reddit_post.sql", [str(sub), crypto, stripChars(post.selftext), sentimentScore, subjectivityScore])
                                                          
                        for comment in post.comments.list():

                            if (comment.body.lower().count(crypto) > 0):
                                self.srMentions[sub.display_name][crypto] += comment.body.lower().count(crypto)
                                commentBlob = TextBlob(comment.body)
                                commentSentiment = commentBlob.sentiment.polarity
                                commentSubjectivity = commentBlob.sentiment.subjectivity 

                                self.data.executeSQLFile("lib/sql/insert_reddit_comment.sql", [str(sub), crypto, str(comment), stripChars(comment.body), commentSentiment, commentSubjectivity])

        
        self.data.executeSQLFile("lib/sql/update_last_run.sql")

    def writeMentions(self):
     for source, mentions in self.srMentions.iteritems():
            if isinstance(mentions, dict):
                for currency, number in mentions.iteritems():
                    self.data.executeSQLFile("lib/sql/insert_all_mentions.sql",
                    ["reddit", source, currency, number])

    def setup(self):
        self.data.executeSQLFile("lib/sql/create_all_mentions_table.sql")
        self.data.executeSQLFile("lib/sql/create_reddit_posts_table.sql")
        self.data.executeSQLFile("lib/sql/create_reddit_comments_table.sql")
        self.data.executeSQLFile("lib/sql/create_last_run_table.sql")

def stripChars(text):
    return text.replace("\"", "").replace("'", "")

