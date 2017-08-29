import os

class Source():
    included = set()
    includePath = ""
    lastRunPath = ""
    lastRun = 0
    cryptos = set()

    def __init__(self, includePath, lastRunPath, included=[]):
        self.included = set(included)
        self.includePath = includePath
        self.lastRunPath = lastRunPath
        self.updateIncluded()
        self.updateRun()

    def updateIncluded(self):
        with open(self.includePath) as f:
            for line in f:
                self.included.add(line.split("\n")[0])

    def updateRun(self):
        if os.path.isfile(self.lastRunPath):
            with open(self.lastRunPath) as f:
                for line in f:
                    self.lastRun = int(line.split("\n")[0])
        # if file does not exist, it is created with a timestamp of 0
        else:
            with open(self.lastRunPath,"w+") as f:
                f.write("0")
                self.lastRun = 0
                f.close()
