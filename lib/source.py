import os

class Source():
    included = set()
    includePath = ""
    cryptoPath = ""
    lastRun = 0
    cryptos = set()

    def __init__(self, includePath, lastRunPath, cryptoPath):
        self.included = set()
        self.includePath = includePath
        self.cryptoPath = cryptoPath
        self.updateIncluded()
        self.updateCryptos()

    def updateIncluded(self):
        with open(self.includePath) as f:
            for line in f:
                self.included.add(line.split("\n")[0])

            if (len(self.included) == 0):
                print("\nWARNING: No sources included.\n")

            f.close()

    def updateCryptos(self):
        with open(self.cryptoPath) as f:
            for line in f:
                self.cryptos.add(line.split("\n")[0])

            if (len(self.cryptos) == 0): 
                print("\nWARNING: No crypto-currencies included.\n")

            f.close()

