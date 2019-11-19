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
    
    def _cmpstr(self, og, addition):
        last_idx = -1
        for i in range(max(len(og), len(addition))):
            if i >= len(og) or i >= len(addition):
                return last_idx
            else:
                if og[i] == addition[i]:
                    last_idx = i
                else:
                    return last_idx

    def _noneCheck(self, arr):
        for x in arr:
            if x:
                return False
        return True
    
    def print(self, root, s, level):
        ptr = root.children
        # print("LEVEL " + str(level))
        # print("----------" + str(root.data) + "----------")
        for i in range(len(ptr)):
            if ptr[i]:
                if ptr[i].isLeaf:
                    # print(ptr[i].data)
                    # print("full word: " + (s+ptr[i].data))
                    print((s+ptr[i].data))
                else:
                    # print("addition: " + ptr[i].data)
                    self.print(ptr[i], s+ptr[i].data, level+1)

    def insert(self, key):
        ptr = self.root
        length = len(key)
        flag = 0
        for level in range(length):
            if flag > 0:
                flag = flag - 1
                continue
            else:
                index = self._charToIndex(key[level])
                if not ptr.children[index]: #None at would be location
                    ptr.children[index] = self.newNode(key[level:])
                    ptr.children[index].isLeaf = True
                    return
                else: #Something there
                    cmp = self._cmpstr(ptr.children[index].data, key[level:])
                    if cmp != -1:   #Something there that matches
                        flag = cmp
                        node = ptr.children[index].data
                        # print("node[:cmp+1] = "+ node[:cmp+1])
                        ptr.children[index].data = node[:cmp+1]
                        cur = ptr.children[index]
                        cur.isLeaf = False
                        # New node after split
                        if cmp+1 < len(node):
                            # print("node[cmp+1] = "+ node[cmp+1])
                            index2 = self._charToIndex(node[cmp+1]) #Index is first char of next segment
                            # Move node's children
                            save_children = cur.children
                            cur.children = [None]*26
                            cur.children[index2] = self.newNode(node[cmp+1:])
                            # print("node[cmp+1:] = "+ node[cmp+1:])
                            cur.children[index2].children = save_children
                            if self._noneCheck(save_children):
                                cur.children[index2].isLeaf = True
                            else: 
                                cur.children[index2].isLeaf = False
                    else: #Something that doesn't match at all
                        print('ERROR, insert: something here should have matched')
                    ptr = ptr.children[index]

    # TODO: Fix for compressed trie
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
    keys = ["bear", "bell", "bid", "bull", "buy", "sell", "stock", "stop"] 
    output = ["Not present in trie", 
              "Present in trie"] 
  
    # Trie object 
    t = CompressedTrie() 
    
    # Construct trie 
    for key in keys: 
        t.insert(key) 

    # t.insert("bear")
    # t.insert("bell")
    
    t.print(t.root, "", 0)

    # print(t.root.data)
  
    # # # Search for different keys 
    # print("{} ---- {}".format("the",output[t.search("the")])) 
    # print("{} ---- {}".format("these",output[t.search("these")])) 
    # print("{} ---- {}".format("their",output[t.search("their")])) 
    # print("{} ---- {}".format("thaw",output[t.search("thaw")])) 
    # for child in t.root.children:
        
    #     if child:
    #         print("Level 1")
    #         print(child.data + " " + str(child.isLeaf))
    #         for c in child.children:
                
    #             if c:
    #                 print("level 2")
    #                 print(c.data + " " + str(c.isLeaf))
   
    # t.print(t.root)
  
if __name__ == '__main__': 
    main() 
  