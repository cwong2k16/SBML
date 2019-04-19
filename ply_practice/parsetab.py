
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftNOTleftLESSTHANLESSTHANEQEQUALNOTEQGREATERTHANGREATERTHANEQrightCONleftINleftPLUSMINUSleftTIMESDIVIDEDIVMODrightUMINUSUPLUSrightPOWleftLBRACKETRBRACKETleftHASHleftLPARENRPARENAND COMMA CON DIV DIVIDE EQUAL FALSE GREATERTHAN GREATERTHANEQ HASH IN LBRACKET LESSTHAN LESSTHANEQ LPAREN MINUS MOD NOT NOTEQ NUMBER OR PLUS POW RBRACKET RPAREN SEMI STR TIMES TRUEstatement : expression SEMIlist : LBRACKET in_list RBRACKETin_list : expressionin_list : in_list COMMA expressiontuple : LPAREN in_tuple RPARENin_tuple : expression COMMA expressionin_tuple : in_tuple COMMA expressionexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression DIV expression\n                  | expression MOD expression\n                  | expression POW expression\n                  \n                  | expression IN expression\n                  | expression CON expression\n\n                  | expression LESSTHAN expression\n                  | expression LESSTHANEQ expression\n                  | expression EQUAL expression\n                  | expression NOTEQ expression\n                  | expression GREATERTHAN expression\n                  | expression GREATERTHANEQ expression\n                  \n                  | expression OR expression\n                  | expression AND expressionindex : expression LBRACKET expression RBRACKEThash : HASH expression tuple expression : NUMBER\n                  | STR\n                  | list\n                  | TRUE\n                  | FALSE\n                  | index\n                  | tuple\n                  | hash\n                  expression : LPAREN expression RPARENexpression : MINUS expression %prec UMINUS\n                  | PLUS expression %prec UPLUS\n                  | NOT expression'
    
