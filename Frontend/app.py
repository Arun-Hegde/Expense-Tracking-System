import streamlit as st
from add_update import add_update_tab
from analytics_by_category import analytics_by_category_tab
from analytics_by_month import analytics_by_month_tab
from dashboard import dashboard_tab

st.set_page_config(page_title="Expense Tracker", layout="wide")
st.markdown("""
    <h1 style='text-align: center; color: #4B8BBE;'>💰 Expense Management System</h1>
    <hr style='border: 1px solid #4B8BBE;'>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs([
    "➕ Add/Update",
    "📊 Analytics By Category",
    "📅 Analytics By Month",
    "📈 Dashboard"
])

with tab1:
    add_update_tab()
with tab2:
    analytics_by_category_tab()
with tab3:
    analytics_by_month_tab()
with tab4:
    dashboard_tab()
