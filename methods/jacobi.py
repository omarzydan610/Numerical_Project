import time
class Jacobi:

    def __init__(self, matrixA, matrixB, initial_guess,Figures):
        
        self.matrixA = matrixA
        self.matrixB = matrixB
        self.old = initial_guess
        self.new = [0] * len(initial_guess)
        self.SignificantFigures=Figures
        
        self.res = []
        self.time = 0.0
        self.iterations=0
        
    def getSolution (self):
        return self.res
    
    def getExcutionTime (self):
        return self.time
    
    def getIterations(self):
        return self.iterations

    def solve_with_iterations(self, num_iterations):
        start_time = time.time()
        for t in range(num_iterations):
            for i in range(len(self.matrixB)):
                self.new[i] = self.matrixB[i]
                for j in range(len(self.matrixB)):
                    if i != j:
                        self.new[i] -= round(float(self.matrixA[i][j] )* float(self.old[j]),self.SignificantFigures)
                self.new[i] /= round(self.matrixA[i][i],self.SignificantFigures)
            self.old = self.new[:]
            self.new= [round(num, self.SignificantFigures) for num in self.new]
        end_time = time.time()
        self.time = end_time - start_time  
        self.res=self.new

    def solve_with_tolerance(self, tolerance):
        start_time = time.time()
        tolerance /= 100 
        valid = False
        iteration = 0
        while not valid:
            valid = True
            iteration += 1
            for i in range(len(self.matrixB)):
                self.new[i] = self.matrixB[i]
                for j in range(len(self.matrixB)):
                    if i != j:
                        self.new[i] -= round(float(self.matrixA[i][j]) * float(self.old[j]),self.SignificantFigures)
                self.new[i] /= round(self.matrixA[i][i],self.SignificantFigures)
                
                relative_error = abs(float(self.new[i]) - float(self.old[i])) / abs(self.new[i])
                if relative_error > tolerance:
                    valid = False
            
            self.old = self.new[:]
            self.new= [round(num, self.SignificantFigures) for num in self.new]
        end_time = time.time()
        self.time = end_time - start_time  
        self.res=self.new
        self.iterations=iteration
    


