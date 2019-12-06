from Trie import CompressedTrie
from nltk.corpus import stopwords
import Crawler

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

def partition(arr, low, high):
    """
    Paritioning for quickSort
    Parameters: list arr
                int low
                int high
    """
    i = (low -1)
    pivot = arr[high][0]
    for j in range(low, high):
        if arr[j][0] < pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    """
    QuickSort algoritm
    Parameters: list arr    - elements to be sorted
                int low     - low index for paritioning
                int high    - high index for paritioning
    Return: sorted arr
    """
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def search(terms):
    """
    Search for results for inputted term or terms
    Parameter: list string terms - list of terms to be searched for
    Result:     list of urls with the terms sorted
    """
    results = []
    for x in terms:
        x = x.lower()
        if Crawler.cache.search(x):
            # word found
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
        else:
            return None
    return results

def ranking(results, terms):
    """
    Ranking for search results
    Parameters: list string results - urls returned from search()
                list string terms   - words searched for
    Return:     results sorted by rank in increasing order
    """
    scored_results = []
    for result in results:
        score = 0
        words = Crawler.inv_idx.rank[result]
        for term in terms:
            term = term.lower()
            score += words[term]
        scored_results += [(score, result)]
    quickSort(scored_results, 0, len(scored_results)-1)
    return scored_results

def main():
    """
    1. Loads webpages from ./webpages by reading filenames from input.txt
    2. Webpages are processed and added to trie and inverted index
        - Check if w in index
        - If not add w to index with url and add w to trie
        - If in index add url to list of w
            - If in index and url in list, update ranking dictionary
    3. User inputs search term or terms
        - More than one term? - complete search for both and return intersection of occurence lists
            - Combine occurence counts for rank
    4. Rank results
        - Keep dictionary with (url, wd) where wd is a dictionary of (w, c) 
        where w is word and c is occurence count for the page
    5. Return results
    6. Menu and options available
    """
    fp = open("output.txt", "w+")
    #Load pages into trie
    print("Loading data...")
    fp.write("Loading data..." + "\n")
    # url = "https://www.dataquest.io/blog/"
    # Initial read-in from downloaded pages
    folder = "./webpages/"
    input_file = "./webpages/input.txt"
    wp = open(input_file, "r")
    lines = wp.readlines()
    for line in lines:
        line = line.split()
        filename = line[0]
        url = line[1]
        # page = Crawler.page_load(url)
        page = open(folder+filename, "r")
        Crawler.page_read(page, url, False)

    print("You can begin searching now. When done please exit using the command")
    fp.write("You can begin searching now. When done please exit using the command"+ "\n")
    print(":quit")
    fp.write(":quit"+ "\n")
    print("for more options type ")
    fp.write("for more options type "+ "\n")
    print(":menu")
    fp.write(":menu"+ "\n")
    
    #Loop user searching
    while True:
        search_terms = input("Search: ")
        fp.write("Search: " + search_terms + "\n")
        if not search_terms or search_terms == [] or search_terms == "" or search_terms == " ":
            print("Please enter a non-empty search.")
            fp.write("Please enter a non-empty search.\n")
            continue
        elif search_terms[0] == ":":
            if search_terms[1:].lower() == "urls":
                urls = Crawler.inv_idx.rank.keys()
                print("Count: " + str(len(urls)))
                str_urls = ", ".join(urls)
                print(str_urls)
                fp.write("Count: " + str(len(urls))+ "\n")
                fp.write(str_urls + "\n")
            if search_terms[1:].lower() == "add":
                page = Crawler.page_load(Crawler.unused_urls[0])
                Crawler.unused_urls = Crawler.unused_urls[:-1]
                d = Crawler.page_read(page, Crawler.unused_urls[0], True)
            if search_terms[1:].lower() == "menu":
                print("Menu:")
                print(":menu - to show menu")
                print(":add  - add new webpages to search memory")
                print(":urls - views urls available in memory")
                print(":quit - to end session")
                fp.write("Menu:" + "\n")
                fp.write(":menu - to show menu" + "\n")
                fp.write(":add  - add new urls to search memory" + "\n")
                fp.write(":urls - views urls available in memory" + "\n")
                fp.write(":quit - to end session" + "\n")
            if search_terms[1:].lower() == "quit":
                print("Goodbye!")
                fp.write("Goodbye!" + "\n")
                fp.close()
                return
        else:
            search_terms = Crawler.remove_punc(search_terms)

            excluded_words = []
            for w in search_terms:
                if not Crawler.str_check(w):
                    excluded_words += [w]
                    
            for w in excluded_words:
                search_terms.remove(w)
            
            results = search(search_terms)
            if results:
                #results found
                ranked = ranking(results, search_terms)
                for i in range(len(ranked)-1, -1, -1):
                    print(ranked[i][1])
                    fp.write(ranked[i][1] + "\n")
            else:
                print("No results found")
                fp.write("No results found" + "\n")
            
            if excluded_words != []:
                print("Words excluded from search: " + str(excluded_words))
                fp.write("Words excluded from search: " + str(excluded_words) + "\n")
            search_terms = ""
                    
if __name__ == '__main__': 
    main() 