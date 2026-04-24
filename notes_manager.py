import sqlite3
import streamlit as st
from datetime import datetime

NOTES_DB = "engine_notes.db"

def init_notes_db():
    """Initializes the notes database and table."""
    conn = sqlite3.connect(NOTES_DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS engine_notes 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  note_date TEXT, 
                  content TEXT, 
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def save_note(log_date, note_text):
    """Saves a note to the SQLite database."""
    if note_text.strip():
        try:
            conn = sqlite3.connect(NOTES_DB)
            c = conn.cursor()
            c.execute("INSERT INTO engine_notes (note_date, content) VALUES (?, ?)", 
                      (str(log_date), note_text.strip()))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            st.error(f"Error saving note: {e}")
    return False

def read_notes():
    """Returns all notes formatted as a string for display."""
    conn = sqlite3.connect(NOTES_DB)
    c = conn.cursor()
    c.execute("SELECT note_date, content FROM engine_notes ORDER BY note_date DESC, timestamp DESC")
    rows = c.fetchall()
    conn.close()
    
    if not rows:
        return "No notes found in database."
    
    formatted_notes = ""
    for date, content in rows:
        formatted_notes += f"DATE: {date}\n{content}\n{'-'*30}\n"
    return formatted_notes

def get_filtered_notes(start_date, end_date):
    """Fetches notes between two dates for exporting."""
    conn = sqlite3.connect(NOTES_DB)
    c = conn.cursor()
    c.execute("SELECT note_date, content FROM engine_notes WHERE note_date BETWEEN ? AND ? ORDER BY note_date ASC", 
              (str(start_date), str(end_date)))
    rows = c.fetchall()
    conn.close()
    
    if not rows:
        return ""
    
    return "\n".join([f"DATE: {r[0]}\n{r[1]}\n{'-'*30}" for r in rows])

def delete_note_by_date(target_date):
    """Deletes all notes for a specific date."""
    conn = sqlite3.connect(NOTES_DB)
    c = conn.cursor()
    c.execute("DELETE FROM engine_notes WHERE note_date = ?", (str(target_date),))
    conn.commit()
    conn.close()

def purge_notes():
    """Deletes every entry in the notes table."""
    conn = sqlite3.connect(NOTES_DB)
    c = conn.cursor()
    c.execute("DELETE FROM engine_notes")
    conn.commit()
    conn.close()