class TrieNode:
    def __init__(self,key):
        self.children=[None]*26
        self.data=key
        self.isLeaf = False
        self.isWord = False

class CompressedTrie:
    def __init__(self):
        """
        Initialize CompressedTrie
        """
        self.root = self.newNode(None)
    
    def newNode(self,key):
        """
        Create new node for CompressedTrie
        Parameters: string key - string to be added to CompressedTrie
        Return:     new Trie node with key
        """
        return TrieNode(key)
    
    def _charToIndex(self, ch):
        """
        Get index or character starting at 'a'
        Parameters: string ch   - character to get index for
        Return:     int
        """
        return ord(ch)-ord('a')
    
    def _cmpstr(self, og, addition):
        """
        Compare two strings, one from node in trie and one string to be added
        Parameters: string og       - original string from node
                    string addition - string to be added to trie
        Return:     int index       - the index of the end of the common substring 
                                    between og and addition
        """
        last_idx = -1
        if og == addition:
            return len(og)
        for i in range(max(len(og), len(addition))):
            if i >= len(og) or i >= len(addition):
                return last_idx
            else:
                if og[i] == addition[i]:
                    last_idx = i
                else:
                    return last_idx

    def _noneCheck(self, arr):
        """
        Check if there array is all None
        Parameters: list arr    - list to check
        Returns:    boolean
        """
        for x in arr:
            if x:
                return False
        return True
    
    def print(self, root, s, level, all_words):
        """
        Print words from compressed trie
        Parameters:     TrieNode root   - where to start the print
                        string s        - string accumulating the word (start with "")
                        int level       - level of compressed trie to start on (start with 0)
                        all_words       - accumulation of all words
        """
        ptr = root.children
        for i in range(len(ptr)):
            if ptr[i]:
                if ptr[i].isWord:
                    print((s+ptr[i].data))
                    all_words += [s+ptr[i].data]
                self.print(ptr[i], s+ptr[i].data, level+1, all_words)

    def insert(self, key):
        """
        Insert new word into CompressedTrie
        Parameters: string key  - word to be added
        """
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
                    if comp == len(ptr.children[index].data):    # Exact match - mark it as word
                        ptr.children[index].isWord = True
                        return
                    if comp != -1:   #Something there that matches
                        flag = comp
                        node = ptr.children[index].data # current contents of node
                        
                        ptr.children[index].data = node[:comp+1]
                        # Node data will be split - therefore no longer a word
                        ptr.children[index].isWord = False
                        cur = ptr.children[index]
                        cur.isLeaf = False
                        # New node after split
                        if comp+1 < len(node):
                            
                            index2 = self._charToIndex(node[comp+1]) #Index is first char of next segment
                            # Move node's children
                            save_children = cur.children
                            cur.children = [None]*26
                            # Split causes new Node to be word
                            cur.children[index2] = self.newNode(node[comp+1:])

                            cur.children[index2].children = save_children
                            if self._noneCheck(save_children):
                                cur.children[index2].isWord = True
                                cur.children[index2].isLeaf = True
                            else: 
                                cur.children[index2].isLeaf = False
                    else: #Something that doesn't match at all
                        print('ERROR, insert: something here should have matched')
                    ptr = ptr.children[index]

    def search(self, key):
        """
        Check if word exists in trie
        Parameter:  string key  - word to be checked
        Return:     boolean
        """
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
                    if comp != None and comp+1 < len(ptr.children[index].data):
                        return False
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
  
    # # # Search for different keys 
    print("{} ---- {}".format("bear",output[t.search("bear")])) 
    print("{} ---- {}".format("bit",output[t.search("bit")])) 
    print("{} ---- {}".format("stop",output[t.search("stop")])) 
    print("{} ---- {}".format("stoop",output[t.search("stoop")])) 

    x = []
    t.print(t.root, "", 0, x)
  
if __name__ == '__main__': 
    main() 
  