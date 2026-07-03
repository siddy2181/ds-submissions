class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
  
        result = defaultdict(list)

        for i in strs:
            count = [0]*26
            for char in i:
                count[ord(char) - ord("a")] += 1

            result[tuple(count)].append(i)
        print(result)
        return list(result.values());

        