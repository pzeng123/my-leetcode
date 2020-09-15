#
# @lc app=leetcode id=1360 lang=python
#
# [1360] Number of Days Between Two Dates
#

# @lc code=start
class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        

days = [(153 * i + 8) // 5 for i in range(3, 16)]
diffDays = [days[i] - days[i-1] for i in range(1, len(days))]
print(diffDays)


# @lc code=end

