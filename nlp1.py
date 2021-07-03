from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import spacy
from  nltk.parse.corenlpnltk.pa  import CoreNLPParser


nlp = spacy.load('en_core_web_sm')
myFile = open("antxt.txt").read()
doc_file = nlp(myFile)

for num , sentence in enumerate(doc_file.sents):
    print(f'{num}: {sentence}')

for token in doc_file: 
    print(token.text, token.pos_)

chunks = (list(doc_file.noun_chunks))
print (chunks)

wnl = WordNetLemmatizer()
ps = PorterStemmer()
for token in doc_file:
    print(wnl.lemmatize(str(token)), ps.stem(str(token)))

