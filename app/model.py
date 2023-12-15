# app/model.py
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import numpy as np

# Cache the models and tokenizers
model_cache = {}
tokenizer_cache = {}

def load_model(model_name):
    if model_name not in model_cache:
        model_cache[model_name] = AutoModelForSequenceClassification.from_pretrained(model_name, output_attentions=True)
        tokenizer_cache[model_name] = AutoTokenizer.from_pretrained(model_name)
    return model_cache[model_name], tokenizer_cache[model_name]

# Load the model and tokenizer
#load_model("bert-base-uncased")

def analyze_text(text, model_name):
    # Load the model and tokenizer
    model, tokenizer = load_model(model_name)
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs, output_attentions=True)

    # Get the attention scores
    attentions = outputs.attentions
    visualization_data = visualize_attention(attentions)
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

    # Return the results
    results = {
        "attentions": visualization_data,
        "tokens": tokens
    }
    return results


def visualize_attention(attention):
    

    # Average the attention weights across all layers
    attention_matrix = torch.stack(attention).mean(dim=0).mean(dim=0)
    attention_matrix = attention_matrix.squeeze().detach().numpy()  

    # Normalize the attention matrix
    min_val = np.min(attention_matrix)
    max_val = np.max(attention_matrix)
    normalized_attention = (attention_matrix - min_val) / (max_val - min_val) if max_val > min_val else attention_matrix

    return normalized_attention.tolist()  
