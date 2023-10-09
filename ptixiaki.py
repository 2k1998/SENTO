import streamlit as st
from textblob import TextBlob
import plotly.express as px
import re
import emoji


def clean_text(text):
    # Remove non-alphabetic characters
    text = re.sub('[^A-Za-z0-9\s]+', ' ', text)

    # Convert emojis to text
    text = emoji.demojize(text)

    # Convert to lowercase
    text = text.lower()

    double_negative_patterns = ["not the worst", "isn't the worst", "not bad", "isn't bad"]
    for pattern in double_negative_patterns:
        if pattern in text:
            text = text.replace(pattern, "good")

    return text


def app():
    st.title("Sentiment Analysis Program")

    # Get user input
    text = st.text_area("Enter text to analyze:")

    # Clean the text
    cleaned_text = clean_text(text)

    # Analyze sentiment
    blob = TextBlob(cleaned_text)
    sentiment = blob.sentiment.polarity

    # Display results
    if st.button("Analyze"):
        if sentiment > 0:
            st.write("Positive")
            fig = px.pie(values=[0, sentiment], names=['Negative', 'Positive'])
            st.plotly_chart(fig)
        elif sentiment < 0:
            st.write("Negative")
            fig = px.pie(values=[-sentiment, 0], names=['Negative', 'Positive'])
            st.plotly_chart(fig)
        else:
            st.write("Neutral")
            fig = px.pie(values=[0.5, 0.5], names=['Negative', 'Positive'])
            st.plotly_chart(fig)


if __name__ == "__main__":
    app()
