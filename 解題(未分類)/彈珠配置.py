def dfs(i,j):
    print(i,j,path)
    if len(path) == 6 or note_matrix[i][j] or i >= 6 or j >= 6:
        del path[-1]
        return
    path.append(num_list[i][j])
    count = 0
    if len(path) == 6:
        print("len = 6",path)
        for x in num_list:
            for y in range(0,len(x)-1):
                if x[y] in path:
                    count += 1
            if count == x[len(x) - 1]:
                ans_path.append(path)
                print("ans",ans_path)
            else:
                return
            count = 0 
        

    dir = [[1,0],[0,1],[-1,0],[0,-1]]
    note_matrix[i][j] = True
    for x in dir:
        dfs(i + x[0],j + x[1])
        
    note_matrix[i][j] = False

while True:
    #try:
        num_list = []
        note_matrix = [[False]*6 for i in range(6)]
        path = []
        ans_path = []
        for i in range(6):
            num = input().split(" ")
            num = list(map(int,num))
            num_list.append(num)

        dfs(0,0)    







    #except:
        #break