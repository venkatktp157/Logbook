# main.py
import streamlit as st
from datetime import date
from config import ALL_KEYS
import database as db
import pages_content as ui
import notes_manager as nm  # Import the new manager
from database import reset_testing_db


# --- CONFIGURATION ---
st.set_page_config(layout='wide', page_title="Engine Data Logger")

# Initialize DB and Session State
db.init_db()
for key in ALL_KEYS:
    if key not in st.session_state:
        st.session_state[key] = 0.0

# --- NAVIGATION ---
pg = st.navigation([
    st.Page(ui.page_one, title="ME parameters 1", icon="📊"),
    st.Page(ui.page_two, title="ME parameters 2", icon="📊"),
    st.Page(ui.page_three, title="ME parameters 3", icon="📊"),
    st.Page(ui.page_four, title="ME parameters 4", icon="📊"),
    st.Page(ui.page_five, title="ME parameters 5", icon="📊"),
    st.Page(ui.page_six, title="LNG Parameters", icon="📊"),
    st.Page(ui.page_seven, title="AE Parameters 1", icon="📊"),
    st.Page(ui.page_eight, title="AE Parameters 2", icon="📊"), 
    st.Page(ui.page_nine, title="Other Parameters", icon="📊"),
    st.Page(ui.page_ten, title="Boiler & EGB Parameters", icon="📊"),
    st.Page(ui.page_eleven, title="Navigation Parameters", icon="📊"),
    st.Page(ui.page_twelve, title="CPP Common Parameters", icon="📊"),
    st.Page(ui.page_thirteen, title="Wartsila CPP parameters", icon="📊"),
    st.Page(ui.page_fourteen, title="KAMEWA CPP Parameters", icon="📊"),
    st.Page(ui.page_fifteen, title="Ref. AC, FW Generator", icon="📊"),
    st.Page(ui.page_sixteen, title="Tank Levels & Temps", icon="📊")    
])

# # --- SIDEBAR PARAMETER INPUTS---
with st.sidebar:
    st.header("📅 Data Management")
    log_date = st.date_input("Select Log Date", value=date.today())
    
    if st.button("💾 Save All Data to DB", use_container_width=True, type="primary"):
        db.save_to_db(log_date)

    st.divider()
    full_df = db.get_all_data_df()
    
    if not full_df.empty:
        csv = full_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Historical CSV", data=csv, 
                           file_name=f"Engine_Report_{date.today()}.csv", mime='text/csv')
        if st.checkbox("Show Database Preview"):
            st.dataframe(full_df)

    if st.button("🗑️ Clear Current Inputs", use_container_width=True):
        for key in ALL_KEYS:
            st.session_state[key] = 0.0
        st.rerun()

    # delete specific day records or purge all records
    with st.expander("🛠️ Advanced Database Tools"):
        
        # Section 1: Specific Delete
        st.write("---")
        target_date = st.date_input("Target Date", value=date.today(), key="target")
        if st.button("Delete Specific Day", use_container_width=True):
            db.delete_record(log_date=target_date)
            st.rerun()

        # Section 2: Full Purge
        st.write("---")
        st.warning("Warning: This cannot be undone.")
        confirm = st.checkbox("Confirm Full Purge")
        if st.button("🔥 Purge All Data", use_container_width=True, disabled=not confirm, type="primary"):
            db.delete_record(purge_all=True)
            st.rerun()       

# # --- SIDEBAR NOTES MANAGEMENT ---
# --- Notes Section in Sidebar ---
with st.sidebar:
    st.divider()
    st.header("📝 Logbook Notes")
    
    # 1. Save New Note
    note_text = st.text_area("Enter your note here:", key="current_note_input")
    if st.button("💾 Save Note", use_container_width=True):
        if nm.save_note(log_date, note_text):
            st.success(f"Note saved for {log_date}!")
            st.rerun() # Refresh to clear the text area
        else:
            st.warning("Please enter some text before saving.")
    
    # 2. Toggle View Checkbox
    show_notes = st.checkbox("📖 View Historical Notes")
    
    if show_notes:
        notes_content = nm.read_notes()
        # Using height=400 to make it easier to read on a large screen
        st.text_area("Logbook History:", value=notes_content, height=400, disabled=True)

    
    # download filtered notes
    # st.divider()
    with st.expander("📥 Export/Download Notes"):
        st.write("Filter by Date Range")
        col_a, col_b = st.columns(2)
        with col_a:
            start_filter = st.date_input("From", value=log_date, key="note_start")
        with col_b:
            end_filter = st.date_input("To", value=log_date, key="note_end")
        
        # Fetch the filtered content
        filtered_text = nm.get_filtered_notes(start_filter, end_filter)
        
        if filtered_text:
            st.download_button(
                label="💾 Download Filtered Notes (.txt)",
                data=filtered_text,
                file_name=f"Engine_Notes_{start_filter}_to_{end_filter}.txt",
                mime="text/plain",
                use_container_width=True
            )
        else:
            st.info("No notes found for this range.")    

        # 3. Targeted & Full Purge (Inside an expander to prevent accidents)
        with st.expander("🗑️ Delete/Purge Options"):
            st.subheader("Delete Specific Date")
            purge_date = st.date_input("Select Date to Purge", value=log_date, key="purge_date_picker")
            
            # if st.button("❌ Clear This Date", use_container_width=True):
            #     nm.delete_note_by_date(purge_date)
            #     st.toast(f"Notes for {purge_date} removed.", icon="🗑️")
            #     st.rerun()

            # st.divider()
            
            st.subheader("Full Reset")
            confirm_purge = st.checkbox("Confirm Purge All Notes")
            if st.button("🔥 Purge Everything", use_container_width=True, type="primary", disabled=not confirm_purge):
                nm.purge_notes()
                st.success("All notes wiped.")
                st.rerun()

# # Logic for Authorised Developer Tools  (uncomment for streamlit community cloud deployment)
with st.sidebar:
    st.divider()
    
    # Use an expander to keep the UI clean
    with st.expander("🛠️ Admin Access"):
        input_pass = st.text_input("Enter Developer Key", type="password")
        
        # Accessing the password from the secrets file
        if input_pass == st.secrets["DEV_PASSWORD"]:
            st.success("Access Granted")
            
            if st.button("♻️ Reset Database & Schema"):
                try:
                    reset_testing_db()
                    st.success("Database recreated successfully!")
                    # Use st.rerun() to refresh the UI with the new schema
                    st.rerun()
                except Exception as e:
                    st.error(f"Reset failed: {e}")
        
        elif input_pass != "":
            st.error("Incorrect Key")

# In main_page.py or wherever your sidebar logic lives  (for local running, comment out when deploying to streamlit community cloud to avoid exposing reset functionality to end users)
# import streamlit as st
# from database import reset_testing_db

# with st.sidebar:
#     st.divider()
#     st.subheader("Developer Tools")
#     if st.button("♻️ Reset Schema & Clear Data"):
#         reset_testing_db()
#         st.success("Database recreated using latest config.py!")
#         st.rerun() # Refresh the app to show the new structure

pg.run()