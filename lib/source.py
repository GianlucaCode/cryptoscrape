class Source():
    included = set([])

    def __init__(self, included=[]):
        self.included = set(included)

    def updateIncluded(path):
        with open(path) as f:
            for line in f:
                included.append(line.split("\n")[0])
