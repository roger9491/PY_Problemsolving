'''
#e 
#e1 = str(e) 我們把 e轉成文字型態   '12.454545' 9 -(2+1) = 7
e1 = input()

e = float(e1)
for i in range(len(e1)):         
    if '.' == e1[i]:
        t = i       #會儲存 . 的索引值位置  
        break
if len(e1) - t >= 2:
    if int(e1[t+2]) >=5:
        e += 0.1
           #12.454545 + 0.1 = 12.554545 
e = e*10        #e = 125.54545          
e = int(e)       #e = 125
e = e / 10      #e=12.5
print(e)

and or not  只能計算 true 和 false
and : 和     想要出門玩，天氣要好 和 心情好 才出去玩
or :  或     想要出門玩，天氣要好 或 心情好 才出去玩

'''
a = 0
'''
print(a > 3)
if  True:    if 才執行
    False:   if 就不執行

    not True  not(5>3)
    not False not(5<3)

什麼東西會產生 true 或 False
判斷式 
  >
  < 
  !=
  ==                                        
  >=
  <=                    1 2 3 4 5 6 7      2 30            
  '''                   7 -1 = 6 + 1         30 -    
                        7 - 2 = 6
print(not 3>5)
'''                 x:禮拜幾  y:過了幾天
1.獨立出當"週"         6-x = b    7 - x + 1   當週的公里數   

2.求出剩餘的天數        y - (7-x+1)

3.剩餘的天數 有多少公里


'
