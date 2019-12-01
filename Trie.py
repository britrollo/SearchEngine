# TODO : comment and remove print statements
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
        for x in arr:
            if x:
                return False
        return True
    
    def print(self, root, s, level, all_words):
        ptr = root.children
        for i in range(len(ptr)):
            if ptr[i]:
                if ptr[i].isWord:
                    print((s+ptr[i].data))
                    all_words += [s+ptr[i].data]
                self.print(ptr[i], s+ptr[i].data, level+1, all_words)

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
                    # print(key + " - " + ptr.children[index].data)
                    ptr.children[index].isWord = True
                    return
                else: #Something there
                    comp = self._cmpstr(ptr.children[index].data, key[level:])
                    # print(comp) 
                    if comp == len(ptr.children[index].data):    # Exact match - mark it as word
                        # print(key + " -- " + ptr.children[index].data)
                        ptr.children[index].isWord = True
                        return
                    if comp != -1:   #Something there that matches
                        flag = comp
                        node = ptr.children[index].data # current contents of node
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
                            # print(key + " --- " + cur.children[index2].data)
                            # print("node[cmp+1:] = "+ node[comp+1:])
                            cur.children[index2].children = save_children
                            if self._noneCheck(save_children):
                                cur.children[index2].isWord = True
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

    # driver function 
