from front import lex
import re

def check(arry, val):
    for i in arry:
        if i == val:
            return True
    return False
    
def main():
    test = open('test.txt','r').read()
    Token_arry = lex().tokenize(test)
    print(Token_arry)
    while True:
        Token_arry = statement(Token_arry)
        if len(Token_arry) == 0:
            break



def error():
    raise Exception("INVALID SYNTAX!!!")


def statement(Token_arry):
    lexT = Token_arry[0]
    small_stmt_arry = ['ID','RETURN','IMPORT','GLOBAl','NONLOCAL']
    compound_stmt_arry = ['DEF','IF','WHILE','FOR','CLASS','TRY']
    if check(small_stmt,lexT):
        Token_arry = small_stmt(Token_arry)
    else:
        Token_arry = compound_stmt
    return Token_arry


 # small_stmt --> assign_stmt | return_stmt | import_stmt | global_stmt | nonlocal_stmt | print_stmt

def small_stmt(Token_arry):
    lexT = Token_arry[0]
    if lexT == 'ID':
        Token_arry = assign_stmt()
    elif lexT == 'RETURN':
        Token_arry = return_stmt()
    elif lexT == 'IMPORT':
        Token_arry == import_stmt()
    elif lexT == 'GLOBAL':
        Token_arry == global_stmt()
    elif lexT == 'NONLOCAL':
        Token_arry == nonlocal_stmt()
    return Token_arry

  # compound_stmt --> func_def | if_stmt | while_stmt | for_stmt | class_def | try_stmt

def compound_stmt(Token_arry):
    lexT = Token_arry[0]
    if lexT == 'DEF':
        Token_arry = func_def(Token_arry)
    elif lexT == 'IF':
        Token_arry = if_stmt(Token_arry)
    elif lexT == 'WHILE':
        Token_arry = while_stmt(Token_arry)
    elif lexT == 'FOR':
        Token_arry = for_stmt(Token_arry)
    elif lexT == 'CLASS':
        Token_arry = class_stmt(Token_arry)
    elif lexT == 'TRY':
        Token_arry = try_stmt(Token_arry)
    return Token_arry

    # assign_stmt --> type NAME assignment basic_expression

#TODO
def assign_stmt(Token_arry):
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:]
    if lexT != 'ID':
        error()
    else:
        lexT = Token_arry[0]
        Token_arry = Token_arry[1:]
        assignment_arry = ['EQUAL','PLUS_EQUAL','MINUS_EQUAL','TIME_EQUAL']
        if check(assignment_arry,lexT)==False:
            error()
        else:
            error()
            Token_arry = basic_expression(Token_arry)
    return Token_arry

  # basic_expression --> TERM '+' basic_expression | TERM '-' basic_expression | TERM '*' basic_expression | TERM '/' basic_expression | TERM '**' basic_expression | TERM '*' basic_expression | TERM 

# This may need to be changed to basic_expression() and combine with multi_div() to corroborate  
# grammar above

def basic_expression(Token_arry):
    tmp = ['ID','FLOAT','INT','CHAR','BOOL','STRING']
    tmp2 = ['PLUS','MINUS','TIMES','DIV']
    #check if it basic like ID = ID
    if Token_arry[1] == 'NEWLINE' and check(tmp,Token_arry[0]):
        return Token_arry[2:]
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:]
    while True:
        if check(tmp,lexT) == False:
            error()
        else:
            lexT = Token_arry[0]
            Token_arry = Token_arry[1:]
            if check(tmp2,lexT) == False:
                error()
        if Token_arry[1] == 'NEWLINE':
            return Token_arry[2:]



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

def start(Token_arry):
    Token_arry = variable(Token_arry)
    if( is '='):
        LexT = Token_arry[0]
        Token_arry = Token_arry[1:-1]
        Token_arry = plus_minus(Token_arry)
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


def print_stmt(Token_arry):
    LexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    if LexT == "PRINT":
        LexT = Token_arry[0]
        Token_arry = Token_arry[1:-1]
        if LexT == "LEFT_PAREN"
            while(LexT != 'RIGHT_PAREN'):
                LexT = Token_arry[0]
                Token_arry = Token_arry[1:-1]


main()
