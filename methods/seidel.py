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
        self.steps=""

    def getSolution (self):
        return self.res
    
    def getIterations(self):
        return self.iteration

    def getExcutionTime(self):
        return self.time
    
    def getSteps(self):
        return self.steps

    def writeSolution(self, matrix, signifcantFigure):
        self.steps += "\n"
      

    def solve_with_iterations(self, num_iterations):
        self.steps += "\n"
        self.steps += f"Given intial guess of solution as {initial_guess}"
        self.steps += "\n \n"
        startTime=time.time()
        for t in range(num_iterations):
            self.steps += "\n"
            self.steps += f"iteration # {t+1}"
            self.steps += "\n"
            for i in range(len(self.matrixB)):
                sum = self.matrixB[i]
                self.steps += f"x{i} = ( {self.matrixB[i]} "
                for j in range(len(self.matrixB)):
                    if i != j:
                        sum -= round(float(self.matrixA[i][j] )* float(self.new[j]), self.SignificantFigures)
                        self.steps += f"+ {-1*self.matrixA[i][j]} ({self.new[j]}) "
                self.new[i] = round(sum / self.matrixA[i][i], self.SignificantFigures)
                self.steps += f")/{self.matrixA[i][i]} = {self.new[i]}\n"
            self.steps+="\n"
            
            self.old = self.new[:]
            self.steps+="\n"
            self.steps+=f"Solution after #{t+1} iteration is {self.old}"
            self.steps+="\n "
        endTime=time.time()
        self.time=endTime - startTime
        self.res=self.new

    def solve_with_tolerance(self, tolerance):
     startTime = time.time()
     old = self.new[:] 
     tolerance /= 100
     valid = False
     iteration = 0
     self.steps += "\n"
     self.steps += f"Given intial guess of solution as {initial_guess}"
     self.steps += "\n \n"

     while not valid:
        valid = True
        iteration += 1
        
        self.steps += "\n" 
        self.steps += f"iteration # {iteration}"
        self.steps += "\n"

        for i in range(len(self.matrixB)):
            sum = self.matrixB[i]
           
            self.steps += f"x{i} = ( {self.matrixB[i]} "
            for j in range(len(self.matrixB)):
                if i != j:
                    sum -= round(self.matrixA[i][j] * self.new[j], self.SignificantFigures)
                    if iteration<=10:
                     self.steps += f"+ {-1*self.matrixA[i][j]} ({self.new[j]}) "
            self.new[i] = round(sum / self.matrixA[i][i], self.SignificantFigures)
            
            self.steps += f")/{self.matrixA[i][i]} = {self.new[i]}"
            self.steps+="\n"
            relative_error = abs(self.new[i] - old[i]) / abs(self.new[i])
           
            self.steps+=f"   #Relative error of x{i} after {iteration} iteration = |{self.new[i]} - {old[i]} / {abs(self.new[i])}| ={relative_error}"
            self.steps+="\n"
            if relative_error > tolerance:
                valid = False
       
        self.steps+="\n"
        self.steps+=f"Solution after #{iteration} iteration is {self.new}"
        self.steps+="\n"
        old = self.new[:]

     endTime = time.time()
     self.time = endTime - startTime
     self.res = self.new[:]
     self.iteration = iteration

 
