import numpy as np
import time

class Gauss :

    def __init__(self):
        self.res = np.array([])
        self.time = 0.0
        self.steps=""""""
        
    def grtSteps(self):
        return self.steps
    

    def writeSolution(self, matrix, signifcantFigure):
        self.steps += "\n"
        for i in matrix:
            self.steps += "        |  "
            for j in i:
                self.steps += f"{round(j,signifcantFigure)}   "
            self.steps += "|\n"

    def setBackwardSubstitution(self, x, index, signifcantFigure):
        self.steps += ">> final step\n" 
        self.steps += "    backward substitution\n"
        for i in x[-1::-1]:
            self.steps += f"        X{index} = {round(i, signifcantFigure)}\n" 
            index -= 1
        

    def getSolution (self):
        return self.res
    
    def getExcutionTime (self):
        return self.time
    

    def gaussScale(self, system, n):

        system = np.array(system, dtype=float)

        A = system[:, :-1]  
        b = system[:, -1]   
        A = np.array(A, dtype=float)  
        b = np.array(b, dtype=float)

        scale = np.max(np.abs(A), axis=1)

    
        for k in range(n - 1):                                     # Forward Elimination
            pivot_row = np.argmax(np.abs(system[k:n, k]) / scale[k:n]) + k
            if pivot_row != k:
                system[[k, pivot_row]] = system[[pivot_row, k]]     # Swap rows
                scale[[k, pivot_row]] = scale[[pivot_row, k]]       # Swap scaling factors

        
            for i in range(k + 1, n):
                factor = system[i, k] / system[k, k]
                system[i, k:] -= factor * system[k, k:]

        x = np.zeros(n)                                              # Back Substitution
        for i in range(n - 1, -1, -1):
            x[i] = (system[i, -1] - np.dot(system[i, i + 1:n], x[i + 1:n])) / system[i, i]
        return x



    def solve (self, system, n, signifcantFigure=3):

        system = np.array(system, dtype=float)
        x = np.zeros(n)

        start_time = time.time()
        
        for i in range(n):
            self.steps += f">> step {i+1}\n"
            
            max_value = abs(system[i][i])
            max_index = i

            for j in range (i+1, n):                                  #find the largest pivot
                if abs(system[j][i]) > max_value :
                    max_value = abs(system[j][i])
                    max_index = j
            self.steps += f"    The largest pivot is '{round(max_value, signifcantFigure)}' at index '{max_index+1}'\n"
            
            if max_index != i:                                         #interchanging
                system[[i, max_index]] = system[[max_index, i]]
            
            self.steps += "    System after interchanging:"
            self.writeSolution(system, signifcantFigure)

            for k in range(i+1, n):                                   #forward elimination          
                factor = (system[k][i]/system[i][i])
                for j in range(i, n+1):
                    system[k][j] = -1*factor*system[i][j] + system[k][j]
            
            self.steps += "    System after forward elimination:"
            self.writeSolution(system,signifcantFigure)
            self.steps += "\n\n"


                
        for k in range(n-1, -1, -1):                                  #backward substitution
            d = 0
            for j in range(k+1, n):
                d += system[k][j]*x[j]

            x[k] = (system[k][n] - d)/system[k][k]
                
        end_time = time.time()
        self.time = end_time - start_time                    # set excution time
        self.res = np.round(x, signifcantFigure)             #set solution
        
        self.setBackwardSubstitution(x, n, signifcantFigure)

