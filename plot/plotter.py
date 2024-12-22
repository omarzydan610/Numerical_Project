import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
class Plotter:
    def __init__(self, equation: str, x_range=(0, 5)):
        self.equation = equation
        self.x_range = x_range

    def plot_equation(self):
        # Define the symbol for x
        x = sp.symbols('x')
    
        # Parse the equation
        equation = self.equation.replace('e', f"{sp.E}")  # Handle e**x and e properly
        expr = sp.sympify(equation)
        
        # Convert the symbolic expression to a Python function
        f = sp.lambdify(x, expr, "numpy")
        
        #   Generate x values within the specified range
        x_vals = np.linspace(self.x_range[0], self.x_range[1], 400)
        
        # If the expression is constant, just plot a horizontal line
        if expr.is_constant():
            y_vals = np.full_like(x_vals, expr.evalf())  # Fill y_vals with the constant value
        else:
            # Generate y values using the function for non-constant expressions
            y_vals = f(x_vals)
    
        # Plot the equation
        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=self.equation, color='b')
        plt.title(f"Plot of the equation: {self.equation}")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.grid(True)
        plt.legend()
        plt.show()

# Example usage with a constant equation
plotter = Plotter('sin(3*x)+sin(5*x)')
plotter.plot_equation()

