from Trie import CompressedTrie
from nltk.corpus import stopwords
import Crawler

from nltk.stem.wordnet import WordNetLemmatizer # maybe all words should be changed to their stem word?

# ARTICLES = ["a", "an", "the", "this", "these", "those"]
# PRONOUNS = ["he", "his", "she", "her", "hers", "they", "you", "your", 
#             "yours", "i", "it", "we", "our", "us", "them", "their", "theirs"]
# PREPOSITIONS = ["about", "above", "across", "after", "along", "amid", "among", 
#                 "anti", "around", "as", "at", "before", "behind", "below", "beneath", 
#                 "beside", "besides", "between", "beyond", "but", "except", "for", 
#                 "from", "in", "inside", "into", "like", "near", "of", "off", "on",
#                 "onto", "over", "past", "per", "plus", "regarding", "than", "since"
#                 "to", "up", "unlike", "via", "with", "without", "not", "and"]
# STOPWORDS = ARTICLES + PRONOUNS + PREPOSITIONS

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
    url = input("Site to search: ")
    #Load pages into trie
    page = Crawler.page_load(url)
    d = Crawler.page_read(page)

    #Loop user searching
    # while True:
    #     search = input("Search: ")
    #     search = search.split()
    #     if search == []:
    #         continue
    #     elif search[0][0] == ":":
    #         if search[0][1:] == "quit":
    #             print("Goodbye!")
    #             return
    #     else:
    #         for x in search:
    #             if x not in set(stopwords.words('english')):
    #                 print(x)
                    

if __name__ == '__main__': 
    main() 