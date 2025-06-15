# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
sizes = map(int, input().split())
n = int(input())
avail = Counter(sizes)
sales = 0
for i in range(n):
    order = list(map(int, input().split()))
    size = order[0]
    if size in avail.keys() and avail[size] > 0:
        sales += order[1]
        avail[size] -= 1

print(sales)