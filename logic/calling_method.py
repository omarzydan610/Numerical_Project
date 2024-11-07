from methods.method import *

def callingMethod(arr, method, numberEquations, initialGuess=0, significantFigures=1, NumberOfIterations=-1, AbseluteRelativeError=-1):
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
            
    


    if(AbseluteRelativeError==-1):
        flag=1
    else:
        flag=2


    if(method=="Gauss"):
        Gauss(matrix_values,numberEquations,significantFigures)
        pass
    elif(method=="Gauss jordan"):
        GaussJordan(matrix_values,numberEquations,significantFigures)
        pass
    elif(method=="Doolittle"):
        Doolittle(matrix_values,numberEquations,significantFigures)
        pass
    elif(method=="Crout"):
        Crout(matrix_values,numberEquations,significantFigures)
        pass
    elif(method=="Cholesky"):
        Cholesky(matrix_values,numberEquations,significantFigures)
        pass
    elif(method=="Jacobi"):
        Doolittle(matrix_values,numberEquations,significantFigures)
        pass
    elif(method=="Gauss Seidel"):
        GaussSeidel(matrix_values,numberEquations,significantFigures,initialGuess,NumberOfIterations,AbseluteRelativeError,flag)
        pass
    pass