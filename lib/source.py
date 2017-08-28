class Source():
    included = set([])
    includePath = ""
    mentions = dict()
    
    def __init__(self, includePath, included=[]):
        self.included = set(included)
        self.includePath = includePath
        self.updateIncluded(self.includePath)

    def updateIncluded(self, path):
        with open(path) as f:
            for line in f:
                self.included.add(line.split("\n")[0])

