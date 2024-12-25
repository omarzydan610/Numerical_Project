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
        expr = sp.sympify(self.equation)
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
        expr = sp.sympify(self.equation)  # Parse the equation
        f = sp.lambdify(x, expr, "numpy")  # Lambdify to numpy

        # Generate x values for plotting
        x_vals = np.linspace(self.x_range[0], self.x_range[1], 400)

        # Evaluate y values for the equation
        try:
            y_vals = f(x_vals)  # Function applied to x values
        except Exception as e:
            print(f"Error evaluating function: {e}")
            return

        # Plotting the equation
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
        expr_f = sp.sympify(self.equation)
        expr_g = sp.sympify(equation)
        f = sp.lambdify(x, expr_f, "numpy")
        g = sp.lambdify(x, expr_g, "numpy")

        def find_intersections(func1, func2):
            def diff_func(x_val):
                return func1(x_val) - func2(x_val)

            guesses = np.linspace(self.x_range[0], self.x_range[1], 400)
            intersections = []
            for guess in guesses:
                try:
                    intersection = fsolve(diff_func, guess)[0]
                    if intersection not in intersections and np.isclose(diff_func(intersection), 0):
                        intersections.append(intersection)
                except:
                    pass
            return intersections

        intersections = find_intersections(f, g)
        if intersections:
            min_intersect, max_intersect = min(intersections), max(intersections)
            x_range = (min_intersect - 1, max_intersect + 1)
        else:
            x_range = self.x_range

        x_vals = np.linspace(x_range[0], x_range[1], 400)
        y_vals_f = f(x_vals)
        y_vals_g = g(x_vals)

        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals_f, label=self.equation, color='b')
        plt.plot(x_vals, y_vals_g, label=equation, color='r')
        plt.title(f"Plot of the equations: g(x) = {self.equation} and f(x) = {equation}")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(0, color='black', linewidth=2)
        plt.axvline(0, color='black', linewidth=2)
        plt.grid(True)
        plt.legend()
        plt.show()

# Example usage:
plotter = Plotter("2**x")
plotter.plot_equation()
