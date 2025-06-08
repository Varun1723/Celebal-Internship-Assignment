# Problem: String Formatting
''' Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
Function Description

Complete the print_formatted function in the editor below.

print_formatted has the following parameters:

int number: the maximum value to print'''

# Solution:
def print_formatted(number):
    # your code goes here
    for i in range(1, number+1):
        s = len(bin(number)[2:])
        print(f"{i:>{s}} {i:>{s}o} {i:>{s}X} {i:>{s}b}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)