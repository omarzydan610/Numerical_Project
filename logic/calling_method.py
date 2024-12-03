from methods.gauss import Gauss
from methods.jordan import GaussJordan
from methods.jacobi import Jacobi
from methods.seidel import Seidel
from methods.decompositionsMethods.doolittle import Doolittle
from methods.decompositionsMethods.cholesky import Cholesky
from methods.decompositionsMethods.crout import Crout
import numpy as np

def callingMethod(arr, method, numberEquations, initialGuess=0, significantFigures=3, NumberOfIterations=-1, AbseluteRelativeError=-1, scalling=False):
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
        
    b=[]
    
    for i in range (numberEquations):
        b.append(matrix_values[i][numberEquations])
        
    a=[]
    for i in range (numberEquations):
        row=[]
        for j in range (numberEquations):
            row.append(matrix_values[i][j])
        a.append(row)
    
    matrix = np.array(a)
    determinant = np.linalg.det(matrix)
    if(determinant==0):
        return "There Is No Unique Solution"


    if(method=="Gauss"):
        if scalling==False:
            gauss=Gauss()
            gauss.solve(system=matrix_values,n=numberEquations,signifcantFigure=significantFigures)
            solution=["Gauss",gauss.getSolution(),gauss.getExcutionTime(), gauss.grtSteps()]
            return solution
        elif scalling==True:
            gauss=Gauss()
            gauss.gaussScale_solve(system=matrix_values,n=numberEquations,signifcantFigure=significantFigures)
            solution=["Gauss",gauss.getSolution(),gauss.getExcutionTime(), gauss.grtSteps()]
            return solution
    
    elif(method=="Gauss Jordan"):
        if scalling==False:
            gaussJordan=GaussJordan()
            gaussJordan.solve(system=matrix_values,n=numberEquations,signifcantFigure=significantFigures)
            solution=["Gauss Jordan",gaussJordan.getSolution(),gaussJordan.getExcutionTime(),gaussJordan.grtSteps()]
            return solution
        elif scalling==True:
            gaussJordan=GaussJordan()
            gaussJordan.jordanScale_solve(system=matrix_values,n=numberEquations,signifcantFigure=significantFigures)
            solution=["Gauss Jordan",gaussJordan.getSolution(),gaussJordan.getExcutionTime(),gaussJordan.grtSteps()]
            return solution
    
    elif(method=="Doolittle"):
        dolittle = Doolittle(matrixA=a, matrixB=b, figures=significantFigures)
        dolittle.solve()
        solution=["Doolittle",dolittle.getSolution(),dolittle.getExcutionTime(), dolittle.getSteps()]
        return solution
    
    elif(method=="Crout"):
        crout = Crout(matrixA=a, matrixB=b, figures=significantFigures)
        crout.solve()
        solution=["Crout", crout.getSolution(), crout.getExcutionTime(), crout.getSteps()]
        return solution 

    elif(method=="Cholesky"):
        cholesky = Cholesky(matrixA=a, matrixB=b, figures=significantFigures)
        if cholesky.checkSymmetric():
            if cholesky.checkPositiveDefinite():
                cholesky.solve()
                solution=["Cholesky", cholesky.getSolution(), cholesky.getExcutionTime(), cholesky.getSteps()]
                return solution
            else :
                return "The Matrix is Not Positive Definit"
        else:
            return "The Matrix is Not Symmetric"

    elif(method=="Jacobi"):
        initial_guess=[float(element) for element in initialGuess]
        if(is_diagonally_dominant(a)==False):
            a,b=make_diagonally_dominant(a,b)
        if(is_diagonally_dominant(a)==False):
            return "The Matrix is Not Diagonally Dominant"
        jacobi=Jacobi(matrixA=a,matrixB=b,initial_guess=initial_guess,Figures=significantFigures)
        if NumberOfIterations!=-1:
            jacobi.solve_with_iterations(num_iterations=NumberOfIterations)
            solution=["Jacobi",jacobi.getSolution(),jacobi.getExecutionTime(),NumberOfIterations,jacobi.getSteps()]
        else:
            jacobi.solve_with_tolerance(tolerance=AbseluteRelativeError)
            solution=["Jacobi",jacobi.getSolution(),jacobi.getExecutionTime(),jacobi.getIterations(),jacobi.getSteps()]
            
        return solution
    

    elif(method=="Gauss Seidel"):
        initial_guess=[float(element) for element in initialGuess]
        if(is_diagonally_dominant(a)==False):
            a,b=make_diagonally_dominant(a,b)
        if(is_diagonally_dominant(a)==False):
            return "The Matrix is Not Diagonally Dominant"
        seidel = Seidel(matrixA=a,matrixB=b,initial_guess=initial_guess,Figures=significantFigures)
        if NumberOfIterations!=-1:
            seidel.solve_with_iterations(num_iterations=NumberOfIterations)
            solution=["Gauss Seidel",seidel.getSolution(),seidel.getExcutionTime(),NumberOfIterations,seidel.getSteps()]
        else:
            seidel.solve_with_tolerance(tolerance=AbseluteRelativeError)
            solution=["Gauss Seidel",seidel.getSolution(),seidel.getExcutionTime(),seidel.getIterations(),seidel.getSteps()]
        return solution
        
    
    
def is_diagonally_dominant(matrix):
    n = len(matrix)
    for i in range(n):
        row_sum = sum(abs(matrix[i][j]) for j in range(n) if j != i)
        if abs(matrix[i][i]) < row_sum:
            return False
    return True

def make_diagonally_dominant(matrix, b):
    matrix = np.array(matrix)  
    b = np.array(b) 
    original_matrix = matrix.copy()  
    original_b = b.copy()  
    n = len(matrix)

    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j
        if max_row != i:
            matrix[[i, max_row], :] = matrix[[max_row, i], :]
            b[[i, max_row]] = b[[max_row, i]]  
        row_sum = sum(abs(matrix[i][j]) for j in range(n) if j != i)
        if abs(matrix[i][i]) < row_sum:
            return original_matrix.tolist(), original_b.tolist()
    if not is_diagonally_dominant(matrix):
        return original_matrix.tolist(), original_b.tolist()
    return matrix.tolist(), b.tolist()
