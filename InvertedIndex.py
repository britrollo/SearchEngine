class InvertedIndex:
    def __init__(self):
        self.idx = {}
        self.rank = {}

    def add_word(self, w, url, c):
        self.idx[w] = [url]
        if url in self.rank.keys():
            self.rank[url][w] = c
        else:
            self.rank[url] = {}
            self.rank[url][w] = c


    def add_url(self, w, url, c):
        if url not in self.idx[w]:
            self.add_word(w, url, c)
        else:
            self.rank[url][w] = self.rank[url][w] + c
    
    