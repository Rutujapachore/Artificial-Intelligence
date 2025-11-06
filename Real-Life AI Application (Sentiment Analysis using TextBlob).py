from textblob import TextBlob

text = input("Enter a sentence: ")
blob = TextBlob(text)

print("Sentiment Polarity:", blob.sentiment.polarity)
if blob.sentiment.polarity > 0:
    print("Sentiment: Positive 😊")
elif blob.sentiment.polarity < 0:
    print("Sentiment: Negative 😞")
else:
    print("Sentiment: Neutral 😐")
