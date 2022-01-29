import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords

# Created Tokens
# Tokens were created for each article saved as a word file
# Code was the same but the only changes was which file was opened and what the final file was named

ps = PorterStemmer()
file_content = open("CNN_article.txt", encoding="utf-8").read()
tokens = nltk.word_tokenize(file_content)

filtered_text = [t for t in tokens if not t in stopwords.words("english")]

# Stemming

for words in tokens:
    stemmed_words = ps.stem(words)


text_for_project = " ".join(filtered_text)

text_file = open('Final_CNN.txt', 'w')
n = text_file.write(text_for_project)
text_file.close()