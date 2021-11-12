
def solve(l, r, number):

    print(l,r)
    if r == 1:
        return number[0]
    elif r - l <= 1:
        if number[l] > number[r]:
            return number[r]
        else:
            return number[l]
    else:
        m = (l + r) // 2
        # 将整个列表分为左右两部分
        left_min = solve(l, m, number)
        right_min = solve(m+1, r, number)
        return min(left_min, right_min)
a = list(map(int,input().split()))
print(solve(0, len(a)-1, a))


