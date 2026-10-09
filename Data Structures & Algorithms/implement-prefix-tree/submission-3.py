class TrieNode:
    def __init__(self):
        self.trie_dict = {}
        self.ends_here = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        it = self.root
        for char in word:
            if char not in it.trie_dict:
                new_node = TrieNode()
                it.trie_dict[char] = new_node
            else:
                it = it.trie_dict[char]
            
            if char == word[-1]:
                it.ends_here = True            

    def search(self, word: str) -> bool:
        it = self.root

        for char in word:
            if char not in it.trie_dict:
                return False
            else:
                it = it.trie_dict[char]

        return True if it.ends_here else False
    

    def startsWith(self, prefix: str) -> bool:
        
        it = self.root

        for char in prefix:
            if char not in it.trie_dict:
                return False
            else:
                it = it.trie_dict[char]

        return True

        
        