#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Solution
class Solution(object):
    def twoSum(self, nums, target):
        original = 0
        sumArray = []
        while original < len(nums):
            pointer = original + 1
            while pointer < len(nums):
                if nums[original]+nums[pointer] == target:
                    sumArray.append(original)
                    sumArray.append(pointer)
                    return sumArray
                else:
                    pointer += 1

            original += 1

solution = Solution()
result = solution.twoSum([3,2,4], 6)
print(result)
