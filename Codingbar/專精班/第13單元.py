'''
密碼檢查器
'''
# paw = input()

# for i in range(5):
#     x = input()
#     if x != paw:
#         print("密碼輸入錯誤",(4-i))
#     else:
#         print("密碼輸入正確")
#         break
# else:
#     print("此帳戶已被鎖定")

'''

凱薩解密法


'''
a=int(input("請輸入全班人數："))
b=input()
b=b.split()

for i in range(a):
  b[i]=int(b[i])

b.sort()

for h in range(a):
  b[h]=str(b[h])

print(" ".join(b))

for i in range(a):
  b[i]=int(b[i])

if b[a-1]<60:
  print("worst case")
  c=0
else:
  lowest_success=b[a-1]
  c=1

if b[0]>60:
  print("best case")
  d=0
else:
  highest_fail=b[0]
  d=1

for j in range(a):
  if c==1:
    if b[j]>=60:
      if lowest_success>b[j]:
        lowest_success=b[j]
  elif d==1:
    if highest_fail<b[j]:
      highest_fail=b[j]

if c!=0:
  print(lowest_success)

if d!=0:
  print(highest_fail)

'''
(1)
" ".join(串列) 
串列 = list(map(型態, 串列))

忘了要怎麼讀是字串第幾個
              0123
eng_letter = "abcdefghijklmnopqrstuvwxyz"
eng_letter[0] = a
eng_letter[1] = b
d
'''