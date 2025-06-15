#Solution
def average(array):
    # your code goes here
    avg = sum(set(array)) / len(set(array))
    return round(avg, 3)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)