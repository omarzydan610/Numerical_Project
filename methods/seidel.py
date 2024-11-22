import time
class Seidel:
    
    def __init__(self, matrixA, matrixB, initial_guess, Figures):
        self.matrixA = matrixA
        self.matrixB = matrixB
        self.new =initial_guess
        self.SignificantFigures = Figures
        self.iteration=0
        self.time=0
        self.res=[]

    def getSolution (self):
        return self.res
    
    def getIterations(self):
        return self.iteration

    def getExcutionTime(self):
        return self.time
    
    def solve_with_iterations(self, num_iterations):
        startTime=time.time()
        for t in range(num_iterations):
            for i in range(len(self.matrixB)):
                sum = self.matrixB[i]
                for j in range(len(self.matrixB)):
                    if i != j:
                        sum -= round(float(self.matrixA[i][j] )* float(self.new[j]), self.SignificantFigures)
                self.new[i] = round(sum / self.matrixA[i][i], self.SignificantFigures)
            self.old = self.new[:]
        endTime=time.time()
        self.time=endTime - startTime
        self.res=self.new

    def solve_with_tolerance(self, tolerance):
        startTime=time.time()
        tolerance /= 100
        valid = False
        iteration = 0
        while not valid:
            valid = True
            iteration += 1
            for i in range(len(self.matrixB)):
                sum = self.matrixB[i]
                for j in range(len(self.matrixB)):
                    if i != j:
                        sum -= round(float(self.matrixA[i][j]) * float(self.new[j]), self.SignificantFigures)
                self.new[i] = round(sum / self.matrixA[i][i], self.SignificantFigures)

                relative_error = abs(self.new[i] - self.old[i]) / abs(self.new[i])
                if relative_error > tolerance:
                    valid = False
            self.old = self.new[:]
        endTime=time.time()
        self.time=endTime - startTime
        self.res=self.new
        self.iterations=iteration
    