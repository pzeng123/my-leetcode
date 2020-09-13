"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000

Output: 1

Example 2:
Input:
11000
11000
00100
00011

Output: 3
"""


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    
    if not grid or not grid[0]:
        print("return 0")
        return 0
    row_size = len(grid)
    col_size = len(grid[0])
    status = [[0 for col in range(col_size)] for row in range(row_size)]
    ret = 0
    for i in range(row_size):
        for j in range(col_size):
            if status[i][j] == 0:
                if grid[i][j] == '1':
                    ret += 1              
                    status = dfs(grid, i, j, status)
    return ret  

def dfs(grid,i,j,status):
    print(status)
    if grid[i][j] == '0' or status[i][j] == 1:
        return status
    status[i][j] = 1
    if i > 0:
        status[i-1][j] = 1
        if grid[i-1][j] == '1':
            status = dfs(grid, i-1, j, status)
    if j > 0:
        status[i][j-1] = 1
        if grid[i][j-1] == '1':
            status = dfs(grid, i, j-1, status)
       
    if i < len(grid)-1:
        status[i+1][j] = 1
        if grid[i+1][j] == '1':
            status = dfs(grid, i+1, j, status)
    if j < len(grid[0])-1:
        status[i][j+1] = 1
        if grid[i][j+1] == '1':
            status = dfs(grid, i, j+1, status)
    return status        

grid1 = [['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']]
print(numIslands(grid1))

grid2 = [['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']]
print(numIslands(grid2))

grid3 = [['1'],['1']]
print(numIslands(grid3))

grid4 = [['1','0','0','0','0'],
['0','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']]
print(numIslands(grid4))