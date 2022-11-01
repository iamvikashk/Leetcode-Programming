"""
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:
Input: n = 27
Output: true

Example 2:
Input: n = 0
Output: false

Example 3:
Input: n = 9
Output: true
"""
# n = 27
# n = 0
n = 9

class Solution:
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        if n % 3 == 0:
            return self.isPowerOfThree(n // 3)
        if n == 1:
            return True
        return False


sol = Solution()
print(sol.isPowerOfThree(n))
