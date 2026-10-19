"""
Regional Medical Symptom & Entity Extraction Engine
===================================================
Developer: Sandeep Yadav (NLP & Backend Developer)
Project: Early Health Disease Prediction using AI Chatbot (NLP-Based)
Department of CSE (Data Science), SKIT Jaipur

Purpose:
--------
The core engine that integrates the dialect lexicon, regex patterns, and
transformer representations to extract standardized clinical symptoms, 
anatomical body parts, clinical severity, and duration from patient utterances.
"""

import re
from typing import Dict, List, Any
try:
    from dialect_lexicon import SYMPTOM_LEXICON, BODY_PARTS_LEXICON, SEVERITY_LEXICON
    from transformer_pipeline import RegionalTransformerPipeline
except ImportError:
    from .dialect_lexicon import SYMPTOM_LEXICON, BODY_PARTS_LEXICON, SEVERITY_LEXICON
    from .transformer_pipeline import RegionalTransformerPipeline

class RegionalSymptomExtractor:
    def __init__(self, use_transformers: bool = False):
        self.use_transformers = use_transformers
        self.transformer = RegionalTransformerPipeline() if use_transformers else None
        
        # Compile duration regex patterns for Hadoti / Marwari / Hindi
        self.duration_patterns = [
            r'(\d+|एक|दो|तीन|चार|पाँच|पांच|छह|सात|आठ|नौ|दस)\s*(दिन|दन|मीना|महीना|महीने|हफ्ता|हफ्ते|घंटे|घंटा)\s*(सूं|सू|सु|से|सुन)?',
            r'(कल|आज|रात|सवेरे|परसों)\s*(सूं|सू|सु|से|संज्या|बार)?',
            r'(हफ्ता\s*भर\s*सूं|महीना\s*भर\s*सूं)'
        ]

    def detect_dialect(self, text: str) -> str:
        """Detects whether text has predominantly Hadoti or Marwari markers."""
        hadoti_markers = ["कणा", "खल डंत्या", "भामाशाह", "मलचाव", "बग गया", "दुक्रियो", "अन्मू"]
        marwari_markers = ["घणो", "घणी", "म्हाने", "महाने", "थारो", "थारी", "पड़सी", "करासूं", "पीजो", "होवे", "होयो", "बखत"]
        
        h_score = sum(1 for m in hadoti_markers if m in text)
        m_score = sum(1 for m in marwari_markers if m in text)
        
        if m_score > h_score:
            return "Marwari"
        elif h_score > m_score:
            return "Hadoti"
        return "Regional Rajasthani"

    def extract_duration(self, text: str) -> str:
        """Extracts medical symptom duration from text."""
        for pattern in self.duration_patterns:
            match = re.search(pattern, text)
            if match:
                return match.group(0).strip()
        return "Not Specified"

    def extract_severity(self, text: str) -> str:
        """Extracts symptom severity (Severe / Moderate / Mild)."""
        for severity, keywords in SEVERITY_LEXICON.items():
            for kw in keywords:
                if kw in text:
                    return severity
        return "Moderate"

    def extract_symptoms(self, text: str) -> List[str]:
        """Identifies clinical symptoms mentioned in regional dialect text."""
        detected = []
        for symptom, keywords in SYMPTOM_LEXICON.items():
            for kw in keywords:
                if kw in text:
                    if symptom not in detected:
                        detected.append(symptom)
                    break
        return detected

    def extract_body_parts(self, text: str) -> List[str]:
        """Identifies anatomical body parts mentioned in text."""
        detected = []
        for part, keywords in BODY_PARTS_LEXICON.items():
            for kw in keywords:
                if kw in text:
                    if part not in detected:
                        detected.append(part)
                    break
        return detected

    def process_transcript(self, text: str, filename: str = "", gender: str = "") -> Dict[str, Any]:
        """
        Processes a single transcript string and returns structured medical entity record.
        """
        clean_text = re.sub(r'[\r\n\t]+', ' ', text).strip()
        dialect = self.detect_dialect(clean_text)
        symptoms = self.extract_symptoms(clean_text)
        body_parts = self.extract_body_parts(clean_text)
        severity = self.extract_severity(clean_text)
        duration = self.extract_duration(clean_text)
        
        # Clinical Summary string
        if symptoms:
            sym_str = ", ".join(symptoms)
            summary = f"Patient presents with {sym_str} ({severity} severity, duration: {duration})."
        else:
            summary = f"General health inquiry / check-up consultation."
            
        return {
            "filename": filename,
            "gender": gender,
            "raw_transcript": clean_text,
            "detected_dialect": dialect,
            "extracted_symptoms": symptoms,
            "symptoms_count": len(symptoms),
            "affected_body_parts": body_parts,
            "severity_level": severity,
            "duration": duration,
            "clinical_summary": summary
        }
