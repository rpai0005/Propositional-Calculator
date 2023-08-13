priority = {'&': 1, "v": 2, "-": 3, ">": 4, "~": 5}
operators = {'&',"v","-", ">","~", "(", ")"} 

from HC2 import Node, implies, bicond, constructTree, inToPost, evalExpr
from HonorsConversion import truthTableGen, combinePremises, compPremCon, tempStringGen

print("WELCOME to the Propositional Logic Calculator!" + 
      "\nThis application will let you imput a set of premises, and will verify if a certain conclusion is VALID or INVALID!")

print("\n\t\t  ~~~~Instructions~~~~\n")
print("-------------------------------------------")
print("\nInput premises that have up to 5 VARIABLES. Use variable names a, b, c, d, e (LOWERCASE) when inputting all premises."+
      "\nFor the operators and, or, xor, not, implies, and biconditional, use the symbols &, v, +, -, >, and ~ respectively."+
      "\nDO NOT PUT ANY SPACES BETWEEN THE SYMBOLS AND VARIABLES")
print("\nMake sure to PUT PERENTHESIS AROUND ANY EXPRESSIONS that should get preference in premises!")
print("\nExample Premise: (a&b)v(-c) for \"(a and b) or (not c)\"")


var = input("How many variables will there be in all: ")
var = int(var)
premiseDict = dict()
count = 1
tempPrem = ""
print("\nInput Premises. Enter 'Q' to stop inputting premises!")
print("---------------------------------------------------------")
while tempPrem != "Q":
    tempPrem = input("Premise: ")
    if tempPrem != "Q":
        premiseDict[count] = tempPrem
        count += 1

conclusion = input("What is the conclusion you would like to verify? : ")

table = truthTableGen(var)

count = 0
count2 = 1
tempString = ''
tempList = []

for prem in premiseDict.values():
    for row in table:
        t = tempStringGen(prem, var, row)

        post = inToPost(t)
        tempTree = constructTree(post)
        tempEval = evalExpr(tempTree)
        
        if tempEval:
            tempList.append(count)
        
        count += 1
    
    count = 0
    premiseDict[count2] = tempList
    tempList = []
    count2 += 1

concludeList = []
count3 = 0

for r in table:
    h = tempStringGen(conclusion, var, r)
    p = inToPost(h)
    tree = constructTree(p)
    e = evalExpr(tree)
    
    if e:
      concludeList.append(count3)
    count3 += 1

c = combinePremises(premiseDict)
validity = compPremCon(c, concludeList)

if validity:
    print("\nThis is a VALID argument!")
else:
    print("\nUnfortunately, this argument is NOT VALID")