class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initiate the result array with 1 [1,1,1,1]
        result = [1] * (len(nums))

        prefix = 1
        # loop through the nums array l> r and multiply the values to left while updating result
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # loop through the nums array r>l multiply the values to the right while updating result

        postFix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= postFix
            postFix *= nums[i]
        return result

# # class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res = [1] * (len(nums))

#         prefix = 1
#         for i in range(len(nums)):
#             res[i] = prefix
#             prefix *= nums[i]
#         postfix = 1
#         for i in range(len(nums) - 1, -1, -1):
#             res[i] *= postfix
#             postfix *= nums[i]
#         return res