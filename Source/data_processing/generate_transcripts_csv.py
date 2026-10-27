import os
import csv

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))

def clean_transcript(text):
    text = text.strip()
    # Strip enclosing quotes if present (e.g., in M11-M20 files)
    if (text.startswith('"') and text.endswith('"')) or (text.startswith('“') and text.endswith('”')):
        text = text[1:-1].strip()
    return text

def generate_csv(output_paths, transcripts_dir=None):
    if transcripts_dir is None:
        transcripts_dir = os.path.join(REPO_DIR, 'Data', 'Transcripts', 'Hadoti')
        if not os.path.exists(transcripts_dir):
            transcripts_dir = os.path.join(REPO_DIR, 'Data', 'Hadoti_Transcripts')
    rows = []

    # Process Male voice transcripts (M1 to M20)
    for i in range(1, 21):
        txt_name = f"M{i}.txt"
        txt_path = os.path.join(transcripts_dir, txt_name)
        if not os.path.exists(txt_path):
            continue
        with open(txt_path, 'r', encoding='utf-8') as f:
            transcript = clean_transcript(f.read())
        audio_name = f"M{i}.m4a" if i <= 10 else f"M{i}.mp4"
        rows.append({
            'filename': audio_name,
            'gender': 'Male',
            'transcript': transcript
        })

    # Process Female voice transcripts (F1 to F11)
    for i in range(1, 12):
        txt_name = f"F{i}.txt"
        txt_path = os.path.join(transcripts_dir, txt_name)
        if not os.path.exists(txt_path):
            continue
        with open(txt_path, 'r', encoding='utf-8') as f:
            transcript = clean_transcript(f.read())
        audio_name = f"F{i}.m4a"
        rows.append({
            'filename': audio_name,
            'gender': 'Female',
            'transcript': transcript
        })

    # Write CSV to all target output paths with utf-8-sig (with BOM) and CRLF line terminators
    for out_path in output_paths:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['filename', 'gender', 'transcript'], lineterminator='\r\n')
            writer.writeheader()
            writer.writerows(rows)
        print(f"Generated {out_path} with {len(rows)} rows.")

if __name__ == '__main__':
    targets = [
        os.path.join(REPO_DIR, 'Data', 'Transcripts', 'Hadoti', 'hadoti_transcripts.csv'),
    ]
    generate_csv(targets)
