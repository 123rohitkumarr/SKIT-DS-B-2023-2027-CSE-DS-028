# Early Health Disease Prediction using AI Chatbot (NLP-Based) for Hadoti & Marwari Language

[![Project Status](https://img.shields.io/badge/Project_Stage-Sprint_4_NLP_Completed-brightgreen.svg)]()
[![Academic Session](https://img.shields.io/badge/Academic_Session-2026--2027-blue.svg)]()
[![Institution](https://img.shields.io/badge/Institution-SKIT_Jaipur-orange.svg)]()
[![Department](https://img.shields.io/badge/Department-CSE_(Data_Science)-purple.svg)]()
[![SDG](https://img.shields.io/badge/SDG_Mapping-SDG--3_Good_Health-red.svg)]()

An academic research and development project focused on developing an AI-driven, speech-enabled medical chatbot capable of understanding colloquial symptoms in **Hadoti** and **Marwari** (two major regional dialects of Rajasthan, India) and predicting potential health conditions with clinical severity assessment.

---

## 📌 Academic Metadata & Institutional Profile

* **Project ID:** `SKIT/DS/2023-2027/CSE-F-102`
* **Document Reference:** Form-1 (Abstract) & Form-2 (Roles & Responsibilities)
* **Institution:** Swami Keshvanand Institute of Technology, Management & Gramothan (SKIT), Jaipur
* **Department:** Department of Computer Science & Engineering
* **Specialization:** Computer Science and Engineering (Data Science)
* **Section:** B | **Session:** 2026–2027
* **Lab Coordinator:** Mr. Sumit Kumar
* **Project Mentor / Verified By:** Richa Sharma (Approved: 12/09/2026)
* **Project Track:** R&D Innovation *(Approved)*
* **Mandatory External Evaluation:** Research Paper Publication *(Approved)*
* **SDG Mapping:** **SDG-3: Good Health and Well-being**

---

## 👥 Team Members & Responsibilities (Form-2)

| Team Member | Role | Mobile | Core Technical Domain | Primary Assigned Sprints |
| :--- | :--- | :---: | :--- | :--- |
| **Rohit Kumar** | **Team Leader** | 6261551154 | Machine Learning, AI Development | Sprint 1 (Hadoti Voice Collection), Sprint 2 (Data Cleaning & Quality), Sprint 5 & 6 (Disease Prediction ML & Chatbot), Sprint 8 & 9 (Model Integration & Evaluation), Sprint 10 (System Testing & Deployment) |
| **Sandeep Yadav** | **Developer** | 7689979976 | NLP, Backend Development | Sprint 3 (Audio Transcription), Sprint 4 (NLP Processing & Extraction), Sprint 5 (Symptom-based Disease Prediction), Sprint 6 & 9 (Response Optimization), Sprint 10 (Backend & Integration Testing) |
| **Saurav Singh Tanwar** | **Developer** | 6283587760 | Frontend & UI/UX Development | Sprint 1 (Marwari Voice Collection), Sprint 2 (Data Cleaning & Organization), Sprint 7 (UI/UX Development with React & Tailwind), Sprint 10 (UI Usability & User Flow Testing) |

---

## 🎯 Problem Statement & Objectives (Form-1)

### Problem Statement
1. **Linguistic Accessibility Barrier:** Rural populations in Rajasthan face immense difficulties accessing timely healthcare guidance because digital healthcare tools are unavailable in their local languages.
2. **Dialect Exclusion in Existing AI:** Prevailing healthcare chatbots support only English or formal Hindi, failing to comprehend regional idioms, colloquial symptom expressions, and dialectal nuances (*ताप आ रय्यो है*, *गलो घणो दुके*, *उल्टी जेसो मन*, *पिशाब में जलन*).
3. **Proposed AI Solution:** A hybrid speech-processing and regional NLP framework that transcribes local spoken dialects, maps colloquial terms to clinical features, and predicts possible diseases to assist rural patients.

### Core Objectives
1. Collect, structure, and curate authentic Hadoti and Marwari voice recordings from male and female speakers.
2. Develop acoustic and speech-to-text preprocessing pipelines to generate high-fidelity transcripts.
3. Build a regional clinical NLP engine integrating dialect lexicons and multilingual transformer representations for symptom, severity, and duration extraction.
4. Train disease classification models using Scikit-learn for early diagnostic guidance.
5. Deploy a simple, accessible React.js/Tailwind CSS frontend interface for rural user communities.

---

## 🛠️ Technology Stack (Form-1)

| Layer / Subsystem | Name of Tool / Technology | Type | Purpose of Use |
| :--- | :--- | :---: | :--- |
| **Frontend UI/UX** | **React.js, Tailwind CSS, Figma** | Software | Responsive, user-friendly interface design tailored for rural accessibility |
| **Speech & Core Dev** | **Python, Whisper** | Software | Core backend development, audio preprocessing, and speech-to-text |
| **NLP & Language** | **Transformers (MuRIL / IndicBERT), NLP** | Software | Dialect contextualization, entity recognition, and clinical symptom extraction |
| **Machine Learning** | **Scikit-learn, SQLite** | Software | Disease classification model training/validation and structured data storage |
| **CI/CD & Reporting** | **GitHub Actions, ReportLab, Matplotlib** | Software | Automated weekly Form-3 academic progress report compilation |

---

## 📅 10 Proposed Project Sprints (Form-1 & Form-2)

```text
Aug 2026       Sep 2026       Oct 2026       Nov 2026       Dec 2026       Jan 2027       Feb 2027       Mar 2027
   │              │              │              │              │              │              │              │
   ▼              ▼              ▼              ▼              ▼              ▼              ▼              ▼
[Sprint 1] ──► [Sprint 2] ──► [Sprint 3] ──► [Sprint 4] ──► [Sprint 5] ──► [Sprint 6-7] ─► [Sprint 8-9] ─► [Sprint 10]
Voice Data     Data Cleaning   Audio          NLP Symptom    Disease        Chatbot & UI   Integration    Deployment
Collection     & Organization  Transcription  Extraction     Prediction     Development    & Evaluation   & Testing
```

| Sprint | Timeline | Sprint Name | Primary Owner | User Story / Deliverables | Status |
| :---: | :---: | :--- | :--- | :--- | :---: |
| **1** | 01/08/26 – 20/08/26 | **Data Collection** | Rohit Kumar, Saurav Singh Tanwar | Collect Hadoti & Marwari voice samples across male and female speakers. | ✅ Completed |
| **2** | 21/08/26 – 10/09/26 | **Data Cleaning & Organization** | Rohit Kumar, Saurav Singh Tanwar | Preprocess and clean voice data; check audio quality; structure datasets. | ✅ Completed |
| **3** | 11/09/26 – 30/09/26 | **Audio Transcription** | Sandeep Yadav | Convert voice recordings into text transcripts and generate structured CSVs. | ✅ Completed |
| **4** | 01/10/26 – 20/10/26 | **NLP Processing** | Sandeep Yadav | Extract clinical symptoms, severity, and duration using regional NLP engine. | ✅ Completed |
| **5** | 21/10/26 – 15/11/26 | **Disease Prediction** | Rohit Kumar, Sandeep Yadav | Develop and train ML model (Scikit-learn) predicting diseases from symptoms. | 🔄 Next Sprint |
| **6** | 16/11/26 – 10/12/26 | **Chatbot Development** | Rohit Kumar | Develop AI chatbot communicating with users and generating guidance responses. | 📅 Scheduled |
| **7** | 11/12/26 – 05/01/27 | **UI/UX Development** | Saurav Singh Tanwar | Design and develop simple, accessible React.js/Tailwind CSS frontend interface. | 📅 Scheduled |
| **8** | 06/01/27 – 31/01/27 | **Chatbot & Model Integration** | Rohit Kumar, Sandeep Yadav | Integrate NLP extraction, disease prediction, and voice processing pipelines. | 📅 Scheduled |
| **9** | 01/02/27 – 20/02/27 | **Model Evaluation & Response Optimization** | Rohit Kumar, Sandeep Yadav | Evaluate with Accuracy, Precision, Recall, F1-Score; optimize bot responses. | 📅 Scheduled |
| **10** | 21/02/27 – 15/03/27 | **System Testing & Deployment** | All Members | Perform integration, usability, and performance testing; final deployment. | 📅 Scheduled |

---

## 📂 Repository Structure

The repository is structured strictly according to **Form 1** and **Form 2** specifications:

```text
SKIT-DS-B-2023-2027-CSE-DS-028/
│
├── .github/
│   └── workflows/
│       └── auto_weekly_report.yml               # Automated Form-3 weekly PDF reporting workflow
│
├── docs/                                        # Project Documentation & Academic Governance
│   ├── academic_forms/                          # Official academic evaluation forms
│   │   ├── Form-1_Project_Abstract.md           # Form-1: Project Abstract, Tech Stack, 10 Sprints
│   │   ├── Form-2_Roles_and_Responsibilities.md # Form-2: Team Member Sprint Allocations & Timelines
│   │   └── Form-3_Weekly_Progress_Reports.md    # Form-3: Weekly Progress Report mechanism & index
│   └── recording_guidelines/                    # Voice recording scripts and speaker instructions
│       ├── Marwari_Audio_Recording_Script_Hindi.docx
│       ├── Marwari_Audio_Recording_Script_Hindi.md
│       └── Marwari_Audio_Recording_Script_Hindi.pdf
│
├── Data/                                        # Datasets organized by Sprint and Dialect
│   ├── Audio/                                   # SPRINT 1: Voice Sample Collection
│   │   ├── Hadoti/                              # Hadoti Audio Corpus (Rohit Kumar)
│   │   │   ├── Female/                          # 11 Female audio files (F1 (1).m4a ... F1 (21).m4a)
│   │   │   └── Male/                            # 20 Male audio/video files (M1.m4a ... M20.mp4)
│   │   └── Marwari/                             # Marwari Audio Corpus (Saurav Singh Tanwar)
│   │       ├── Female/                          # 121 Female audio files (MF1.mpeg ... MF121.ogg)
│   │       └── Male/                            # 28 Male audio files (MM1.ogg ... MM28.ogg)
│   │
│   ├── Transcripts/                             # SPRINT 2 & 3: Audio Transcription & Datasets
│   │   ├── Hadoti/                              # Hadoti Transcripts (Sandeep Yadav & Rohit Kumar)
│   │   │   ├── F1.txt ... F11.txt               # 11 Individual female transcript text files
│   │   │   ├── M1.txt ... M20.txt               # 20 Individual male transcript text files
│   │   │   ├── statistics.txt                   # Hadoti corpus audio & transcript statistics
│   │   │   └── hadoti_transcripts.csv           # Consolidated Hadoti tabular dataset (31 rows)
│   │   └── Marwari/                             # Marwari Transcripts (Sandeep Yadav & Saurav Singh)
│   │       ├── MF1.txt ... MF121.txt            # 121 Individual female transcript text files
│   │       ├── MM1.txt ... MM28.txt             # 28 Individual male transcript text files
│   │       └── marwari_transcripts.csv          # Consolidated Marwari tabular dataset (149 rows)
│   │
│   ├── Processed/                               # SPRINT 4: Regional NLP Extraction Outputs
│   │   ├── processed_symptoms.csv               # 180 Standardized clinical records (UTF-8 BOM)
│   │   └── processed_symptoms.json              # Full structured entity metadata for Sprint 5 ML
│   │
│   └── MF_audio_data/                           # Preserved audio dataset (User approved retention)
│       └── [121 audio files]
│
├── Source/                                      # Source Code & Algorithms by Sprint / Module
│   ├── data_processing/                         # SPRINT 2 & 3: Audio Transcription Processing
│   │   └── generate_transcripts_csv.py          # Generates consolidated Hadoti transcripts CSV
│   └── nlp_processing/                          # SPRINT 4: Regional NLP Engine (Sandeep Yadav)
│       ├── __init__.py
│       ├── dialect_lexicon.py                   # Regional medical lexicon & colloquial mapping
│       ├── symptom_extractor.py                 # Core RegionalSymptomExtractor engine
│       ├── transformer_pipeline.py              # Multilingual transformer pipeline
│       ├── process_all_transcripts.py           # Batch processing ingestion & export script
│       └── README.md                            # Detailed Sprint 4 architecture documentation
│
├── weekly_reports/                              # Academic Evaluation Archives (Form-3 PDFs)
│   ├── SKIT-DS-B-2023-2027-CSE-DS-028_Weekly_Progress_Report_Form-3_2026-09-24.pdf
│   ├── SKIT-DS-B-2023-2027-CSE-DS-028_Weekly_Progress_Report_Form-3_2026-10-10.pdf
│   ├── SKIT-DS-B-2023-2027-CSE-DS-028_Weekly_Progress_Report_Form-3_2026-10-15.pdf
│   └── SKIT-DS-B-2023-2027-CSE-DS-028_Weekly_Progress_Report_Form-3_2026-10-22.pdf
│
├── generate_report.py                           # Automated Weekly Form-3 Report Generator
└── README.md                                    # Master Project Documentation
```

---

## 🚀 Execution & Verification Guide

### 1. Re-generate Hadoti Transcripts Dataset (Sprint 2/3)
To re-compile individual text transcripts from `Data/Transcripts/Hadoti/` into `hadoti_transcripts.csv`:
```bash
python Source/data_processing/generate_transcripts_csv.py
```

### 2. Run Regional NLP Symptom Extraction Pipeline (Sprint 4)
To batch process all 180 transcripts (31 Hadoti + 149 Marwari) through the NLP engine and export clinical datasets:
```bash
python Source/nlp_processing/process_all_transcripts.py
```
*Outputs generated in `Data/Processed/`:*
* `Data/Processed/processed_symptoms.csv` (180 clinical feature vectors for Sprint 5 ML training)
* `Data/Processed/processed_symptoms.json` (Structured JSON entities)

### 3. Generate Academic Weekly Progress Report (Form-3)
To generate the latest weekly progress report with commit analytics and mentor evaluation tables:
```bash
python generate_report.py weekly
```

---

## 📑 Governance & Academic Documentation Links

* [Form-1: Project Abstract & Sprints](file:///docs/academic_forms/Form-1_Project_Abstract.md)
* [Form-2: Roles & Responsibilities of Team Members](file:///docs/academic_forms/Form-2_Roles_and_Responsibilities.md)
* [Form-3: Weekly Progress Reports Framework](file:///docs/academic_forms/Form-3_Weekly_Progress_Reports.md)
* [Audio Recording Script & Speaker Guidelines](file:///docs/recording_guidelines/Marwari_Audio_Recording_Script_Hindi.md)
* [Sprint 4 NLP Engine Documentation](file:///Source/nlp_processing/README.md)
