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


class Crout:
    def __init__(self, matrixA, matrixB, figures):
        self.matrix = np.matrix(matrixA)
        self.n = len(matrixA)
        self.b = matrixB
        self.L = np.zeros_like(matrixA)
        self.x = np.zeros_like(matrixB)
        self.U = np.zeros_like(matrixA)
        self.y = np.zeros_like(self.b)
        self.execution_time = 0
        self.significantFigures = figures
    
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
        for i in self.U:
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

    def decompose(self):
        for i in range(self.n):
            for j in range(self.n):
                if j == 0:
                    self.L[i, j] = self.matrix[i, j]
                elif i == 0:
                    self.U[i, j] = self.matrix[i, j] / self.L[0, 0]
                elif i > j:
                    sumVar = 0
                    for z in range(j):
                        sumVar += self.L[i, z] * self.U[z, j]
                    self.L[i, j] = self.matrix[i, j] - sumVar
                elif i < j:
                    sumVar = 0
                    for z in range(i):
                        sumVar += self.L[i, z] * self.U[z, j]
                    self.U[i, j] = (self.matrix[i, j] - sumVar) / self.L[i, i]
                elif i == j:
                    sumVar = 0
                    for z in range(i):
                        sumVar += self.L[i, z] * self.U[z, j]
                    self.L[i, j] = self.matrix[i, j] - sumVar
                    self.U[i, j] = 1

        

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
                sumVar += self.U[i, j] * self.x[j]
            self.x[i] = (self.y[i]  - sumVar)
        self.x = [SFCalc(element, self.significantFigures) for element in self.x]
        self.y = [SFCalc(element, self.significantFigures) for element in self.y]
        self.execution_time = time.perf_counter_ns() - start_time
    