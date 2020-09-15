#
# @lc app=leetcode id=1268 lang=python
#
# [1268] Search Suggestions System
#

# @lc code=start
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        ret = []
        for i in range(len(searchWord)):
            products = self.findInSortedList(products, i, searchWord[i])
            cur_ret = []
            if products:
                for cur_word in products[:3]:
                    if searchWord[:i+1] in cur_word:
                        cur_ret.append(cur_word)
            ret.append(cur_ret)        
        return ret

    def findInSortedList(self, sortedList, charIndex, char):
        if not sortedList:
            return None
        for i in range(len(sortedList)):
            if len(sortedList[i]) >= charIndex+1:
                if sortedList[i][charIndex] == char:
                    return sortedList[i:]


        
# @lc code=end

