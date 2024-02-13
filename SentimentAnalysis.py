#We'll use the transformers library from Hugging Face and the torch library for deep learning. 
#pip install transformers torch


import torch
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

def perform_sentiment_analysis(text):
    model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    sentiment_labels = ["Very Negative", "Negative", "Neutral", "Positive", "Very Positive"]
    predicted_sentiment = sentiment_labels[predicted_class]
    return predicted_sentiment
if __name__ == "__main__":
    example_text = "I really enjoyed watching that movie. The acting was superb!"
    predicted_sentiment = perform_sentiment_analysis(example_text)
    print(f"Predicted sentiment: {predicted_sentiment}")
