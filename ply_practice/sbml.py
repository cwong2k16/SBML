'''
Christopher Wong 110410665
'''

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

class BooleanNode(Node):
    def __init__(self, v):
        if v=='True':
            self.v = True
        else:
            self.v = False
    def evaluate(self):
        return self.v

class ListNode(Node):
    def __init__(self, v):
        self.v = [v]
    def evaluate(self):
        return self.v

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
    'LPAREN', 'RPAREN', 'SEMI',
    'NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE',
    'TRUE', 'FALSE',
    'LBRACKET', 'RBRACKET'
    )

# Tokens
# t_PRINT    = 'print'
t_SEMI    = r';'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

def t_TRUE(t):
    'True'
    t.value = BooleanNode(t.value)
    

def t_FALSE(t):
    'False'
    t.value = BooleanNode(t.value)

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

def p_list(t):
    '''expression LBRACKET in_list RBRACKET'''
    t[0] = t[2]

def p_in_list(t):
    '''in_list : expression'''
    t[0] = ListNode(t[1])

def p_in_list2(t):
    '''in_list : in_list expression'''
    t[0] = t[1].v.append(t[2])

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
    try:
        lex.input(code)
        while True:
            token = lex.token()
            if not token: break
        ast = yacc.parse(code)
    except Exception as e:
        print("SYNTAX ERROR")
    try:
        ast.execute()
    except Exception as e:
        print("SEMANTIC ERROR", e)