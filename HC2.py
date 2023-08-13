priority = {'-': 1, "&": 2, "v": 3, "+": 4, ">": 5, "~": 6}
operators = {'&',"v","-", ">","~", "+", "(", ")"} 

class Node:
    def __init__(self, value,  left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
    def changeValBool(self):
        if self.value == 'T':
            self.value = True
        elif self.value == 'F':
            self.value = False
            
    def __str__(self):
        return str(self.value)

def isOperator(c):
    return c == "&" or c == "v" or c == "-" or c == ">" or c == "<" or c == "~"

def implies(a, b):
    if a is True and b is False:
        return False
    return True

def bicond(a, b):
    return implies(a, b) and implies(b, a)

def xor(a, b):
    if (a and (not b)) or (b and (not a)):
        return True
    return False

def postorder(root):
    if root is None:
        return None
    postorder(root.left)
    postorder(root.right)
    print(root.value, end = '')

def inorder(root):
    if root is None:
        return
    if isOperator(root.value):
        print("(", end = '')
    
    inorder(root.left)
    print(root.value, end = '')
    inorder(root.right)
    
    if isOperator(root.value):
        print(')', end='')
        
def constructTree(postfix):
    stack = []
    
    for ch in postfix:
        if ch in operators:
            if ch == "-":
                nt = stack.pop()
                
                t = Node(ch, nt, None)
                stack.append(t)
            
            else:
                x = stack.pop()
                y = stack.pop()
                temp = Node(ch, y, x)
                stack.append(temp)
        else:
            n = Node(ch)
            n.changeValBool()
            stack.append(n)
    
    return stack[-1]

def inToPost(formula):
    s = []
    output = ""
    for ch in formula:
        if ch not in operators:
            output += ch
        elif ch == "(":
            s.append(ch)
        elif ch == ")":
            while s and s[-1] != "(":
                output += s.pop()
            s.pop()
        else:
            while s and s[-1] != "(" and priority[ch] <= priority[s[-1]]:
                output += s.pop()
            s.append(ch)
     
    while s: output += s.pop()
    return output

def evalExpr(root):
    if root is None:
        return
    
    if root.left is None and root.right is None:
        return root.value
    
    leftTruth = evalExpr(root.left)
    rightTruth = evalExpr(root.right)

    if root.value == "&":
        return (leftTruth and rightTruth)
    elif root.value == "v":
        return (leftTruth or rightTruth)
    elif root.value == "-":
        return not(leftTruth)
    elif root.value == ">":
        return implies(leftTruth, rightTruth)
    elif root.value == "~":
        return bicond(leftTruth, rightTruth)
    elif root.value == "+":
        return xor(leftTruth, rightTruth)

#a = True
#b = False
#print(xor(a, b))
#infix = "T"
#r1 = inToPost(infix)
#print(r1)
#t1 = constructTree(r1)
#print(t1.value)
#print(t1.left.left)
#print(t1.right.left)
#print(type(t1.value))
#print(type(t1))
#print(t1)
#print(t1.left)
#print("PostFix")
#postorder(t1)
#print("\nInfix")
#inorder(t1)
#print("\n")
#print(evalExpr(t1))
#print(type(evalExpr(t1)))
#n1 = Node(True)
#print(n1.value)
#print(n1.left)
#print(n1.right)
#&, v, -, >, <

