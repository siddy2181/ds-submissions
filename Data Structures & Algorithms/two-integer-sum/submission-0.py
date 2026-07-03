class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumIndex = {}
        #loop over the list
        for i,v in enumerate(nums):
        # check if value is present in the dictionary
            if(v in twoSumIndex):
            # return the current index and the dictionary's index
                return [twoSumIndex[v], i]
            #else
            else:
                twoSumIndex.setdefault(target-v,i)
            #store target-current value as key and index as the value
        



        