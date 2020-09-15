#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode()
        l = dummy
        while l1 and l2:
            if l1.val > l2.val:
                l.next = ListNode(l2.val)
                l2 = l2.next
            else:
                l.next = ListNode(l1.val)
                l1 = l1.next
            l = l.next
        l3 = l1 or l2
        if l3:
            l.next = l3
        return dummy.next
        
# @lc code=end

