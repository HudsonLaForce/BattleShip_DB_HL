class Shot():
    def __init__(self,res,ro,co):
        self.result = res
        self.row = ro
        self.col = co

    def getResult(self):
        return self.result

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col