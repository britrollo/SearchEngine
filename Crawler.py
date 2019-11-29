from bs4 import BeautifulSoup
import requests
# from Trie import CompressedTrie

def page_load(url):
    """
    Loads all data from webpage given the url 
    Parameters: string url - webpage url
    Return: string data - webpage HTML data
    """
    r = requests.get("http://"+url)
    data = r.text
    return data

# TODO: Read data from webpage
def page_read(webpage):
    """
    Process data loaded from webpage
    Parameters: webpage - data loaded from webpage
    Return: None - all data is loaded into Trie
    """
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