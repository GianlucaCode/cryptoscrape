import os

class Source():
    included = set()
    includePath = ""
    lastRunPath = ""
    cryptoPath = ""
    lastRun = 0
    cryptos = set(["bitcoin"])

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

    def updateCryptos(self):
        with open(self.cryptoPath) as f:
            for line in f:
                self.cryptos.add(line.split("\n")[0])
