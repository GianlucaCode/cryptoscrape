import links, source
from simplesql import db
import praw
import time
from textblob import TextBlob
from datetime import datetime

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
        self.lastRun = str(self.data.retrieveData("last_run", "lib/sql/get_last_run.sql")[-1])[3:-3]
        for sr in self.included:
            self.subreddits.add(self.instance.subreddit(sr))
            self.srMentions[sr] = {}
            for crypto in self.cryptos:
                self.srMentions[sr][crypto] = 0

    def collectMentions(self, lim):
        self.lastRun = str(self.data.retrieveData("last_run", "lib/sql/get_last_run.sql")[-1])[3:-3]
        
        if (lim == 0):
            beginning = int(time.mktime(datetime.strptime(self.lastRun, "%Y-%m-%d %H:%M:%S").timetuple()))
            for sub in self.subreddits:
                for submission in self.instance.subreddit(str(sub)).submissions(None, beginning):
                    # now search for cryptos
                    for crypto in self.cryptos:
                        if ((post.selftext + post.title).lower().count(crypto) > 0):
                            # cases where selftext references a crypto
                            self.srMentions[sub.display_name][crypto] += (post.selftext + post.title).lower().count(crypto)
                            selfTextBlob = TextBlob(submission.selftext)
                            sentimentScore = selfTextBlob.sentiment.polarity
                            subjectivityScore = selfTextBlob.sentiment.subjectivity
                            self.data.executeSQLFile("lib/sql/insert_reddit_post.sql", [submission.title, str(sub), crypto, stripChars(post.selftext), sentimentScore, subjectivityScore])
                            # now retrieve comments from the post
                            submission.comments.replace_more(limit = None)
                            for comment in submission.comments.list():
                                if (comment.body.lower().count(crypto) > 0):
                                    self.srMentions[sub.display_name][crypto] += comment.body.lower().count(crypto)
                                    commentBlob = TextBlob(comment.body)
                                    commentSentiment = commentBlob.sentiment.polarity
                                    commentSubjectivity = commentBlob.sentiment.subjectivity
                                    self.data.executeSQLFile("lib/sql/insert_reddit_comment.sql", [str(sub), crypto, str(comment), stripChars(comment.body), commentSentiment, commentSubjectivity])

        else:
            # cases where user supplies a limit
            pass

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

