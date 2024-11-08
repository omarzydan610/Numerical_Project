class Sedial:
    def __init__(self, matrixA, matrixB, initial_guess, Figures):
        self.matrixA = matrixA
        self.matrixB = matrixB

        self.new =initial_guess
        self.SignificantFigures = Figures

    def solve_with_iterations(self, num_iterations):
        for t in range(num_iterations):
            for i in range(len(self.matrixB)):
                sum = self.matrixB[i]
                for j in range(len(self.matrixB)):
                    if i != j:
                        sum -= round(self.matrixA[i][j] * self.new[j], self.SignificantFigures)
                self.new[i] = round(sum / self.matrixA[i][i], self.SignificantFigures)
            self.old = self.new[:]
        return self.new

    def solve_with_tolerance(self, tolerance):
        tolerance /= 100
        valid = False
        iteration = 0
        while not valid:
            valid = True
            iteration += 1
            for i in range(len(self.matrixB)):
                sum = self.matrixB[i]
                for j in range(len(self.matrixB)):
                    if i != j:
                        sum -= round(self.matrixA[i][j] * self.new[j], self.SignificantFigures)
                self.new[i] = round(sum / self.matrixA[i][i], self.SignificantFigures)

                relative_error = abs(self.new[i] - self.old[i]) / abs(self.new[i])
                if relative_error > tolerance:
                    valid = False
            self.old = self.new[:]
        return self.new, iteration


########################## TEST input ########################################################

variables = int(input("number of unknowns: "))
matrixA = []
matrixB = []
SignificantFigures = 5

for i in range(variables):
    row = []
    for j in range(variables):
        value = int(input(f"A[{i}][{j}]: "))
        row.append(value)
    matrixA.append(row)

print("matrix B:")
for i in range(variables):
    value = int(input(f"B[{i}]: "))
    matrixB.append(value)

initial_guess = []
print("initial guess:")
for i in range(variables):
    value = float(input(f"old[{i}]: "))
    initial_guess.append(value)


sedial = Sedial(matrixA, matrixB, initial_guess, SignificantFigures)

stop_condition = input("stopping condition (1 for number of iterations, 2 for absolute relative error): ")

if stop_condition == '1':
    num_iterations = int(input("number of iterations: "))
    solution = sedial.solve_with_iterations(num_iterations)
    print(solution)

elif stop_condition == '2':
    error_tolerance = float(input("error tolerance in %: "))
    solution, num_iterations = sedial.solve_with_tolerance(error_tolerance)
    print(solution)
