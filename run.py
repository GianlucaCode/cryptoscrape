from lib import *
import argparse
import time

startTime = time.time()

parser = argparse.ArgumentParser(description="Select a post limit for reddit collection.")
parser.add_argument('integer', metavar='limit', type=int, nargs='+',help='the post limit')
args = parser.parse_args()

postLimit = 0

if (len(args.integer) > 0):
    postLimit = args.integer[0]

print("Searching %i posts..." % (postLimit))

anInstance = reddit.Reddit()

anInstance.collectMentions(postLimit)
anInstance.writeMentions()

print("Done, execution took %f seconds." % (time.time() - startTime))
