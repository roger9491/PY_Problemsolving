"""
公車時刻表
"""

# n = int(input())
# h = int(input())
# m = int(input())

# h_t = [h]
# m_t = [m]

# for i in range(n):
#     a = int(input())
    
#     new_m = (m_t[i] + a) % 60
#     new_h = (h_t[i] + (a + m_t[i]) // 60) % 24
#     h_t.append(new_h)
#     m_t.append(new_m)

# # print(h_t)
# # print(m_t)
# p = int(input())

# print(str(h_t[p]).zfill(2),":",str(m_t[p]).zfill(2))

'''
今天吃蘋果了嗎
'''
# day = 1
# while True:
#     n = input()
#     if n == "no":
#         break
#     n = int(n)
#     f = 0
#     for i in range(n):
#         food = input()
#         if food == "apple":
#             f += 1
#     if f == 1:
#         print("You exactly eat an apple in Day",day)
#     else:
#         print("Not an apple in Day",day)
#     day += 1

'''
    刮刮樂
'''
lucky = list(map(int,input().split()))
number = list(map(int,input().split()))
mon = list(map(int,input().split()))

ans = 0
for i in range(len(lucky)):
    if i == 0 or i == 1:
        if lucky[i] in number:
            ans += mon[number.index(lucky[i])]
    else:
        if lucky[i] in number:
            ans -= mon[number.index(lucky[i])]
        else:
            ans *= 2

print(max(ans,0))
