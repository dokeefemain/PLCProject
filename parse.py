from front import lex
import re

# class Syntax_Analyzer:
#   def __init__(self, lex.tokenize(str)
# ):
#     self.lex.tokenize(str)
#  = lex.tokenize(str)

    
def main():
    test = open('test.txt','r').read()
    Token_arry = lex().tokenize(test)
    print(Token_arry)
    statement(Token_arry)


def error():
    raise Exception("INVALID SYNTAX!!!")

  # def start():
  #   lex() 
  #   plus_minus()

  # statement --> small_stmt | compound_stmt


def statement(Token_arry):
    #lex()
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    print(lexT)
    small_stmt(Token_arry)
    compound_stmt(toke)


 # small_stmt --> assign_stmt | return_stmt | import_stmt | global_stmt | nonlocal_stmt | print_stmt

def small_stmt(Token_arry):
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
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
    class_def()
    try_stmt()

    # assign_stmt --> type NAME assignment basic_expression

# TODO
def assign_stmt():
    type()
    lex()
    assignment()
    basic_expression()

  # basic_expression --> TERM '+' basic_expression | TERM '-' basic_expression | TERM '*' basic_expression | TERM '/' basic_expression | TERM '**' basic_expression | TERM '*' basic_expression | TERM 

# This may need to be changed to basic_expression() and combine with multi_div() to corroborate  
# grammar above

def basic_expression():
    plus_minus()

def plus_minus():
      lex()
      plus_minus()
      while(lex.tokenize(str) is '+'):
          lex()
          multi_div()
          plus_minus()
          while(lex.tokenize(str) is '-'):
              lex()
              multi_div()
              multi_div()

def multi_div():
      multi_div()
      while(lex.tokenize(str) is '*'):
          lex()
          parens()
          multi_div()
          while(lex.tokenize(str) is '\/'):
              lex()
              parens()
              multi_div()
              while(lex.tokenize(str) is '%'):
                  lex()
                  parens()
                  parens()


  # assignment --> = | += | -= | *= | **=

def assignment():
    while(lex.tokenize(str) is '='):
      lex()
      while(lex.tokenize(str) is '+='):
        lex()
        while(lex.tokenize(str) is '-='):
          lex()
          while(lex.tokenize(str) is '*='):
            lex()
            while(lex.tokenize(str) is '**='):
              lex()

  # type --> int | String | float | char | bool

def type():
    while(lex.tokenize(str) is 'INT'):
      lex()
      while(lex.tokenize(str) is 'STRING'):
        lex()
        while(lex.tokenize(str) is 'FLOAT'):
          lex()
          while(lex.tokenize(str) is 'CHAR'):
            lex()
            while(lex.tokenize(str) is 'BOOL'):
              lex()

def parens():
      if(lex.tokenize(str) is 'INT'):
          lex()
      elif(lex.tokenize(str) is '('):
          lex()
          start()
      elif(lex.tokenize(str) is ')'):
          lex()
      else:
          error()

# while_stmt --> 'while' expression ':' block [else_block]


def while_stmt():
    if(lex.tokenize(str) is 'WHILE'):
        lex()
    
        if(lex.tokenize(str) is '('):
            lex()
            bool()
        
            if(lex.tokenize(str) is ')'):
                lex()
                statement()
            else:
                error()
# if_stmt --> 'if' expression ':' block ifel_stmt | 'if' expression ':' block [else_block]
#TODO
# def if_stmt():
#     if(lex.tokenize(str) is not 'IF'): # change 
#         error()
#     else:
#         lex()
#         if(lex.tokenize(str) is not '('):
#             error()
#         else:
#             lex()
#             bool()
#             if (lex.tokenize(str) is not ')'):
#                 error()
#             else:
#                 lex()
#                 statement()
#                 if(lex.tokenize(str) is 'ELSE'):
#                     lex()
#                     statement()
#                 else:
#                     error()

def if_stmt(Token_arry):
    LexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    if(LexT is not 'IF'): # change 
        error()
    else:
        LexT = Token_arry[0]
        Token_arry = Token_arry[1:-1]
        if(LexT is not '('):
            error()
        else:
            LexT = Token_arry[0]
            Token_arry = Token_arry[1:-1]
            #bool(Token_arry)
            if (LexT is not ')'):
                error()
            else:
                LexT = Token_arry[0]
                Token_arry = Token_arry[1:-1]
                #statement(Token_arry)
                if(LexT is 'IFEL'):
                    #ifel_stmt(Token_arry)
                
                else:
                    LexT = Token_arry[0]
                    Token_arry = Token_arry[1:-1]
                    #statement(Token_arry)
                    if(LexT is 'ELSE'):
                        LexT = Token_arry[0]
                        Token_arry = Token_arry[1:-1]
                        #statement(Token_arry)
                    else:
                        error()


# ifel_stmt --> 'ifel' expression ':' block ifel_stmt | 'ifel' expression ':' block [else_block]
#TODO
# def ifel_stmt():
#     if(lex.tokenize(str) is not 'IFEL'): # change 
#         error()
#     else:
#         lex()
#         if(lex.tokenize(str) is not '('):
#             error()
#         else:
#             lex()
#             bool()
#             if (lex.tokenize(str) is not ')'):
#                 error()
#             else:
#                 lex()
#                 statement()
#                 if(lex.tokenize(str) is 'ELSE'):
#                     lex()
#                     statement()
#                 else:
#                     error()

