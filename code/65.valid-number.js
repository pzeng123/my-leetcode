/*
 * @lc app=leetcode id=65 lang=javascript
 *
 * [65] Valid Number
 */

// @lc code=start
/**
 * @param {string} s
 * @return {boolean}
 */
var isNumber = function(s) {
    s = s.trim()
    if (!s) {
        return false
    }
    if (s[0] === '.' || s[0] === 'e' || s[s.length - 1] === 'e') {
        return false
    }
    let hasE = false;
    let hasSign = false;
    let hasPoint = false;
    let afterPoint = false;
    const validArray = ['0','1','2','3','4','5','6','7','8','9','e','+','-','.']
    for (let char of s) {
        if (!(validArray.includes(char))) {
            console.log('char :>> ', char);
            console.log("1");
            return false
        }
        if (char === 'e') {
            if (hasE) {
            console.log("2");

                return false
            } else {
                hasE = true
                hasPoint = true
                hasSign = false
            }
        }

        if (char === '+' || char === '-') {
            if (hasSign) {
            console.log("3");

                return false
            } else {
                hasSign = true;
            }
        }



        if (afterPoint) {
            if (['0','1','2','3','4','5','6','7','8','9'].includes(char)) {
                afterPoint = false
            } else {
                console.log('char :>> ', char);
                return false
            }
        }

        if (char === '.') {
            if (hasPoint) {
            console.log("4");

                return false
            } else {
                hasPoint = true;
                afterPoint = true;
            }
        }
    }
    return true
    
};

//TODO

let a = isNumber("     .3e0       ")
console.log('a :>> ', a);
// @lc code=end

