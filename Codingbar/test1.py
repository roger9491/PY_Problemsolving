
=======
a = '''print()
ex.
		print(1)
		print(“hello”)
		
		a = 5
		print(a)
		
	需要印出多個值可以用 , 分開， 會占用一個空格
	ex.
		a = 5
		b = 3
		print(a,b)'''
ans = ""
for i in a:
    if i == "\t":
        ans += "\\t"
    elif i == "\n":
        ans += "\\n"
    else:
        ans += i
print(ans)
>>>>>>> 018deae5ad581007c8aac0e2e92f5076fd89fe9c
