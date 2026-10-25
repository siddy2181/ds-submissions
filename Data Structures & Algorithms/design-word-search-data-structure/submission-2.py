class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                # insert
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(j,root):
            curr = root
            for i in range(j,len(word)):
                if word[i] == '.':
                    for char in curr.children.values():
                        if dfs(i+1, char):
                            return True
                    return False
                else:
                    if word[i] in curr.children:
                        curr = curr.children[word[i]]
                    else:
                        return False
                
            return curr.endOfWord
        return dfs(0,self.root)
        