_lr_action_items = {'NUMBER':([0,3,4,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,63,65,67,69,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'STR':([0,3,4,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,63,65,67,69,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'TRUE':([0,3,4,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,63,65,67,69,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'FALSE':([0,3,4,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,63,65,67,69,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'LPAREN':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,40,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,64,65,66,67,68,69,70,],[13,13,13,-27,-28,-29,-30,-31,-32,-33,-34,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,-37,-36,-38,69,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-35,13,-5,13,-2,13,-26,13,-25,]),'MINUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,],[4,19,4,4,-27,-28,-29,-30,-31,-32,-33,-34,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,-37,-36,19,19,19,19,-8,-9,-10,-11,-12,-13,-14,19,19,19,19,19,19,19,19,19,19,19,-35,4,-5,4,-2,4,-26,4,-25,19,19,19,19,]),'PLUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,],[3,18,3,3,-27,-28,-29,-30,-31,-32,-33,-34,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,-37,-36,18,18,18,18,-8,-9,-10,-11,-12,-13,-14,18,18,18,18,18,18,18,18,18,18,18,-35,3,-5,3,-2,3,-26,3,-25,18,18,18,18,]),'NOT':([0,3,4,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,63,65,67,69,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'LBRACKET':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,],[15,35,15,15,-27,-28,-29,-30,-31,-32,-33,-34,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-35,15,-5,15,-2,15,-26,15,-25,35,35,35,35,]),'HASH':([0,3,4,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,63,65,67,69,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'$end':([1,17,],[0,-1,]),'SEMI':([2,5,6,7,8,9,10,11,12,36,37,40,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,64,66,68,70,],[17,-27,-28,-29,-30,-31,-32,-33,-34,-37,-36,-38,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-35,-5,-2,-26,-25,]),'TIMES':([2,5,6,7,8,9,10,11,12,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,68,70,71,72,73,74,],[20,-27,-28,-29,-30,-31,-32,-33,-34,-37,-36,20,20,20,20,20,20,-10,-11,-12,-13,-14,20,20,20,20,20,20,20,20,20,20,20,-35,-5,-2,-26,-25,20,20,20,20,]),'DIVIDE':([2,5,6,7,8,9,10,11,12,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,68,70,71,72,73,74,],[21,-27,-28,-29,-30,-31,-32,-33,-34,-37,-36,21,21,21,21,21,21,-10,-11,-12,-13,-14,21,21,21,21,21,21,21,21,21,21,21,-35,-5,-2,-26,-25,21,21,21,21,]),'DIV':([2,5,6,7,8,9,10,11,12,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,68,70,71,72,73,74,],[22,-27,-28,-29,-30,-31,-32,-33,-34,-37,-36,22,22,22,22,22,22,-10,-11,-12,-13,-14,22,22,22,22,22,22,22,22,22,22,22,-35,-5,-2,-26,-25,22,22,22,22,]),'MOD':([2,5,6,7,8,9,10,11,12,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,68,70,71,72,73,74,],[23,-27,-28,-29,-30,-31,-32,-33,-34,-37,-36,23,23,23,23,23,23,-10,-11,-12,-13,-14,23,23,23,23,23,23,23,23,23,23,23,-35,-5,-2,-26,-25,23,23,23,23,]),'POW':([2,5,6,7,8,9,10,11,12,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,68,70,71,72,73,74,],[24,-27,-28,-29,-30,-31,-32,-33,-34,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-35,-5,-2,-26,-25,24,24,24,24,]),'IN':([2,5,6,7,8,9,10,11,12,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,68,70,71,72,73,74,],[25,-27,-28,-29,-30,-31,-32,-33,-34,-37,-36,25,25,25,25,-8,-9,-10,-11,-12,-13,-14,-15,25,25,25,25,25,25,25,25,25,25,-35,-5,-2,-26,-25,25,25,25,25,]),'CON':([2,5,6,7,8,9,10,11,12,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,68,70,71,72,73,74,],[26,-27,-28,-29,-30,-31,-32,-33,-34,-37,-36,26,26,26,26,-8,-9,-10,-11,-12,-13,-14,-15,26,26,26,26,26,26,26,26,26,26,-35,-5,-2,-26,-25,26,26,26,26,]),'LESSTHAN':([2,5,6,7,8,9,10,11,12,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,68,70,71,72,73,74,],[27,-27,-28,-29,-30,-31,-32,-33,-34,-37,-36,27,27,27,27,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,27,27,27,-35,-5,-2,-26,-25,27,27,27,27,]),'LESSTHANEQ':([2,5,6,7,8,9,10,11,12,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,68,70,71,72,73,74,],[28,-27,-28,-29,-30,-31,-32,-33,-34,-37,-36,28,28,28,28,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,28,28,28,-35,-5,-2,-26,-25,28,28,28,28,]),'EQUAL':([2,5,6,7,8,9,10,11,12,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,68,70,71,72,73,74,],[29,-27,-28,-29,-30,-31,-32,-33,-34,-37,-36,29,29,29,29,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,29,29,29,-35,-5,-2,-26,-25,29,29,29,29,]),'NOTEQ':([2,5,6,7,8,9,10,11,12,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,68,70,71,72,73,74,],[30,-27,-28,-29,-30,-31,-32,-33,-34,-37,-36,30,30,30,30,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,30,30,30,-35,-5,-2,-26,-25,30,30,30,30,]),'GREATERTHAN':([2,5,6,7,8,9,10,11,12,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,68,70,71,72,73,74,],[31,-27,-28,-29,-30,-31,-32,-33,-34,-37,-36,31,31,31,31,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,31,31,31,-35,-5,-2,-26,-25,31,31,31,31,]),'GREATERTHANEQ':([2,5,6,7,8,9,10,11,12,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,68,70,71,72,73,74,],[32,-27,-28,-29,-30,-31,-32,-33,-34,-37,-36,32,32,32,32,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,32,32,32,-35,-5,-2,-26,-25,32,32,32,32,]),'OR':([2,5,6,7,8,9,10,11,12,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,68,70,71,72,73,74,],[33,-27,-28,-29,-30,-31,-32,-33,-34,-37,-36,33,-38,33,33,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,33,-35,-5,-2,-26,-25,33,33,33,33,]),'AND':([2,5,6,7,8,9,10,11,12,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,68,70,71,72,73,74,],[34,-27,-28,-29,-30,-31,-32,-33,-34,-37,-36,34,-38,34,34,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,34,-24,34,-35,-5,-2,-26,-25,34,34,34,34,]),'RPAREN':([5,6,7,8,9,10,11,12,36,37,38,39,40,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,64,66,68,70,71,72,],[-27,-28,-29,-30,-31,-32,-33,-34,-37,-36,62,64,-38,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-35,-5,-2,-26,-25,-6,-7,]),'COMMA':([5,6,7,8,9,10,11,12,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,64,66,68,70,71,72,73,74,],[-27,-28,-29,-30,-31,-32,-33,-34,-37,-36,63,65,-38,67,-3,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-35,-5,-2,-26,-25,-6,-7,-4,63,]),'RBRACKET':([5,6,7,8,9,10,11,12,36,37,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,68,70,73,],[-27,-28,-29,-30,-31,-32,-33,-34,-37,-36,-38,66,-3,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,70,-35,-5,-2,-26,-25,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,3,4,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,63,65,67,69,],[2,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,71,72,73,74,]),'list':([0,3,4,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,63,65,67,69,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'index':([0,3,4,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,63,65,67,69,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'tuple':([0,3,4,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,43,63,65,67,69,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,68,11,11,11,11,]),'hash':([0,3,4,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,63,65,67,69,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'in_tuple':([13,69,],[39,39,]),'in_list':([15,],[41,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression SEMI','statement',2,'p_statement_expr','sbml.py',356),
  ('list -> LBRACKET in_list RBRACKET','list',3,'p_list','sbml.py',363),
  ('in_list -> expression','in_list',1,'p_in_list','sbml.py',367),
  ('in_list -> in_list COMMA expression','in_list',3,'p_in_list2','sbml.py',371),
  ('tuple -> LPAREN in_tuple RPAREN','tuple',3,'p_tuple','sbml.py',376),
  ('in_tuple -> expression COMMA expression','in_tuple',3,'p_in_tuple','sbml.py',380),
  ('in_tuple -> in_tuple COMMA expression','in_tuple',3,'p_in_tuple2','sbml.py',384),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','sbml.py',390),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','sbml.py',391),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','sbml.py',392),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','sbml.py',393),
  ('expression -> expression DIV expression','expression',3,'p_expression_binop','sbml.py',394),
  ('expression -> expression MOD expression','expression',3,'p_expression_binop','sbml.py',395),
  ('expression -> expression POW expression','expression',3,'p_expression_binop','sbml.py',396),
  ('expression -> expression IN expression','expression',3,'p_expression_binop','sbml.py',398),
  ('expression -> expression CON expression','expression',3,'p_expression_binop','sbml.py',399),
  ('expression -> expression LESSTHAN expression','expression',3,'p_expression_binop','sbml.py',401),
  ('expression -> expression LESSTHANEQ expression','expression',3,'p_expression_binop','sbml.py',402),
  ('expression -> expression EQUAL expression','expression',3,'p_expression_binop','sbml.py',403),
  ('expression -> expression NOTEQ expression','expression',3,'p_expression_binop','sbml.py',404),
  ('expression -> expression GREATERTHAN expression','expression',3,'p_expression_binop','sbml.py',405),
  ('expression -> expression GREATERTHANEQ expression','expression',3,'p_expression_binop','sbml.py',406),
  ('expression -> expression OR expression','expression',3,'p_expression_binop','sbml.py',408),
  ('expression -> expression AND expression','expression',3,'p_expression_binop','sbml.py',409),
  ('index -> expression LBRACKET expression RBRACKET','index',4,'p_expression_index','sbml.py',414),
  ('hash -> HASH expression tuple','hash',3,'p_expression_hash','sbml.py',418),
  ('expression -> NUMBER','expression',1,'p_expression_factor','sbml.py',422),
  ('expression -> STR','expression',1,'p_expression_factor','sbml.py',423),
  ('expression -> list','expression',1,'p_expression_factor','sbml.py',424),
  ('expression -> TRUE','expression',1,'p_expression_factor','sbml.py',425),
  ('expression -> FALSE','expression',1,'p_expression_factor','sbml.py',426),
  ('expression -> index','expression',1,'p_expression_factor','sbml.py',427),
  ('expression -> tuple','expression',1,'p_expression_factor','sbml.py',428),
  ('expression -> hash','expression',1,'p_expression_factor','sbml.py',429),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','sbml.py',434),
  ('expression -> MINUS expression','expression',2,'p_expression_unary','sbml.py',438),
  ('expression -> PLUS expression','expression',2,'p_expression_unary','sbml.py',439),
  ('expression -> NOT expression','expression',2,'p_expression_unary','sbml.py',440),
]
