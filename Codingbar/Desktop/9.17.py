
'''

你因為考慮到有些點 沒有4面 可能只有兩面或三面
所以你才先判斷 點的位置 
因為你根據不同的情形來決定要看哪一面

有些點 沒有4面 可能只有兩面或三面
    你必須要指定看哪一面        總體的概念是 因為怕數的點不再範圍裡
        你必須哪一面是1
            如果是一個 就 + 1

你會去看點的四面  
    因為怕數的點不再範圍裡if 0 <= i < n   and 0 <= j < m
        你必須哪一面是1
            如果是一個 就 + 1

'''

# a = [[1,1],
#      [2,2],
#      [3,3]]
# b = [[-1,-1],
#      [-1,-1],
#      [-1,-1]]

'''
stack

(1) 儲存資料: 尾端
(2) 刪除資料 or 查詢資料: 尾端

    先進後出

'''

'''
利用串列來實現堆疊

stack = []

#儲存資料
stack.append("data")

#刪除資料 ex. stack = [1,2,3] => stack = [1,2] , a = 3
a = stack.pop()

#查詢資料
a = stack[-1]
'''

'''
堆疊最大容量
MAX_STACK = 10

堆疊當前的容量
CUR_CAP = 0



'''
MAX_STACK = 10
CUR_CAP = 0
stack = []

# 儲存資料
def push(data):
    if CUR_CAP == MAX_STACK:
        return
    stack.append(data)
    CUR_CAP += 1


# 刪除資料
def pop(data):
    if CUR_CAP == 0:
        return
    a = stack.pop()
    CUR_CAP -= 1

# 查詢資料
def SHOWTOP(data):
    if CUR_CAP == 0:
        return
    print(stack[-1])
'''
括號配對

合法
()[]{}

([( [] )])

不合法
s = ([([)]])
(()

(1) 要怎麼樣找到右括號
(2) 同樣型態
'''
# s = "([([])])"

# (1) 遇不到右括號
# (2) 沒有左括號
# (3) 都有

# ()[]{}
# ([([ ])])

# ([])()([])

'''
queue

queue = []
(1) 儲存資料    右端
    queue.append(data)
(2) 刪除資料    左端
    queue.pop(0)



'''