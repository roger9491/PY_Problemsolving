'''
ceaaaabb
ceaa    aabb
ce aa   aa bb

bbaa    ddcc
1 2 1 2 1
1 1 2 1 2
'''
def divid(string):
    global c
    print(string,c)
    if len(string) == 1 or len(set(string)) == 1:
        print(set(string))
        return

    c += 1

    divid(string[:len(string)//2])
    divid(string[len(string)//2:])    
    c -= 1

n = int(input())

for i in range(n):
    length = int(input()) 
    string = input()
    if length <= 2:
        print(2)
    else:
        c = 0
        divid(string)
        print(c)