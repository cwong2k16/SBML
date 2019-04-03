'''
Christopher Wong 110410665
'''

# # # # # # # #
# data types  #
# # # # # # # #
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

### Class Tuples(Node):

class ListNode(Node):
    def __init__(self, v):
        self.v = [v]
    def evaluate(self):
        lst = []
        for val in self.v:
            if(isinstance(val, list)):
                lst.append(val)
            else:
                lst.append(val.evaluate())
        return lst

class StringNode(Node):
    def __init__(self, v):
        self.v = str(v[1:-1])
    def evaluate(self):
        return self.v

class BooleanNode(Node):
    def __init__(self, v):
        if v=='True':
            self.v = True
        else:
            self.v = False
    def evaluate(self):
        return self.v

# # # # # #  #
# operations #
# # # # # #  #

# class Plus(Node):

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
        elif (self.op == 'div'):
            return self.v1.evaluate() // self.v2.evaluate()
        elif (self.op == 'mod'):
            return self.v1.evaluate() % self.v2.evaluate()
        elif (self.op == '**'):
            return self.v1.evaluate() ** self.v2.evaluate()

tokens = (
    # orelse
    'OR',   
    # andalso
    'AND',
    # not
    'NOT',
    # comparisons
    'LESSTHAN', 'LESSTHANEQ', 'EQUAL', 'NOTEQ', 'GREATERTHAN', 'GREATERTHANEQ',
    # con or concatenate aka ::
    'CON',
    # in
    'IN',
    # +, -
    'PLUS','MINUS',
    # *, /, div, mod
    'TIMES','DIVIDE', 'DIV', 'MOD',
    # pow
    'POW',
    # brackets for indexing
    'LBRACKET', 'RBRACKET',
    'LPAREN', 'RPAREN', 
    # hash
    'HASH',
    'COMMA', 'SEMI',
    # integer, real
    'NUMBER',
    # boolean
    'TRUE', 'FALSE'
    # string
    'STR'
    )

# t_PRINT    = 'print'
t_OR = r'orelse'
t_AND = r'andalso'
t_NOT = r'not'
t_LESSTHAN = r'<'
t_LESSTHANEQ = r'<='
t_EQUAL = r'=='
t_NOTEQ = r'<>'
t_GREATERTHAN = r'>'
t_GREATERTHANEQ = r'>='
t_CON = r'::'
t_IN = r'in'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_DIV = r'div'
t_MOD = r'mod'
t_POW = r'\*\*'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_HASH = r'\#'
t_COMMA   = r','
t_SEMI    = r';'

def t_NUMBER(t):
    r'-?\d*(\d\.|\.\d)\d* | \d+'
    try:
        t.value = NumberNode(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_TRUE(t):
    'True'
    t.value = BooleanNode(t.value)
    return t
    
def t_FALSE(t):
    'False'
    t.value = BooleanNode(t.value)
    return t

def t_STR(t):
    r'((\"[^\"]*\")|(\'[^\']*\'))'
    t.value = StringNode(t.value)
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
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NOT'),
    ('left', 'LESSTHAN', 'LESSTHANEQ', 'EQUAL', 'NOTEQ', 'GREATERTHAN', 'GREATERTHANEQ'),
    ('right', 'CON'),
    ('left', 'IN'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE', 'DIV', 'MOD'),
    ('right', 'POW'),
    ('left', 'LBRACKET', 'RBRACKET'),
    ('left', 'HASH'),
    ('left', 'LPAREN', 'RPAREN')
    )

def p_statement_expr(t):
    'statement : expression SEMI'
    print(t[1].evaluate())

def p_list(t):
    '''list : expression LBRACKET in_list RBRACKET'''
    t[0] = t[2]

def p_in_list(t):
    '''in_list : expression'''
    t[0] = ListNode(t[1])

def p_in_list2(t):
    '''in_list : in_list expression'''
    t[0] = t[1].v.append(t[2])

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression DIV expression
                  | expression MOD expression
                  | expression POW expression'''
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
            if not token: 
                break
        ast = yacc.parse(code)
    except Exception as e:
        print("SYNTAX ERROR")