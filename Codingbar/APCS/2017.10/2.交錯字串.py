n = int(input())

string = input()

length = len(string)
s = ""

for i in string:
    if ord(i) <= 90:
        s += "0"
    else:
        s += "1"

test1 = "0"*n + "1"*n 
test2 = "1"*n + "0"*n 

# print(s)
count = length // (2**n)

ans = 0
if n == 1:
    ans = 1
for i in range(0,count):
    if test1*i in s:
        if test1*i + "0"*n in s:
            ans = max(ans, 2*i*n + n)
        else:
            ans = max(ans, 2*i*n)
    if test2*i in s:    
        if test2*i + "1"*n in s:
            ans = max(ans, 2*i*n + n)
        else:
            ans = max(ans, 2*i*n)
print(ans)       