def main(): 

    # Input keys (use only 'a' through 'z' and lower case) 
    # keys = ["bear", "bell", "bid", "bull", "buy", "sell", "stock", "stop"] 

    keys = ['dataquest', 'vs', 'udacity', 'better', 'choice', 'learning', 'data', 'science', 'compare', 'nanodegree', 'scientist', 'path', 'help', 'little', 'biased', 'give', 'straight', 'decide', 'option', 'best', 'let', 'start', 'high', 'level', 'comparison', 'springboard', 'bootcamp', 'platform', 'learn', 'use', 'average', 'variability', 'measures', 'like', 'mean', 'median', 'mode', 'range', 'standard', 'deviation', 'z', 'scores', 'hands', 'r', 'statistics', 'course', 'first', 'sql', 'common', 'work', 'single', 'table', 'real', 'world', 'databases', 'generally', 'one', 'want', 'able', 'combine', 'multiple', 'tables', 'within', 'query', 'joins', 'tutorial', 'lists', 'powerful', 'types', 'python', 'list', 'analyzing', 'mobile', 'apps', 'assume', 'know', 'fundamentals', 'including', 'working', 'strings', 'integers', 'floats', 'familiar', 'supercharge', 'study', 'anything', 'else', 'trying', 'habits', 'according', 'teaching', 'enroll', 'online', 'try', 'expensive', 'offline', 'schools', 'options', 'stack', 'comes', 'make', 'sure', 'missing', 'free', 'tools', 'top', 'packages', 'well', 'great', 'software', 'interactive', 'hypothesis', 'testing', 'build', 'skills', 'need', 'test', 'statistical', 'significance', 'analysis', 'end', 'pipeline', 'engineering', 'transform', 'website', 'log', 'usable', 'visitor', 'metrics', 'conditional', 'probability', 'bayes', 'theorem', 'naive', 'algorithms', 'new', 'manipulate', 'times', 'dates', 'time', 'series', 'become', 'master', 'datetime', 'module', 'tasks', 'cover', 'someone', 'needs', 'hired', 'analyst', 'year', 'studying', 'awful', 'lot', 'knowing', 'difference', 'success', 'failure', 'tips', 'tricks', 'function', 'way', 'quickly', 'generate', 'count', 'numbers', 'simple', 'elif', 'control', 'code', 'building', 'projects', 'extremely', 'succesful', 'beginners', 'difficult', 'certificate', 'get', 'certifications', 'cost', 'thousands', 'dollars', 'worth', 'engineer', 'covers', 'postgres', 'browse', 'blog', 'resources', 'whether', 'field', 'looking', 'take', 'step', 'career', 'teach', 'visualization', 'machine', 'missions', 'journey', 'creating', 'account', 'agree', 'acceptour', 'terms', 'privacy', 'policy', 'trusted', 'companies', 'universities', 'around', 'writing', 'interacting', 'peers', 'life', 'sets', 'browser', 'check', 'hints', 'along', 'support', 'coding', 'experience', 'progress', 'fast', 'guide', 'showcase', 'future', 'employers', 'interact', 'inspire', 'motivate', 'trade', 'ideas', 'next', 'project', 'job', 'search', 'read', 'philosophy', 'helped', 'develop', 'credit', 'guided', 'getting', 'today', 'christian', 'l', 'heureux', 'global', 'insights', 'blizzard', 'choose', 'pick', 'individual', 'analytics', 'courses', 'sharpen', 'beginner', 'basics', 'using', 'sources', 'cleaning', 'techniques', 'perform', 'analyses', 'predictive', 'view', 'intermediate', 'advanced', 'large', 'datasets', 'topics', 'basic', 'computer', 'architecture', 'parallel', 'processing', 'production', 'pipelines', 'handle', 'larger', 'key', 'concepts', 'structures', 'recursion', 'curated', 'sequence', 'carefully', 'arranged', 'zero', 'ready', 'meet', 'specific', 'allow', 'programming', 'important', 'toolbox', 'analyze', 'pandas', 'numpy', 'libraries', 'explore', 'interpreting', 'graphics', 'taught', 'matplotlib', 'communicate', 'tell', 'stories', 'clean', 'practice', 'bash', 'establish', 'foundation', 'command', 'line', 'workflow', 'multi', 'postgresql', 'customize', 'indexing', 'improve', 'database', 'performance', 'acquire', 'apis', 'web', 'sampling', 'variables', 'distributions', 'summarize', 'measure', 'variance', 'values', 'theory', 'b', 'tests', 'chi', 'squared', 'k', 'nearest', 'neighbors', 'premium', 'calculus', 'necessary', 'linear', 'regression', 'algebra', 'model', 'dive', 'construct', 'interpret', 'decision', 'trees', 'deep', 'neural', 'networks', 'includes', 'graph', 'representation', 'activation', 'functions', 'hidden', 'layers', 'image', 'classification', 'complete', 'looks', 'started', 'participate', 'kaggle', 'competitions', 'titanic', 'competition', 'nlp', 'clustering', 'predictions', 'textual', 'write', 'quality', 'computers', 'object', 'oriented', 'lambda', 'exception', 'handling', 'apache', 'spark', 'map', 'reduce', 'technique', 'enhance', 'understanding', 'works', 'optimize', 'optimizing', 'batches', 'augmenting', 'sqlite', 'process', 'cpu', 'parallelize', 'different', 'speed', 'applies', 'tree', 'used', 'scratch', 'popular', 'language', 'package', 'exploratory', 'statistic', 'calculating', 'directory', 'changing', 'victoria', 'example', 'doubled', 'salary', 'almost', 'overnight', 'mohammad', 'went', 'background', 'becoming', 'kopa', 'solar', 'team', 'realized', 'needed', 'came', 'training', 'found', 'exactly', 'jorge', 'varade', 'decided', 'wanted', 'tried', 'datacamp', 'strongly', 'preferred', 'latter', 'school', 'university', 'javier', 'fernandez', 'suarez', 'liked', 'caitlin', 'retail', 'ikea', 'exciting', 'teams', 'amazon', 'huyen', 'vu', 'masters', 'business', 'interest', 'hezekiah', 'specialized', 'offer', 'fit', 'bill', 'offered', 'felt', 'tufts', 'armed', 'strong', 'faced', 'limited', 'isaac', 'pato', 'dropped', 'everything', 'six', 'months', 'built', 'skillset', 'landed', 'meteorology', 'graduated', 'worked', 'without', 'math', 'student', 'living', 'proof', 'anybody', 'curtly', 'critchlow', 'solve', 'massive', 'excel', 'problem', 'miguel', 'couto', 'story']
    keys2 = ["need", "networks", "networkx", "netherlands", "nearly", "nested", "newline", 
        "next", "new", "needs", "near", "nearest", "necessary", "neural", "neighbors", "needed", "newer"]
    
    output = ["Not present in trie", 
              "Present in trie"] 
  
    # Trie object 
    t = CompressedTrie() 
    
    # Construct trie 
    for key in keys:
        t.insert(key) 

    x=[]
    t.print(t.root, "", 0, x)
    print("-----------------------------------------------------------")
    for w in x:
        if w not in keys:
            print(w)
  
    # # # Search for different keys 
    # print("{} ---- {}".format("begins",output[t.search("begins")])) 
    # print("{} ---- {}".format("network",output[t.search("network")])) 
    # print("{} ---- {}".format("stop",output[t.search("stop")])) 
    # print("{} ---- {}".format("stoop",output[t.search("stoop")])) 
  
if __name__ == '__main__': 
    main() 
  