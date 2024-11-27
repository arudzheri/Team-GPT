import os
from agents.summarizer import SummarizerAgent
from agents.sentiment import SentimentAgent
from utils.data_loader import load_text_data

def main():
    # Load text data
    text_data = load_text_data("data/input.txt")
    
    # Initialize agents
    summarizer = SummarizerAgent()
    sentiment_analyzer = SentimentAgent()
    
    # Summarize the text
    summary = summarizer.summarize(text_data)
    print(f"Summary:\n{summary}")
    
    # Analyze sentiment of the summary
    sentiment = sentiment_analyzer.analyze_sentiment(summary)
    print(f"Sentiment Analysis:\n{sentiment}")

if __name__ == "__main__":
    main()


