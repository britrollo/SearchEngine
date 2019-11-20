from Trie import CompressedTrie

STOPWORDS = ["a", "an", "the", "this", "these", "those"]
AND = ["and"]
NOT = ["not"]

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