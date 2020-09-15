# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

# Example 1:



# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Note:

# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # if not self.gridHasRotten(grid):
        #     return 0


        ret = 0
        while True:
            next_grid = [row[:] for row in grid]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        if i > 0:
                            if grid[i-1][j] == 1:
                                next_grid[i-1][j] = 2
                        if j > 0:
                            if grid[i][j-1] == 1:
                                next_grid[i][j-1] = 2
                        if i < len(grid)-1:
                            if grid[i+1][j] == 1:
                                next_grid[i+1][j] = 2
                        if j < len(grid[0])-1:
                            if grid[i][j+1] == 1:
                                next_grid[i][j+1] = 2
            if self.gridSum(grid) == self.gridSum(next_grid):
                if self.gridHasGood(grid):
                    return -1
                return ret
            ret += 1
            grid = next_grid

        
        
    def gridHasGood(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return True
        return False    

    def gridHasRotten(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    return True
        return False
    
    def gridSum(self, grid):
        s = sum(map(sum,grid))
        return s

solution = Solution()
a1 = [[2,1,1],[1,1,0],[0,1,1]]
print(solution.orangesRotting(a1))


a2 = [[2,1,1],[0,1,1],[1,0,1]]
print(solution.orangesRotting(a2))

a3 = [[0,2]]
print(solution.orangesRotting(a3))

a4 = [[2,1,1,1],[1,1,0,0],[0,1,1,0],[1,1,0,1]]
print(solution.orangesRotting(a4))

a5 = [[1]]
print(solution.orangesRotting(a5))