import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.optimize import fsolve

class Plotter:
    def __init__(self, equation: str, x_range=None):
        self.equation = equation
        self.x_range = x_range or self._generate_x_range()

    def _generate_x_range(self):
        x = sp.symbols('x')
        equation = self.equation.replace('e', f"{sp.E}")  
        expr = sp.sympify(equation)
        f = sp.lambdify(x, expr, "numpy")

        def find_roots(func):
            roots = []
            guesses = np.linspace(-10, 10, 100)
            for guess in guesses:
                try:
                    root = fsolve(func, guess)[0]
                    if root not in roots and np.isclose(func(root), 0):
                        roots.append(root)
                except:
                    pass
            return roots

        roots = find_roots(f)
        if roots:
            min_root, max_root = min(roots), max(roots)
            return (float(min_root) - 1, float(max_root) + 1)
        return (-10, 10)

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
        plt.axhline(0, color='black', linewidth=2)
        plt.axvline(0, color='black', linewidth=2)
        plt.grid(True)
        plt.legend()
        plt.show()

    def plot_g_x(self, equation):
        x = sp.symbols('x')
        equation_f = self.equation.replace('e', f"{sp.E}")  
        equation_g = equation.replace('e', f"{sp.E}")
        expr_f = sp.sympify(equation_f)
        expr_g = sp.sympify(equation_g)
        f = sp.lambdify(x, expr_f, "numpy")
        g = sp.lambdify(x, expr_g, "numpy")
        x_vals = np.linspace(self.x_range[0], self.x_range[1], 400)
        if expr_f.is_constant():
            y_vals_f = np.full_like(x_vals, expr_f.evalf())  
        else:
            y_vals_f = f(x_vals)
        y_vals_g = g(x_vals)
        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals_f, label=self.equation, color='b')
        plt.plot(x_vals, y_vals_g, label=equation, color='r')
        plt.title(f"Plot of the equations: g(x) = {self.equation} ")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(0, color='black', linewidth=2)
        plt.axvline(0, color='black', linewidth=2)
        plt.grid(True)
        plt.legend()
        plt.show()


x = Plotter("e^x + x^2 - x - 4")
x.plot_equation()
x.plot_g_x("x")