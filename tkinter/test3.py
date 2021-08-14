def rec(n):
    print(n%10)
    
    if n >= 10:
        rec(n//10)

s = rec(136)