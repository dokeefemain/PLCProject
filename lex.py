def check(arry,mychar):
  for i in arry:
    if i == mychar:
      return True
  return False


file = open("test.txt","r")
basic_exp = ["+","-","*","/"]
quote = ['"']
assignment = ["=","+=","-=","*=", "**="]
type = ["int", "String", "float", "char" , "bool"]
bool = [">", ">=", "<", "<=" , "==" "!="]
logic = ["and", "or", "nah"]
line = file.read()
str = line.split()
keywords = ["and", "or", "nah", "Tru", "False", "import", "from", "class", "def", "if", "ifel", "else", "for", "while", "return", "try", "except", "int", "String", "char", "bool", "global", "nonlocal"]
for i in str:
  if i[0] in quote:
    print("string: " ,i)

for i in str:
  if i.isdigit():
    print("integers: ", i)

for i in str:
  if i.isalpha() and check(keywords,i) == False:
    print("Identifier: ", i)


for i in str:                               
  if i[0].isalnum() and i != "=":
    for ch in range(len(i)):
      if check(basic_exp,i[ch]) and i[ch+1]!= '=': 
        print("basic_exp : ",i)

for i in str:
  if i[0].isalnum():
    for ch in i:
      if check(assignment,ch):
        print("assignment: ", i)

for i in str:
  if i in type:
    print("type = ",i )

for i in str:
  if i == "import":
    print ("import_stmt:", i)

for i in str:
  if i == "return":
    print ("return_stmt:", i)

for i in str:
  if i == "global":
    print ("global_stmt:", i)

for i in str:
  if i == "def":
    print ("func_def:", i)

for i in str:
  if i == "nonlocal":
    print ("nonlocal_stmt:", i)

for i in str:
  if i == "if":
    print ("if_stmt:", i)

for i in str:
  if i == "elif":
    print ("elif_stmt:", i)

for i in str:
  if i == "while":
    print ("while_stmt:", i)

for i in str:
  if i == "for":
    print ("for_stmt:", i)    

for i in str:
  if i == "class_def":
    print ("class_def:", i)

for i in str:
  if i == "try":
    print ("try_stmt:", i) 

for i in str:
  if i[0].isalnum():
    for ch in i:
      if ch in bool:
        print("bool: ", i)

for i in str:
  if i in logic:
    print ("logic: ",i)

for i in str: 
  if i[0].isdigit() or i[0] == '.':
    for ch in i:
      if ch == 'e' or ch == 'E' or ch == '.':
        print ("real: ",i)
