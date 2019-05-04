import inspect

'''
Christopher Wong 110410665
'''

# dictionary of variable names
names = { }

# dictionary of function names
functions = { }

# # # # # # # #
# error types #
# # # # # # # #
class SyntaxError(Exception):
    pass
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

class BlockNode(Node):
    def __init__(self,sl):
        self.statementList = sl

    def execute(self):
         for statement in self.statementList:
             statement.execute()

class NumberNode(Node):
    def __init__(self, v):
        if('.' in v or 'e' in v):
            self.value = float(v)
        else:
            self.value = int(v)

    def evaluate(self):
        return self.value

class TupleNode(Node):
    def __init__(self, v, v2):
        self.v = [v, v2]
    def evaluate(self):
        lst = []
        for val in self.v:
            if(type(val) != list):
                lst.append(val.evaluate())
            else:
                lst.append(val)
        return tuple(lst)

class ListNode(Node):
    def __init__(self, v):
        if(v == []):
            self.v = v
        else:
            self.v = [v]
    def evaluate(self):
        lst = []
        for val in self.v:
            if(type(val) != list):
                lst.append(val.evaluate())
            else:
                lst.append(val)
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

# statements
class PrintNode(Node):
    def __init__(self, e):
        self.e = e
    def execute(self):
        print(self.e.evaluate())

class AssignNode(Node):
    def __init__(self, name, e):
        self.name = name
        self.e = e

    def execute(self):
        names[self.name.value] = self.e.evaluate()

class AssignNodeList(Node):
    def __init__(self, node, e):
        self.needle = node.needle
        self.haystack = node.haystack
        self.e = e

    def execute(self):
        needle = self.needle.evaluate()
        haystack = self.haystack.evaluate()
        haystack[needle] = self.e.evaluate()

class IfNode(Node):
    def __init__(self, cond, block):
        self.cond = cond
        self.block = block

    def execute(self):
        if(self.cond.evaluate()):
            self.block.execute()

class ElseNode(Node):
    def __init__(self, ifsmt, elseb):
        self.cond = ifsmt.cond
        self.ifb = ifsmt.block
        self.elseb = elseb
    def execute(self):
        if(self.cond.evaluate()):
            self.ifb.execute()
        else:
            self.elseb.execute()

class WhileNode(Node):
    def __init__(self, exp, block):
        self.exp = exp
        self.block = block
    def execute(self):
        while(self.exp.evaluate()):
            self.block.execute()

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
        elif (self.op == '**'):
            if(isNumber(self.v1, self.v2)):
                return self.v1.evaluate() ** self.v2.evaluate()
            else:
                raise SemanticError()
        elif (self.op == '::'):
            if(isinstance(self.v2.evaluate(), list)):
                res = self.v2.evaluate()
                if(isinstance(self.v1.evaluate(), list)):
                    res = ListNode(self.v1.evaluate()).evaluate() + res
                    return res
                else:
                    res.insert(0, self.v1.evaluate())
                    return res
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
        elif (self.op.value == 'orelse'):
            if(isBool(self.v1, self.v2)):
                return self.v1.evaluate() or self.v2.evaluate()
            else:
                raise SemanticError()
        elif (self.op.value == 'andalso'):
            if(isBool(self.v1, self.v2)):
                return self.v1.evaluate() and self.v2.evaluate()
            else:
                raise SemanticError()
        elif (self.op.value == 'div'):
            if(isNumber(self.v1, self.v2) and self.v2.evaluate() != 0):
                return self.v1.evaluate() // self.v2.evaluate()
            else:
                raise SemanticError()
        elif (self.op.value == 'mod'):
            if(isNumber(self.v1, self.v2) and self.v2.evaluate() != 0):
                return self.v1.evaluate() % self.v2.evaluate()
            else:
                raise SemanticError()
        elif (self.op.value == 'in'):
            if(isString(self.v1, self.v2) or isinstance(self.v2.evaluate(), list)):
                return self.v1.evaluate() in self.v2.evaluate()
            else:
                raise SemanticError()

class NameNode(Node):
    def __init__(self, v):
        self.value = v

    def evaluate(self):
        try:
            return names[self.value]
        except:
            raise SemanticError()

class FunctionNode(Node):
    def __init__(self, name, params, block, e):
        self.name = name
        self.params = params
        self.block = block
        self.e = e
        functions[self.name.value] = self

    def execute(self):
        self.block.execute()

