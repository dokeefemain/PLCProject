from front import lex
import re

# class Syntax_Analyzer:
#   def __init__(self, lex.tokenize(str)
# ):
#     self.lex.tokenize(str)
#  = lex.tokenize(str)
def check(arry, val):
    for i in arry:
        if i == val:
            return True
    return False
    
def main():
    test = open('test.txt','r').read()
    Token_arry = lex().tokenize(test)
    while True:
        Token_arry = statement(Token_arry)
        if len(Token_arry) == 0:
            break



def error():
    raise Exception("INVALID SYNTAX!!!")

  # def start():
  #   lex() 
  #   basic_expression()

  # statement --> small_stmt | compound_stmt


def statement(Token_arry):
    #lex()
    lexT = Token_arry[0]
    small_stmt_arry = ['ID','RETURN','IMPORT','GLOBAl','NONLOCAL']
    #compound_stmt_arry = ['DEF','IF','WHILE','FOR','CLASS','TRY']
    if check(small_stmt_arry,lexT):
        Token_arry = small_stmt(Token_arry)

    return Token_arry


 # small_stmt --> assign_stmt | return_stmt | import_stmt | global_stmt | nonlocal_stmt | print_stmt

def small_stmt(Token_arry):
    # lexT = Token_arry[0]
    # if lexT == 'ID':
    #     Token_arry = assign_stmt(Token_arry)

    # return Token_arry

    
    lexT = Token_arry[0]
    if lexT == 'ID':
        Token_arry = assign_stmt(Token_arry)
    elif lexT == 'RETURN':
        Token_arry = return_stmt(Token_arry)
    elif lexT == 'IMPORT':
        Token_arry = import_stmt(Token_arry)
    elif lexT == 'GLOBAL':
        Token_arry = global_stmt(Token_arry)
    elif lexT == 'NONLOCAL':
        Token_arry = nonlocal_stmt(Token_arry)
    else:
        Token_arry = print_stmt

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
        Token_arry = class_def(Token_arry)
    else:
        Token_arry = try_stmt

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
            print(Token_arry)
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
            


# def compound_stmt(Token_arry):
#     lexT = Token_arry[0]
#     if lexT == 'ID':
#         Token_arry = func_def(Token_arry)

#     return Token_arry

def func_def(Token_arry):
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    if(lexT is 'DEF'):
        Token_arry = Token_arry[1:-1]
        Token_arry = basic_expression(Token_arry)
    
        if(lexT is 'LEFT_PAREN'):
            Token_arry = Token_arry[1:-1]
            Token_arry = basic_expression(Token_arry)
            Token_arry = bool(Token_arry)

            if(lexT is 'ID'):
                Token_arry = Token_arry[1:-1]
                Token_arry = basic_expression(Token_arry)

                if(lexT is 'RIGHT_PAREN'):
                    Token_arry = Token_arry[1:-1]
                    Token_arry = basic_expression(Token_arry)
                    Token_arry = statement(Token_arry)
                else:
                    error()

def return_stmt(Token_arry):
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    while(lexT is 'return'):
        Token_arry = Token_arry[1:-1]
        Token_arry = basic_expression(Token_arry)
        Token_arry = return_list(Token_arry)
    while not(lexT is 'return'):
        error()

def return_list(Token_arry):
    LexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    if LexT == "RETURNVAR":
        LexT = Token_arry[0]
        Token_arry = Token_arry[1:-1]
        if LexT == "LEFT_PAREN":
            while(LexT != 'RIGHT_PAREN'):
                LexT = Token_arry[0]
                Token_arry = Token_arry[1:-1]

def import_stmt(Token_arry):
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    while(lexT is 'import'):
        Token_arry = Token_arry[1:-1]
        Token_arry = basic_expression(Token_arry)
        return 'ID'

def global_stmt(Token_arry):
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    if(lexT is 'GLOBAL'):
        Token_arry = Token_arry[1:-1]
        Token_arry = basic_expression(Token_arry)
    else:
        error()            

def nonlocal_stmt(Token_arry):
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    if(lexT is 'NONLOCAL'): 
        Token_arry = Token_arry[1:-1]
        Token_arry = basic_expression(Token_arry)
    else:
        error()

