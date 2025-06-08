# Problem: Iterables and Iterators
'''
The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here.

You are given a list of  lowercase English letters. For a given integer , you can select any  indices (assume -based indexing) with a uniform probability from the list.

Find the probability that at least one of the  indices selected will contain the letter: ''.

Input Format

The input consists of three lines. The first line contains the integer , denoting the length of the list. The next line consists of  space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer , denoting the number of indices to be selected.
'''
# Solution:
from itertools import combinations
n = int(input())                 
letters = input().split()       
k = int(input())                
combs = list(combinations(letters, k))

countwitha=sum([1 for comb in combs if "a" in comb])
ratio=countwitha/len(combs)
print(f"{ratio:.3f}")