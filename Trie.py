class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.isLeaf = False

class Trie:
    def __init__(self):
        self.root = self.newNode()
    
    def newNode(self):
        return TrieNode()
    
    def _charToIndex(self, ch):
        return ord(ch)-ord('a')

    def insert(self, key):
        ptr = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            if not ptr.children[index]:
                ptr.children[index] = self.newNode()
            ptr = ptr.children[index]

        ptr.isLeaf = True
    
    def search(self, key):
        ptr = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not ptr.children[index]:
                return False
            ptr = ptr.children[index]
        return ptr != None and ptr.isLeaf