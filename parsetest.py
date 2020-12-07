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
  #   plus_minus()

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
    lexT = Token_arry[0]
    if lexT == 'ID':
        Token_arry = assign_stmt(Token_arry)

    return Token_arry

  # compound_stmt --> func_def | if_stmt | while_stmt | for_stmt | class_def | try_stmt



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
            

main()