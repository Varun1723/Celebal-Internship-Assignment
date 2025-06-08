# Problem Statement: Compress the String!
'''In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . 
To read more about this function, Check this out .
You are given a string . Suppose a character '' occurs consecutively  times in the string. 
Replace these consecutive occurrences of the character '' with  in the string.'''
    
# Solution:
from itertools import groupby
a=input()
for k,v in groupby(a):
    print((len(list(v)),int(k)),end=" ")