class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumMap = {}

        for i in range(len(nums)):
            targetSum = target - nums[i]
            if targetSum in twoSumMap:
                return [twoSumMap[targetSum], i]
            else:
                twoSumMap[nums[i]] = i
        


        