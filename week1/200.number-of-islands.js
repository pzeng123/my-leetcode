/*
 * @lc app=leetcode id=200 lang=javascript
 *
 * [200] Number of Islands
 */

// @lc code=start
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    if (!grid || !grid[0]) {
        return 0;
    }
    let ret = 0;
    for (let i = 0 ; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (grid[i][j] === "1") {
                dfs(grid, i, j);
                ret++;
            }
        }
    }
    return ret
    
};

const dfs = (grid, i, j) => {
    if (i<0 || j<0 || i >= grid.length || j >=grid[0].length || grid[i][j] !== "1" ) {
        return null
    }
    grid[i][j] = "#";
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)


}  

// @lc code=end

