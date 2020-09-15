#
# @lc app=leetcode id=937 lang=python
#
# [937] Reorder Data in Log Files
#

# @lc code=start
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letterList = []
        numberList = []
        for i in logs:
            splitedLog = i.split()
            if splitedLog[1].isdigit():
                numberList.append(i)
            else:
                letterList.append(i)
        return letterList + numberList
      
# @lc code=end

