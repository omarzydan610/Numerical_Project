import numpy as np
import time
import math

def SFCalc(number, significantFigures):
    if number == 0:
        return 0

    # Calculate the order of magnitude of the number
    order_of_magnitude = math.floor(math.log10(abs(number)))
    
    # Scale the number to the desired significant figures
    scale = 10**(significantFigures - 1 - order_of_magnitude)
    scaled_number = math.trunc(number * scale)
    
    # Scale back to the original magnitude
    result = scaled_number / scale
    return result


class Gauss:

    def __init__(self):
        self.res = np.array([])
        self.time = 0.0
        self.steps = ""

    def grtSteps(self):
        return self.steps

    def writeSolution(self, matrix, signifcantFigure):
        self.steps += "\n"
        for i in matrix:
            self.steps += "        |  "
            for j in i:
                self.steps += f"{SFCalc(j, signifcantFigure)}   "
            self.steps += "|\n"

    def setBackwardSubstitution(self, x, index, signifcantFigure):
        self.steps += ">> final step\n"
        self.steps += "    backward substitution\n"
        for i in x[-1::-1]:
            self.steps += f"        X{index} = {SFCalc(i, signifcantFigure)}\n"
            index -= 1

    def getSolution(self):
        return self.res

    def getExcutionTime(self):
        return self.time

    def gaussScale_solve(self, system, n, signifcantFigure):
        system = np.array(system, dtype=float)
        x = np.zeros(n)
        start_time = time.perf_counter_ns()

        A = system[:, :-1]
        b = system[:, -1]
        A = np.array(A, dtype=float)
        b = np.array(b, dtype=float)

        scale = np.max(np.abs(A), axis=1)

        for k in range(n - 1):  # Forward Elimination
            self.steps += f">> step {k+1}\n"
            pivot_row = np.argmax(np.abs(system[k:n, k]) / scale[k:n]) + k
            self.steps += f"    Pivot row selected: {pivot_row+1}\n"
            if pivot_row != k:
                system[[k, pivot_row]] = system[[pivot_row, k]]  # Swap rows
                scale[[k, pivot_row]] = scale[[pivot_row, k]]  # Swap scaling factors
            self.steps += "    System after row swapping:"
            self.writeSolution(system, signifcantFigure)
            for i in range(k + 1, n):
                factor = system[i, k] / system[k, k]
                system[i, k:] -= factor * system[k, k:]
            self.steps += "    System after forward elimination:"
            self.writeSolution(system, signifcantFigure)
            self.steps += "\n\n"
            

        step_number = n 
        for i in range(n - 1, -1, -1):  # Backward Substitution
            self.steps += f">> step {step_number}\n"
            x[i] = (system[i, -1] - np.dot(system[i, i + 1:n], x[i + 1:n])) / system[i, i]
            self.steps += f"    x[{i}] = {x[i]}\n"
            self.steps += "\n\n"
            step_number += 1

        end_time = time.perf_counter_ns()
        self.time = end_time - start_time  # Set execution time
        self.res = [SFCalc(element, signifcantFigure)for element in x ]  # Set solution
        self.setBackwardSubstitution(x, n, signifcantFigure)

    def solve(self, system, n, signifcantFigure=3):
        system = np.array(system, dtype=float)
        x = np.zeros(n)

        start_time = time.perf_counter_ns()

        for i in range(n):
            self.steps += f">> step {i+1}\n"

            max_value = abs(system[i][i])
            max_index = i

            for j in range(i+1, n):  # Find the largest pivot
                if abs(system[j][i]) > max_value:
                    max_value = abs(system[j][i])
                    max_index = j
            self.steps += f"    The largest pivot is '{SFCalc(max_value, signifcantFigure)}' at index '{max_index+1}'\n"

            if max_index != i:  # Interchanging
                system[[i, max_index]] = system[[max_index, i]]

            self.steps += "    System after interchanging:"
            self.writeSolution(system, signifcantFigure)

            for k in range(i+1, n):  # Forward elimination
                factor = (system[k][i] / system[i][i])
                for j in range(i, n+1):
                    system[k][j] = -1 * factor * system[i][j] + system[k][j]

            self.steps += "    System after forward elimination:"
            self.writeSolution(system, signifcantFigure)
            self.steps += "\n\n"

        for k in range(n-1, -1, -1):  # Backward substitution
            d = 0
            for j in range(k+1, n):
                d += system[k][j] * x[j]

            x[k] = (system[k][n] - d) / system[k][k]

        end_time = time.perf_counter_ns()
        self.time = (end_time - start_time) # Set execution time
        self.res = [SFCalc(element, signifcantFigure)for element in x ]  # Set solution

        self.setBackwardSubstitution(x, n, signifcantFigure)
