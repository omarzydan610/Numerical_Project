import math

# def significantFiguresCalculation(number, significantFigures):
#     if number == 0:
#         return 0

#     # Calculate the order of magnitude of the number
#     order_of_magnitude = math.floor(math.log10(abs(number)))
    
#     # Scale the number to the desired significant figures
#     scale = 10**(significantFigures - 1 - order_of_magnitude)
#     scaled_number = math.trunc(number * scale)
    
#     # Scale back to the original magnitude
#     result = scaled_number / scale
#     return result

import time

# Start time
start_time = time.perf_counter_ns()

# Your code here
# For example, a simple loop
for _ in range(1000000):
    pass

# End time
end_time = time.perf_counter_ns()

# Calculate the difference in nanoseconds
execution_time_ns = end_time - start_time

print(f"Execution time: {execution_time_ns} nanoseconds")
