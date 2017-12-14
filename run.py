from lib import *
import argparse
import time
import os.path

# check if database has been created
allowArgs = not os.path.isfile("cryptos.db") 

startTime = time.time()

parser = argparse.ArgumentParser(description="Select a post limit for reddit collection.")
parser.add_argument('--limit', metavar="[int]",  type=int,required=allowArgs,help='the post limit; must be supplied on first run: afterwards, default will be to collect all new material')
args = parser.parse_args()

postLimit = args.limit

if (not args.limit):
   postLimit = 0
   print("Getting newest posts...")
else:  
    print("Searching %i posts..." % (postLimit))

anInstance = reddit.Reddit()

anInstance.collectMentions(postLimit)
anInstance.writeMentions()

print("Done, execution took %f seconds." % (time.time() - startTime))
