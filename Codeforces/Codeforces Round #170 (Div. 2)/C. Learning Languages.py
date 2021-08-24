'''
來源: https://codeforces.com/contest/278/my

學語言

在一家壓榨勞力的公司裡，有n個員工，他們使用m種語言，每一個員工所會的語言都不一樣，甚至有些
員工還不會公司裡使用的語言(你就把他當成不會講話的人就可以了，必須要上課才會講話)，
這家公司的老闆為了省最多錢，它會讓員工去學習語言，但是只有一些必要的員工要學習，他們之間的溝通只要
靠這些中間員工翻譯就好了
ex: 員工1:中文 英文 員工2:英文 法語 員工3:俄語
    我們可以知道 員工1 員工2溝通沒有障礙
    但是 員工3 就沒有辦法跟 員工1 員工2溝通
    那怎辦?
    為了達到最省錢的目的
    我們只需要讓員工1 或 員工2 其中一個學會 俄語 就可以溝通拉~~
    員工1學俄語 ，若員工2 要跟 員工3 溝通 ， 只要員工1負責翻譯就行了

一名員工學會一們語言只需花費 1 元
問這間公司最少需花費多少元，員工間才能溝通無障礙
輸入格式:
第一行 輸入兩個整數n,m 代表 n:員工數量 m:語言數量
接下來n行 每一行 會有多個數字 ，第一個數字代表 員工編號 ，之後數字代表 這名員工所會的語言

輸出:
最少花費

詳情請見範例


'''
n,m = list(map(int,input().split()))

employee = []
c = 0
for i in range(n):
    l = list(map(int,input().split()))
    if l[0] == 0:
        c += 1
    else:
        employee.append(l[1:])


flag = True
while flag:
    for i in range(len(employee)):
        flag1 = False
        for j in range(i+1,len(employee)):
            # print("i,j",employee[i],employee[j])
            if set(employee[i]) & set(employee[j]):
                # print(employee[i],employee[j])
                employee[i] = set(employee[j]) | set(employee[i])
                flag1 = True
                del employee[j]
                break
        if flag1:
            break
    else:
        flag = False

# if len(employee) == 0:
#     print(0)
# else:
if n - c == 0:
    print(c)
else:
    print(len(employee) + c - 1)