class Node:
    def __init__(self):
        print("init node")

    def evaluate(self):
        return 0

    def execute(self):
        return 0

class NumberNode(Node):
    def __init__(self, v):
        if('.' in v):
            self.value = float(v)
        else:
            self.value = int(v)

    def evaluate(self):
        return self.value

class BopNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op

    def evaluate(self):
        if (self.op == '+'):
            return self.v1.evaluate() + self.v2.evaluate()
        elif (self.op == '-'):
            return self.v1.evaluate() - self.v2.evaluate()
        elif (self.op == '*'):
            return self.v1.evaluate() * self.v2.evaluate()
        elif (self.op == '/'):
            return self.v1.evaluate() / self.v2.evaluate()

tokens = (
    'LPAREN', 'RPAREN',
    'NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE'
    )

# Tokens
# t_PRINT    = 'print'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'

def t_NUMBER(t):
    r'-?\d*(\d\.|\.\d)\d* | \d+'
    try:
        t.value = NumberNode(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_error(t):
    print("Syntax error at '%s'" % t.value)
    
# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules
precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE')
    )

def p_statement_expr(t):
    'statement : expression'
    print(t[1].evaluate())

def p_expression_binop(t):
    '''expression : expression PLUS factor
                  | expression MINUS factor
                  | expression TIMES factor
                  | expression DIVIDE factor'''
    t[0] = BopNode(t[2], t[1], t[3])

def p_expression_factor(t):
    '''expression : factor'''
    t[0] = t[1]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_factor_number(t):
    'factor : NUMBER'
    t[0] = t[1]

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
yacc.yacc()

import sys

if (len(sys.argv) != 2):
    sys.exit("invalid arguments")
fd = open(sys.argv[1], 'r')

for line in fd:
    code = line.strip()
    yacc.parse(code)