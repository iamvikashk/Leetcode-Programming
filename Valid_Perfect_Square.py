"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.

Example 1:
"""
num = 100
"""
Output: true

Example 2:
"""
# num = 14
"""
Output: false
"""


class Solution:
    def isPerfectSquare(self, num) -> bool:
        if int(str(num)[-1]) not in [0, 1, 4, 9, 6, 5]:
            return False
        else:
            return num**(1/2) == int(num**(1/2))



sol = Solution()
print(sol.isPerfectSquare(num))