class FunctionCallNode(Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args
    
    def evaluate(self):
        global names
        old_vars = names
        global functions
        func_node = functions[self.name.value]
        new_vars = {}
        for i in range(len(func_node.params)):
            new_vars[func_node.params[i].value] = self.args[i].evaluate()
        old_vars = names
        names = new_vars
        func_node.execute()
        result = func_node.e.evaluate()
        names = old_vars
        return result

class UNode(Node):
    def __init__(self, op, v1):
        self.v1 = v1
        self.op = op

    def evaluate(self):
        if (self.op == '-'):
            if(type(self.v1.evaluate()) in [float,int]):
                return -self.v1.evaluate()
            else:
                raise SemanticError()
        elif(self.op == '+'):
            if(type(self.v1.evaluate()) in [float,int]):
                return self.v1.evaluate()
            else:
                raise SemanticError()
        elif(self.op.value == 'not'):
            if(type(self.v1.evaluate()) == bool):
                return not self.v1.evaluate()
            else:
                raise SemanticError()

class IndexNode(Node):
    def __init__(self, haystack, needle):
        self.haystack = haystack
        self.needle = needle

    def evaluate(self):
        if(type(self.needle.evaluate()) == int):
            if(type(self.haystack.evaluate()) in [str, list]):
                try:
                    return self.haystack.evaluate()[self.needle.evaluate()]
                except Exception:
                    raise SemanticError()
        raise SemanticError()

class HashNode(Node):
    def __init__(self, haystack, needle):
        self.haystack = haystack
        self.needle = needle

    def evaluate(self):
        if(type(self.needle.evaluate()) == int):
            if(type(self.haystack.evaluate()) == tuple):
                try:
                    return self.haystack.evaluate()[self.needle.evaluate()-1]
                except Exception:
                    raise SemanticError()
        raise SemanticError()

# helper functions
def isNumber(v1, v2):
    return type(v1.evaluate()) in [int, float] and type(v2.evaluate()) in [int,float]

def isString(v1, v2):
    return isinstance(v1.evaluate(), str) and isinstance(v2.evaluate(), str)

def isList(v1, v2):
    return isinstance(v1.evaluate(), list) and isinstance(v2.evaluate(), list)

def isBool(v1, v2):
    return (type(v1.evaluate()) == bool) and (type(v2.evaluate()) == bool)

reserved = {
    'print' : 'PRINT',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'orelse' : 'OR',
    'andalso' : 'AND',
    'in' : 'IN',
    'mod' : 'MOD',
    'div' : 'DIV',
    'not' : 'NOT',
    'fun' : 'FUN'
 }

tokens = [
    # name
    'NAME',
    # comparisons
    'LESSTHAN', 'LESSTHANEQ', 'EQUAL', 'NOTEQ', 'GREATERTHAN', 'GREATERTHANEQ',
    # assign or = 
    'ASSIGN',
    # con or concatenate aka ::
    'CON',
    # +, -
    'PLUS','MINUS', 
    # *, /, div, mod
    'TIMES','DIVIDE',
    # pow
    'POW',
    # brackets for indexing
    'LBRACKET', 'RBRACKET',
    'LPAREN', 'RPAREN', 
    'L_CURLY', 'R_CURLY',
    # hash
    'HASH',
    'COMMA', 'SEMI',
    # integer, real
    'NUMBER',
    # boolean
    'TRUE', 'FALSE',
    # string
    'STR'
    ] + list(reserved.values())

t_LESSTHAN = r'<'
t_LESSTHANEQ = r'<='
t_EQUAL = r'=='
t_NOTEQ = r'<>'
t_GREATERTHAN = r'>'
t_GREATERTHANEQ = r'>='
t_CON = r'::'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_POW = r'\*\*'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_L_CURLY = r'\{'
t_R_CURLY = r'\}'
t_ASSIGN = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_HASH = r'\#'
t_COMMA   = r','
t_SEMI    = r';'
    
def t_NUMBER(t):
    r'\d*([.][\d]+)?[e]([-+])?[\d]+ | \d*(\d\.|\.\d)\d* | \d+'
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

def t_NAME(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'NAME')
    t.value = NameNode(t.value)
    return t

# Ignored characters
t_ignore = " \t"

def t_error(t):
    raise SyntaxError()
    
# Build the lexer
import ply.lex as lex
lex.lex(debug=0)

# Parsing rules
precedence = (
    ('right', 'ASSIGN'),
    ('left', 'PRINT'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NOT'),
    ('left', 'LESSTHAN', 'LESSTHANEQ', 'EQUAL', 'NOTEQ', 'GREATERTHAN', 'GREATERTHANEQ'),
    ('right', 'CON'),
    ('left', 'IN'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE', 'DIV', 'MOD'),
    ('right','UMINUS', 'UPLUS'),
    ('right', 'POW'),
    ('left', 'LBRACKET', 'RBRACKET'),
    ('left', 'HASH'),
    ('left', 'LPAREN', 'RPAREN'),
    )

# functions stuff, hw 5
def p_program(p):
    '''
    program : functions block
    '''
    p[0] = p[2]

def p_functions(p):
    '''
    functions : functions function
    '''
    p[0] = p[1] + [p[2]]

def p_inner_function(p):
    '''
    functions : function
    '''
    p[0] = [p[1]]

def p_function(p):
    '''
    function : FUN NAME LPAREN params RPAREN ASSIGN block expression SEMI
    '''
    p[0] = FunctionNode(p[2], p[4], p[7], p[8])

def p_params(p):
    '''
    params : params COMMA NAME
    '''
    p[0] = p[1] + [p[3]]

def p_param(p):
    '''
    params : NAME
    '''
    p[0] = [p[1]]

def p_function_call(p):
    '''
    function_call : NAME LPAREN args RPAREN
    '''
    p[0] = FunctionCallNode(p[1], p[3])

def p_args(p):
    '''
    args : args COMMA expression
    '''
    p[0] = p[1] + [p[3]]

def p_args2(p):
    '''
    args : expression
    '''
    p[0] = [p[1]]

def p_block(p):
    '''
     block : L_CURLY statement_list R_CURLY
    '''
    p[0] = BlockNode(p[2])

def p_empty_block(p):
    '''
    block : L_CURLY R_CURLY
    '''
    p[0] = BlockNode([])

def p_statement_list(p):
    '''
     statement_list : statement_list statement 
    '''
    p[0] = p[1] + [p[2]]

def p_statement_list_val(p):
    '''
    statement_list : statement
    '''
    p[0] = [p[1]]

def p_statement(t):
    """
    statement : print_smt
              | assign_smt
              | if_smt
              | else_smt
              | while_smt
              | assign_smt_list
              | single_block
              | function_call
    """
    t[0] = t[1]

def p_statement_single_block(t):
    '''single_block : block'''
    t[0] = t[1]

def p_print_smt(t):
    '''print_smt : PRINT LPAREN expression RPAREN SEMI %prec PRINT'''
    t[0] = PrintNode(t[3])

def p_assign_smt(t):
    '''assign_smt : NAME ASSIGN expression SEMI %prec ASSIGN'''
    t[0] = AssignNode(t[1], t[3])

def p_assign_list_smt(t):
    '''assign_smt_list : index ASSIGN expression SEMI %prec ASSIGN'''
    t[0] = AssignNodeList(t[1], t[3])

def p_if_smt(t):
    '''if_smt : IF LPAREN expression RPAREN block'''
    t[0] = IfNode(t[3], t[5])

def p_else_smt(t):
    '''else_smt : if_smt ELSE block'''
    t[0] = ElseNode(t[1], t[3])

def p_while_smt(t):
    '''while_smt : WHILE LPAREN expression RPAREN block'''
    t[0] = WhileNode(t[3], t[5])
    
def p_list(t):
    '''list : LBRACKET in_list RBRACKET'''
    t[0] = t[2]

def p_empty_list(t):
    '''list : LBRACKET RBRACKET'''
    t[0] = ListNode([])

def p_in_list(t):
    '''in_list : expression'''
    t[0] = ListNode(t[1])

def p_in_list2(t):
    '''in_list : in_list COMMA expression'''
    t[1].v.append(t[3])
    t[0] = t[1]

def p_tuple(t):
    '''tuple : LPAREN in_tuple RPAREN'''
    t[0] = t[2]

def p_in_tuple(t):
    '''in_tuple : expression COMMA expression'''
    t[0] = TupleNode(t[1], t[3])

def p_in_tuple2(t):
    '''in_tuple : in_tuple COMMA expression'''
    t[1].v.append(t[3])
    t[0] = t[1]

# cluster**** of everything
def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression DIV expression
                  | expression MOD expression
                  | expression POW expression
                  
                  | expression IN expression
                  | expression CON expression

                  | expression LESSTHAN expression
                  | expression LESSTHANEQ expression
                  | expression EQUAL expression
                  | expression NOTEQ expression
                  | expression GREATERTHAN expression
                  | expression GREATERTHANEQ expression
                  
                  | expression OR expression
                  | expression AND expression'''
    t[0] = BopNode(t[2], t[1], t[3])


def p_expression_index(t):
    '''index : expression LBRACKET expression RBRACKET'''
    t[0] = IndexNode(t[1], t[3])

def p_expression_hash(t):
    '''hash : HASH expression expression '''
    t[0] = HashNode(t[3], t[2])

def p_expression_factor(t):
    '''expression : NUMBER
                  | STR
                  | list
                  | TRUE
                  | FALSE
                  | index
                  | tuple
                  | hash
                  | NAME
                  | assign_smt_list
                  | function_call
                  '''
    t[0] = t[1]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_unary(t):
    '''expression : MINUS expression %prec UMINUS
                  | PLUS expression %prec UPLUS
                  | NOT expression'''
    t[0] = UNode(t[1], t[2])

def p_error(t):
    raise SyntaxError()

import ply.yacc as yacc
yacc.yacc(debug=0)

import sys

if (len(sys.argv) != 2):
    sys.exit("invalid arguments")
with open(sys.argv[1], 'r') as myfile:
    data = myfile.read().replace('\n', '')
try:
    root = yacc.parse(data)
    root.execute()
except SemanticError:
    print("SEMANTIC ERROR")
except SyntaxError:
    print("SYNTAX ERROR")