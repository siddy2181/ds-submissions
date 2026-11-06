class Solution:
    def rob(self, nums: List[int]) -> int:
        # calculate the max you can rob until each index
        # 2 pointers
        #store the max in a temp
        # keep incrementing and storing the max to the right pointers
        # So by the end of the array, you get the max you can get till that pointers

        l, r = 0,0
        for i in nums:
            temp = max(i+l, r)
            l = r
            r = temp
        return r
