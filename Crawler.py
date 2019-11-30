from bs4 import BeautifulSoup
import requests
from Trie import CompressedTrie
from InvertedIndex import InvertedIndex
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

global cache
global inv_idx
cache = CompressedTrie()
inv_idx = InvertedIndex()

def page_load(url):
    """
    Loads all data from webpage given the url 
    Parameters: string url - webpage url
    Return: string data - webpage HTML data
    """
    r = requests.get(url)
    data = r.content
    return data

# TODO: Read data from webpage
def page_read(webpage, url):
    """
    Process data loaded from webpage
    Parameters: webpage - data loaded from webpage
    Return: None - all data is loaded into Trie
    """
    soup = BeautifulSoup(webpage, 'html.parser')

    # html = list(soup.children)[2]
    # print(list(html.children))

    # p tags 
    p_tags = soup.find_all('p')
    for p in p_tags:
        txt = p.get_text()
        txt = remove_punc(txt)
        for w in txt:
            w = w.lower()
            if w not in set(stopwords.words('english')) and not w.isnumeric():
                load_into_memory(w, url, 1)

    # title tags
    title_tags = soup.find_all('title')
    for title in title_tags:
        txt = title.get_text()
        txt = remove_punc(txt)
        for w in txt:
            w = w.lower()
            if w not in set(stopwords.words('english')) and not w.isnumeric():
                load_into_memory(w, url, 3)

    # Get all hyperlinks - a tags
    hyperlinks = soup.find_all('a', href=True)
    for a in hyperlinks:
        print(a['href'])

def load_into_memory(w, url, c):
    """
    Adds word w to compressed trie, inverted index, and rank 
    Parameters: string w    - word
                string url  - url with owrd present
                int c       - count for ranking
    """
    # Check existence in trie
    if cache.search(w):
        inv_idx.add_url(w, url, c)
    else:
        cache.insert(w)
        inv_idx.add_word(w, url, c)
        
def remove_punc(txt):
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(txt)


if __name__ == '__main__': 
    # print("in" in set(stopwords.words('english')))
    url = "http://www.dataquest.io/blog/web-scraping-tutorial-python/"
    webpage = page_load(url)
    page_read(webpage, url)

    # cache.print(cache.root, "", 0)
    # print(cache.root)