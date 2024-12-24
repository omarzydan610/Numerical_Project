import math
import time

class Bracketing_methods:
    def __init__(self, equation, x_upper, x_lower, relativeError, significantFigures, maxNumOfIterations):
        self.equation = equation.replace("^", "**")
        self.x_upper = x_upper
        self.x_lower = x_lower
        self.relativeError = relativeError
        self.significantFigures = significantFigures
        self.maxNumOfIterations = maxNumOfIterations
        self.steps = []
        self.execution_time = None

    def get_equation(self):
        return self.equation

    def get_steps(self):
        return self.steps

    def get_execution_time(self):
        return self.execution_time
    
    

    def f(self, x):
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names['x'] = x
        return eval(self.equation, {"__builtins__": {}}, allowed_names)

    def SFCalc(self, number, significantFigures):
        if number == 0:
            return 0
        order_of_magnitude = math.floor(math.log10(abs(number)))
        scale = 10 ** (significantFigures - 1 - order_of_magnitude)
        scaled_number = math.trunc(number * scale)
        result = scaled_number / scale
        return result

    def bisection(self):
        x_lower = self.x_lower
        x_upper = self.x_upper
        max_iter = self.maxNumOfIterations
        rel_error = self.relativeError
        sig_fig = self.significantFigures

        step = 0
        xr_old = None

        start_time = time.time()
        while step < max_iter:
            xr = (x_lower + x_upper) / 2
            if xr_old is not None:
                ea = abs((xr - xr_old) / xr) * 100
            else:
                ea = None

            self.steps.append(f"Iteration {step + 1}: x_lower = {x_lower}, x_upper = {x_upper}, xr = {xr}, ea = {ea}")

            if ea is not None and ea < rel_error:
                break

            f_lower = self.f(x_lower)
            f_upper = self.f(x_upper)
            f_mid = self.f(xr)

            if f_lower * f_mid < 0:
                x_upper = xr
            else:
                x_lower = xr

            xr_old = xr
            step += 1
        end_time = time.time()

        xr = self.SFCalc(xr, sig_fig)
        self.execution_time = end_time - start_time
        return xr

    def false_position(self):
        x_lower = self.x_lower
        x_upper = self.x_upper
        max_iter = self.maxNumOfIterations
        rel_error = self.relativeError
        sig_fig = self.significantFigures

        step = 0
        xr_old = None

        start_time = time.time()
        while step < max_iter:
            f_lower = self.f(x_lower)
            f_upper = self.f(x_upper)
            xr = x_upper - (f_upper * (x_lower - x_upper) / (f_lower - f_upper))

            if xr_old is not None:
                if xr == 0:
                    break
                ea = abs((xr - xr_old) / xr) * 100
            else:
                ea = None

            self.steps.append(f"Iteration {step + 1}: x_lower = {x_lower}, x_upper = {x_upper}, xr = {xr}, ea = {ea}")

            if ea is not None and ea < rel_error:
                break

            f_mid = self.f(xr)

            if f_lower * f_mid < 0:
                x_upper = xr
            else:
                x_lower = xr

            xr_old = xr
            step += 1
        end_time = time.time()

        xr = self.SFCalc(xr, sig_fig)
        self.execution_time = end_time - start_time
        return xr


# Example usage of the Bracketing_methods class

# Define the equation as a string
equation = "sin(x) - e^x + e^(-x)"

# Define the parameters
x_upper = 2
x_lower = 0
relativeError = 0.0001  # 1%
significantFigures = 5
maxNumOfIterations = 100

# Create an instance of Bracketing_methods
bracketing = Bracketing_methods(equation, x_upper, x_lower, relativeError, significantFigures, maxNumOfIterations)

# Perform the bisection method
root_bisection = bracketing.bisection()
print("Bisection Method:")
print(f"Root: {root_bisection}")
print(f"Steps: {bracketing.get_steps()}")
print(f"Execution Time: {bracketing.get_execution_time()} seconds")

# Perform the false position method
bracketing.steps = []  # Clear previous steps
root_false_position = bracketing.false_position()
print("\nFalse Position Method:")
print(f"Root: {root_false_position}")
print(f"Steps: {bracketing.get_steps()}")
print(f"Execution Time: {bracketing.get_execution_time()} seconds")
