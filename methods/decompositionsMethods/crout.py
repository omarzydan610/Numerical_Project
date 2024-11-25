import time
import numpy as np


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
    
    def getExcutionTime(self):
        return self.execution_time
    
    def getSolution(self):
        return self.x
    
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
                sumVar += self.U[i, j] * self.x[j]
            self.x[i] = (self.y[i]  - sumVar) 
        self.execution_time = time.time() - start_time
    