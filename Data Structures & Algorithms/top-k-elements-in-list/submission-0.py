class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = {}
        # loop over the array and store <value, count> to a dict
        for i in nums:
            count[i] = 1 + count.get(i,0)

        # loop over the dict and check count
        # create an array of the length of the input array

        freq = {key: [] for key in range(len(nums)+1)}
        for i,v in count.items():
            freq[v].append(i)

            # if count >=K, append the value to result
        # return result
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
