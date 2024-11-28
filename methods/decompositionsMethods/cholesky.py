import time
import numpy as np
import math

def SFCalc(number, significantFigures):
    if number == 0:
        return 0

    # Calculate the order of magnitude of the number
    order_of_magnitude = math.floor(math.log10(abs(number)))
    
    # Scale the number to the desired significant figures
    scale = 10**(significantFigures - 1 - order_of_magnitude)
    scaled_number = math.trunc(number * scale)
    
    # Scale back to the original magnitude
    result = scaled_number / scale
    return result


class Cholesky:
    def __init__(self, matrixA, matrixB, figures):
        self.eigenvalues = np.linalg.eigvals(matrixA)
        self.matrix = np.matrix(matrixA)
        self.n = len(matrixA)
        self.b = matrixB
        self.L = np.zeros_like(matrixA)
        self.x = np.zeros_like(matrixB)
        self.flag = True
        self.y = np.zeros_like(self.b)
        self.significantFigures = figures
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
                matrixL += f"{SFCalc(j, 3)}  "
            matrixL += "|\n        "
        for i in np.transpose(self.L):
            matrixU += "|  "
            for j in i:
                matrixU += f"{SFCalc(j, 3)}  "
            matrixU += "|\n        "
        steps = f"""
the equation is:
            AX = b
            A = LU
            LUX = b
            LY = b
            UX = Y

L matrix:
        {matrixL}

U matrix:
        {matrixU}

Y vector = {self.y}

x vector = {self.x}
"""
        return steps
    def checkPositiveDefinite(self):
        for i in self.eigenvalues:
            if i <= 0:
                return False
        return True

    def checkSymmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i, j] != self.matrix[j, i]:
                    return False
                else:
                    continue
        return True

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
        start_time = time.perf_counter_ns()
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
        self.x = [SFCalc(element, self.significantFigures) for element in self.x]
        self.y = [SFCalc(element, self.significantFigures) for element in self.y]
        self.execution_time = time.perf_counter_ns() - start_time
