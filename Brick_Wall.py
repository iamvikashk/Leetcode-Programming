"""
There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.
Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.
Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

Example 1:
Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2

Example 2:
Input: wall = [[1],[1],[1]]
Output: 3
"""


class Solution:
    def leastBricks(self, wall):
        dic = {}
        for i in range(len(wall)):
            sum = 0
            for j in range(len(wall[i]) - 1):
                sum += wall[i][j]
                if dic.get(sum) is not None:
                    dic[sum] += 1
                else:
                    dic[sum] = 1
        if dic.values():
            return len(wall) - max(dic.values())
        else:
            return len(wall)


wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
# wall = [[1],[1],[1]]
sol = Solution()
print(sol.leastBricks(wall))
