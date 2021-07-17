'''
解法: 
    dfs

詳解:
    我們利用dfs遍歷樹的過程，來去遍歷此樹組
    遍歷的過程儲存每個節點的深度
'''
def dfs(a):
    global depth    #深度
    if not a:   #沒有 樹組需要遍歷 即完成
        return
    root = max(a)   #選擇最大值 當root(父節點)
    ans_index = temp_a.index(root)  #找出 該root的索引值(在原本的數組裡)
    index = a.index(root)       #找出 "剩餘" 的數組的左子樹與右子樹
    ans[ans_index] = depth      #儲存深度
    depth += 1                  #深度 + 1
    dfs(a[:index])
    dfs(a[index+1:])
    depth -= 1                  #上述兩個 做完 等同 遍歷完 一個節點的 子樹


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    temp_a = a[:]
    ans = [0]*n
    depth = 0
    dfs(a)
    ans = list(map(str,ans))
    print(" ".join(ans))