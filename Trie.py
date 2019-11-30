class TrieNode:
    def __init__(self,key):
        self.children=[None]*26
        self.data=key
        self.isLeaf = False
        self.isWord = False

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
                if ptr[i].isWord:
                    # print(ptr[i].data)
                    # print("full word: " + (s+ptr[i].data))
                    print((s+ptr[i].data))
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
                    ptr.children[index].isWord = True
                    return
                else: #Something there
                    comp = self._cmpstr(ptr.children[index].data, key[level:])
                    # print(comp) 
                    if comp is None:    # Exact match - mark it as word
                        ptr.children[index].isWord = True
                        return
                    if comp != -1:   #Something there that matches
                        flag = comp
                        node = ptr.children[index].data
                        # print("node[:cmp+1] = "+ node[:comp+1])
                        ptr.children[index].data = node[:comp+1]
                        # Node data will be split - therefore no longer a word
                        ptr.children[index].isWord = False
                        cur = ptr.children[index]
                        cur.isLeaf = False
                        # New node after split
                        if comp+1 < len(node):
                            # print("node[cmp+1] = "+ node[comp+1])
                            index2 = self._charToIndex(node[comp+1]) #Index is first char of next segment
                            # Move node's children
                            save_children = cur.children
                            cur.children = [None]*26
                            # Split causes new Node to be word
                            cur.children[index2] = self.newNode(node[comp+1:])
                            cur.children[index2].isWord = True
                            # print("node[cmp+1:] = "+ node[comp+1:])
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
        flag = 0
        for level in range(length):
            if flag > 0:
                flag = flag - 1
            else:
                index = self._charToIndex(key[level])
                if not ptr.children[index]:
                    return False
                else:
                    comp = self._cmpstr(ptr.children[index].data, key[level:])
                    # print(key)
                    # print("ptr.children[index].data: " + ptr.children[index].data) 
                    # print("key[level:]: " + key[level:])
                    # print("comp: " + str(comp))
                    # print(ptr.children[index].data == key[level:])
                    # print(ptr.children[index].isWord)

                    #The node matches rest of the string
                    if ptr.children[index].data == key[level:] and ptr.children[index].isWord:
                        return True
                    elif ptr.children[index].data != key[level:] and ptr.children[index].isLeaf:
                        return False
                    elif ptr.children[index].data == key[level:] and not ptr.children[index].isWord:
                        return False
                    else:
                        flag = comp
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
    print("{} ---- {}".format("bear",output[t.search("bear")])) 
    print("{} ---- {}".format("bit",output[t.search("bit")])) 
    print("{} ---- {}".format("stop",output[t.search("stop")])) 
    print("{} ---- {}".format("stoop",output[t.search("stoop")])) 
  
# if __name__ == '__main__': 
#     main() 
  