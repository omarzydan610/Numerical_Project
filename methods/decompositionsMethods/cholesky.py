import time
import numpy as np


class Cholesky:
    e
    def __init__(self, matrixA, matrixB, figures):
        self.eigenvalues = np.linalg.eigvals(matrixA)
        self.matrix = np.matrix(matrixA)
        self.n = len(matrixA)
        self.b = matrixB
        self.L = np.zeros_like(matrixA)
        self.x = np.zeros_like(matrixB)
        self.flag = True
        self.y = np.zeros_like(self.b)
        self.execution_time = 0

    def getExcutionTime(self):
        return self.execution_time

    def getSolution(self):
        return self.x

    def getSteps(self):
        matrixL = ""
        matrixU = ""
        for i in self.L:
            matrixL += "|  "
            for j in i:
                matrixL += f"{round(j, 3)}  "
            matrixL += "|\n        "
        for i in np.transpose(self.L):
            matrixU += "|  "
            for j in i:
                matrixU += f"{round(j, 3)}  "
            matrixU += "|\n        "
        steps = f"""
L matrix:
        {matrixL}

U matrix:
        {matrixU}

the equation is:

            LUX = b
            UX = Y
            LY = b
        """
        return steps
    def checkPositiveDefinite(self):
        for i in self.eigenvalues:
            if i <= 0:
                return "The matrix is not positive definite" + str(self.eigenvalues)
        return True
    def checkSymmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i, j] != self.matrix[j, i]:
                    self.flag = False
                    return
                else:
                    continue
        return self.flag

    def decompose(self):
        for i in range(self.n):
            for j in range(i + 1):
                sumVar = 0
                if i == j:
                    for z in range(i):
                        sumVar += self.L[i, z] ** 2
                    self.L[i, j] = (self.matrix[i, j] - sumVar) ** 0.5
                else:
                    for z in range(j):
                        sumVar += self.L[j, z] * self.L[i, z]
                    self.L[i, j] = (self.matrix[i, j] - sumVar) / (self.L[j, j])

        

    def solve(self):
        start_time = time.time()
        self.decompose()
        for i in range(self.n):
            sumVar = 0
            for j in range(i):
                sumVar += self.L[i, j] * self.y[j]
            self.y[i] = (self.b[i] * 1.0 - sumVar) / self.L[i, i]

        for i in range(self.n - 1, -1, -1):
            sumVar = 0
            for j in range(i + 1, self.n):
                sumVar += self.L[j, i] * self.x[j]
            self.x[i] = (self.y[i] * 1.0 - sumVar) * 1.0 / self.L[i, i]
        self.execution_time = time.time() - start_time
