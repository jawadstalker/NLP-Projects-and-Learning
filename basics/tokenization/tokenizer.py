# #week 1 - tokenization
# import re

# def simple_tokenize(text):
#     # 1. Lowercase
#     text = text.lower()

#     # 2. Remove punctuation
#     # text = re.sub(r'[^\w\s]', '', text)
#     text = re.sub(r'[^\w\s]', "", text )

#     # 3. Split by whitespace
#     tokens = text.split()

#     return tokens


# if __name__ == "__main__":
#     sample_text = "this is a test text"
#     print(simple_tokenize(sample_text))


#week 1 - train 2 chatgpt answer 
import re

def simple_tokenize(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    
    stopwords = {"the", "is", "in", "of", "and", "to", "a"}  
    tokens = text.split()
    
    filtered = [t for t in tokens if t not in stopwords]
    return filtered

if __name__ == "__main__":
    sample_text = "this is a test text"
    print(simple_tokenize(sample_text))
