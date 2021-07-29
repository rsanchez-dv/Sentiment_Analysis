import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words('english')

email_regex = re.compile(r"[\w.-]+@[\w.-]+")
url_regex = re.compile(r"(http|www)[^\s]+")
date_regex = re.compile(r"[\d]{2,4}[ -/:]*[\d]{2,4}([ -/:]*[\d]{2,4})?") # a way to match date
keep_word_regex = re.compile(r"[^A-Za-z ]+")

def lemmatize_text(text):
    word_tokens = word_tokenize(text)
    lemm_text = ' '.join([lemmatizer.lemmatize(words) for words in word_tokens])
    return lemm_text
def decontracted(text):
    # specific
    text = re.sub(r"won\'t", "will not", text)
    text = re.sub(r"can\'t", "can not", text)

    # general
    text = re.sub(r"n\'t", " not", text)
    text = re.sub(r"\'re", " are", text)
    # This might get confused with possession
    #text = re.sub(r"\'s", " is", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'t", " not", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'m", " am", text)
    return text

def clean_special_patterns(text):
    text = url_regex.sub("", text)
    text = email_regex.sub("", text)
    text = date_regex.sub("", text)
    text = re.sub('\s+',' ',text)
    text = text.strip()
    return text

def clean_stopwords(text):
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    joined_text = " ".join(filtered_sentence)
    return joined_text

def clean_keep_words(text):
    return keep_word_regex.sub(" ", text)

def clean_text(text):
    text = decontracted(text)
    text = clean_special_patterns(text)
    text = clean_stopwords(text)
    text = clean_keep_words(text)
    text = lemmatize_text(text)    
    tokens = [word.lower() for word in word_tokenize(text)]
    text = " ".join(tokens)
    return text