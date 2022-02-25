'''
f(x) = 2x-3
g(x,y) = 2x+y-7
h(x,y,z) = 3x-2y+z



'''
def isnumber(x):
    x = str(x)
    if x in "fgh":
        return False
    return True
a = input().split()

stack1 = []
stack2 = []
for i in a:
    if i in "fgh":
        stack1.append(i)
        stack2.append(i)
    else: 
        stack2.append(int(i))
    
    while stack1:
        if stack1[-1] == "f":
            if isnumber(stack2[-1]): 
                del stack1[-1]
                n = stack2[-1]
                del stack2[-1]
                stack2[-1] = 2*n - 3
            else:
                break
        elif stack1[-1] == "g":
            if isnumber(stack2[-1]) and isnumber(stack2[-2]):
                del stack1[-1]
                temp = stack2[-1]
                del stack2[-1]
                temp2 = stack2[-1]
                del stack2[-1]
                stack2[-1] = 2*temp2 + temp - 7
            else:
                break
        else:
            if isnumber(stack2[-1]) and isnumber(stack2[-2]) and isnumber(stack2[-3]):
                del stack1[-1]
                n1 = stack2[-1]
                n2 = stack2[-2]
                n3 = stack2[-3]
                del stack2[-1]
                del stack2[-1]
                del stack2[-1]
                stack2[-1] = n3*3 - 2 * n2 + n1
            else:
                break
    print(stack2)

print(stack2[-1])
