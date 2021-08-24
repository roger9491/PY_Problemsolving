M = list(map(int, input().split()))
flag = True
ans = []
for i in range(1, len(M)-1):
    if M[i] > M[i-1]:
        for r in range(i+1, len(M)-1):
            if M[r] == M[i]:
                continue
            else:
                break
        if M[r] < M[i]:
            if r == i+1:
                print(1)
                print(f"{i+1} {M[i]}")
                flag = False
                 
            else:
                print(2)
                print(f"{i+1} {r} {M[i]}")
                flag = False
        i = r+1
         
if flag:
    print(f"0 0")