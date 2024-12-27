from sympy import *
import time
import math

class Bisection:

    def __init__(self):
        self.res = 0
        self.time = 0.0
        self.iterations = 0
        self.error = 0
        self.correctSF = 0
        self.steps = ""

    def getSolution (self):
        return self.res
      
    def getExcutionTime (self):
        return self.time
    
    def getIterations (self):
        return self.iterations

    def getError (self):
        return self.error
    
    def getcorrectSF (self):
        return self.correctSF
    
    def getSteps(self):
        return self.steps

    def solve(self,func,a, b, tolerance,max_iterations, SF):
        X = symbols('x')
        expr_str = func
        expr = sympify(expr_str)
        func = lambdify(X, expr)
        x = a
        prev_x = 0  
        error = 1
        counter = 0
        start_time = time.perf_counter_ns()
        self.steps += " i \t Xl \t Xu \t Xr \t sign \t εt %"
        while ( error >= tolerance and counter<=max_iterations):

            if func(a)*func(b) > 0 :
                raise ValueError("No root in the given interval")
            
            prev_x = x
            x = (a + b) / 2
            x = round(x,SF)
            counter+=1
            if(x != 0):
                error = abs((x - prev_x) / x)
            signn = "(+)"
            if(func(x) < 0):
                signn = "(-)"
            self.steps += f" \n {counter} \t {a} \t {b} \t {x} \t {signn} \t {error*100}"

            if func(x) == 0:  
                break

            if func(x) * func(a) < 0:
                b = x
            else:
                a = x


        try:
            self.correctSF = math.floor(2-math.log10(error/0.5))
        except ValueError as e:
            self.correctSF = float('inf')

        self.error = error*100
        end_time = time.perf_counter_ns()
        self.time = end_time - start_time
        self.iterations = counter
        self.res = f"%{SF/10}f" % x





# func = "e^(-x)"
#
# b = Bisection()
# try:
#     b.solve(func, 1, 2, 1e-4, 100, 5)
#     print(b.getSteps())
# except ValueError as e:
#     print(f"An error occurred: {e}")
