import links

class Thread(links.NamedLink):
    timestamp
    replyCount = 0
    replies = set()

    def __init__(self, url, name, timestamp, replyCount):
        links.NamedLink.__init__(self, url, name)
        self.timestamp = timestamp
        self.replyCount = replyCount
