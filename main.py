import os
import re
import string
import nltk
from collections import Counter
from nltk.corpus import stopwords
from gensim.utils import tokenize
from nltk import PorterStemmer
nltk.download('stopwords')

folder = '/Users/aayushmakharia/Downloads/citeseer'

# 1. Write a program that preprocesses the collection.

def preprocessing(folder):
    words = []
    for file in os.listdir(folder):
            data = open(os.path.join(folder, file), 'r').read()
            data = re.sub(rf"[{string.punctuation}]", "", data)
            data = re.sub('\n',' ',data)
            words += tokenize(data.lower())
    return words

preprocessed_words = preprocessing(folder)

# 2. Determine the frequency of occurrence for all the words in the collection. Answer the following questions:
# a. What is the total number of words in the collection?
print("Q2.a Total words in the collection are:",len(preprocessed_words),"Words")

# b. What is the vocabulary size? (i.e., number of unique terms).
dic = dict()
for ele in preprocessed_words:
    if ele in dic:
        dic[ele] += 1
    else:
        dic[ele] = 1
vocab =len(dic)
print("Q2.b Vocabulary size of the collection is:",vocab)

# c. What are the top 20 words in the ranking? (i.e., the words with the highest frequencies).
count = Counter(preprocessed_words)
most_common = count.most_common(20)
print("Q2.c Top 20 words in ranking are:",most_common)

# d. From these top 20 words, which ones are stop-words?
stops = stopwords.words('english')
stop_most_common = []
for ele in most_common:
    if ele[0] in stops:
        stop_most_common.append(ele[0])
print("Q2d. The stop-words are:",stop_most_common)

# e. What is the minimum number of unique words accounting for 15% of the total number of words in the collection?
percentage_of_words = (15 * len(preprocessed_words))//100
list_fifteen = []
count = 0
i = 0
for ele in most_common:
    if count > percentage_of_words:
        break
    else:
        count += ele[1]
        i += 1
        # list_fifteen.append(ele[0])
print("Minimum number of unique words accounting for 15% of total words are",i)

# 3. Integrate a stemmer and a stopword eliminator into your code


ps = PorterStemmer()
words_stemmed = []
for ele in preprocessed_words:
    if ele not in stops:
        words_stemmed.append(ps.stem(ele))

print("Q3.a Total words in the collection after stemming are:",len(words_stemmed),"Words")

stemmed_dic = dict()
for ele in words_stemmed:
    if ele in stemmed_dic:
        stemmed_dic[ele] += 1
    else:
        stemmed_dic[ele] = 1
stemmed_vocab =len(stemmed_dic)
print("Q3.b Vocabulary size of the collection after stemming is:",stemmed_vocab)


stemmed_count = Counter(words_stemmed)
stemmed_most_common = stemmed_count.most_common(20)
print("Q3.c Top 20 words in ranking after stemming are:",stemmed_most_common)


stops = stopwords.words('english')
stemming_stop_most_common = []
for ele in stemmed_most_common:
    if ele[0] in stops:
        stemming_stop_most_common.append(ele[0])
print("Q3d. The stop-words after stemming are:",stemming_stop_most_common)

stemmed_most_common_fifty = stemmed_count.most_common(50)
stemmed_percentage_of_words = (15 * len(words_stemmed))//100
stemmed_list_fifteen = []
stemmed_count = 0
for ele in stemmed_most_common_fifty:
    if stemmed_count > stemmed_percentage_of_words:
        break
    else:
        stemmed_count += ele[1]
        stemmed_list_fifteen.append(ele[0])
print("Q3e. Minimum number of unique words accounting for 15% of total words after stemming are",len(stemmed_list_fifteen))
