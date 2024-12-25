import time
import numpy as np
import math
from sympy import sympify, lambdify, symbols

class Fixed_point:
    def __init__(self):
        self.root = 0
        self.time = 0.0
        self.steps = ""
        self.gx = None
        self.iteration = 0
        self.tolerance = 0
        self.correctSF = 0

    def getIterations(self):
        return self.iteration

    def getExecutionTime(self):
        return self.time

    def getTolerance(self):
        return self.tolerance
    
    def getSteps(self):
        return self.steps
    
    def getCorrectSF(self):
        return self.correctSF

    def set_function(self, gx):
        gui_str = gx   #string come from gui
        x = symbols('x') 
        expr = sympify(gui_str)  
        fun = lambdify(x, expr) 
        self.gx = fun

    
    def solve(self, initial_guess, max_iteration, tolerance, significantFigures):
        
        startTime = time.perf_counter_ns()
        x0 = initial_guess

        for i in range(1, max_iteration + 1):
            x1 = float(self.gx(x0))

            if abs(x1) > 1e6:  # Divergence threshold
              raise ValueError(f"Divergence detected: g(x) produced too large a value.{i}")

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
                try:
                    self.correctSF = math.floor(2 - math.log10(relative_error / 0.5))
                except ValueError as e:
                    self.correctSF = float('inf')
                return f"{self.root:.{significantFigures}f}"

            x0 = x1

        self.root = round(x1, significantFigures)
        self.iteration = max_iteration
        self.tolerance = relative_error

        endTime = time.perf_counter_ns()
        self.time = endTime - startTime
        try:
            self.correctSF = math.floor(2 - math.log10(relative_error / 0.5))
        except ValueError as e:
            self.correctSF = float('inf')
        return f"{self.root:.{significantFigures}f}"


