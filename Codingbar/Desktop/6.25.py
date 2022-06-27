'''

輸入一串文字

辨別有沒有 "/n"



a23gasd3dg/nasd23

'''

n = input()

for i in range(len(n)-1):
    if n[i] == "/" and n[i+1] == "n":
        print("有")
        break
else:
    print("沒有")
