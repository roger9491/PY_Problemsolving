'''
***不會寫符號不動冥王，請先寫這題***

在遙遠的某一個地方，有一條道路 這條道路上每個一公尺就有一個編號，
這些編號是隨機的數字， 有兩個閒人 玩一個遊戲，他們分別站在道路的兩末端上的編號上
遊戲規則就是 他們會看地板上的編號 若是奇數 就往前走兩步，不是就是往前走一步，
試問兩個人總共要看幾次地板編號，他們才會 走到同一個編號，或是錯過。
            8 19 20 30 10 40 20 2 3
            a                     b
第一次檢查完 8 19 20 30 10 40 20 2 3
               a             b   
第二次檢查完 8 19 20 30 10 40 20 2 3
                     a     b
第三次檢查完 8 19 20 30  10  40 20 2 3
                        a/b
 
兩人總共看了6次地板



詳情請見範例格式


8 19 20 30 10 40 20 2 3


6

8 28 29 6 27 21 20 23 2 27 5 14 17 21 23 5 28 16 17 24
14

'''

n = list(map(int, input().split()))

i = 0
j = len(n) - 1
count = 0 
while True:

    if i >= j:
        print(count)
        break
    if n[i] % 2 == 0:
        i += 1
        count += 1
    else:
        i += 2
        count += 1
    
    if n[j] % 2 == 0:
        j -= 1
        count += 1
    else:
        j -= 2
        count += 1

    

        