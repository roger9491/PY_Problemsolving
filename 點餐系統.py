m1 = ['1.豬肉滿福堡','2.無敵豬肉滿福堡加蛋','3.香雞滿福堡加蛋','4.火腿蛋堡','5.雞塊鬆餅大早餐']
m1_price = [68,88,68,60,119]
m2 = ['1.脆雞腿排烤土司','2.黃金豬排烤土司','3.火腿薯餅烤土司','4.金黃薯餅烤土司']
m2_price = [69,59,49,39]

total = 0
while True:
    print('''
    請輸入指令:
    1   加點套餐
    2   單點
    3   加購塑膠袋
    0   顯示金額並結帳
    謝謝
    ''')
    n = int(input())
    if n == 1:
        print(m1)
        n1 = int(input())
        print(m1[n1+1],m1_price[n1+1])
        total += m1_price[n1+1]
    elif n == 2:
        print(m2)
        n1 = int(input())
        print(m2[n1+1],m2_price[n1+1])
        total += m2_price[n1+1]
    elif n == 3:
        print('購買一個兩元塑膠袋')
        total += 2
    elif n == 0:
        print('總金額',total)
        break