import random
def f1(n,k,p):
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
        # print(record)
        # print(ans)
        c += 1
    # print(index)
    # print(ans)
    return ans

def f2(n,k,l):
    # n,k = map(int,input().split())
    # l = list(map(int,input().split()))

    ms = [0]
    mxs = [0]
    mx = []
    for i in range(n):
        mx.append(l[i]*i)
        mxs.append(mxs[i]+mx[i])
        ms.append(ms[i]+l[i])

    ans = 0
    f2_t = [0,k]
    def cut(s,t,kn):
        xc = (mxs[t+1]-mxs[s]) / (ms[t+1]-ms[s])
        if str(xc)[-2:] == '.5':
            xc = int(xc)
        else:
            xc = round(xc)

        f2_t[0] += l[xc]

        if kn < f2_t[1]:
            if xc-1-s > 1:
                cut(s,xc-1,kn+1)
            if t-xc-1 > 1:
                cut(xc+1,t,kn+1)

    cut(0,n-1,1)
    # print(ans)
    return f2_t[0]

while True:

    n = 4
    m = 1
    t = []
    while len(t) < n:
        a = random.randint(1,100)
        if str(a) not in t:
            t.append(str(a))
    print(n,m)
    print(" ".join(t))
    t = list(map(int,t))
    t1 = f1(n,m,t)
    t2 = f2(n,m,t)
    print(t1,t2)
    if t1 != t2:
        break

'''

1
14*-1 + 8*1 + 94*2
2
14*-2 + 1*-1 + 94*1

'''