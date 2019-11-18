class TrieNode:
    def __init__(self,key):
        self.children=[None]*26
        self.data=key
        self.isLeaf = False

class CompressedTrie:
    def __init__(self):
        self.root = self.newNode(None)
    
    def newNode(self,key):
        return TrieNode(key)
    
    def _charToIndex(self, ch):
        return ord(ch)-ord('a')

    def insert(self, key):
        ptr = self.root
        length = len(key)
        for level in range(length):
            letter = key[level]
            index = self._charToIndex(letter)
            if not ptr.children[index]:
                ptr.children[index] = self.newNode(key[:level+1])
            else:
                node = ptr.children[index].data
                ptr.children[index].data = node[0]
                self.insert(node[1:])
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