#solution

from textwrap import wrap

def clean(s):
    seen = set()
    cleaned = []
    for c in s:
        if c not in seen:
            seen.add(c)
            cleaned.append(c)
    return ''.join(cleaned)

def merge_the_tools(string, k):
    # your code goes here
    split = wrap(string, k)
    for s in split:
        print(clean(s))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)