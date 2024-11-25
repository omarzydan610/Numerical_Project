import time
import numpy as np


class Doolittle:
    def __init__(self, matrixA, matrixB, figures):
        self.A = np.matrix(matrixA)
        self.n = len(matrixA)
        self.b = matrixB
        self.L = np.identity(self.n)  
        self.U = np.zeros_like(matrixA)  
        self.y = np.zeros_like(self.b)  
        self.x = np.zeros_like(self.b)  
        self.execution_time = 0

    def getSteps(self):
        matrixL = ""
        for i in self.L:
            for j in i:
                matrixL += "|  "
                matrixL += f"{round(j, 3)}  "
            matrixL += "  |"
            matrixL += "\n      "
        steps = f"""
L matrix:
        {matrixL}
        """
        return steps

    def getExcutionTime(self):
        return self.execution_time
    
    def getSolution(self):
        return self.x
    
    def decompose(self):
        for k in range(self.n):
            for j in range(k, self.n):
                sum_var = 0
                for m in range(k): 
                    sum_var += self.L[k, m] * self.U[m, j]
                self.U[k, j] = self.A[k, j] - sum_var

            for i in range(k + 1, self.n):
                sum_var = 0
                for m in range(k):  # Replace sum with loop
                    sum_var += self.L[i, m] * self.U[m, k]
                self.L[i, k] = (self.A[i, k] - sum_var) / self.U[k, k]

    def solve(self):
        start_time = time.time()
        self.decompose()

        for i in range(self.n):
            sum_var = 0
            for j in range(i): 
                sum_var += self.L[i, j] * self.y[j]
            self.y[i] = self.b[i] - sum_var

        
        for i in range(self.n - 1, -1, -1):
            sum_var = 0
            for j in range(i + 1, self.n):  # Replace sum with loop
                sum_var += self.U[i, j] * self.x[j]
            self.x[i] = (self.y[i] - sum_var) / self.U[i, i]

        self.execution_time = time.time() - start_time
        
