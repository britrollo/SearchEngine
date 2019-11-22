from bs4 import BeautifulSoup
import requests
# from Trie import CompressedTrie

# TODO: Load webpage from hyperlink
def page_load(url):
    r = requests.get("http://"+url)
    data = r.text
    return data

# TODO: Read data from webpage
def page_read(webpage):
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