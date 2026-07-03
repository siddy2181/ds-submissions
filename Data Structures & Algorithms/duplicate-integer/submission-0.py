class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # iterate through the input array
        dupeSet = set();
        for i in nums:
        # check if the value in the set
            #Yes? -> return true
            if(i in dupeSet):
                return True
            #No? -> Add the value to the set
            dupeSet.add(i)

        return False

        