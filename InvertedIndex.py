class InvertedIndex:
    def __init__(self):
        self.idx = {}
        self.rank = {}

    def add_word(self, w, url, c):
        """
        Add new word,url pair to memory
        Parameters:     string w    - word to be added to memory
                        string url  - url word was found on
                        int c       - score for word
        """
        if url[-1] == "/":
            url = url[:-1]
        self.idx[w] = [url]
        if url in self.rank.keys():
            self.rank[url][w] = c
        else:
            self.rank[url] = {}
            self.rank[url][w] = c

    def add_url(self, w, url, c):
        """
        Word already exists in memory, add url or update word rank for url
        Parameters:     string w    - word to be added to memory
                        string url  - url word was found on
                        int c       - score to be added for word
        """
        if url[-1] == "/":
            url = url[:-1]
        if url not in self.idx[w]:
            self.idx[w] = self.idx[w] + [url]
        if url in self.rank:
            if w in self.rank[url]:
                self.rank[url][w] = self.rank[url][w] + c
            else:
                self.rank[url][w] = c
        else:
            self.rank[url] = {}
            self.rank[url][w] = c
