from bs4 import BeautifulSoup
import requests
from Trie import CompressedTrie
from InvertedIndex import InvertedIndex
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import unicodedata

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

def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(text)

def str_check(w):
    return w not in set(stopwords.words('english')) and \
            not w.isnumeric() and \
            not any(char.isdigit() for char in w)

def page_read(webpage, url, a):
    """
    Process data loaded from webpage
    Parameters: webpage - data loaded from webpage
    Return: None - all data is loaded into Trie
    """
    soup = BeautifulSoup(webpage, 'html.parser')

    # p tags 
    p_tags = soup.find_all('p')
    for p in p_tags:
        txt = p.get_text()
        txt = remove_punc(txt)
        for w in txt:
            w = strip_accents(w).lower()
            if str_check(w):
                load_into_memory(w, url, 1)

    # title tags
    title_tags = soup.find_all('title')
    for title in title_tags:
        txt = title.get_text()
        txt = remove_punc(txt)
        for w in txt:
            w = strip_accents(w).lower()
            if str_check(w):
                load_into_memory(w, url, 3)

    # Get all hyperlinks - a tags
    if a:
        urls = inv_idx.rank.keys()
        hyperlinks = soup.find_all('a', href=True)
        h = [x for x in hyperlinks if x not in urls]
        for i in range(min(10, len(h))):
            url = h[i]['href']
            webpage = page_load(url)
            page_read(webpage, url, False)

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
    """
    Removes punctuation from string, separates words by whitespaces into list
    Parameters: string txt  - string of words
    Return: list[string] - list of strings from txt
    """
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(txt)


if __name__ == '__main__': 
    # print("in" in set(stopwords.words('english')))
    url = "http://www.dataquest.io/blog/web-scraping-tutorial-python/"
    webpage = page_load(url)
    page_read(webpage, url, False)

    # cache.print(cache.root, "", 0)
    # print(cache.root)