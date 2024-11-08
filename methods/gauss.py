import numpy as np
import time

class Gauss :

    def __init__(self):
        self.res = np.array([])
        self.time = 0.0
        
    
    def getSolution (self):
        return self.res
    
    def getExcutionTime (self):
        return self.time
    
    def solve (self, system, n, signifcantFigure=3):

        system = np.array(system, dtype=float)
        x = np.zeros(n)

        start_time = time.time()
        
        for i in range(n):
            max_value = abs(system[i][i])
            max_index = i

            for j in range (i+1, n):                                  #find the largest pivot
                if abs(system[j][i]) > max_value :
                    max_value = abs(system[j][i])
                    max_index = j
            
            if max_index != i:                                         #interchanging
                system[[i, max_index]] = system[[max_index, i]]
                

            for k in range(i+1, n):                                   #forward elimination          
                factor = (system[k][i]/system[i][i])
                for j in range(i, n+1):
                    system[k][j] = -1*factor*system[i][j] + system[k][j]

                
        for k in range(n-1, -1, -1):                                  #backward substitution
            d = 0
            for j in range(k+1, n):
                d += system[k][j]*x[j]

            x[k] = (system[k][n] - d)/system[k][k]
                
        end_time = time.time()
        self.time = end_time - start_time                    # set excution time
        self.res = np.round(x, signifcantFigure)             #set solution
                    




