import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from spacy.lang.en.stop_words import STOP_WORDS
from bs4 import BeautifulSoup
from bs4.element import Comment
from urllib.request import Request, urlopen
import spacy
nlp = spacy.load("en_core_web_sm")
stop = STOP_WORDS


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


def extractText(link):
    try:
        html = urlopen(link).read()
        extractedText = text_from_html(html)
    except Exception as e:
        extractedText = e

    return extractedText


def preprocessText(text):
    doc = nlp(text)
    lemma = [token.lemma_ for token in doc]
    lemma2 = ' '.join([str(elem) for elem in lemma])
    doc2 = nlp(lemma2)
    filtered = [token.text for token in doc2 if (
        (token.is_stop == False) and (len(token) > 2))]
    #filtered2 = ' '.join([str(elem) for elem in filtered])
    # print(len(filtered))
    vectorizer = joblib.load('core/vect_model.pkl')
    # vectorization = TfidfVectorizer(max_df=0.7)
    filterV = vectorizer.transform(filtered)
    # print(filterV)
    clf = joblib.load('core/clf_svm_model.pkl')
    result = clf.predict(filterV)
    for i in range(len(result)):
        if(result[i] == 1):
            return False

    return True


def main():
    link = 'https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/'
    extractedText = extractText(link)
    # print(extractedText)

    safe = preprocessText(extractedText)
    print(safe)


if __name__ == "__main__":
    main()