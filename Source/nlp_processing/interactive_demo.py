"""
Live Interactive Demo for Sprint 4 (NLP Processing)
===================================================
Developer: Sandeep Yadav (NLP & Backend Developer)
Project: Early Health Disease Prediction using AI Chatbot (NLP-Based)
Department of CSE (Data Science), SKIT Jaipur

Purpose:
--------
Allows real-time interactive testing of patient utterances in Hadoti & Marwari dialects.
Extracts clinical symptoms, anatomical body parts, severity, and duration on-the-fly.
"""

import sys
import os

# Ensure UTF-8 console output
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Add parent directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from symptom_extractor import RegionalSymptomExtractor

def print_result(result):
    print("\n" + "=" * 55)
    print("             LIVE CLINICAL NLP ANALYSIS")
    print("=" * 55)
    print(f"Input Text         : {result['raw_transcript']}")
    print(f"Detected Dialect   : {result['detected_dialect']}")
    print(f"Extracted Symptoms : {', '.join(result['extracted_symptoms']) if result['extracted_symptoms'] else 'None detected'}")
    print(f"Symptoms Count     : {result['symptoms_count']}")
    print(f"Affected Body Parts: {', '.join(result['affected_body_parts']) if result['affected_body_parts'] else 'None'}")
    print(f"Severity Level     : {result['severity_level']}")
    print(f"Duration of Illness: {result['duration']}")
    print(f"Clinical Summary   : {result['clinical_summary']}")
    print("=" * 55 + "\n")

def main():
    extractor = RegionalSymptomExtractor()
    
    print("\n" + "#" * 60)
    print("  HADOTI & MARWARI HEALTH CHATBOT - NLP PROCESSING DEMO")
    print("  Developer: Sandeep Yadav (NLP & Backend Developer)")
    print("#" * 60)
    
    # If passed as command line argument
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
        res = extractor.process_transcript(user_input)
        print_result(res)
        return

    print("\nSelect an option:")
    print("1. Test with Pre-built Sample (Hadoti)")
    print("2. Test with Pre-built Sample (Marwari)")
    print("3. Enter your own sentence live (Hindi / Hadoti / Marwari)")
    print("4. Exit")
    
    choice = input("\nEnter choice (1/2/3/4) [Default 1]: ").strip()
    
    if choice == "2":
        sample = "डॉक्टर साहब, कल सू गलो घणो दुके है और तेज बुखार आ रय्यो है, तीन दिन सूं परेशान हूँ।"
    elif choice == "3":
        sample = input("\nEnter patient utterance: ").strip()
        if not sample:
            sample = "मने दो दिन सूं घणो तेज ताप आ रय्यो है और पेट में मरोड़ उठ रिया है।"
    elif choice == "4":
        return
    else:
        sample = "मारो नाम सुरेश है। मने घणी बुखार आ रही है, माथो भी दुक्रियो है और बदन भी गणो दर्द कर रह्यो है तीन दिन सूं।"
        
    res = extractor.process_transcript(sample)
    print_result(res)

if __name__ == "__main__":
    main()
