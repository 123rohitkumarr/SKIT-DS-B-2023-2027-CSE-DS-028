# Module: NLP Processing (Sprint 4)

**Developer:** Sandeep Yadav (NLP & Backend Developer)  
**Project:** Early Health Disease Prediction using AI Chatbot (NLP-Based) for Hadoti & Marwari Language  
**Session:** 2026–2027 | Department of Computer Science & Engineering (Data Science), SKIT Jaipur  

---

## 📌 Executive Summary

This module implements **Sprint 4 (NLP Processing)**. Its objective is to bridge the linguistic gap between raw, colloquial doctor-patient speech transcripts (recorded in regional Rajasthani dialects—**Hadoti** and **Marwari**) and standardized medical clinical features needed for disease prediction.

Because standard clinical NER tools (e.g., BioBERT, standard spaCy) are trained exclusively on English or formal Hindi and fail on regional dialect terms (such as *ताप आ रय्यो है*, *गलो घणो दुके*, *उल्टी जेसो*, *पिशाब में जलन*), this module utilizes a **Hybrid Transformer + Regional Knowledge Engine** architecture.

---

## 🏗️ Architecture & Data Flow

```text
[Raw Voice Transcripts]
(Hadoti: 31 files | Marwari: 149 files)
                │
                ▼
┌───────────────────────────────────────────────┐
│           Regional NLP Engine                 │
│  1. Text Normalization & Dialect Detection    │
│  2. Multilingual Transformer Contextualizer   │
│  3. Hadoti & Marwari Dialect Clinical Lexicon │
│  4. Regex-based Duration & Severity Extractor │
└──────────────────────┬────────────────────────┘
                       │
                       ▼
        [Extracted Clinical Entities]
   • Standardized Symptoms (e.g., Fever, Cough, Sore Throat)
   • Affected Body Parts (e.g., Throat, Head, Abdomen)
   • Severity Level (Severe, Moderate, Mild)
   • Duration of illness (e.g., "दो दिन सु")
   • Clinical Synthesis Summary
                       │
                       ▼
        [Structured Output Datasets]
   ├── Data/Processed/processed_symptoms.csv  (For Sprint 5 ML Model)
   └── Data/Processed/processed_symptoms.json (Full JSON Entity Metadata)
```

---

## 📂 File Structure & Descriptions

| File Name | Description & Role |
| :--- | :--- |
| **`dialect_lexicon.py`** | Comprehensive regional medical dictionary mapping colloquial Hadoti and Marwari expressions, anatomical terms, severity modifiers, and dialectal stopwords to standardized clinical terms. |
| **`transformer_pipeline.py`** | Transformer module leveraging multilingual representations (e.g., MuRIL / IndicBERT) for semantic contextualization and intent representation. |
| **`symptom_extractor.py`** | The core extraction class (`RegionalSymptomExtractor`) which runs text normalization, dialect classification, symptom identification, severity ranking, and duration extraction. |
| **`process_all_transcripts.py`** | Batch processing script that automatically ingests all transcripts from `Data/Transcripts/Hadoti/hadoti_transcripts.csv` and `Data/Transcripts/Marwari/marwari_transcripts.csv`, runs extraction, and saves both CSV and JSON datasets. |

---

## 🚀 How to Run the NLP Pipeline

To re-run or test the complete extraction process from the repository root:

```bash
# Navigate to the repository root
# Navigate to repository root

# Execute the batch extraction script
python Source/nlp_processing/process_all_transcripts.py
```

---

## 📊 Output Deliverables for Sprint 5 (Disease Prediction)

1. **`Data/Processed/processed_symptoms.csv`**:
   * Formatted with UTF-8 BOM (`utf-8-sig`) so it displays Devanagari characters cleanly in Microsoft Excel.
   * Contains tabular columns: `filename`, `gender`, `source_dataset`, `detected_dialect`, `symptoms_count`, `extracted_symptoms`, `affected_body_parts`, `severity_level`, `duration`, `clinical_summary`, `raw_transcript`.
   * **Ready for Team Leader (Rohit Kumar)** to train the Scikit-learn disease classification model in **Sprint 5**.

2. **`Data/Processed/processed_symptoms.json`**:
   * Structured JSON containing complete metadata, entity lists, and nested attributes for future web chatbot API integration.
