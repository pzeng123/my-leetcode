#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        ret = ListNode()
        cur = ret
        add = 0
        while add or l1 or l2:
            v1 = 0
            v2 = 0
            if l1:
                v1 = l1.val
            if l2:
                v2 = l2.val
            cur.val = (add + v1 + v2) % 10
            add = (add + v1 + v2) // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if add or l1 or l2:
                cur.next = ListNode()
                cur = cur.next
        return ret






# @lc code=end

