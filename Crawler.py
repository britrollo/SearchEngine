from bs4 import BeautifulSoup
from Trie import CompressedTrie

def page_load(webpage):
    with open(webpage) as wp:
        soup = BeautifulSoup(wp)

        # Get all hyperlinks
        hyperlinks = soup.find_all('a')

        #Get title
        if len(list(soup.title)) == 1:
            title = soup.title.string

        #Get body
        body = []
        for st in soup.body.stripped_strings:
            body += st