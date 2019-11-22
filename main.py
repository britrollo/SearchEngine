from Trie import CompressedTrie

ARTICLES = ["a", "an", "the", "this", "these", "those"]
PRONOUNS = ["he", "his", "she", "her", "hers", "they", "you", "your", 
            "yours", "i", "it", "we", "our", "us", "them", "their", "theirs"]
PREPOSITIONS = ["about", "above", "across", "after", "along", "amid", "among", 
                "anti", "around", "as", "at", "before", "behind", "below", "beneath", 
                "beside", "besides", "between", "beyond", "but", "except", "for", 
                "from", "in", "inside", "into", "like", "near", "of", "off", "on",
                "onto", "over", "past", "per", "plus", "regarding", "than", "since"
                "to", "up", "unlike", "via", "with", "without", "not", "and"]
STOPWORDS = ARTICLES + PRONOUNS + PREPOSITIONS

def main():
    #Load pages into trie

    #Loop user searching
    while True:
        search = input("Search: ")
        search = search.split()
        if search == []:
            continue
        elif search[0][0] == ":":
            if search[0][1:] == "quit":
                print("Goodbye!")
                return
        else:
            for x in search:
                if x not in STOPWORDS:
                    print(x)
                    

if __name__ == '__main__': 
    main() 