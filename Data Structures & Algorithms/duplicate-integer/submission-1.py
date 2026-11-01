class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        charCount = set()

        for i in nums:
            if i in charCount:
                return True
            charCount.add(i)
        return False

        