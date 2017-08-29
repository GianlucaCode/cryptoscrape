import os
import db

class Source():
    included = set()
    includePath = ""
    lastRunPath = ""
    cryptoPath = ""
    lastRun = 0
    cryptos = set()

    def __init__(self, includePath, lastRunPath, cryptoPath):
        self.included = set()
        self.includePath = includePath
        self.lastRunPath = lastRunPath
        self.cryptoPath = cryptoPath
        self.updateIncluded()
        self.updateRun()
        self.updateCryptos()

    def updateIncluded(self):
        with open(self.includePath) as f:
            for line in f:
                self.included.add(line.split("\n")[0])
            f.close()

    def updateRun(self, ts=0):
        with open(self.lastRunPath,"w+") as f:
            f.write(str(ts))
            self.lastRun = int(ts)
            f.close()

    def updateCryptos(self):
        with open(self.cryptoPath) as f:
            for line in f:
                self.cryptos.add(line.split("\n")[0])
            f.close()

    def writeMentions(self):
        db.setup()
