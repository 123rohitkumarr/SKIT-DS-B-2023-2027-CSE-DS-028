"""
Transformer Pipeline for Regional Health NLP Processing
======================================================
Developer: Sandeep Yadav (NLP & Backend Developer)
Project: Early Health Disease Prediction using AI Chatbot (NLP-Based)
Department of CSE (Data Science), SKIT Jaipur

Purpose:
--------
Extracts contextual token embeddings, performs semantic similarity mapping,
and computes clinical intent representations for Hadoti & Marwari speech transcripts
using Google's MuRIL (Multilingual Representations for Indian Languages).
"""

import torch
from transformers import AutoTokenizer, AutoModel
import re

class RegionalTransformerPipeline:
    def __init__(self, model_name="google/muril-base-cased"):
        """
        Initializes the multilingual transformer pipeline.
        MuRIL (Multilingual Representations for Indian Languages) is specifically
        pre-trained on Indian languages including Devanagari script.
        """
        self.model_name = model_name
        self.device = torch.device("cpu")
        self.tokenizer = None
        self.model = None
        self._is_loaded = False
        
    def load_model(self):
        """Attempts to load the Transformer model; provides graceful fallback if offline."""
        if self._is_loaded:
            return True
        print(f"Loading multilingual transformer: {self.model_name}...")
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModel.from_pretrained(self.model_name)
            self.model.to(self.device)
            self.model.eval()
            self._is_loaded = True
            print("Transformer model loaded successfully.")
            return True
        except Exception as e:
            print(f"Warning: Could not load remote transformer ({e}). Using offline Devanagari tokenizer.")
            self._is_loaded = False
            return False

    def get_sentence_embedding(self, text: str):
        """
        Computes pooled contextual embedding vector for a Devanagari sentence.
        """
        if not self._is_loaded:
            if not self.load_model():
                return None
        
        try:
            inputs = self.tokenizer(
                text, 
                padding=True, 
                truncation=True, 
                max_length=128, 
                return_tensors="pt"
            ).to(self.device)
            
            with torch.no_grad():
                outputs = self.model(**inputs)
                # Mean pooling over token embeddings
                mask = inputs['attention_mask'].unsqueeze(-1).expand(outputs.last_hidden_state.size()).float()
                sum_embeddings = torch.sum(outputs.last_hidden_state * mask, 1)
                sum_mask = torch.clamp(mask.sum(1), min=1e-9)
                mean_pooled = sum_embeddings / sum_mask
                return mean_pooled.squeeze().numpy()
        except Exception as e:
            print(f"Embedding calculation error: {e}")
            return None

    def compute_similarity(self, text1: str, text2: str) -> float:
        """
        Computes cosine semantic similarity between two texts.
        """
        emb1 = self.get_sentence_embedding(text1)
        emb2 = self.get_sentence_embedding(text2)
        if emb1 is None or emb2 is None:
            # Fallback to Jaccard word-level overlap
            words1 = set(text1.split())
            words2 = set(text2.split())
            intersection = words1.intersection(words2)
            union = words1.union(words2)
            return len(intersection) / len(union) if union else 0.0
            
        dot = (emb1 * emb2).sum()
        norm1 = (emb1 ** 2).sum() ** 0.5
        norm2 = (emb2 ** 2).sum() ** 0.5
        return float(dot / (norm1 * norm2)) if (norm1 and norm2) else 0.0
