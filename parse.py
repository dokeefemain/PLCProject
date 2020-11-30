









# import_stmt --> 'import' NAME

# return_stmt --> 'return' return_list

# return_list --> RETURNVAR (',' RETURNVAR )+ [','] | RETURNVAR ',' | RETURNVAR

# global_stmt --> 'global' NAME+

# func_def --> 'def' NAME '(' [NAME] ')' ':'

# nonlocal_stmt --> 'nonlocal' NAME+
# if_stmt --> 'if' expression ':' block ifel_stmt | 'if' expression ':' block [else_block]
# ifel_stmt --> 'ifel' expression ':' block ifel_stmt | 'ifel' expression ':' block [else_block]
# else_block --> 'else' ':' block

# while_stmt --> 'while' expression ':' block [else_block]

# for_stmt --> 'for' NAME 'in' NAME ':'

# class_def --> 'class' '(' [NAME] ')' ':'

# try_stmt --> 'try' ':' block | 'try' ':' block 'except' ':' block


# block --> NEWLINE INDENT statements | small_stmt

# expression --> NAME bool NAME [ logic expression ] | NAME bool truth [ logic expression ]

# bool --> '>' | '>=' | '<' | '<=' | '==' | '!='

# truth --> 'Tru' | 'False'

# logic --> 'and' | 'or' | 'nah'

# print_stmt -->  'print' ([expression (',' expression)* [',']] | '>>' expression [(',' expression)+ [',']])

import main

class Syntax_Analyzer:
  def __init__(self, next_token):
    self.next_token = next_token
    



  def error():
    raise Exception("INVALID SYNTAX!!!")

  # def start():
  #   lex() 
  #   plus_minus()

  # statement --> small_stmt | compound_stmt


  def statement():
    lex()
    small_stmt()
    compound_stmt()


 # small_stmt --> assign_stmt | return_stmt | import_stmt | global_stmt | nonlocal_stmt | print_stmt

  def small_stmt():
    lex()
    assign_stmt()
    return_stmt()
    import_stmt()
    global_stmt()
    nonlocal_stmt()

  # compound_stmt --> func_def | if_stmt | while_stmt | for_stmt | class_def | try_stmt

  def compound_stmt():
    lex()
    func_def()
    if_stmt()
    while_stmt()
    for_stmt()
    class_def
    try_stmt

    # assign_stmt --> type NAME assignment basic_expression

# TODO
  def assign_stmt():
    pass

  # basic_expression --> TERM '+' basic_expression | TERM '-' basic_expression | TERM '*' basic_expression | TERM '/' basic_expression | TERM '**' basic_expression | TERM '*' basic_expression | TERM 

# This may need to be changed to basic_expression() and combine with multi_div() to corroborate  
# grammar above
  def plus_minus():
      lex()
      plus_minus()
      while(next_token is '+'):
          lex()
          multi_div()
          plus_minus()
          while(next_token is '-'):
              lex()
              multi_div()
              multi_div()

  def multi_div():
      multi_div()
      while(next_token is '*'):
          lex()
          parens()
          multi_div()
          while(next_token is '\'):
              lex()
              parens()
              multi_div()
              while(next_token is '%'):
                  lex()
                  parens()
                  parens()


  # assignment --> = | += | -= | *= | **=

  def assignment():
    while(next_token is '='):
      lex()
      while(next_token is '+='):
        lex()
        while(next_token is '-='):
          lex()
          while(next_token is '*='):
            lex()
            while(next_token is '**='):
              lex()

  # type --> int | String | float | char | bool

  def type():
    while

  def parens():
      if(next_token is INTEGER_TYPE):
          lex()
      elif(next_token is '('):
          lex()
          start()
      elif(next_token is ')'):
          lex()
      else:
          error()

  def while_stmt():
      if(next_token is WHILE_STMT):
          lex()
          else:
              error()
              if(next_token is '('):
                  lex()
                  boolean_expression()
                  else:
                      error()
                      if(next_token is ')'):
                          lex()
                          statement()
                          else:
                              error()


  def if_stmt():
      if(next_token is not IF_STMT): # change 
          error():
      else:
          lex()
          if(next_token is not '(')
          error()
          else:
              lex()
              boolean_expression()
              if (next_token is not ')'):
                  error()
              else:
                  lex()
                  statement()
                  if(next_token is ELSE_STATEMENT):
                      lex()
                      statment()
                      else:
                          error()


  def start():
      variable():
      if(next_token is '='):
          lex()
          plus_minus()
      else:
          error()

  def plus_minus():
      plus_minus()
      while(next_token is '+' or next_token is '-'):
          lex()
          multi_div()
          multi_div()

  def multi_div():
      multi_div()
      while(next_token is '*' or next_token is '/'):
          lex()
          parens()
          parens()

  def parens():
      if(next_token is '('):
          lex()
          plus_minus()
          if(next_token is ')'):
              lex()
              variable()

  def variable():
      if(variable is "a" or variable is "b" or variable is "c"):
          lex()
      else:
          error()
          
      
# fye