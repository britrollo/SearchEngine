# SearchEngine
Brianne Trollo  
CS600 Final Project  

Implement the simplified Search Engine described in Section 23.5.4 for the pages of a small Web site. Use all the words in the pages of the site as index terms, excluding stop words such as articles, prepositions, and pronouns.

---

Data Structures used are a compressed trie for storing and lookup of key words from scraped webpages and an inverted index, which is a dictionary with key value pairs (w, L) where w is a word and L is a list of references to pages containing w.

---
## Dependencies:
* nltk
* beautifulsoup4 from bs4
* requests

## How To Run:
### 1. Install depedencies:
(requires python 3)  
    1. pip install nltk  
    2. pip install beautifulsoup4  
    3. pip install requests

### 2. 