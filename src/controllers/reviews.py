from flask import request, jsonify
from transformers import DistilBertTokenizer,  DistilBertForSequenceClassification
import torch


# Load sentiment analysis model
model_name = "sohan-ai/sentiment-analysis-model-amazon-reviews"
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
model = DistilBertForSequenceClassification.from_pretrained(model_name)

def analyze_review():
    # Extract review from request body
    review = request.json.get('review')

    # Tokenize input text
    inputs = tokenizer(review, return_tensors="pt")

    # Make prediction
    outputs = model(**inputs)
    predicted_label = "positive" if outputs.logits.argmax().item() == 1 else "negative"

    return jsonify({"sentiment": predicted_label})

# Load the fine-tuned model for fake reviews
# model_path_fake = "src/machine-models/models/fine_tuned_fake_review_model"
# tokenizer_fake = DistilBertTokenizer.from_pretrained(model_path_fake)
# model_fake = DistilBertForSequenceClassification.from_pretrained(model_path_fake)

# def detect_fake_review():
#     # Extract review from request body
#     review = request.json.get('review')

#     # Tokenize input text
#     inputs = tokenizer_fake(review, return_tensors="pt")

#     # Make prediction
#     with torch.no_grad():
#         outputs = model_fake(**inputs)
#         predicted_label_id = outputs.logits.argmax().item()

#     # Map predicted label to fake/real
#     label_map = {0: "real", 1: "fake"}
#     predicted_label = label_map[predicted_label_id]

#     return jsonify({"fake_review": predicted_label})


