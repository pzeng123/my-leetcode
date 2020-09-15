class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            dic[target - nums[i]] = i


solution = Solution()
n1 = [2,7,11,15]
t1 = 9
print(solution.twoSum(n1, t1))

n2 = [3,2,4]
t2 = 6
print(solution.twoSum(n2, t2))

n3 = [3,3]
t3 = 6
print(solution.twoSum(n3, t3))
