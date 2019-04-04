'''
Christopher Wong 110410665
'''

# # # # # # # #
# error types #
# # # # # # # #
class SemanticError(Exception):
    pass

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
        self.value = str(v)[1:-1]
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

# # # # # #  #
# operations #
# # # # # #  #
class BopNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op

    def evaluate(self):
        if (self.op == '+'):
            if (isNumber(self.v1, self.v2) or isString(self.v1, self.v2) or isList(self.v1, self.v2)):
                return self.v1.evaluate() + self.v2.evaluate()
            else:
                raise SemanticError()
        elif (self.op == '-'):
            if(isNumber(self.v1, self.v2)):
                return self.v1.evaluate() - self.v2.evaluate()
            else:
                raise SemanticError()
        elif (self.op == '*'):
            if(isNumber(self.v1, self.v2)):
                return self.v1.evaluate() * self.v2.evaluate()
            else:
                raise SemanticError()
            return self.v1.evaluate() * self.v2.evaluate()
        elif (self.op == '/'):
            if(isNumber(self.v1, self.v2) and self.v2.evaluate() != 0):
                return self.v1.evaluate() / self.v2.evaluate()
            else:
                raise SemanticError()
            return self.v1.evaluate() / self.v2.evaluate()
        elif (self.op == 'div'):
            if(isNumber(self.v1, self.v2) and self.v2.evaluate() != 0):
                return self.v1.evaluate() // self.v2.evaluate()
            else:
                raise SemanticError()
        elif (self.op == 'mod'):
            if(isNumber(self.v1, self.v2) and self.v2.evaluate() != 0):
                return self.v1.evaluate() % self.v2.evaluate()
            else:
                raise SemanticError()
        elif (self.op == '**'):
            if(isNumber(self.v1, self.v2) and self.v2.evaluate() != 0):
                return self.v1.evaluate() ** self.v2.evaluate()
            else:
                raise SemanticError()
        elif (self.op == 'in'):
            if(isString(self.v1, self.v2) or isinstance(self.v2.evaluate(), list)):
                return self.v1.evaluate() in self.v2.evaluate()
            else:
                raise SemanticError()
        elif (self.op == '<'):
            if(isNumber(self.v1, self.v2) or isString(self.v1, self.v2)):
                return self.v1.evaluate() < self.v2.evaluate()
            else:
                raise SemanticError()
        elif (self.op == '<='):
            if(isNumber(self.v1, self.v2) or isString(self.v1, self.v2)):
                return self.v1.evaluate() <= self.v2.evaluate()
            else:
                raise SemanticError()
        elif (self.op == '=='):
            if(isNumber(self.v1, self.v2) or isString(self.v1, self.v2)):
                return self.v1.evaluate() == self.v2.evaluate()
            else:
                raise SemanticError()
        elif (self.op == '<>'):
            if(isNumber(self.v1, self.v2) or isString(self.v1, self.v2)):
                return self.v1.evaluate() != self.v2.evaluate()
            else:
                raise SemanticError()
        elif (self.op == '>'):
            if(isNumber(self.v1, self.v2) or isString(self.v1, self.v2)):
                return self.v1.evaluate() > self.v2.evaluate()
            else:
                raise SemanticError()
        elif (self.op == '>='):
            if(isNumber(self.v1, self.v2) or isString(self.v1, self.v2)):
                return self.v1.evaluate() >= self.v2.evaluate()
            else:
                raise SemanticError()
        elif (self.op == 'orelse'):
            if(isBool(self.v1, self.v2)):
                return self.v1.evaluate() or self.v2.evaluate()
            else:
                raise SemanticError()
        elif (self.op == 'andalso'):
            if(isBool(self.v1, self.v2)):
                return self.v1.evaluate() and self.v2.evaluate()
            else:
                raise SemanticError()

# helper functions
def isNumber(v1, v2):
    return isinstance(v1.evaluate(), (int, float)) and isinstance(v2.evaluate(), (int,float))

def isString(v1, v2):
    return isinstance(v1.evaluate(), str) and isinstance(v2.evaluate(), str)

def isList(v1, v2):
    return isinstance(v1.evaluate(), list) and isinstance(v2.evaluate(), list)

def isBool(v1, v2):
    return isinstance(v1.evaluate(), bool) and isinstance(v2.evaluate(), bool)

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
    'TRUE', 'FALSE',
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
    r'-?\d*(\d\.|\.\d)\d* | -?\d+'
    try:
        t.value = NumberNode(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_TRUE(t):
    r'True'
    t.value = BooleanNode(t.value)
    return t
    
def t_FALSE(t):
    r'False'
    t.value = BooleanNode(t.value)
    return t

def t_STR(t):
    r'((\"[^\"]*\")|(\'[^\']*\'))'
    t.value = StringNode(t.value)
    return t

# Ignored characters
t_ignore = " \t"

def t_error(t):
    print("SYNTAX ERROR")
    
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
    if type(t[1].evaluate()) == str:
        print("'" + t[1].evaluate() + "'")
    else:
        print(t[1].evaluate())

def p_list(t):
    '''list : LBRACKET in_list RBRACKET'''
    t[0] = t[2]

def p_in_list(t):
    '''in_list : expression'''
    t[0] = ListNode(t[1])

def p_in_list2(t):
    '''in_list : expression COMMA in_list'''
    t[3].v.insert(0,t[1])
    t[0] = t[3]

# cluster**** of everything
def p_expression_binop(t):
                  # mathy-related stuff, comparison-related stuff, logic-related stuff
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression DIV expression
                  | expression MOD expression
                  | expression POW expression
                  
                  | expression IN expression

                  | expression LESSTHAN expression
                  | expression LESSTHANEQ expression
                  | expression EQUAL expression
                  | expression NOTEQ expression
                  | expression GREATERTHAN expression
                  | expression GREATERTHANEQ expression
                  
                  | expression OR expression
                  | expression AND expression'''        
    t[0] = BopNode(t[2], t[1], t[3])

def p_expression_factor(t):
    '''expression : NUMBER
                  | STR
                  | list
                  '''
    t[0] = t[1]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_error(t):
    print("SYNTAX ERROR")

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
    except SemanticError:
        print("SEMANTIC ERROR")
    # except Exception:
        # print("SYNTAX ERROR")