class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dictionary
        ana_group = {}
        # iterate over the List
        for i in strs:
        # sort every key 
            # Check if the sorted key is present in the dict
            temp = tuple(sorted(i))
            ana_group.setdefault(temp,[]).append(i)
            # Yes? Append the dict value to the list 
            # No? Create a list for that key
        print(ana_group)
        # return the new list with all the values merged
        return list(ana_group.values());