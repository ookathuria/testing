import random
class matrixTranspose:

    def __init__(self):

        self.rowCount = 0
        self.colCount = 0
        self.matrix = None
        while True:
            self._run()

    def _run(self):

        self.getUserInput()

    def getUserInput(self):
        self.rowCount = int(input("Enter the number of rows in your matrix : "))
        self.colCount = int(input("Enter the number of columns in your matrix : "))

        self.createMatrix()

    def createMatrix(self):

        #create rowCount count of lists containing 0
        self.matrix = [0] * self.rowCount

        for i in range(self.rowCount):
            #updating the lists created above to point each item to point to another list of colCount number of items, containing 0s
            self.matrix[i] = [0] * self.colCount

        i = 0
        j = 0
        for i in range(self.rowCount):
            for j in range(self.colCount):
                self.matrix[i][j] = random.randint(1,99)

        self.printMatrix()

        response = input("Would you like to transpose the matrix above? y/n")
        if response == "y":
            self.transponse()
        else:
            exit()

    def printMatrix(self):

        print(self.matrix)

    def transponse(self):

        transRowCount = self.colCount
        transColCount = self.rowCount
        transMatrix = None

        transMatrix = [0] * transRowCount
        #create a matrix of colxrow specs, filled with zeros
        for i in range(transRowCount):
            transMatrix[i] = [0] * transColCount

        #fill the transMatrix with real values
        i = 0
        j = 0

        for i in range(self.rowCount):
            for j in range(self.colCount):
                transMatrix[j][i] = self.matrix[i][j]


        self.matrix = transMatrix
        self.printMatrix()

def main():

    matTrans = matrixTranspose()

if __name__ == '__main__':
    main()
