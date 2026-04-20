import os
from datetime import datetime

NOTES_FILE = "engine_notes.txt"

def save_note(log_date, note_text):
    if note_text.strip():
        # Append note with date header
        with open(NOTES_FILE, "a") as f:
            f.write(f"DATE: {log_date}\n{note_text}\n{'-'*30}\n")
        return True
    return False

def read_notes():
    if not os.path.exists(NOTES_FILE):
        return "No notes found."
    with open(NOTES_FILE, "r") as f:
        return f.read()

def purge_notes():
    if os.path.exists(NOTES_FILE):
        os.remove(NOTES_FILE)

def delete_note_by_date(target_date):
    if not os.path.exists(NOTES_FILE):
        return
    
    date_str = f"DATE: {target_date}"
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    
    new_lines = []
    skip = False
    for line in lines:
        if line.strip() == date_str:
            skip = True
            continue
        if skip and line.startswith("---"):
            skip = False
            continue
        if not skip:
            new_lines.append(line)
            
    with open(NOTES_FILE, "w") as f:
        f.writelines(new_lines)

def get_filtered_notes(start_date, end_date):
    """Returns a string of notes between two dates (inclusive)."""
    if not os.path.exists(NOTES_FILE):
        return ""
    
    with open(NOTES_FILE, "r") as f:
        content = f.read()
    
    # Split by the separator to get individual note blocks
    blocks = content.split("-" * 30)
    filtered_blocks = []
    
    for block in blocks:
        block = block.strip()
        if not block:
            continue
            
        try:
            # Extract date from "DATE: YYYY-MM-DD"
            first_line = block.split('\n')[0]
            date_str = first_line.replace("DATE: ", "").strip()
            note_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            
            if start_date <= note_date <= end_date:
                filtered_blocks.append(block)
        except (ValueError, IndexError):
            continue # Skip malformed blocks
            
    return ("\n" + "-" * 30 + "\n").join(filtered_blocks)        