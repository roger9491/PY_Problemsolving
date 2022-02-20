n,k = map(int,input().split())
p = list(map(int,input().split()))

# 0 2 
pre1 = [0]
pre2 = [0]
sum1 = 0
sum2 = 0
for i in range(1,n+1):
    sum1 += p[i-1]
    sum2 = sum2 + i*p[i-1]
    pre1.append(sum1)
    pre2.append(sum2)
# print(pre1)
# print(pre2)
c = 0
record = [-1,n]
ans = 0
while c < k:
    index = 0
    min_v = 10**9
    if c == 0:
        for i in range(1,n-1):
            temp = pre2[-1] - (i+1) * pre1[-1]
            # print(temp,i)
            if temp < 0:
                temp = temp*-1
            if temp < min_v:
                index = i
                min_v = temp
        ans += p[index]
        record.append(index)
        record.sort()
    else:
        temp_list = []
        for i in range(1,len(record)):
            # print("record",record)
            if (record[i]- record[i-1] - 1) > 2:
                start = record[i-1]
                end = record[i]
                start += 1
                end -= 1
                index = 0
                min_v = 10**9
                # print("s,e",start,end)
                for j in range(start+1,end):
                    # print(i+1)
                    temp = pre2[end+1] - pre2[start] - (j+1) * (pre1[end+1] - pre1[start])
                    # print(j,temp)
                    if temp < 0:
                        temp = temp*-1
                    if temp < min_v:
                        index = j
                        min_v = temp
                    # print("temp",temp,j)
                ans += p[index]
                temp_list.append(index)
                # print(record)
                # print(ans)
        record = record + temp_list
        record.sort()
    print(record)
    # print(ans)
    c += 1
# print(index)
print(ans)



'''
9 2
69 80 38 93 47 57 65 96 74
1  2  3  4
218 93 = 125
224 - 69 = 155


181
0 3
1
715 - 280



0 8
03
58


38 + 47 + 96 = 85 + 96 = 181
2   4 7
3181 - 2*619
3181 - 1238


'''