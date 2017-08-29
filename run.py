from lib import *

db.setup()

anInstance = reddit.Reddit()

postLimit = 5

anInstance.collectMentions(postLimit)
anInstance.writeMentions()
