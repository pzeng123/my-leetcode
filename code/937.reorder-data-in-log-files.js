/*
 * @lc app=leetcode id=937 lang=javascript
 *
 * [937] Reorder Data in Log Files
 */

// @lc code=start
/**
 * @param {string[]} logs
 * @return {string[]}
 */
var reorderLogFiles = function(logs) {
    const letterArray = []
    const numberArray = []
    const getBody = string => string.slice(string.indexOf(" ") + 1)
    for (const i of logs) {
        let splitLog = i.split(" ")
        if (splitLog[1][0]>="0" && splitLog[1][0] <= "9") {
            numberArray.push(i);
        } else {
            letterArray.push(i);
        }        
    }
    const compare = (a,b) => {
        if (getBody(a) === getBody(b)) {
            return a.localeCompare(b)
        }
        return getBody(a).localeCompare(getBody(b))
    }
    return [...letterArray.sort(compare), ...numberArray]    
};


// const reorderLogFiles = (logs) => {
//     const body = s => s.slice(s.indexOf(' ') + 1); // get the body after identifier
//     const isNum = c => /\d/.test(c);
  
//     // if body same then compare identifier
//     const compare = (a, b) => {
//       const n = body(a).localeCompare(body(b));
//       if (n !== 0) return n;
//       return a.localeCompare(b);
//     };
  
//     const digitLogs = [];
//     const letterLogs = [];
//     for (const log of logs) {
//       if (isNum(body(log))) digitLogs.push(log);
//       else letterLogs.push(log);
//     }
//     return [...letterLogs.sort(compare), ...digitLogs];
//   };

// @lc code=end

