def check(arry,mychar):
  for i in arry:
    if i == mychar:
      return True
  return False


file = open("test.txt","r")
basic_exp = ["+","-","*","/"]
quote = ['"']
assignment = ["=","+=","-=","*=", "**="]
types = ["int", "String", "float", "char" , "bool"]
bools = [">", ">=", "<", "<=" , "==" "!="]
logic = ["and", "or", "nah"]
line = file.read()
strs = line.split()
keywords = ["and", "or", "nah", "Tru", "False", "import", "from", "class", "def", "if", "ifel", "else", "for", "while", "return", "try", "except", "int", "String", "char", "bool", "global", "nonlocal"]
for i in strs:
  if i[0] in quote:
    print("string: " ,i)

for i in strs:
  if i.isdigit():
    print("integers: ", i)

for i in strs:
  if i.isalpha() and check(keywords,i) == False:
    print("Identifier: ", i)


for i in strs:                               
  if i[0].isalnum() and i != "=":
    for ch in range(len(i)):
      if check(basic_exp,i[ch]) and i[ch+1]!= '=': 
        print("basic_exp : ",i)

for i in strs:
  if i[0].isalnum():
    for ch in range(len(i)):
      if (i[ch] == '+' or i[ch] == '-' or i[ch] =='*') and i[ch+1] == '=':
        tmp = i[ch:ch+2]
        if check(assignment,tmp):
          print("assignment: ", i)
      elif i[ch] == '=' and i[ch-1].isalnum() and i[ch+1].isalnum():
        print("assignment: ", i)

for i in strs:
  if i in types:
    print("type = ",i )

for i in strs:
  if i == "import":
    print ("import_stmt:", i)

for i in strs:
  if i == "return":
    print ("return_stmt:", i)

for i in strs:
  if i == "global":
    print ("global_stmt:", i)

for i in strs:
  if i == "def":
    print ("func_def:", i)

for i in strs:
  if i == "nonlocal":
    print ("nonlocal_stmt:", i)

for i in strs:
  if i == "if":
    print ("if_stmt:", i)

for i in strs:
  if i == "elif":
    print ("elif_stmt:", i)

for i in strs:
  if i == "while":
    print ("while_stmt:", i)

for i in strs:
  if i == "for":
    print ("for_stmt:", i)    

for i in strs:
  if i == "class_def":
    print ("class_def:", i)

for i in strs:
  if i == "try":
    print ("try_stmt:", i) 


for i in strs:
  if i[0].isalnum():
    for ch in range(len(i)):
      test = False
      if i[ch] == '>' or i[ch] == '<' or i[ch] == '=' or i[ch] == '!':
        if i[ch] == '='and i[ch+1] == '=':
          test = True
        elif i[ch] != '=':
          test = True
        if test == True:
          print("bool: ", i)

for i in strs:
  if i in logic:
    print ("logic: ",i)

for i in strs: 
  if i[0].isdigit() or i[0] == '.':
    for ch in i:
      if ch == 'e' or ch == 'E' or ch == '.':
        print ("real: ",i)
