#week 1 - lowercase and remove punctuation
import re 
def lowercase(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', "", text)
    stopwords = ["the", "is", "in", "of", "and", "to", "a"]
    tokens= text.split()
    news = [i for i in tokens if i not in stopwords]
    return news
if  __name__ == "__main__":
    sample_text = "this is a new text for traning "
    print(lowercase(sample_text))