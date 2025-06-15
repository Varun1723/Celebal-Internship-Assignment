#Solution

def print_rangoli(size):
    # your code goes here
    realist = []
    for j in range(size-1, -1, -1):
        strs,rev = "",""
        for i in range(j,size):
            strs += chr(97 + i)
        if len(strs) > 1:
            rev = strs[::-1]
        realist.append(("-".join(rev[:len(rev)-1] + strs)).center((size * 4) - 3, "-"))

    print(*realist, sep='\n')
    realist.pop()
    realist.reverse()
    print(*realist, sep='\n')

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)