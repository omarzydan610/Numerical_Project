import math

def significantFiguresCalculation(number, significantFigures):
    if number == 0:
        return 0  # If the number is 0, it has no significant figures.

    # Calculate the order of magnitude of the number
    order_of_magnitude = math.floor(math.log10(abs(number)))
    
    # Scale the number to the desired significant figures
    scale = 10**(significantFigures - 1 - order_of_magnitude)
    scaled_number = math.trunc(number * scale)
    
    # Scale back to the original magnitude
    result = scaled_number / scale
    return result