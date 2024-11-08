from methods.method import *
from methods.gauss import Gauss
from methods.jordan import GaussJordan
import numpy as np

def callingMethod(arr, method, numberEquations, initialGuess=0, significantFigures=3, NumberOfIterations=-1, AbseluteRelativeError=-1):
    matrix_values = []
    for row in arr:
        row_values = []
        for input_field in row:
                try:
                    value = float(input_field.text())
                except ValueError:
                    value = 0.0 
                row_values.append(value)
        matrix_values.append(row_values)
            
    a=[]
    for i in range (numberEquations):
        row=[]
        for j in range (numberEquations):
            row.append(matrix_values[i][j])
        a.append(row)
    
    matrix = np.array(a)
    determinant = np.linalg.det(matrix)
    if(determinant==0):
        return "error"


    if(AbseluteRelativeError==-1):
        flag=1
    else:
        flag=2


    if(method=="Gauss"):
        gauss=Gauss()
        gauss.solve(system=matrix_values,n=numberEquations,signifcantFigure=significantFigures)
        solution=["Gauss",gauss.getSolution(),gauss.getExcutionTime()]
        return solution
    
    elif(method=="Gauss Jordan"):
        gaussJordan=GaussJordan()
        gaussJordan.solve(system=matrix_values,n=numberEquations,signifcantFigure=significantFigures)
        solution=["Gauss Jordan",gaussJordan.getSolution(),gaussJordan.getExcutionTime()]
        print (solution)
        return solution
    
    # elif(method=="Doolittle"):
    #     Doolittle(matrix_values,numberEquations,significantFigures)
    #     pass
    # elif(method=="Crout"):
    #     Crout(matrix_values,numberEquations,significantFigures)
    #     pass
    # elif(method=="Cholesky"):
    #     Cholesky(matrix_values,numberEquations,significantFigures)
    #     pass
    # elif(method=="Jacobi"):
    #     Doolittle(matrix_values,numberEquations,significantFigures)
    #     pass
    # elif(method=="Gauss Seidel"):
    #     GaussSeidel(matrix_values,numberEquations,significantFigures,initialGuess,NumberOfIterations,AbseluteRelativeError,flag)
    #     pass