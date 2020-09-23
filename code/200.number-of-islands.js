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
        return 0
    }
    let ret = 0;
    const row = grid.length
    const col = grid[0].length
    let mark = Array(row).fill().map(() => Array(col).fill(0));
    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (grid[i][j] === "0" || mark[i][j] === 1) {
                continue;
            }
            mark[i][j] = 1;
            mark = dfs(i, j, grid, mark);
            ret ++;
        }
    }
    return ret
    
};

const dfs = (i, j, grid, mark) => {
    const row = grid.length
    const col = grid[0].length
    if (i > 0) {
        if (mark[i-1][j] !== 1 && grid[i - 1][j] === "1") {
            mark[i - 1][j] = 1
            mark = dfs(i-1, j, grid, mark);
        }
    }
    if (j > 0) {
        if (mark[i][j-1] !== 1 && grid[i][j - 1] === "1") {
            mark[i][j - 1] = 1
            mark = dfs(i, j-1, grid, mark);

        }
    }
    if (i < row - 1) {
        if (mark[i+1][j] !== 1 && grid[i + 1][j] === "1") {
            mark[i + 1][j] = 1
            mark = dfs(i+1, j, grid, mark);

        }
    }
    if (j < col - 1) {
        if (mark[i][j+1] !== 1 && grid[i][j + 1] === "1") {
            mark[i][j + 1] = 1
            mark = dfs(i, j+1, grid, mark);

        }
    }
    return mark;
}


// @lc code=end

