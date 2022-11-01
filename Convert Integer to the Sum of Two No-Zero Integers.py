"""
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [A, B] where:

A and B are No-Zero integers.
A + B = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions you can return any of them.



Example 1:

Input: n = 2
Output: [1,1]
Explanation: A = 1, B = 1. A + B = n and both A and B do not contain any 0 in their decimal representation.
Example 2:

Input: n = 11
Output: [2,9]
"""


def getNoZeroIntegers(n):
    lst = []
    a = 1
    b = n - a
    while '0' in str(a) or '0' in str(b):
        a += 1
        b = n - a
    lst.append(a)
    lst.append(b)
    return lst


n = 21
print(getNoZeroIntegers(n))
