import numpy as np
import time


class Doolittle:
    def __init__(self, matrix, b):
        self.A = matrix
        self.n = matrix.shape[0]
        self.b = b
        self.L = np.identity(self.n)  
        self.U = np.zeros_like(matrix)  
        self.y = np.zeros_like(self.b)  
        self.x = np.zeros_like(self.b)  
        self.execution_time = 0

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
        return self.x

                


class Cholesky:
    def __init__(self, matrix, b):
        self.matrix = matrix
        self.n = matrix.shape[0]
        self.b = b
        self.L = np.zeros_like(matrix)
        self.x = np.zeros_like(b)
        self.flag = True
        self.y = np.zeros_like(self.b)
        self.execution_time = 0

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
        return self.x

class Crout:
    def __init__(self, matrix, b):
        self.matrix = matrix
        self.n = matrix.shape[0]
        self.b = b
        self.L = np.zeros_like(matrix)
        self.x = np.zeros_like(b)
        self.U = np.zeros_like(matrix)
        self.y = np.zeros_like(self.b)
        self.execution_time = 0

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
        return self.x
    
    
    
    
    
    


# Example matrix A and vector b
A = np.array([[3, 2, -1],
              [2, -2, 4],
              [-1, 0.5, -1]], dtype=float)

b = np.array([1, -2, 0], dtype=float)

# Initialize and solve using Crout's decomposition
solver = Doolittle(A, b)

# Solve for x in A * x = b
x = solver.solve()
print("Solution vector x:", x)

# Verify the solution
Ax = A @ x
print("Computed A * x:", Ax)
print("Original vector b:", b)
print("time: ", solver.execution_time)