def print_stmt(Token_arry):
    LexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    if LexT == "PRINT":
        LexT = Token_arry[0]
        Token_arry = Token_arry[1:-1]
        if LexT == "LEFT_PAREN":
            while(LexT != 'RIGHT_PAREN'):
                LexT = Token_arry[0]
                Token_arry = Token_arry[1:-1]

def if_stmt(Token_arry):
    LexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    if(LexT is not 'IF'): # change 
        error()
    else:
        LexT = Token_arry[0]
        Token_arry = Token_arry[1:-1]
        if(LexT is not 'LEFT_PAREN'):
            error()
        else:
            LexT = Token_arry[0]
            Token_arry = Token_arry[1:-1]
            Token_arry = bool(Token_arry)
            if (LexT is not 'RIGHT_PAREN'):
                error()
            else:
                LexT = Token_arry[0]
                Token_arry = Token_arry[1:-1]
                Token_arry = statement(Token_arry)
                if(LexT is 'IFEL'):
                    Token_arry = ifel_stmt(Token_arry)
                else:
                    LexT = Token_arry[0]
                    Token_arry = Token_arry[1:-1]
                    Token_arry = statement(Token_arry)
                    if(LexT is 'ELSE'):
                        LexT = Token_arry[0]
                        Token_arry = Token_arry[1:-1]
                        Token_arry = statement(Token_arry)
                    else:
                        error()

def ifel_stmt(Token_arry):
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    if(lexT is not 'IF'):
        error()
    else:
        lexT = Token_arry[0]
        Token_arry = Token_arry[1:-1]
        if(lexT is not 'LEFT_PAREN'):
            error()
        else:
            lexT = Token_arry[0]
            Token_arry = Token_arry[1:-1]
            Token_arry = bool(Token_arry)
            if (lexT is not 'RIGHT_PAREN'):
                error()
            else:
                lexT = Token_arry[0]
                Token_arry = Token_arry[1:-1]
                Token_arry = statement(Token_arry)
                if(lexT is 'IFEL'):
                    lexT = Token_arry[0]
                    Token_arry = Token_arry[1:-1]
                    Token_arry = statement(Token_arry)               
                else:
                    lexT = Token_arry[0]
                    Token_arry = Token_arry[1:-1]
                    Token_arry = statement(Token_arry)
                    if(lexT is not 'ELSE'):
                        error()
                    else:
                        lexT = Token_arry[0]
                        Token_arry = Token_arry[1:-1]
                        Token_arry = statement(Token_arry)

def while_stmt(Token_arry):
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    if(lexT is 'WHILE'):
        lexT = Token_arry[0]
        Token_arry = Token_arry[1:-1]
    
        if(lexT is 'LEFT_PAREN'):
            lexT = Token_arry[0]
            Token_arry = Token_arry[1:-1]
            Token_arry = bool(Token_arry)
        
            if(lexT is 'RIGHT_PAREN'):
                lexT = Token_arry[0]
                Token_arry = Token_arry[1:-1]
                Token_arry = statement(Token_arry)
            else:
                error()

def for_stmt(Token_arry):
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    if(lexT is 'FOR'): 
        Token_arry = basic_expression(Token_arry)
        Token_arry = statement(Token_arry)
        if(lexT is 'ID'):
            Token_arry = basic_expression(Token_arry)
            Token_arry = statement(Token_arry)
            if(lexT is 'in'):
                Token_arry = basic_expression(Token_arry)
                Token_arry = statement(Token_arry)
                if(lexT is 'ID'):
                    Token_arry = basic_expression(Token_arry)
                    Token_arry = statement(Token_arry)

def class_def(Token_arry):
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    if(lexT is 'CLASS'): 
        Token_arry = basic_expression(Token_arry)
        Token_arry = statement(Token_arry)
    
        if(lexT is 'LEFT_PAREN'):
            Token_arry = basic_expression(Token_arry)
            Token_arry = statement(Token_arry)
            Token_arry = bool(Token_arry)

            if(lexT is 'ID'):
                Token_arry = basic_expression(Token_arry)
                Token_arry = statement(Token_arry)
        
                if(lexT is 'RIGHT_PAREN'):
                    Token_arry = basic_expression(Token_arry)
                    Token_arry = statement(Token_arry)
                    Token_arry = statement(Token_arry)
                else:
                    error()
