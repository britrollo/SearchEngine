from Trie import CompressedTrie
from nltk.corpus import stopwords
import Crawler

from nltk.stem.wordnet import WordNetLemmatizer # maybe all words should be changed to their stem word?

def merge(s1, s2, s):
    """
    Modified merge from 8.1 to merge two sorted lists and return the intersection of the inputs sorted
    Parameters: list string s1  - list to be merged
                list string s2  - list to be merged
                list empty s    - list to hold result of merge
    Return: list string s       - merged and sorted lists
    """
    i = 0
    j = 0
    n1 = len(s1)
    n2 = len(s2)
    while i < n1 and j < n2:
        if s1[i] < s2[j]:
            i = i + 1
        elif s1[i] > s2[j]:
            j = j + 1
        else:
            s = s + [s1[i]]
            i = i + 1
            j = j + 1
    return s

# TODO : comment 
#TODO: debug - something wrong with how urls are added to inv_idx.idx - only one is being returned
def search(terms):
    results = []
    for x in terms:
        if x not in set(stopwords.words('english')):
            if Crawler.cache.search(x):
                # word found
                # if x in Crawler.inv_idx.idx.keys():
                urls = sorted(Crawler.inv_idx.idx[x])
                if results == []:
                    results = urls
                else: #intersection
                    # To facilitate the intersection computation, 
                    # each occurrence list should be implemented with a 
                    # sequence sorted by address or with a dictionary, 
                    # which allows for a simple intersection algorithm 
                    # similar to sorted sequence merging (Section 8.1).
                    results = merge(urls, results, [])
                # else:
                #     return None
            else:
                return None
    return results

def ranking(results, terms):
    scored_results = []
    for result in results:
        score = 0
        words = Crawler.inv_idx.rank[result]
        # print(Crawler.inv_idx.rank)
        # print(result)
        # print(words)
        for term in terms:
            # print(Crawler.inv_idx.idx[term])
            score += words[term]
        scored_results += (score, result)
    return scored_results

def main():
    """
    1. User inputs website
    2. Webpage and 5-10 connected webpages are loaded
    3. Webpages are processed and added to trie and inverted index
        - Check if w in index
        - If not add w to index with url and add w to trie
        - If in index add url to list of w
            - If in index and url in list, update ranking dictionary
    4. User inputs search term or terms
        - More than one term? - complete search for both and return intersection of occurence lists
            - Combine occurence counts for rank
    5. Rank results
        - Maybe keep dictionary with (url, wd) where wd is a dictionary of (w, c) 
        where w is word and c is occurence count for the page
    6. Return results
    """
    # url = input("Site to search: ")
    #Load pages into trie
    print("Loading data...")
    url = "http://www.dataquest.io/blog/web-scraping-tutorial-python/"
    # url = "https://stackoverflow.com/questions/15478127/remove-final-character-from-string-python"
    page = Crawler.page_load(url)
    d = Crawler.page_read(page, url, True)

    #Loop user searching
    while True:
        search_terms = input("Search: ")
        if search_terms == []:
            continue
        elif search_terms[0] == ":":
            if search_terms[1:] == "quit":
                print("Goodbye!")
                return
        else:
            search_terms = Crawler.remove_punc(search_terms)
            results = search(search_terms)
            if results:
                #results found
                ranked = ranking(results, search_terms)
                print(ranked)
            else:
                print("No results found")
            search_terms = ""
                    
if __name__ == '__main__': 
    main() 