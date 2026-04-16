# main.py
import streamlit as st
from datetime import date
from config import ALL_KEYS
import database as db
import pages_content as ui

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
    st.Page(ui.page_ten, title="Boiler & EGB Parameters", icon="📊")
])

# --- SIDEBAR ---
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

# main.py sidebar

# log_date = st.date_input("Select Log Date", value=date.today())

# if st.button("📂 Load Data for this Date"):
#     existing_data = db.get_record_by_date(log_date)
#     if not existing_data.empty:
#         for key in ALL_KEYS:
#             st.session_state[key] = existing_data.iloc[0][key]
#         st.rerun()
#     else:
#         st.info("No data found for this date. Starting with empty inputs.")        

# main.py (Sidebar section)

with st.sidebar:
    st.divider()
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

pg.run()