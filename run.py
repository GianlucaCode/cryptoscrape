from lib import *

db.setup()

anInstance = reddit.Reddit()

postLimit = 20 

anInstance.collectMentions(postLimit)
anInstance.writeMentions()
