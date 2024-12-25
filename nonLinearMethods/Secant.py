import time
from sympy import sympify, lambdify, symbols


class Secant:
    def __init__(self):
        self.root = 0
        self.time = 0.0
        self.steps = ""
        self.iteration = 0
        self.tolerance = 0
        self.fx = None
    
    def set_function(self, fx): 
        gui_str = fx    #string come from gui
        x = symbols('x') 
        expr = sympify(gui_str)  
        fun = lambdify(x, expr)  
        self.fx = fun

    def getIterations(self):
        return self.iteration

    def getExecutionTime(self):
        return self.time
    
    def getTolerance(self):
        return self.tolerance 
    
    def getSteps(self):
        return self.steps

    def solve(self, x0, x1, max_iteration, tolerance, significantFigures):
        startTime = time.perf_counter_ns()
        for i in range(1, max_iteration + 1):
            fx0 = round(self.fx(x0), significantFigures)
            fx1 = round(self.fx(x1), significantFigures)
            
            if fx1 - fx0 == 0:
                raise ZeroDivisionError ("Division by zero encountered at iteration {i}.")
            
          
            xi = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
            xi = round(xi, significantFigures)
            
          
            if xi != xi or xi == float('inf') or xi == float('-inf'):
               raise KeyError ("Error: Invalid result encountered at iteration {i}.")

            relative_error = abs(xi - x1) / abs(xi) if xi != 0 else float('inf')
        
            
           
            self.steps += (
                f"Iteration {i}:\n"
                f"  x0 = {x0:.{significantFigures}f}, f(x0) = {fx0:.{significantFigures}f}\n"
                f"  x1 = {x1:.{significantFigures}f}, f(x1) = {fx1:.{significantFigures}f}\n"
                f"  xi = {xi:.{significantFigures}f}, relative error = {relative_error}\n"
            )
            
            if relative_error <= tolerance:
                self.root = xi
                self.iteration = i
                self.tolerance = relative_error
                self.time = time.perf_counter_ns() - startTime
                return f"{self.root:.{significantFigures}f}"
            
            x0 = x1 
            x1 = xi
        
        self.root = xi
        self.iteration = max_iteration
        self.tolerance = relative_error
        self.time = time.perf_counter_ns() - startTime
        return f"{self.root:.{significantFigures}f}"







# # #testcase
func = "e^(-x)"


fun = "sin(x) "    #string come from gui


solver = Secant()
solver.set_function(fun)
try:
    root = solver.solve(x0=0.1,  x1=3.0416, max_iteration=3, tolerance=0.0001, significantFigures=5)
except ValueError as e:
    print(f"An error occurred: {e}")
#
# print("Test Root found:", root)
# print("Steps:\n", solver.steps)
