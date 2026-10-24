"""
Batch Processing Pipeline for Hadoti & Marwari Transcripts
==========================================================
Sprint 4: NLP Processing
Developer: Sandeep Yadav (NLP & Backend Developer)
Project: Early Health Disease Prediction using AI Chatbot (NLP-Based)
Department of CSE (Data Science), SKIT Jaipur

Purpose:
--------
Automates the batch ingestion of all Hadoti (31 records) and Marwari (149 records)
speech transcripts, runs the RegionalSymptomExtractor engine, and exports the 
standardized clinical datasets (Data/processed_symptoms.csv & Data/processed_symptoms.json)
required for Sprint 5 (Disease Prediction).
"""

import os
import sys
import json
import pandas as pd

# Ensure UTF-8 output on Windows terminal
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from symptom_extractor import RegionalSymptomExtractor

REPO_DIR = r"C:\Users\sande\Desktop\SKIT-DS-B-2023-2027-CSE-DS-028"
DATA_DIR = os.path.join(REPO_DIR, "Data")

HADOTI_CSV = os.path.join(DATA_DIR, "hadoti_transcripts.csv")
MARWARI_CSV = os.path.join(DATA_DIR, "marwari_transcripts.csv")

OUTPUT_CSV = os.path.join(DATA_DIR, "processed_symptoms.csv")
OUTPUT_JSON = os.path.join(DATA_DIR, "processed_symptoms.json")

def main():
    print("=" * 60)
    print("STARTING SPRINT 4: REGIONAL NLP SYMPTOM PROCESSING")
    print("=" * 60)
    
    extractor = RegionalSymptomExtractor()
    all_processed_records = []
    
    # 1. Process Hadoti Transcripts
    if os.path.exists(HADOTI_CSV):
        print(f"Reading Hadoti transcripts from: {HADOTI_CSV}")
        df_hadoti = pd.read_csv(HADOTI_CSV)
        print(f"  -> Found {len(df_hadoti)} Hadoti records.")
        for _, row in df_hadoti.iterrows():
            transcript = str(row.get('transcript', '')).strip()
            if not transcript or transcript.lower() == 'nan':
                continue
            rec = extractor.process_transcript(
                text=transcript,
                filename=str(row.get('filename', '')),
                gender=str(row.get('gender', 'Unknown'))
            )
            # Tag dataset source
            rec["source_dataset"] = "Hadoti"
            all_processed_records.append(rec)
    else:
        print(f"Warning: Hadoti CSV not found at {HADOTI_CSV}")
        
    # 2. Process Marwari Transcripts
    if os.path.exists(MARWARI_CSV):
        print(f"\nReading Marwari transcripts from: {MARWARI_CSV}")
        df_marwari = pd.read_csv(MARWARI_CSV)
        print(f"  -> Found {len(df_marwari)} Marwari records.")
        for _, row in df_marwari.iterrows():
            transcript = str(row.get('transcript', '')).strip()
            if not transcript or transcript.lower() == 'nan':
                continue
            rec = extractor.process_transcript(
                text=transcript,
                filename=str(row.get('filename', '')),
                gender=str(row.get('gender', 'Unknown'))
            )
            # Tag dataset source
            rec["source_dataset"] = "Marwari"
            all_processed_records.append(rec)
    else:
        print(f"Warning: Marwari CSV not found at {MARWARI_CSV}")

    total_records = len(all_processed_records)
    print(f"\nSuccessfully processed total {total_records} regional transcripts!")

    # 3. Save JSON Output
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(all_processed_records, f, ensure_ascii=False, indent=2)
    print(f"[SUCCESS] Saved JSON dataset: {OUTPUT_JSON}")

    # 4. Prepare & Save CSV Output
    csv_rows = []
    for r in all_processed_records:
        csv_rows.append({
            "filename": r["filename"],
            "gender": r["gender"],
            "source_dataset": r["source_dataset"],
            "detected_dialect": r["detected_dialect"],
            "symptoms_count": r["symptoms_count"],
            "extracted_symptoms": "; ".join(r["extracted_symptoms"]),
            "affected_body_parts": "; ".join(r["affected_body_parts"]),
            "severity_level": r["severity_level"],
            "duration": r["duration"],
            "clinical_summary": r["clinical_summary"],
            "raw_transcript": r["raw_transcript"]
        })
        
    df_out = pd.DataFrame(csv_rows)
    df_out.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
    print(f"[SUCCESS] Saved CSV dataset: {OUTPUT_CSV}")

    # 5. Summary Statistics
    print("\n" + "=" * 60)
    print("NLP SYMPTOM EXTRACTION SUMMARY STATISTICS")
    print("=" * 60)
    
    # Symptom frequencies
    all_symptoms = []
    for r in all_processed_records:
        all_symptoms.extend(r["extracted_symptoms"])
    
    symptom_series = pd.Series(all_symptoms).value_counts()
    print("\nTop Detected Symptoms:")
    for sym, count in symptom_series.head(10).items():
        print(f"  • {sym:<30}: {count} occurrences")
        
    # Severity distribution
    print("\nSeverity Distribution:")
    for sev, count in df_out["severity_level"].value_counts().items():
        print(f"  • {sev:<15}: {count}")

    print("\n" + "=" * 60)
    print("SPRINT 4 NLP PROCESSING COMPLETED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    main()
