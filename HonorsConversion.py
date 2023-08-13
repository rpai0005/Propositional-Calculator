def truthTableGen(numOfVars):
    rowNum = 2 ** numOfVars
    change = rowNum / 2
    truthTable = list()
    switch = True
    
    for p in range(rowNum):
        truthTable.append([])
    
    while change >= 1:
        count = 0
        for row in truthTable:
            if switch:
                row.append('T')
                count = count + 1
                
            if not switch:
                row.append('F')
                count = count + 1
                
            if count % change == 0:
                    switch = not(switch)
                    
        change = change / 2
                    
    return truthTable
  
#x = truthTableGen(2)
#print(x)

def combinePremises(d):
    combList = []
    simList = []
    count = 0
    for lis in d.values():
        combList += lis
        count += 1

    combList.sort()
    
    for ele in combList:
        num = combList.count(ele)
        if num == count and ele not in simList:
            simList.append(ele)
    return simList

d1 = {1: [1, 2, 3, 4, 5], 
      2: [5, 4, 3, 2, 1],
      3: [5, 6, 7]}

#print(combinePremises(d1))

def compPremCon(prem, con):
    for model in prem:
        if model not in con:
            return False
    return True

p = [1, 6]
c = [1, 2, 3, 4, 5]

#print(compPremCon(p, c))

def tempStringGen(prem, var, row):
    tempString = ''
    if var == 1:
        tempString = prem.replace("a", row[0])
    elif var == 2:
        tempString = prem.replace("a", row[0])
        tempString = tempString.replace("b", row[1])
    elif var == 3:
        tempString = prem.replace("a", row[0])
        tempString = tempString.replace("b", row[1])
        tempString = tempString.replace("c", row[2])
    elif var == 4:
        tempString = prem.replace("a", row[0])
        tempString = tempString.replace("b", row[1])
        tempString = tempString.replace("c", row[2])
        tempString = tempString.replace("d", row[3])
    else:
        tempString = prem.replace("a", row[0])
        tempString = tempString.replace("b", row[1])
        tempString = tempString.replace("c", row[2])
        tempString = tempString.replace("d", row[3])
        tempString = tempString.replace("e", row[4])
    
    return tempString

#print(tempStringGen("a&b", 2, ['T', 'T']))