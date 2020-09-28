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
var numIslands = function (grid) {
    if (!grid || !grid[0]) {
        return 0;
    }
    let ret = 0;
    const row = grid.length;
    const col = grid[0].length;
    let mark = Array(row)
        .fill()
        .map(() => Array(col).fill(0));
    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (grid[i][j] === "0" || mark[i][j] === 1) {
                continue;
            }
            mark[i][j] = 1;
            // ----- dfs -----
            // mark = dfs(i, j, grid, mark);
            // ----- dfs end -----

            // ----- bfs -----
            let q = [[i, j]];
            [mark, q] = bfs(grid, mark, q);
            // ----- bfs end -----

            ret++;
        }
    }
    return ret;
};

const dfs = (i, j, grid, mark) => {
    const row = grid.length;
    const col = grid[0].length;
    if (i > 0) {
        if (mark[i - 1][j] !== 1 && grid[i - 1][j] === "1") {
            mark[i - 1][j] = 1;
            mark = dfs(i - 1, j, grid, mark);
        }
    }
    if (j > 0) {
        if (mark[i][j - 1] !== 1 && grid[i][j - 1] === "1") {
            mark[i][j - 1] = 1;
            mark = dfs(i, j - 1, grid, mark);
        }
    }
    if (i < row - 1) {
        if (mark[i + 1][j] !== 1 && grid[i + 1][j] === "1") {
            mark[i + 1][j] = 1;
            mark = dfs(i + 1, j, grid, mark);
        }
    }
    if (j < col - 1) {
        if (mark[i][j + 1] !== 1 && grid[i][j + 1] === "1") {
            mark[i][j + 1] = 1;
            mark = dfs(i, j + 1, grid, mark);
        }
    }
    return mark;
};

const bfs = (grid, mark, q) => {
    const row = grid.length;
    const col = grid[0].length;
    if (!q.length) {
        return [mark, []];
    }

    for (let point of q) {
        let [i, j] = point;
        if (i > 0) {
            if (mark[i - 1][j] !== 1 && grid[i - 1][j] === "1") {
                mark[i - 1][j] = 1;
                q.push([i - 1, j]);
            }
        }
        if (j > 0) {
            if (mark[i][j - 1] !== 1 && grid[i][j - 1] === "1") {
                mark[i][j - 1] = 1;
                q.push([i, j - 1]);
            }
        }
        if (i < row - 1) {
            if (mark[i + 1][j] !== 1 && grid[i + 1][j] === "1") {
                mark[i + 1][j] = 1;
                q.push([i + 1, j]);
            }
        }
        if (j < col - 1) {
            if (mark[i][j + 1] !== 1 && grid[i][j + 1] === "1") {
                mark[i][j + 1] = 1;
                q.push([i, j + 1]);
            }
        }
    }
    q.shift();
    [(mark, q)] = bfs(grid, mark, q);
    return [mark, q];
};

// const grid = [
//     ["1","1","0","0","0"],
//     ["1","1","0","0","0"],
//     ["0","0","1","0","0"],
//     ["0","0","0","1","1"]
// ]
// const ret = numIslands(grid)
// console.log('ret :>> ', ret);
// @lc code=end
