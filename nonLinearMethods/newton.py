from sympy import *
import time
import math

class Newton:

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

    @staticmethod
    def derivative(func, x, h=1e-5):
        return (func(x + h) - func(x - h)) / (2 * h)


    @staticmethod
    def second_derivative(func, x, h=1e-5):
        return (func(x + h) - 2 * func(x) + func(x - h)) / h**2


    def original(self, func, x, tolerance, max_iterations, SF):
        oldx = x
        newx = x
        counter = 0
        error = 1
        start_time = time.time()
        self.steps += " i \t xi \t  εt %"
        self.steps += f"\n {counter} \t {x} \t {error*100}"
        while(counter <= max_iterations and error >= tolerance):

            derivative = self.derivative(func, oldx)
            if(derivative == 0):
                raise ValueError(f"Derivative is zero at {counter} iteration. Method fails.")
        

            newx = oldx - (func(oldx)/ derivative)
            newx = round(newx,SF)

            if(newx != 0):
                error = abs(newx - oldx)/newx
        
            counter+=1
            oldx = newx
            restr = f"%{SF/10}f" %newx
            self.steps += f"\n {counter} \t {restr} \t {error*100}"

        if(counter > max_iterations and error > tolerance):
            raise ValueError("The Method diverges.")

        end_time = time.time()
        self.time = end_time - start_time
        self.iterations = counter

        try:
            self.correctSF = math.floor(2-math.log10(error/0.5))
        except ValueError as e:
            self.correctSF = float('inf')

        self.error = error*100

        self.res = f"%{SF/10}f" % newx


    def modified(self,func, x, tolerance, max_iterations, SF):
        oldx = x
        newx = x
        counter = 0
        error = 1
        start_time = time.time()
        self.steps += " i \t xi \t  εt %"
        self.steps += f"\n {counter} \t {x} \t {error*100}"
        while(counter <= max_iterations and error >= tolerance):
    
            derivative = (self.derivative(func, oldx))**2 - func(oldx)*self.second_derivative(func,oldx)
            if(derivative == 0):
                raise ValueError(f"The denominator is zero at {counter} iteration. Method fails.")

            newx = oldx - ((func(oldx)*self.derivative(func,oldx))/ derivative)
            newx = round(newx, SF)

            if(newx != 0):
                error = abs(newx - oldx)/newx
        
            counter+=1
            oldx = newx
            restr = f"%{SF/10}f" %newx
            self.steps += f"\n {counter} \t {restr} \t {error*100}"

        if(counter > max_iterations and error > tolerance):
            raise ValueError("The Method diverges.")

        end_time = time.time()
        self.time = end_time - start_time 
        self.iterations = counter

        try:
            self.correctSF = math.floor(2-math.log10(error/0.5))
        except ValueError as e:
            self.correctSF = float('inf')

        self.error = error*100
        self.res = f"%{SF/10}f" % newx




#test

x = symbols('x')
expr_str = "x**3-2*x**2-4*x+8"
expr = sympify(expr_str)
func = lambdify(x, expr)


n = Newton()
n.modified(func, 1.2,0.001, 100, 5)
print(n.getSteps())
# print(n.getSolution())
# print(n.getIterations())
# print(n.getError())
# print(n.getcorrectSF())