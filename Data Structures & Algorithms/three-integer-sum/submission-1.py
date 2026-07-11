class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, a in enumerate(nums):
            # if current value is 0, all after this are either  or greater than 0.
            if a > 0:
                break
            # Duplicates: Continue till the same value 
            if i > 0 and a == nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                threeSum = a+nums[l]+nums[r]
                if threeSum > 0:
                    r-=1
                elif threeSum <0:
                    l+=1
                else:
                    result.append([a,nums[l],nums[r]])
                    l +=1
                    r -=1
                    # continue till the same value
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
                

        return result
            

