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

    keys = ['performing', 'data', 'science', 'tasks', 'common', 'want', 'use', 
    'found', 'internet', 'usually', 'able', 'access', 'csv', 'format', 'via', 
    'application', 'programming', 'interface', 'api', 'however', 'times', 'accessed', 
    'part', 'web', 'page', 'cases', 'like', 'technique', 'called', 'scraping', 'get', 
    'work', 'analysis', 'tutorial', 'show', 'perform', 'using', 'python', 'beautifulsoup', 
    'library', 'weather', 'forecasts', 'national', 'service', 'analyzing', 'pandas', 'site', 
    'started', 'looking', 'background', 'apis', 'might', 'check', 'dataquest', 'courses', 
    'visit', 'browser', 'makes', 'request', 'server', 'since', 'getting', 'files', 'sends', 
    'back', 'tell', 'render', 'us', 'fall', 'main', 'types', 'receives', 'renders', 'displays', 
    'lot', 'happens', 'behind', 'scenes', 'nicely', 'need', 'worry', 'interested', 'content', 'look', 
    'html', 'hypertext', 'markup', 'language', 'pages', 'created', 'instead', 'tells', 'layout', 
    'allows', 'similar', 'things', 'word', 'processor', 'microsoft', 'make', 'text', 'bold', 'create', 
    'paragraphs', 'nearly', 'complex', 'let', 'take', 'quick', 'tour', 'know', 'enough', 'scrape', 
    'effectively', 'consists', 'elements', 'tags', 'basic', 'tag', 'everything', 'inside', 'simple', 
    'document', 'added', 'yet', 'viewed', 'see', 'anything', 'right', 'put', 'two', 'head', 'body', 
    'goes', 'contains', 'title', 'information', 'generally', 'useful', 'still', 'may', 'noticed', 
    'nested', 'go', 'add', 'first', 'form', 'p', 'defines', 'paragraph', 'shown', 'separate', 'second', 
    'commonly', 'used', 'names', 'depend', 'position', 'relation', 'also', 'properties', 'change', 
    'behavior', 'learn', 'online', 'example', 'links', 'link', 'another', 'href', 'property', 
    'determines', 'extremely', 'others', 'full', 'list', 'move', 'actual', 'class', 'id', 'special', 
    'give', 'easier', 'interact', 'one', 'element', 'multiple', 'classes', 'shared', 'ids', 'optional', 
    'adding', 'rendered', 'thing', 'download', 'requests', 'contents', 'given', 'several', 'different', 
    'try', 'downloading', 'sample', 'website', 'http', 'dataquestio', 'github', 'io', 'method', 'running', 
    'response', 'object', 'status_code', 'indicates', 'downloaded', 'successfully', 'means', 'fully', 
    'dive', 'status', 'codes', 'code', 'starting', 'success', 'error', 'print', 'parse', 'extract', 
    'import', 'instance', 'formatted', 'prettify', 'structure', 'level', 'time', 'select', 'top', 
    'children', 'soup', 'note', 'returns', 'generator', 'call', 'function', 'initial', 'doctype', 
    'newline', 'character', 'n', 'well', 'type', 'items', 'objects', 'navigablestring', 'represents', 
    'final', 'item', 'important', 'deal', 'often', 'navigate', 'various', 'taking', 'third', 'returned', 
    'find', 'finding', 'isolate', 'isolated', 'get_text', 'figuring', 'took', 'commands', 'something', 
    'fairly', 'single', 'find_all', 'instances', 'loop', 'indexing', 'return', 'introduced', 'earlier', 
    'probably', 'clear', 'css', 'determine', 'apply', 'certain', 'styles', 'specify', 'specific', 
    'illustrate', 'principle', 'following', 'url', 'ids_and_classes', 'search', 'outer', 'selectors', 
    'developers', 'style', 'examples', 'support', 'searching', 'div', 'proceed', 'extracting', 'local', 
    'step', 'downtown', 'san', 'francisco', 'extended', 'forecast', 'image', 'next', 'week', 'including', 
    'day', 'temperature', 'brief', 'description', 'conditions', 'inspect', 'chrome', 'devtools', 
    'firefox', 'safari', 'equivalents', 'recommended', 'though', 'start', 'developer', 'tools', 
    'clicking', 'view', 'end', 'panel', 'bottom', 'sure', 'highlighted', 'really', 'handy', 'feature', 
    'near', 'says', 'open', 'scroll', 'outermost', 'corresponds', 'case', 'seven', 'click', 'around', 
    'console', 'explore', 'discover', 'tonight', 'thursday', 'night', 'contained', 'tombstone', 
    'container', 'parsing', 'pieces', 'name', 'short', 'attribute', 'img', 'treat', 'dictionary', 
    'pass', 'key', 'individual', 'piece', 'combine', 'knowledge', 'comprehensions', 'gets', 'period', 
    'order', 'fields', 'dataframe', 'analyze', 'store', 'tabular', 'making', 'easy', 'free', 'course', 
    'become', 'column', 'values', 'regular', 'expression', 'series', 'str', 'pull', 'numeric', 'could', 
    'mean', 'high', 'low', 'temperatures', 'rows', 'happen', 'good', 'understanding', 'would', 'pick', 
    'keep', 'city', 'topics', 'covered', 'interactive', 'vik', 'ceo', 'founder', 'sql', 'joins', 
    'working', 'databases', 'lists', 'loops', 'building', 'analytics', 'pipeline', 'datetime', 
    'manipulate', 'dates', 'spans', 'browse', 'blog', 'resources', 'whether', 'new', 'field', 
    'career', 'teach', 'skills', 'r', 'visualization', 'machine', 'learning', 'missions', 
    'journey', 'creating', 'account', 'agree', 'acceptour', 'terms', 'privacy', 'policy', 
    'trusted', 'companies', 'universities', 'world', 'writing', 'projects', 'interacting', 'peers', 
    'real', 'life', 'sets', 'hints', 'along', 'way', 'coding', 'experience', 'help', 'progress', 
    'fast', 'guide', 'showcase', 'future', 'employers', 'inspire', 'motivate', 'trade', 'ideas', 
    'project', 'job', 'read', 'philosophy', 'helped', 'develop', 'analyst', 'credit', 'guided', 
    'today', 'christian', 'l', 'heureux', 'global', 'insights', 'blizzard', 'choose', 'path', 'sharpen', 
    'beginner', 'basics', 'sources', 'cleaning', 'techniques', 'statistical', 'analyses', 'predictive', 
    'intermediate', 'advanced', 'large', 'datasets', 'computer', 'architecture', 'parallel', 
    'processing', 'production', 'build', 'pipelines', 'handle', 'larger', 'concepts', 'structures', 
    'algorithms', 'recursion', 'curated', 'sequence', 'carefully', 'arranged', 'zero', 'ready', 
    'meet', 'needs', 'hands', 'allow', 'quickly', 'toolbox', 'numpy', 'libraries', 'interpreting', 
    'graphics', 'taught', 'matplotlib', 'communicate', 'stories', 'clean', 'practice', 'bash', 
    'establish', 'foundation', 'command', 'line', 'springboard', 'workflow', 'multi', 'table', 
    'postgresql', 'customize', 'improve', 'database', 'performance', 'acquire', 'sampling', 
    'variables', 'distributions', 'summarize', 'measure', 'variability', 'variance', 'standard', 
    'deviation', 'compare', 'z', 'scores', 'fundamentals', 'probability', 'theory', 'conditional', 
    'bayes', 'theorem', 'naive', 'b', 'tests', 'chi', 'squared', 'powerful', 'k', 'nearest', 
    'neighbors', 'premium', 'calculus', 'necessary', 'linear', 'regression', 'algebra', 
    'model', 'construct', 'interpret', 'decision', 'trees', 'deep', 'neural', 'networks', 
    'includes', 'graph', 'representation', 'activation', 'functions', 'hidden', 'layers', 
    'classification', 'complete', 'looks', 'participate', 'kaggle', 'competitions', 'titanic', 
    'competition', 'nlp', 'clustering', 'predictions', 'textual', 'write', 'quality', 'computers', 
    'oriented', 'lambda', 'exception', 'handling', 'apache', 'spark', 'map', 'reduce', 'engineering', 
    'enhance', 'works', 'postgres', 'optimize', 'optimizing', 'batches', 'augmenting', 'sqlite', 
    'process', 'cpu', 'parallelize', 'better', 'speed', 'applies', 'tree', 'scratch', 'popular', 
    'package', 'exploratory', 'statistic', 'calculating', 'hypothesis', 'testing', 'directory', 
    'changing', 'victoria', 'studying', 'doubled', 'salary', 'almost', 'overnight', 'mohammad', 
    'went', 'becoming', 'engineer', 'kopa', 'solar', 'team', 'realized', 'needed', 'came', 'training', 
    'exactly', 'jorge', 'varade', 'decided', 'wanted', 'tried', 'datacamp', 'strongly', 'preferred', 
    'latter', 'school', 'university', 'javier', 'fernandez', 'suarez', 'liked', 'caitlin', 'retail', 
    'ikea', 'exciting', 'teams', 'amazon', 'little', 'huyen', 'vu', 'masters', 'business', 'interest', 
    'hezekiah', 'specialized', 'offer', 'fit', 'bill', 'offered', 'felt', 'tufts', 'armed', 'strong', 
    'faced', 'limited', 'options', 'isaac', 'pato', 'dropped', 'six', 'months', 'built', 'skillset', 
    'landed', 'meteorology', 'graduated', 'worked', 'year', 'without', 'math', 'student', 'living', 
    'proof', 'anybody', 'curtly', 'critchlow', 'solve', 'massive', 'excel', 'problem', 'miguel', 
    'couto', 'story', 'begins', 'rejection', 'got', 'dry', 'email', 'saying', 'hi', 'giving', 
    'scholarship', 'said', 'applied', 'prestigious', 'expensive', 'bootcamp', 'berlin', 'despite', 
    'qualifications', 'include', 'phd', 'material', 'carlos', 'cutillas', 'de', 'frutos', 'administration', 
    'program', 'cunef', 'madrid', 'knew', 'extra', 'skill', 'set', 'settled', 'enjoyed', 'statistics', 
    'potential', 'growth', 'adam', 'zabrodski', 'originally', 'plan', 'scientist', 'college', 'studied', 
    'rocks', 'jobs', 'included', 'ops', 'management', 'uber', 'brutal', 'slog', 'investment', 'banking', 
    'mission', 'prepare', 'scientists', 'sunishchal', 'dev', 'degree', 'technology', 'innovation', 
    'technical', 'pol', 'brigneti', 'pompeu', 'fabra', 'barcelona', 'idea', 'intern', 'ridelink', 
    'discovered', 'importance', 'acheive', 'goal', 'product', 'manager', 'eric', 'sales', 'andrade', 
    'quora', 'seemed', 'mining', 'putting', 'stuff', 'intelligence', 'break', 'mba', 'changed', 
    'landscape', 'especially', 'trying', 'codeacademy', 'mike', 'roberts', 'physics', 'gave', 'art', 
    'professional', 'poker', 'playing', 'shot', 'bi', 'joined', 'beef', 'learned', 'switch', 'much', 
    'interesting', 'role', 'within', 'aaron', 'melton', 'saw', 'power', 'plant', 'report', 'consuming', 
    'prone', 'fix', 'attempts', 'networkx', 'great', 'moment', 'archives', 'join', 'education', 'chance', 
    'millions', 'people', 'traditional', 'gain', 'ahead', 'unfortunately', 'always', 'opportunities', 
    'result', 'seriously', 'inclusion', 'major', 'promises', 'hope', 'industry', 'direction', 'worldwide', 
    'capable', 'amazing', 'face', 'barriers', 'feel', 'insurmountable', 'done', 'share', 'vision', 
    'connect', 'maybe', 'even', 'josh', 'devlincontent', 'lead', 'randall', 'halldata', 'mary', 
    'conditdirector', 'seb', 'vettersr', 'backend', 'bruno', 'cunhadata', 'julie', 'chipkopython', 
    'rana', 'el', 'garembackend', 'ella', 'matutis', 'digalstudent', 'assistant', 'srini', 
    'kadamatiproduct', 'rebecca', 'mccrackeneditor', 'loryn', 'colemarketing', 'generalist', 'wes', 
    'john', 'alderdirector', 'daniel', 'hunter', 'frontend', 'paruchurifounder', 'charlie', 
    'custercontent', 'marketing', 'sabrina', 'baeztalent', 'darla', 'shockleysr', 'infrastructure', 
    'ash', 'kestrelbackend', 'meghan', 'cassidydata', 'mikael', 'karlssondigital', 'marketer', 'rose', 
    'martin', 'phddirector', 'alex', 'olteanudata', 'francois', 'aubrydata', 'casey', 'batesdata', 
    'aoga', 'phddata', 'merlobdirector', 'celeste', 'grupmandirector', 'operations', 'sahil', 
    'sunnystudent', 'specialist', 'hiring', 'vs', 'udacity', 'choice', 'nanodegree', 'biased', 
    'straight', 'decide', 'option', 'best', 'comparison', 'platform', 'average', 'measures', 'median', 
    'mode', 'range', 'tables', 'query', 'mobile', 'apps', 'assume', 'strings', 'integers', 'floats', 
    'familiar', 'supercharge', 'study', 'else', 'habits', 'according', 'teaching', 'enroll', 'offline', 
    'schools', 'stack', 'comes', 'missing', 'packages', 'software', 'test', 'significance', 'transform', 
    'log', 'usable', 'visitor', 'metrics', 'master', 'module', 'cover', 'someone', 'hired', 'awful', 
    'knowing', 'difference', 'failure', 'tips', 'tricks', 'generate', 'count', 'numbers', 'elif', 
    'control', 'succesful', 'beginners', 'difficult', 'certificate', 'certifications', 'cost', 
    'thousands', 'dollars', 'worth', 'covers', 'communication', 'protocol', 'parts', 'intended', 
    'simplify', 'implementation', 'maintainance', 'based', 'system', 'operating', 'hardware', 
    'specification', 'many', 'forms', 'specifications', 'routines', 'remote', 'calls', 'posix', 
    'windows', 'aspi', 'documentation', 'provided', 'facilitate', 'usage', 'recently', 'term', 'refer', 
    'kind', 'client', 'described', 'contract', 'initiate', 'defined', 'action', 'precisely', 
    'applications', 'simplifies', 'abstracting', 'underlying', 'exposing', 'actions', 'graphical', 
    'provide', 'user', 'button', 'performs', 'steps', 'fetching', 'highlighting', 'emails', 'file', 
    'input', 'output', 'copies', 'location', 'requiring', 'understand', 'occurring', 'related', 
    'describes', 'prescribes', 'expected', 'rules', 'implementations', 'none', 'abstract', 
    'separation', 'programs', 'written', 'scala', 'java', 'compile', 'compatible', 'bytecode', 
    'advantage', 'vary', 'depending', 'involved', 'procedural', 'lua', 'consist', 'primarily', 
    'execute', 'errors', 'methods', 'bindings', 'mapping', 'features', 'capabilities', 
    'implemented', 'binding', 'developing', 'swig', 'fortran', 'creation', 'interfaces', 
    'framework', 'implementing', 'unlike', 'normal', 'mediated', 'extending', 'plugged', 
    'moreover', 'overall', 'flow', 'caller', 'inversion', 'mechanism', 'specifies', 'aim', 
    'enable', 'conformant', 'compiled', 'linux', 'berkeley', 'distribution', 'systems', 
    'implement', 'commitment', 'backward', 'particularly', 'older', 'run', 'newer', 'versions', 
    'executable', 'setting', 'compatibility', 'differs', 'binary', 'abi', 'source', 'provides', 
    'base', 'protocols', 'standards', 'technologies', 'together', 'regardless', 'connectivity', 
    'invocation', 'uses', 'operate', 'remotely', 'appear', 'therefore', 'maintaining', 'abstraction', 
    'executed', 'locally', 'proxy', 'invokes', 'corresponding', 'remoting', 'acquires', 'value', 
    'modification', 'interactions', 'enterprise', 'assets', 'agreement', 'sla', 'functional', 'provider', 
    'expose', 'users', 'approach', 'architectural', 'revolves', 'providing', 'services', 'serving', 
    'consumers', 'context', 'development', 'typically', 'transfer', 'messages', 'definition', 
    'extensible', 'xml', 'javascript', 'notation', 'json', 'shipping', 'company', 'ecommerce', 
    'focused', 'ordering', 'automatically', 'current', 'rates', 'enter', 'shipper', 'rate', 
    'historically', 'virtually', 'synonymous', 'recent', 'trend', 'moving', 'away', 'soap', 
    'soa', 'towards', 'direct', 'representational', 'state', 'rest', 'resource', 'roa', 
    'semantic', 'movement', 'toward', 'rdf', 'concept', 'promote', 'ontology', 'combination', 
    'known', 'mashups', 'social', 'media', 'space', 'allowed', 'communities', 'sharing', 'place', 
    'dynamically', 'posted', 'updated', 'locations', 'twitter', 'core', 'trends', 'citation', 
    'design', 'significant', 'impact', 'hiding', 'enabling', 'modular', 'details', 'modules', 
    'complexities', 'thus', 'expect', 'organization', 'authors', 'recommendations', 'joshua', 
    'bloch', 'kin', 'lane', 'michi', 'henning', 'patterns', 'evolution', 'europlop', 'papers', 
    'ways', 'integrate', 'considered', 'members', 'ecosystem', 'policies', 'releasing', 'factor', 
    'becomes', 'public', 'stability', 'changes', 'parameters', 'clients', 'publicly', 'presented', 
    'subject', 'stable', 'particular', 'documented', 'explicitly', 'unstable', 'google', 'guava', 
    'marked', 'annotation', 'beta', 'sometimes', 'declare', 'deprecated', 'rescinded', 'candidate', 
    'removed', 'modified', 'incompatible', 'transition', 'supported', 'contain', 'innovative', 
    'opportunistic', 'usages', 'designers', 'words', 'diverse', 'offers', 'aiming', 'practical', 
    'purposes', 'crucial', 'maintenance', 'traditionally', 'blogs', 'forums', 'q', 'websites', 
    'javadoc', 'pydoc', 'consistent', 'appearance', 'clarity', 'typical', 'scenarios', 'snippets', 
    'rationales', 'discussions', 'contracts', 'omitted', 'restrictions', 'limitations', 'cannot', 
    'null', 'thread', 'safe', 'decrement', 'cancel', 'averts', 'self', 'trading', 'clarification', 
    'tends', 'comprehensive', 'challenge', 'writers', 'potentially', 'yielding', 'bugs', 'enriched', 
    'metadata', 'annotations', 'compiler', 'environment', 'custom', 'behaviors', 'possible', 'driven', 
    'manner', 'observing', 'infer', 'required', 'directives', 'templates', 'natural', 'mined', 'oracle', 
    'corporation', 'sued', 'distributed', 'embedded', 'android', 'acquired', 'permission', 'reproduce', 
    'although', 'openjdk', 'judge', 'william', 'alsup', 'ruled', 'v', 'copyrighted', 'u', 'victory', 
    'widely', 'expanded', 'copyright', 'protection', 'copyrighting', 'accept', 'claim', 'anyone', 
    'version', 'carry', 'thereby', 'bar', 'ruling', 'overturned', 'appeal', 'court', 'appeals', 
    'federal', 'circuit', 'question', 'constitutes', 'fair', 'left', 'unresolved', 'trial', 'jury', 
    'determined', 'reimplementation', 'constituted', 'vowed', 'qualify', 'appealed', 'supreme', 
    'united', 'states', 'copyrightability', 'rulings', 'wikipedia', 'notice', 'essential', 
    'interaction', 'please', 'turn', 'os', 'unix', 'mac', 'x', 'prereleases', 'docker', 'images', 
    'releases', 'number', 'gpl', 'licenses', 'must', 'archive', 'point', 'ports', 'platforms', 
    'latest', 'hosts', 'nicknamed', 'cpython', 'alternative', 'available', 'early', 'guido', 
    'van', 'rossum', 'stichting', 'mathematisch', 'centrum', 'netherlands', 'successor', 'abc', 
    'remains', 'principal', 'author', 'contributions', 'executables', 'signed', 'release', 'builder', 
    'openpgp', 'currently', 'reached', 'person', 'keys', 'keyserver']

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
    for w in x:
        if w not in keys:
            print(w)
  
    # # # Search for different keys 
    # print("{} ---- {}".format("networks",output[t.search("networks")])) 
    # print("{} ---- {}".format("network",output[t.search("network")])) 
    # print("{} ---- {}".format("stop",output[t.search("stop")])) 
    # print("{} ---- {}".format("stoop",output[t.search("stoop")])) 
  
if __name__ == '__main__': 
    main() 
  