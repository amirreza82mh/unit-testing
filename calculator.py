# calculator.py
import math
import re

class Calculator:
    def add(self, a, b):
        return a + b


    def subtract(self, a, b):
        return a - b


    def multiply(self, a, b):
        return a * b


    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


    def power(self, base, exp):
        return math.pow(base, exp)


    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot take the square root of a negative number")
        return math.sqrt(x)


class MathOperations:
    def __init__(self):
        self.calculator = Calculator()


    def evaluate_expression(self, expression):
        def shunting_yard(expression):
            precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, 'sqrt': 4}
            output = []
            operators = []
            tokens = re.findall(r'\d+|\+|\-|\*|\/|\^|\(|\)|sqrt', expression)


            for token in tokens:
                if token.isdigit():
                    output.append(float(token))
                elif token in precedence:
                    while (operators and operators[-1] != '(' and
                           precedence.get(operators[-1], 0) >= precedence[token]):
                        output.append(operators.pop())
                    operators.append(token)
                elif token == '(':
                    operators.append(token)
                elif token == ')':
                    while operators and operators[-1] != '(':
                        output.append(operators.pop())
                    operators.pop()
                elif token == 'sqrt' or token == 'log':
                    operators.append(token)

            while operators:
                output.append(operators.pop())

            return output


        def evaluate_postfix(postfix):
            stack = []
            for token in postfix:
                if isinstance(token, float):
                    stack.append(token)
                else:
                    if token == 'sqrt':
                        if len(stack) == 0:
                            raise ValueError("Invalid expression")
                        value = stack.pop()
                        stack.append(self.calculator.square_root(value))
                    else:
                        if len(stack) < 2:
                            raise ValueError("Invalid expression")
                        right = stack.pop()
                        left = stack.pop()
                        if token == '+':
                            stack.append(self.calculator.add(left, right))
                        elif token == '-':
                            stack.append(self.calculator.subtract(left, right))
                        elif token == '*':
                            stack.append(self.calculator.multiply(left, right))
                        elif token == '/':
                            stack.append(self.calculator.divide(left, right))
                        elif token == '^':
                            stack.append(self.calculator.power(left, right))

            if len(stack) != 1:
                raise ValueError("Invalid expression")

            return stack[0]

        postfix_expression = shunting_yard(expression)
        result = evaluate_postfix(postfix_expression)
        return result
