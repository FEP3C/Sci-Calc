import re
import math

class Tokenizer:
    def __init__(self, expression):
        self.expression = expression
        self.tokens = self.tokenize(expression)
        self.index = 0

    def tokenize(self, expression):
        token_specification = [
            ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
            ('ADD',      r'\+'),           # Addition operator
            ('SUB',      r'-'),            # Subtraction operator
            ('MUL',      r'\*'),           # Multiplication operator
            ('DIV',      r'/'),            # Division operator
            ('LPAREN',   r'\('),           # Left Parenthesis
            ('RPAREN',   r'\)'),           # Right Parenthesis
            ('SIN',      r'sin'),          # Sine function
            ('COS',      r'cos'),          # Cosine function
            ('TAN',      r'tan'),          # Tangent function
            ('SQRT',     r'sqrt'),         # Square root function
            ('FACTORIAL',r'!'),            # Factorial operator
            ('WS',       r'\s+'),          # Whitespace (ignored)
        ]
        tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
        get_token = re.compile(tok_regex).match
        tokens = []
        pos = 0
        match = get_token(expression)
        while match is not None:
            type = match.lastgroup
            value = match.group(type)
            if type != 'WS':
                tokens.append((type, value))
            pos = match.end()
            match = get_token(expression, pos)
        if pos != len(expression):
            raise SyntaxError(f'Unexpected character {expression[pos]} at position {pos}')
        return tokens

    def next_token(self):
        if self.index < len(self.tokens):
            token = self.tokens[self.index]
            self.index += 1
            return token
        return None

    def peek(self):
        if self.index < len(self.tokens):
            return self.tokens[self.index]
        return None

class ShuntingYard:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.output = []
        self.operators = []
        self.precedence = {
            'ADD': 1,
            'SUB': 1,
            'MUL': 2,
            'DIV': 2,
            'SIN': 3,
            'COS': 3,
            'TAN': 3,
            'SQRT': 3,
            'FACTORIAL': 4
        }
        self.associativity = {
            'ADD': 'L',
            'SUB': 'L',
            'MUL': 'L',
            'DIV': 'L',
            'SIN': 'R',
            'COS': 'R',
            'TAN': 'R',
            'SQRT': 'R',
            'FACTORIAL': 'L'
        }

    def parse(self):
        token = self.tokenizer.next_token()
        while token:
            type, value = token
            if type == 'NUMBER':
                self.output.append(value)
            elif type in ('ADD', 'SUB', 'MUL', 'DIV', 'SIN', 'COS', 'TAN', 'SQRT', 'FACTORIAL'):
                while (self.operators and self.operators[-1] != 'LPAREN' and
                       (self.precedence[self.operators[-1]] > self.precedence[type] or
                       (self.precedence[self.operators[-1]] == self.precedence[type] and self.associativity[type] == 'L'))):
                    self.output.append(self.operators.pop())
                self.operators.append(type)
            elif type == 'LPAREN':
                self.operators.append('LPAREN')
            elif type == 'RPAREN':
                while self.operators and self.operators[-1] != 'LPAREN':
                    self.output.append(self.operators.pop())
                self.operators.pop()
            token = self.tokenizer.next_token()
        while self.operators:
            self.output.append(self.operators.pop())
        return self.output

class Evaluator:
    def __init__(self, rpn):
        self.rpn = rpn

    def evaluate(self):
        stack = []
        for token in self.rpn:
            if re.match(r'\d+(\.\d*)?', token):  # if token is a number
                stack.append(float(token))
            elif token in ('ADD', 'SUB', 'MUL', 'DIV'):
                b = stack.pop()
                a = stack.pop()
                if token == 'ADD':
                    stack.append(a + b)
                elif token == 'SUB':
                    stack.append(a - b)
                elif token == 'MUL':
                    stack.append(a * b)
                elif token == 'DIV':
                    stack.append(a / b)
            elif token in ('SIN', 'COS', 'TAN', 'SQRT'):
                a = stack.pop()
                if token == 'SIN':
                    stack.append(math.sin(math.radians(a)))
                elif token == 'COS':
                    stack.append(math.cos(math.radians(a)))
                elif token == 'TAN':
                    stack.append(math.tan(math.radians(a)))
                elif token == 'SQRT':
                    stack.append(math.sqrt(a))
            elif token == 'FACTORIAL':
                a = stack.pop()
                stack.append(math.factorial(int(a)))
        return stack[0]

class ExpressionParser:
    def __init__(self, expression):
        self.tokenizer = Tokenizer(expression)
        self.shunting_yard = ShuntingYard(self.tokenizer)
        self.rpn = self.shunting_yard.parse()
        self.evaluator = Evaluator(self.rpn)

    def evaluate(self):
        return self.evaluator.evaluate()

