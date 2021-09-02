
'''
***不會寫網路封包監聽，請先寫這題***


重複輸入數字，存到串列，直到輸入no

再輸入一個數字N，先把串列sort，再去檢查串列裡的數字，留下的數字必須要

大於等於輸入的數字N，然後直接印出串列來


詳情請見範例格式

'''

t = []

while True:
    n = input()

    if n == "no":
        break
    
    t.append(int(n))

target = int(input())

ans = []

for i in range(len(t)):
    if t[i] > target:
        ans.append(t[i])
print(ans)
    
