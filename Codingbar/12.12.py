'''
week2 邊緣偵測



'''



'''
均攤時間複雜度



'''


def insert(val):
    global count
    if count == len(array):
        sum = 0
        for i in range(len(array)):
            sum = sum + array[i]
        array[0] = sum
        count = 1
    array[count] = val
    count += 1



n = int(input())
array = [0]*n

count = 0