def try_stmt(Token_arry):
    lexT = Token_arry[0]
    if lexT == 'TRY':
        Token_arry = block(Token_arry)
        if lexT == 'EXCEPT':
            Token_arry = except_stmt(Token_arry)

def except_stmt(Token_arry):
    lexT = Token_arry[0]
    if lexT == 'EXCEPT':
        Token_arry = block(Token_arry)


def block(Token_arry):
    lexT = Token_arry[0]
    Token_arry = statement(Token_arry)
    Token_arry = small_stmt(Token_arry)

def type(Token_arry):
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    while(lexT is 'INT'):
        lexT = Token_arry[0]
        Token_arry = Token_arry[1:-1]
        while(lexT is 'STRING'):
            lexT = Token_arry[0]
            Token_arry = Token_arry[1:-1]
            while(lexT is 'FLOAT'):
                lexT = Token_arry[0]
                Token_arry = Token_arry[1:-1]
                while(lexT is 'CHAR'):
                    lexT = Token_arry[0]
                    Token_arry = Token_arry[1:-1]
                    while(lexT is 'BOOL'):
                        lexT = Token_arry[0]
                        Token_arry = Token_arry[1:-1]

def parens(Token_arry):
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    if(lexT is 'INT'):
        lexT = Token_arry[0]
        Token_arry = Token_arry[1:-1]
    elif(lexT is 'LEFT_PAREN'):
        lexT = Token_arry[0]
        Token_arry = Token_arry[1:-1]
        Token_arry = start(Token_arry)
    elif(lexT is 'RIGHT_PAREN'):
        lexT = Token_arry[0]
        Token_arry = Token_arry[1:-1]
    else:
        error()

def start(Token_arry):
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    Token_arry = variable(Token_arry)
    if(lexT is 'EQUAL'):
        LexT = Token_arry[0]
        Token_arry = Token_arry[1:-1]
        Token_arry = basic_expression(Token_arry)
    else:
        error()

def variable(Token_arry):
    if(variable is "a" or variable is "b" or variable is "c"):
        Token_arry = Token_arry[1:-1]
        Token_arry = basic_expression(Token_arry)
    else:
        error()

def bool(Token_arry):
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    if(lexT is 'GREATER'):
        Token_arry = Token_arry[1:-1]
        Token_arry = basic_expression(Token_arry)
    elif(lexT is 'GREATER_EQUAL'):
        Token_arry = Token_arry[1:-1]
        Token_arry = basic_expression(Token_arry)
    elif(lexT is 'LESS'):
        Token_arry = Token_arry[1:-1]
        Token_arry = basic_expression(Token_arry)
    elif(lexT is 'LESS_EQUAL'):
        Token_arry = Token_arry[1:-1]
        Token_arry = basic_expression(Token_arry)
    elif(lexT is 'EQUAL_TO'):
        Token_arry = Token_arry[1:-1]
        Token_arry = basic_expression(Token_arry)
    elif(lexT is 'DOESNT_EQUAL'):
        Token_arry = Token_arry[1:-1]
        Token_arry = basic_expression(Token_arry)
    else:
        error()

def logic(Token_arry):
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    if(lexT is 'and'):
        lex()
    elif(lexT is 'or'):
        lex()
    elif(lexT is 'nah'):
        lex()
    else:
        error()

def truth(Token_arry):
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    if(lexT is 'Tru'):
        lex()
    elif(lexT is 'False'):
        lex()
    else:
        error()

def except_block(Token_arry):
    lexT = Token_arry[0]
    if lexT == 'EXCEPT':
        Token_arry = block(Token_arry)

def else_block(Token_arry):
    lexT = Token_arry[0]
    Token_arry = Token_arry[1:-1]
    if(lexT is 'ELSE'):
        lexT = Token_arry[0]
        Token_arry = Token_arry[1:-1]
        Token_arry = statement(Token_arry)
    else:
        error()
    
main()