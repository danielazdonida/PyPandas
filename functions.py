import pandas as pd

class Functions:

    def __init__(self):
        self.file = 0
        self.name = 0

    def readFileExcel(self, filePath):
        self.file = pd.read_excel(filePath)

    def readFileCSV(self, filePath):
        self.file = pd.read_csv(filePath)

    def lerArquivo(self):
        return self.file.head()

    def readSomeLines(self, lines):
        return self.file.head(lines)

    def shape(self):
        return self.file.shape

    def describe(self):
        return self.file.describe()

    def filterColumn(self, columnName):
        return self.file[columnName]

    def filterLines(self, lineInitial, lineFinal):
        return self.file.loc[lineInitial:lineFinal]

    def filterColumnInLines(self, column, word):
        return self.file.loc[self.file[column]==word]