from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, sent_tokenize

def sentimentAnalysis(text):
    sid = SentimentIntensityAnalyzer()
    s = sid.polarity_scores(text)
    j=["Negative", "Neutral", "Positive", "Compounded"]
    s={j[i]:list(s.values())[i] for i in range(len(j))}
    s.update({'Tokenized Words':word_tokenize(text)})
    s.update({'Tokenized Sentences':sent_tokenize(text)})
    return s