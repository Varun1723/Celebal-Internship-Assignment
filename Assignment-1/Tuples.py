# Problem: Tuples
'''Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
'''
# Solution:

# Python 2 compatibility Solution:
'''
if __name__ == '__main__':
   n = int(raw_input())
   integer_list = map(int, raw_input().split())
   print(hash(tuple(integer_list)))
   '''