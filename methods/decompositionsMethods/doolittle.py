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
        matrixU = ""
        for i in self.L:
            matrixL += "|  "
            for j in i:
                matrixL += f"{round(j, 3)}  "
            matrixL += "|\n        "
        for i in self.U:
            matrixU += "|  "
            for j in i:
                matrixU += f"{round(j, 3)}  "
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
        start_time = time.perf_counter_ns()
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

        self.execution_time = time.perf_counter_ns() - start_time
        
