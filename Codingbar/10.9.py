s = input()
a = int(input())

length = len(s) - a
while len(s) != length:
    minv = 10**251
    index = 0
    for i in range(len(s)):
        # print(minv,int(s[:i] + s[i+1:]))
        if minv > int(s[:i] + s[i+1:]): 
            minv = int(s[:i] + s[i+1:])
            index = i
    # print(s[index])
    s = s[:index] + s[index+1:]
while s and s[0] == "0":
    s = s[1:]
if s:
    print(s)
else:
    print(0)

    '''
    
    175438 
    1

    175438

    17543
    '''