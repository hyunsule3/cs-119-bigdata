"""
Use Functional Programming (Recursion)
"""
import requests, re
import string
stopwords_list = requests.get("https://gist.githubusercontent.com/rg089/35e00abf8941d72d419224cfd5b5925d/raw/12d899b70156fd0041fa9778d657330b024b959c/stopwords.txt").content
stopwords = list(set(stopwords_list.decode().splitlines()))


def remove_stopwords(words):
    list_ = re.sub(r'[^a-zA-Z0-9]', " ", words.lower()).split()
    return [itm for itm in list_ if itm not in stopwords]

def ο(text):
    if any(char.isupper() for char in text):
        return ο(text.lower())
    if re.search(r'\[.*?\]', text) is not None:
        return ο(re.sub(r'\[.*?\]', '', text))
    if re.search(r'[%s]' % re.escape(string.punctuation), text) is not None:
        return ο(re.sub(r'[%s]' % re.escape(string.punctuation), ' ', text))
    if re.search(r'[\d]', text) is not None:
        return ο(re.sub(r'[\d]', ' ', text))
    
    return ' '.join(remove_stopwords(text))