def ifel_stmt():
    if(lex.tokenize(str) is not 'IF'):
        error()
    else:
        lex()
        if(lex.tokenize(str) is not '('):
            error()
        else:
            lex()
            bool()
            if (lex.tokenize(str) is not ')'):
                error()
            else:
                lex()
                statement()
                if(lex.tokenize(str) is 'IFEL'):
                    lex()
                    statement()
                
                else:
                    lex()
                    statement()
                    if(lex.tokenize(str) is not 'ELSE'):
                        error()
                    else:
                        lex()
                        statement()


# else_block --> 'else' ':' block
#TODO
def else_block():
    if(lex.tokenize(str) is 'ELSE'):
        lex()
        statement()
    else:
        error()

def start():
    variable()
    if(lex.tokenize(str) is '='):
        lex()
        plus_minus()
    else:
        error()



# def plus_minus():
#     plus_minus()
#     while(lex.tokenize(str) is '+' or lex.tokenize(str) is '-'):
#         lex()
#         multi_div()
#         multi_div()

# def multi_div():
#     multi_div()
#     while(lex.tokenize(str) is '*' or lex.tokenize(str) is '/'):
#         lex()
#         parens()
#         parens()

def parens():
    if(lex.tokenize(str) is '('):
        lex()
        plus_minus()
        if(lex.tokenize(str) is ')'):
            lex()
            variable()

def variable():
    if(variable is "a" or variable is "b" or variable is "c"):
        lex()
    else:
        error()
          
      
# import_stmt --> 'import' NAME

def import_stmt():
    while(lex.tokenize(str) is 'import'):
        lex()
        return 'NAME'

# return_stmt --> 'return' return_list

def return_stmt():
    while(lex.tokenize(str) is 'return'):
        lex()
        return_list()
    while not(lex.tokenize(str) is 'return'):
        error()


# bool --> '>' | '>=' | '<' | '<=' | '==' | '!='
def bool():
    if(lex.tokenize(str) is '>'):
        lex()
    elif(lex.tokenize(str) is '>='):
        lex()
    elif(lex.tokenize(str) is '<'):
        lex()
    elif(lex.tokenize(str) is '<='):
        lex()
    elif(lex.tokenize(str) is '=='):
        lex()
    elif(lex.tokenize(str) is '!='):
        lex()
    else:
        error()


# global_stmt --> 'global' NAME+

def global_stmt():
    if(lex.tokenize(str) is 'global'):
        lex()
    else:
        error()


# nonlocal_stmt --> 'nonlocal' NAME+

def nonlocal_stmt():
    if(lex.tokenize(str) is 'nonlocal'): 
        lex()
    else:
        error()

# func_def --> 'def' NAME '(' [NAME] ')' ':'
def func_def():
    if(lex.tokenize(str) is 'DEF'):
        lex()
    
        if(lex.tokenize(str) is '('):
            lex()
            bool()

            if(lex.tokenize(str) is 'NAME'):
                lex()
        
                if(lex.tokenize(str) is ')'):
                    lex()
                    statement()
                else:
                    error()

# for_stmt --> 'for' NAME 'in' NAME ':'

def for_stmt():
    if(lex.tokenize(str) is 'for'): 
        lex()
        if(lex.tokenize(str) is 'NAME'):
            lex()
            if(lex.tokenize(str) is 'in'):
                lex()
                if(lex.tokenize(str) is 'NAME'):
                    lex()

# class_def --> 'class' '(' [NAME] ')' ':'
def class_def():
    if(lex.tokenize(str) is 'CLASS'): 
        lex()
    
        if(lex.tokenize(str) is '('):
            lex()
            bool()

            if(lex.tokenize(str) is 'NAME'):
                lex()
        
                if(lex.tokenize(str) is ')'):
                    lex()
                    statement()
                else:
                    error()


# try_stmt --> 'try' ':' block | 'try' ':' block 'except' ':' block
def try_stmt():
    while(lex.tokenize(str) is 'try'):
        lex()

#TODO       
# return_list --> RETURNVAR (',' RETURNVAR )+ [','] | RETURNVAR ',' | RETURNVAR
def return_list():
    pass

# truth --> 'Tru' | 'False'
def truth():
    if(lex.tokenize(str) is 'Tru'):
        lex()
    elif(lex.tokenize(str) is 'False'):
        lex()
    else:
        error()

# block --> NEWLINE INDENT statements | small_stmt
#TODO
def block():
    pass

# expression --> NAME bool NAME [ logic expression ] | NAME bool truth [ logic expression ]
#TODO

def expression():
    pass

# logic --> 'and' | 'or' | 'nah'
def logic():
    if(lex.tokenize(str) is 'and'):
        lex()
    elif(lex.tokenize(str) is 'or'):
        lex()
    elif(lex.tokenize(str) is 'nah'):
        lex()
    else:
        error()

# print_stmt -->  'print' ([expression (',' expression)* [',']] | '>>' expression [(',' expression)+ [',']])


def print_stmt():
    while(lex.tokenize(str) is 'print'):
        lex()


main()
