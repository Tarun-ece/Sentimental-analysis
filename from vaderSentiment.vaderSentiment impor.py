from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentences = ["you are looser but you play a good game"]
analyzer = SentimentIntensityAnalyzer()

for sentence in sentences:
    a = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(a)))
