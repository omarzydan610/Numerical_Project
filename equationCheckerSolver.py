import math

def check_equation_validation_and_convert_to_postfix(equation):
    # Stack for operators and parentheses
    operator_stack = []
    postfix_string = ''
    i = 0

    while i < len(equation):
        char = equation[i]
        print(i,"char",char, "operator_stack",operator_stack, "postfix_string",postfix_string,i)
        if char == ' ':  # Skip whitespaces
            i += 1
            continue
        # Handle opening parenthesis
        elif char == '(':
            operator_stack.append(char)
        
        # Handle operators with precedence
        elif char in '+-':
            while operator_stack and operator_stack[-1] in '+-*/^':
                postfix_string += operator_stack.pop()
            operator_stack.append(char)
        elif char in '*/':
            print("char",char, "operator_stack",operator_stack, "postfix_string",postfix_string,i)
            while operator_stack and operator_stack[-1] in '*/^':
                postfix_string += operator_stack.pop()
            operator_stack.append(char)
        elif char == '^':
            while operator_stack and operator_stack[-1] == '^':
                postfix_string += operator_stack.pop()
            operator_stack.append(char)
        
        # Handle closing parenthesis
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                postfix_string += operator_stack.pop()
            if not operator_stack:
                return "Invalid Expression: Mismatched Parentheses"
            operator_stack.pop()  # Pop the '('
            # Append function names like sin, cos, etc., if present
            if operator_stack and operator_stack[-1] in ['s', 'c', 't', 'l']:
                postfix_string += operator_stack.pop()
        
        # Handle functions like sin, cos, tan, log
        elif char in 'sctl':  # Assuming sin, cos, tan, log
            operator_stack.append(char)
            i += 2  # Skip the next two characters (e.g., "in", "os", "an", "og")
        
        # Handle numeric and variable characters
        elif char == 'x' or char == 'e':
            postfix_string += char
        elif char.isdigit():
            postfix_string +='_'
            postfix_string += char
            i += 1
            print("i",i, "len",len(equation), "char",char, "postfix_string",postfix_string, "equation",equation)
            while i < len(equation) and (equation[i].isdigit() or equation[i] == '.'):
                postfix_string += equation[i]
                i += 1
            postfix_string += '_'
            i -= 1
        # Handle unexpected characters
        else:
            return f"Invalid Character in Expression: {char}"
        
        i += 1

    # Pop remaining operators
    while operator_stack:
        top = operator_stack.pop()
        if top in '()':
            return "Invalid Expression: Mismatched Parentheses"
        postfix_string += top
    
    return postfix_string

postfix = check_equation_validation_and_convert_to_postfix("sin(x) + 12.764/0")
def solve_equation(x):
    stack = []
    i = 0

    while i < len(postfix):
        char = postfix[i]

        if char == 'x':
            stack.append(x)
        elif char == 'e':
            stack.append(math.e)
        elif char == '_':
            i += 1
            number = ''
            while i < len(postfix) and postfix[i] != '_':
                number += postfix[i]
                i += 1
            stack.append(float(number))
        elif char == '+':
            stack.append(stack.pop() + stack.pop())
        elif char == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif char == '*':
            stack.append(stack.pop() * stack.pop())
        elif char == '/':
            b = stack.pop()
            if b == 0:
                return "Division by zero"
            a = stack.pop()
            stack.append(a / b)
        elif char == '^':
            b = stack.pop()
            a = stack.pop()
            stack.append(a ** b)
        elif char == 's':
            stack.append(math.sin(stack.pop()))
        elif char == 'c':
            stack.append(math.cos(stack.pop()))
        elif char == 't':
            stack.append(math.tan(stack.pop())) 
        elif char == 'l':
            stack.append(math.log(stack.pop()))

        i += 1

    return stack.pop()

print(postfix)
print(solve_equation(math.pi/4))  # Output: 3.0001220703125



# from sympy import symbols, sympify
# try:
#     x = symbols('x')
#     equation = "sin(x) + 30 / 0 "
#     parsed = sympify(equation)  # Safely parse and validate
#     print(parsed)  # Output: sin(x) + 60
# except Exception as e:
#     print(invalid_expression := f"Invalid Expression: {e}")
# else:
#     try:
#         print("enter in else ")
#         answer=  parsed.evalf(subs={x: math.pi/4})  # Output: 1
#     except NameError:
#         print(math_error := "Math Error: Invalid Expression")
#     except ZeroDivisionError:
#         print(div_error := "Math Error: Division by zero")
#     else:
#         print (answer)

#  # Output: 6.7071