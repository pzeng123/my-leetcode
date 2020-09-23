/*
 * @lc app=leetcode id=168 lang=javascript
 *
 * [168] Excel Sheet Column Title
 */

// @lc code=start
/**
 * @param {number} n
 * @return {string}
 */
var convertToTitle = function(n) {
    if (!n) return ""
    n --;
    let quotient = Math.floor(n / 26)
    let remainderChar = String.fromCharCode(n % 26 + "A".charCodeAt(0))
    return convertToTitle(quotient) + remainderChar
};
// @lc code=end

