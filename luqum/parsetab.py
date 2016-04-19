
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '23DDA892EB146F0FC342069E466A547A'
    
_lr_action_items = {'RBRACKET':([27,],[28,]),'LPAREN':([0,1,2,3,4,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,24,25,26,28,],[1,1,-10,-6,1,1,-13,-15,1,1,-11,-5,-13,-12,1,1,1,-14,1,-4,-7,1,1,-9,-8,]),'RPAREN':([2,3,7,8,10,11,12,13,15,17,19,21,22,24,25,26,28,],[-10,-6,-13,-15,22,-11,-5,-13,-12,-3,-14,-4,-7,-2,-1,-9,-8,]),'PHRASE':([0,1,2,3,4,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,24,25,26,28,],[2,2,-10,-6,2,2,-13,-15,2,2,-11,-5,-13,-12,2,2,2,-14,2,-4,-7,2,2,-9,-8,]),'LBRACKET':([0,1,2,3,4,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,24,25,26,28,],[5,5,-10,-6,5,5,-13,-15,5,5,-11,-5,-13,-12,5,5,5,-14,5,-4,-7,5,5,-9,-8,]),'AND_OP':([2,3,6,7,8,10,11,12,13,15,17,19,21,22,24,25,26,28,],[-10,-6,16,-13,-15,16,-11,-5,-13,-12,16,-14,-4,-7,-2,16,-9,-8,]),'APPROX':([2,7,13,],[11,19,19,]),'MINUS':([0,1,2,3,4,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,24,25,26,28,],[4,4,-10,-6,4,4,-13,-15,4,4,-11,-5,-13,-12,4,4,4,-14,4,-4,-7,4,4,-9,-8,]),'$end':([2,3,6,7,8,11,12,13,15,17,19,21,22,24,25,26,28,],[-10,-6,0,-13,-15,-11,-5,-13,-12,-3,-14,-4,-7,-2,-1,-9,-8,]),'COLUMN':([7,],[20,]),'TERM':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,28,],[7,7,-10,-6,13,14,7,-13,-15,13,7,-11,-5,-13,-12,7,7,7,-14,13,-4,-7,27,7,7,-9,-8,]),'TO':([0,1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,28,],[8,8,-10,-6,8,8,-13,-15,8,8,-11,-5,-13,23,-12,8,8,8,-14,8,-4,-7,8,8,-9,-8,]),'OR_OP':([2,3,6,7,8,10,11,12,13,15,17,19,21,22,24,25,26,28,],[-10,-6,18,-13,-15,18,-11,-5,-13,-12,18,-14,-4,-7,-2,-1,-9,-8,]),'PLUS':([0,1,2,3,4,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,24,25,26,28,],[9,9,-10,-6,9,9,-13,-15,9,9,-11,-5,-13,-12,9,9,9,-14,9,-4,-7,9,9,-9,-8,]),'BOOST':([2,3,6,7,8,10,11,12,13,15,17,19,21,22,24,25,26,28,],[-10,-6,15,-13,-15,15,-11,-5,-13,-12,15,-14,-4,-7,15,15,-9,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,1,6,10,16,17,18,24,25,],[6,10,17,17,24,17,25,17,17,]),'unary_expression':([0,1,4,6,9,10,16,17,18,20,24,25,],[3,3,12,3,21,3,3,3,3,26,3,3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression OR_OP expression','expression',3,'p_expression_or','parser.py',130),
  ('expression -> expression AND_OP expression','expression',3,'p_expression_and','parser.py',135),
  ('expression -> expression expression','expression',2,'p_expression_and','parser.py',136),
  ('unary_expression -> PLUS unary_expression','unary_expression',2,'p_expression_plus','parser.py',141),
  ('unary_expression -> MINUS unary_expression','unary_expression',2,'p_expression_minus','parser.py',146),
  ('expression -> unary_expression','expression',1,'p_expression_unary','parser.py',151),
  ('unary_expression -> LPAREN expression RPAREN','unary_expression',3,'p_grouping','parser.py',156),
  ('unary_expression -> LBRACKET TERM TO TERM RBRACKET','unary_expression',5,'p_range','parser.py',161),
  ('expression -> TERM COLUMN unary_expression','expression',3,'p_field_search','parser.py',168),
  ('unary_expression -> PHRASE','unary_expression',1,'p_quoting','parser.py',175),
  ('unary_expression -> PHRASE APPROX','unary_expression',2,'p_proximity','parser.py',180),
  ('expression -> expression BOOST','expression',2,'p_boosting','parser.py',185),
  ('unary_expression -> TERM','unary_expression',1,'p_terms','parser.py',190),
  ('unary_expression -> TERM APPROX','unary_expression',2,'p_fuzzy','parser.py',195),
  ('unary_expression -> TO','unary_expression',1,'p_to_as_term','parser.py',201),
]