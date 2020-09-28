/*
 * @lc app=leetcode id=207 lang=javascript
 *
 * [207] Course Schedule
 */

// @lc code=start
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {

    let dict = {}
    prerequisites.forEach(element => {
        if (element[0] in dict) {


        } else {
            dict[element[0]] = [element[0], element[1]]
            while (dict[element[0]][dict[element[0]].length - 1] in dict) {
                dict[element[0]] = [...dict[element[0]], 
            }
        }
    });
    
};
// @lc code=end

