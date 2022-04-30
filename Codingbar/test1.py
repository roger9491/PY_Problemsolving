mem = []
for i in range(9):
    mem.append(input().split()[1:])

base = [0,0,0,0,0]

point = 0
def run(n):
    global point
    for i in range(n):
        base[1],base[2],base[3],base[4] = base[0],base[1],base[2],base[3]
        base[0] = 0
        if base[4]:
            point += 1;base[4] = 0

def main():
    out = int(input())
    outcount = 0
    for j in range(5):
        for i in range(9):
            s = mem[i][j]
            base[0] = 1
            if s[1] == 'O':
                outcount += 1
                if outcount == out: return print(point)
                if outcount % 3 == 0:
                    # base = [0,0,0,0,0]
                    
            elif s[1] == 'B':
                run(int(s[0]))
            else:
                run(4)

main()


