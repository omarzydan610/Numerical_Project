import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

class Plotter:
    def __init__(self, equation: str, x_range=None):
        self.equation = equation
        self.x_range = x_range or self._generate_x_range()

    def _generate_x_range(self):
        x = sp.symbols('x')
        equation = self.equation.replace('e', f"{sp.E}")  
        expr = sp.sympify(equation)
        roots = sp.solvers.solve(expr, x)
        if roots:
            roots = [root.evalf() for root in roots if root.is_real]
            if roots:
                min_root, max_root = min(roots), max(roots)
                return (float(min_root) - 1, float(max_root) + 1)
        return (-50, 50)

    def plot_equation(self):
        x = sp.symbols('x')
        equation = self.equation.replace('e', f"{sp.E}")  
        expr = sp.sympify(equation)
        f = sp.lambdify(x, expr, "numpy")
        x_vals = np.linspace(self.x_range[0], self.x_range[1], 400)
        if expr.is_constant():
            y_vals = np.full_like(x_vals, expr.evalf())  
        else:
            y_vals = f(x_vals)
        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=self.equation, color='b')
        plt.title(f"Plot of the equation: {self.equation}")
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.axhline(0, color='black',linewidth=2)
        plt.axvline(0, color='black',linewidth=2)
        plt.grid(True)
        plt.legend()
        plt.show()
