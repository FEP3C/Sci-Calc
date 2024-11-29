import re
import math

class Tokenizer:
    def __init__(self, expression):
        self.expression = expression
        self.tokens = self.tokenize(expression)
        self.index = 0

    def tokenize(self, expression):
        token_specification = [
            ('NUMBER',   r'\d+(\.\d*)?'),  # 整数或小数
            ('ADD',      r'\+'),           # 加法运算符
            ('SUB',      r'-'),            # 减法运算符
            ('MUL',      r'\*'),           # 乘法运算符
            ('DIV',      r'/'),            # 除法运算符
            ('LPAREN',   r'$'),           # 左括号
            ('RPAREN',   r'$'),           # 右括号
            ('SIN',      r'sin'),          # 正弦函数
            ('COS',      r'cos'),          # 余弦函数
            ('TAN',      r'tan'),          # 正切函数
            ('SQRT',     r'sqrt'),         # 平方根函数
            ('FACTORIAL',r'!'),            # 阶乘运算符
            ('WS',       r'\s+'),          # 空格（忽略）
        ]
        tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
        get_token = re.compile(tok_regex).match
        tokens = []
        pos = 0
        while pos < len(expression):
            match = get_token(expression, pos)
            if match is None:
                raise SyntaxError(f'Unexpected character {expression[pos]} at position {pos}')
            type = match.lastgroup
            value = match.group(type)
            if type != 'WS':
                tokens.append((type, value))
            pos = match.end()
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
            elif type in self.precedence:
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
                if not self.operators:
                    raise SyntaxError("Mismatched parentheses.")
                self.operators.pop()
            token = self.tokenizer.next_token()
        while self.operators:
            if self.operators[-1] == 'LPAREN':
                raise SyntaxError("Mismatched parentheses.")
            self.output.append(self.operators.pop())
        return self.output

class Evaluator:
    def __init__(self, rpn):
        self.rpn = rpn

    def evaluate(self):
        stack = []
        for token in self.rpn:
            if re.match(r'\d+(\.\d*)?', token):  # 如果token是数字
                stack.append(float(token))
            elif token in ('ADD', 'SUB', 'MUL', 'DIV'):
                b, a = stack.pop(), stack.pop()
                if token == 'ADD':
                    stack.append(a + b)
                elif token == 'SUB':
                    stack.append(a - b)
                elif token == 'MUL':
                    stack.append(a * b)
                elif token == 'DIV':
                    if b == 0:
                        raise ZeroDivisionError("Division by zero.")
                    stack.append(a / b)
            elif token in ('SIN', 'COS', 'TAN', 'SQRT', 'FACTORIAL'):
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
                    if a < 0:
                        raise ValueError("Factorial of a negative number is undefined.")
                    stack.append(math.factorial(int(a)))
        return stack[0] if stack else None  # Return None if stack is empty

class ExpressionParser:
    def __init__(self, expression):
        self.tokenizer = Tokenizer(expression)
        self.shunting_yard = ShuntingYard(self.tokenizer)
        self.rpn = self.shunting_yard.parse()
        self.evaluator = Evaluator(self.rpn)

    def evaluate(self):
        return self.evaluator.evaluate()
