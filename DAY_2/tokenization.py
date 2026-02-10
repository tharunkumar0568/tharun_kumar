import nltk
from nltk.tokenize import word_tokenize
text="tokenization using genai"
tokens=word_tokenize(text)
print("length of token:",len(tokens))
print("num of tokens:",tokens)
