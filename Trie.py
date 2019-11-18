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


    def print(self, p):
        ptr = p
        if ptr.isLeaf:
            return
        while True:
            print(ptr)
            children = ptr.children
            for child in children:
                print(child.data)
                self.print(child) 


    def insert(self, key):
        ptr = self.root
        length = len(key)
        for level in range(length):
            letter = key[level]
            index = self._charToIndex(letter)
            if not ptr.children[index]:
                ptr.children[index] = self.newNode(key[level:])
                ptr.children[index].isLeaf = True
                return
            else:
                node = ptr.children[index].data

                ptr.children[index].data = node[0]
                ptr.isLeaf = False
                # self._insert_below(ptr.children[index], node[1:])
                cur = ptr.children[index]
                index2 = self._charToIndex(node[1])
                next = cur.children[index2]
                next = self.newNode(node[1:])
            
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

    # driver function 
def main(): 
  
    # Input keys (use only 'a' through 'z' and lower case) 
    keys = ["the","a","there","anaswe","any", 
            "by","their"] 
    output = ["Not present in trie", 
              "Present in trie"] 
  
    # Trie object 
    t = CompressedTrie() 

    t.insert("by")
    t.insert("both")
    
    # # Construct trie 
    # for key in keys: 
    #     t.insert(key) 
  
    # # # Search for different keys 
    # print("{} ---- {}".format("the",output[t.search("the")])) 
    # print("{} ---- {}".format("these",output[t.search("these")])) 
    # print("{} ---- {}".format("their",output[t.search("their")])) 
    # print("{} ---- {}".format("thaw",output[t.search("thaw")])) 
    for child in t.root.children:
        if child:
            print(child.data + " " + str(child.isLeaf))
            for c in child.children:
                if c:
                    print(c.data + " " + str(c.isLeaf))
   
    # t.print(t.root)
  
if __name__ == '__main__': 
    main() 
  