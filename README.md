# SearchEngine
Brianne Trollo  
CS600: Advanced Algorithm Design & Implementation
Final Project  

Implement the simplified Search Engine described in Section 23.5.4 for the pages of a small Web site. Use all the words in the pages of the site as index terms, excluding stop words such as articles, prepositions, and pronouns.

---

Data Structures used are a compressed trie for storing and lookup of key words from scraped webpages and an inverted index, which is a dictionary with key value pairs (w, L) where w is a word and L is a list of references to pages containing w. In addition, to calculate ranks by keeping count of the number of occurences of a word, a dictionary was used with key value pairs (u, D) where u is the url of a webpage and D is a dictionary with the key value pair (w, c) where w is a word on the webpage and c is the occurence count.

Algorithms used are a modified version of merge (Section 8.1) to find the intersection of two sorted lists of search results and quicksort to sort the rankings of the resulting webpages of a sort.

Search results are ranked in decreasing order by an acculumation of the counts of each search term on each page. For example, if the inputted search is for 'cat' and 'dog', page x, with the respective counts of 10 and 3, will rank higher than page y, which has the respective counts of 9 and 1. In addition, words used in titles were given a slightly higher count than if the word was just in the body of the webpage.

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

### 2. Run project
In project directory (../SearchEngine):
~~~
python main.py
~~~
Wait for data to load. Begin entering search terms when this appears:
~~~
Search:
~~~
For options menu enter:
~~~
Search: :menu
~~~
To add more pages to search memory:
~~~
Search: :add
~~~
To view all urls in memory:
~~~
Search: :urls
~~~
To end session:
~~~
Search: :quit
~~~