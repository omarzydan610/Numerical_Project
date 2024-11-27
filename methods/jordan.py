import numpy as np
import time

class GaussJordan :

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
    

    def jordanScale_solve(self, system, n, signifcantFigure):

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

    
        for i in range(n-1, -1, -1):                                        #backward elimination
                for j in range(i-1, -1, -1):
                    factor = system[j][i]/system[i][i]
                    system[j][i] -= system[i][i]*factor
                    system[j][n] -= system[i][n]*factor


        x = np.zeros(n)     
        for i in range(n):
            x[i] = system[i][n]/system[i][i]


        self.res = x    
    
    def solve (self, system, n, signifcantFigure=3):

        system = np.array(system, dtype=float)
        x = np.zeros(n)

        start_time = time.perf_counter()
        
        for i in range(n):
            self.steps += f">> step {i+1}\n"
            max_value = abs(system[i][i])
            max_index = i

            for j in range (i+1, n):                                           #find the largest pivot
                if abs(system[j][i]) > max_value :
                    max_value = abs(system[j][i])
                    max_index = j
            self.steps += f"    The largest pivot is '{round(max_value, signifcantFigure)}' at index '{max_index+1}'\n"
            
            if max_index != i:                                                #interchanging
                system[[i, max_index]] = system[[max_index, i]]
            self.steps += "    System after interchanging:"
            self.writeSolution(system, signifcantFigure)

            for k in range(i+1, n):                                          #forward elimination
                factor = (system[k][i]/system[i][i])
                for j in range(i, n+1):
                    system[k][j] = -1*factor*system[i][j] + system[k][j]
            self.steps += "    System after forward elimination:"
            self.writeSolution(system,signifcantFigure)
            self.steps += "\n\n"

        
        step_number = n+1
        for i in range(n-1, -1, -1):                                        #backward elimination
            self.steps += f">> step {step_number}\n"
            for j in range(i-1, -1, -1):
                factor = system[j][i]/system[i][i]
                system[j][i] -= system[i][i]*factor
                system[j][n] -= system[i][n]*factor
            self.steps += f"    System after #{step_number-n} backward elimination:"
            self.writeSolution(system,signifcantFigure)
            self.steps += "\n\n"
            step_number += 1

        
        for i in range(n):
            x[i] = system[i][n]/system[i][i]
        
                
        end_time = time.perf_counter()
        self.time = end_time - start_time                         # set excution time
        self.res = np.round(x, signifcantFigure)                  #set solution
        self.setBackwardSubstitution(x, n, signifcantFigure)