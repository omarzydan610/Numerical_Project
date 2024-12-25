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
        return (-5, 5)

    def plot_equation(self):
        x = sp.Symbol('x')
        # Parse the equation with proper handling for e
        expr = sp.sympify(self.equation.replace('e', 'E'))
        
        # Create numerical function
        f = sp.lambdify(x, expr, modules=[{'E': np.e, 'exp': np.exp}, 'numpy'])
        
        # Generate x values
        x_vals = np.linspace(self.x_range[0], self.x_range[1], 400)
        
        # Safely evaluate y values
        y_vals = f(x_vals)
        y_vals = np.where(np.isfinite(y_vals), y_vals, np.nan)  # Handle infinities
        
        # Plot the function
        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=self.equation, color='b')
        plt.title(f"Plot of the equation: {self.equation}")
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True)
        plt.legend()
        plt.show()

    def plot_g_x(self, equation):
        x = sp.Symbol('x')
        try:
            # Parse expressions directly without manual replacement
            expr_f = sp.sympify(self.equation)
            expr_g = sp.sympify(equation)
            
            # Create numerical functions with proper exp handling
            f = sp.lambdify(x, expr_f, modules=[{'exp': np.exp, 'E': np.e}, 'numpy'])
            g = sp.lambdify(x, expr_g, modules=[{'exp': np.exp, 'E': np.e}, 'numpy'])

            def find_intersections(func1, func2):
                def diff_func(x_val):
                    try:
                        return float(func1(x_val) - func2(x_val))
                    except:
                        return float('inf')

                intersections = []
                guesses = np.linspace(self.x_range[0], self.x_range[1], 100)
                
                for guess in guesses:
                    try:
                        root = fsolve(diff_func, guess)[0]
                        if self.x_range[0] <= root <= self.x_range[1]:
                            if not any(np.isclose(root, x, atol=1e-6) for x in intersections):
                                if np.isclose(diff_func(root), 0, atol=1e-6):
                                    intersections.append(root)
                    except:
                        continue
                
                return intersections

            # Find intersections and adjust plot range if needed
            intersections = find_intersections(f, g)
            if intersections:
                min_x = min(min(intersections) - 1, self.x_range[0])
                max_x = max(max(intersections) + 1, self.x_range[1])
            else:
                min_x, max_x = self.x_range

            # Generate x values and compute y values
            x_vals = np.linspace(min_x, max_x, 400)
            y_vals_f = f(x_vals)
            y_vals_g = g(x_vals)

            # Create plot
            plt.figure(figsize=(8, 6))
            plt.plot(x_vals, y_vals_f, label=self.equation, color='b')
            plt.plot(x_vals, y_vals_g, label=equation, color='r')
            
            # Plot intersection points
            for x_int in intersections:
                plt.plot(x_int, f(x_int), 'ko', label='Intersection')
            
            plt.title("Intersection of functions")
            plt.xlabel('x')
            plt.ylabel('y')
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            plt.grid(True)
            plt.legend()
            plt.show()
            
        except Exception as e:
            print(f"Error plotting equations: {str(e)}")