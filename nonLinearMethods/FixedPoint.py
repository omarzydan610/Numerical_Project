import time
import numpy as np
from sympy import sympify, lambdify, symbols

class Fixed_point:
    def __init__(self):
        self.root = 0
        self.time = 0.0
        self.steps = ""
        self.gx = None
        self.iteration = 0
        self.tolerance = 0

    def getIterations(self):
        return self.iteration

    def getExecutionTime(self):
        return self.time

    def getTolerance(self):
        return self.tolerance

    def set_function(self, gx):
        self.gx = gx

    
    def solve(self, initial_guess, max_iteration, tolerance, significantFigures):
        
        startTime = time.perf_counter_ns()
        x0 = initial_guess

        for i in range(1, max_iteration + 1):
            x1 = self.gx(x0)

            if isinstance(x1, (float, int)) and (np.isnan(x1) or np.isinf(x1)):
                raise ValueError("Invalid operation detected (e.g., division by zero or negative square root).")

            x1 = round(x1, significantFigures)
            self.steps += f"Iteration {i}: g({x0:.{significantFigures}f})={x1}  ,  x = {x1:.{significantFigures}f}  \n"

            relative_error = abs(x1 - x0) / abs(x1) if x1 != 0 else float('inf')
            self.steps += f"   relative error = {relative_error}\n"

            if relative_error <= tolerance:
                self.root = round(x1, significantFigures)
                self.iteration = i
                self.tolerance = relative_error
                endTime = time.perf_counter_ns()
                self.time = endTime - startTime
                return f"{self.root:.{significantFigures}f}"

            x0 = x1

        self.root = round(x1, significantFigures)
        self.iteration = max_iteration
        self.tolerance = relative_error

        endTime = time.perf_counter_ns()
        self.time = endTime - startTime
        return f"{self.root:.{significantFigures}f}"


# #testcase

# gui_str = "sin(sqrt(x))"   #string come from gui
# x = symbols('x') 
# expr = sympify(gui_str)  
# fun = lambdify(x, expr)  

# solver = Fixed_point()
# solver.set_function(fun)

# root = solver.solve(initial_guess=0.5, max_iteration=100, tolerance=0.0001, significantFigures=6)

# print("Test Root found:", root)
# print("Steps:\n", solver.steps)
