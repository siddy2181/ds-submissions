class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        l,r = 1, max_pile
        result = max_pile

        while l<=r:
            mid = l+((r-l)//2)
            print(mid)
            temp = 0
            for i in piles:
                temp+= math.ceil(i/mid)
            if(temp<=h):
                result=min(mid,result)
                r=mid-1
            else:
                l=mid+1
        return result
            
