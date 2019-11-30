class InvertedIndex:
    def __init__(self):
        self.idx = {}
        self.rank = {}

    def add_word(self, w, url, c):
        """
        Add new word,url pair to memory
        """
        self.idx[w] = [url]
        if url in self.rank.keys():
            self.rank[url][w] = c
        else:
            self.rank[url] = {}
            self.rank[url][w] = c


    def add_url(self, w, url, c):
        """
        Word already exists in memory, add url or update word rank for url
        """
        if url not in self.idx[w]:
            self.add_word(w, url, c)
        else:
            self.rank[url][w] = self.rank[url][w] + c
    
    