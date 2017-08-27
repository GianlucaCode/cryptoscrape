import requests
from bs4 import BeautifulSoup
import os, datetime

class Link():
    url = ""

    def __init__(self, url):
        self.url = url

class NamedLink(Link):
    name = ""

    def __init__(self, url, name):
        Link.__init__(self, url)
        self.name = name

class Thread(NamedLink):
    timestamp
    replyCount = 0 
    replies = set()

    def __init__(self, url, name, timestamp, replyCount):
        NamedLink.__init__(self, url, name)
        self.timestamp = timestamp
        self.replyCount = replyCount
        
class SubReddit(NamedLink):
    posts = set()

    def __init__(self, url, name):
        NamedLink.__init__(self, url, name)
  
        
