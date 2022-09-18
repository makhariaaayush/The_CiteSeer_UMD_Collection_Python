CS 582 Information Retrieval
HW 1
The CiteSeer UMD collection

###Name : Aayush Makharia
###UIN 676412286

The Folder name is pythonProject which contains main.py and venv main.py contains the code and venv has the lib and bin

###Functions Functionality:
PREPROCESSING
Method preprocessing() reads the files from citeseer and preprocesses the text and the removal of punctuation marks along with new line is removed
I tokenize and lower case the text and save it to a list called words

TOTAL NO. OF WORDS
I find the total number of words in the files which is the same as the total number of tokens found in the preprocessing step above

VOCABULARY SIZE
The total number of unique words found is what makes the vocabulary of the files I used dictionary implementation to get the vocabulary saved as vocab

TOP 20 WORDS
I used Counter from collections and used the python function most_common(20) to get the top 20 words based on frequency

STOP WORDS IN TOP 20 WORDS
Using from nltk.corpus import stopwords we can find the stop words and matching that with our most common words I got the stop words present in the top 20 words

MINIMUM WORDS TO 15% OF THE TOTAL WORDS
Using most common top 20 words we iterated the count value as sum and found the number of words that made 15% of the total words

STEMMER and STOP ELIMINATOR
Using from nltk import PorterStemmer I implemented Stemmer we remove the stop words and reduce the words to basic words
following this we calculate TOTAL NO. OF WORDS, VOCABULARY SIZE, TOP 20 WORDS, STOP WORDS IN TOP 20 WORDS, AND MINIMUM WORDS TO 15% OF THE TOTAL WORDS

###How To Run The Program:

1.  Install PyCharm and Python in your system
2.  unzip pythonProject.zip
3.  open the pythonProject using PyCharm
4.  Run the program by changing the path as per your requirement to wherever the citeseer file is stored

### Optional:

- There's a requirement.txt file created using pip freeze. pip install will install all the dependencies in the virtual environment.

### Program Output:

Q2.a Total words in the collection are: 472250 Words
Q2.b Vocabulary size of the collection is: 19106
Q2.c Top 20 words in ranking are: [('the', 25662), ('of', 18640), ('and', 14131), ('a', 13365), ('to', 11536), ('in', 10067), ('for', 7379), ('is', 6578), ('we', 5138), ('that', 4820), ('this', 4446), ('are', 3737), ('on', 3660), ('an', 3281), ('with', 3200), ('as', 3057), ('by', 2765), ('data', 2691), ('be', 2500), ('information', 2322)]
Q2d. The stop-words are: ['the', 'of', 'and', 'a', 'to', 'in', 'for', 'is', 'we', 'that', 'this', 'are', 'on', 'an', 'with', 'as', 'by', 'be']
Minimum number of unique words accounting for 15% of total words are 4
Q3.a Total words in the collection after stemming are: 289936 Words
Q3.b Vocabulary size of the collection after stemming is: 13000
Q3.c Top 20 words in ranking after stemming are: [('system', 3741), ('use', 3740), ('data', 2691), ('agent', 2689), ('inform', 2398), ('model', 2317), ('paper', 2246), ('queri', 1906), ('user', 1756), ('learn', 1740), ('algorithm', 1584), ('approach', 1544), ('problem', 1543), ('applic', 1522), ('present', 1507), ('base', 1487), ('web', 1440), ('databas', 1424), ('comput', 1411), ('method', 1223)]
Q3d. The stop-words after stemming are: []
Q3e. Minimum number of unique words accounting for 15% of total words after stemming are 24
