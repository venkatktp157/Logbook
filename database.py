# database.py
import sqlite3
import pandas as pd
import streamlit as st
from config import ALL_KEYS, DB_NAME


def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    # 1. Create table if it doesn't exist
    columns_sql = ", ".join([f"{key} REAL" for key in ALL_KEYS])
    c.execute(f"CREATE TABLE IF NOT EXISTS logs (log_date TEXT PRIMARY KEY, {columns_sql})")
    
    # 2. Check for missing columns (Migration)
    c.execute("PRAGMA table_info(logs)")
    existing_columns = [info[1] for info in c.fetchall()]
    
    for key in ALL_KEYS:
        if key not in existing_columns:
            try:
                c.execute(f"ALTER TABLE logs ADD COLUMN {key} REAL DEFAULT 0.0")
                st.info(f"Detected new parameter: {key}. Updating database...")
            except Exception as e:
                st.error(f"Error adding column {key}: {e}")
                
    conn.commit()
    conn.close()

def save_to_db(selected_date):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM logs WHERE log_date = ?", (str(selected_date),))
    existing_row = c.fetchone()
    column_names = [description[0] for description in c.description]
    
    current_data = dict(zip(column_names, existing_row)) if existing_row else {k: 0.0 for k in ALL_KEYS}
    current_data["log_date"] = str(selected_date)

    for k in ALL_KEYS:
        if st.session_state[k] != 0.0:
            current_data[k] = st.session_state[k]
    
    columns = ", ".join(current_data.keys())
    placeholders = ", ".join(["?"] * len(current_data))
    sql = f"INSERT OR REPLACE INTO logs ({columns}) VALUES ({placeholders})"
    
    try:
        c.execute(sql, list(current_data.values()))
        conn.commit()
        st.toast(f"Entry for {selected_date} updated!", icon="💾")
    except Exception as e:
        st.error(f"Error: {e}")
    finally:
        conn.close()

def get_all_data_df():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM logs ORDER BY log_date DESC", conn)
    conn.close()
    return df


# database.py

def delete_record(log_date=None, purge_all=False):
    """
    Handles both specific deletion and full purge.
    """
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        if purge_all:
            c.execute("DELETE FROM logs")
            message = "Entire database cleared!"
        else:
            c.execute("DELETE FROM logs WHERE log_date = ?", (str(log_date),))
            message = f"Record for {log_date} deleted."
        
        conn.commit()
        st.toast(message, icon="🗑️")
    except Exception as e:
        st.error(f"Database error: {e}")
    finally:
        conn.close()