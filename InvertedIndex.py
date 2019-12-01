class InvertedIndex:
    def __init__(self):
        self.idx = {}
        self.rank = {}
# TODO : comment 
    def add_word(self, w, url, c):
        """
        Add new word,url pair to memory
        """
        if url[-1] == "/":
            url = url[:-1]
        self.idx[w] = [url]
        if url in self.rank.keys():
            self.rank[url][w] = c
        else:
            self.rank[url] = {}
            self.rank[url][w] = c

# TODO : comment 
    def add_url(self, w, url, c):
        """
        Word already exists in memory, add url or update word rank for url
        """
        if url[-1] == "/":
            url = url[:-1]
        if url not in self.idx[w]:
            self.idx[w] = self.idx[w] + [url]
            self.rank[url] = {}
            self.rank[url][w] = c 
        
        if url in self.rank:
            if w in self.rank[url]:
                self.rank[url][w] = self.rank[url][w] + c
            else:
                self.rank[url][w] = c
        else:
            self.rank[url] = {}
            self.rank[url][w] = c

def main():
    i = InvertedIndex()

    i.add_word("hello", "https://www.dataquest.io/blog/topics/student-stories", 1)
    i.add_url("hello", "https://www.dataquest.io/blog/topics/student-stories", 1)

if __name__ == "__main__":
    main()
    