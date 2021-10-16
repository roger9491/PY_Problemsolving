'''
有一個字串
你可以對這個字串做兩種操作
1   取字串的字首加在新字串尾端
2   取字串的字尾加在新字串尾端
求 新字串字典序最小
輸入格式:
1 輸入數字 代表字串長度
2 輸入字串
輸出
新字串
ex
6
ACDBCB

ABCBCD
'''


n = int(input())
string = ""
for i in range(n):
    s = input()
    string += s

ans = ""
while string:
    temp1 = string
    temp2 = string[len(string)-1::-1]
    t = [temp1, temp2]
    t.sort()
    ans += t[0][0]
    string = t[0][1:]

          
if n > 80:
    while ans:
        print(ans[:80])
        try:
            ans = ans[80:]
        except:
            break
else:
    print(ans)
'''
6
ACDBCB
CDBC

AB
'''