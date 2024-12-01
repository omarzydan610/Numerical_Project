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
        if(diagonalyDominant(a)==False):
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
        if(diagonalyDominant(a)==False):
            return "The Matrix is Not Diagonally Dominant"
        seidel = Seidel(matrixA=a,matrixB=b,initial_guess=initial_guess,Figures=significantFigures)
        if NumberOfIterations!=-1:
            seidel.solve_with_iterations(num_iterations=NumberOfIterations)
            solution=["Gauss Seidel",seidel.getSolution(),seidel.getExcutionTime(),NumberOfIterations,seidel.getSteps()]
        else:
            seidel.solve_with_tolerance(tolerance=AbseluteRelativeError)
            solution=["Gauss Seidel",seidel.getSolution(),seidel.getExcutionTime(),seidel.getIterations(),seidel.getSteps()]
        return solution
        
    
    
def diagonalyDominant(matrix):
    greater=0
    for i in range(len(matrix)):
        sum=0
        for j in range (len(matrix[i])):
            sum+=abs(matrix[i][j])
        sum-=abs(matrix[i][i])
        if(abs(matrix[i][i])<sum):
            return False
        elif (abs(matrix[i][i])>sum):
            greater+=1
    if(greater>0):
        return True
    else:
        return False