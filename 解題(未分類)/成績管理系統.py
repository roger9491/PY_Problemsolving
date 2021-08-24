account = "roger"
password = "roger"
name_list = []
math_list = []
chinese_list = []

print("-----歡迎來到成績管理系統-----")
print("請輸入帳號:")
ad = input()
print("請輸入密碼:")
pa = input()
if ad == account and pa == password:
    print("歡迎登入")
    print("請輸入功能")
    print("1.新增學生")
    print("2.修改學生成績")
    print("3.查看排名")
    print("4.離開")
    action = int(input())
    if action == 1:
        print("請輸入學生的名子:")
        name = input()
        name_list.append(name)
        print("請輸入數學成績:")
        math = int(input())
        math_list.append(math)
        print("請輸入國文成績:")
        chinese = int(input())
        chinese_list.append(chinese)

    elif action == 2:
        print("請輸入要修改的學生名子:")
        name1 = input()
        if name1 in name_list:
            for i in range(len(name_list)):
                if name1 == name_list[i]:
                    number = i
                    break

            print(name1+"學生各科成績:\
                \n數學:",math_list[number])
            print("國文:",chinese_list[i])
            print("請輸入要修改哪一門成積:")
            gradename = input()
            print("修改幾分:")
            grade = int(input())
            if gradename == "數學":
                math_list[number] = grade
            elif gradename == "國文":
                chinese_list[number] = grade
        else:
            print("這位學生不存在")
    
    elif action == 3:
        temp1 = []
        temp2 = []






        


    elif action == 4:
        break


else:
    print("帳號或密碼輸入錯誤!!\n請重新開啟~")