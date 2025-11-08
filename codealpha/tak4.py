import pandas as pd
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    'Review': [
        "I love this product! It's fantastic and works perfectly.",
        "Terrible experience, I will never buy this again.",
        "The item is okay, not great but not bad either.",
        "Absolutely wonderful! Exceeded all my expectations.",
        "Worst service ever. Very disappointed.",
        "I’m happy with the quality and price.",
        "The delivery was late but product quality is good.",
        "Not worth the money.",
        "Amazing! I will recommend it to my friends.",
        "It's fine, nothing special."
    ]
}

df = pd.DataFrame(data)
print("🧾 Sample Data:")
print(df)
def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity  # -1 (negative) → +1 (positive)
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

df['Sentiment'] = df['Review'].apply(get_sentiment)
print("\n✅ Sentiment Classification Results:")
print(df)
sns.set(style="whitegrid")
plt.figure(figsize=(7,5))
sns.countplot(
    x='Sentiment',
    data=df,
    hue='Sentiment',    
    dodge=False,
    palette='coolwarm',
    legend=False
)

plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

summary = df['Sentiment'].value_counts()
print("\n📊 Sentiment Summary:")
print(summary)

print("\n🎯 Sentiment Analysis Completed Successfully!")
