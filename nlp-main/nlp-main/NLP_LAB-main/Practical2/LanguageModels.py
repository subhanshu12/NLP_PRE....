import nltk
nltk.download() 
from nltk.tokenize import word_tokenize,sent_tokenize
import string
string.punctuation = string.punctuation +'“'+'”'+'-'+'’'+'‘'+'—'
string.punctuation = string.punctuation.replace('.', '')
file = open('tom_sawyer.txt').read()
#preprocess data to remove newlines and special characters
file_new = ""
for line in file:
    line_new = line.replace("n", " ")      
    file_new += line_new
preprocessedCorpus = "".join([char for char in file_new if char not in string.punctuation])

sentences = sent_tokenize(preprocessedCorpus)
print("1st 5 sentences of preprocessed corpus are : ")
print(sentences[0:5])
words = word_tokenize(preprocessedCorpus)
print("1st 5 words/tokens of preprocessed corpus are : ")
print(words[0:5])

nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in words if not w.lower() in stop_words]