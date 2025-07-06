import streamlit as st
import requests
import pandas as pd

API_URL = 'http://localhost:8000'

def analytics_by_month_tab():
    response = requests.get(f'{API_URL}/analytics/month/')
    response = response.json()

    months = [category["month"] for category in response]
    amounts = [category["total_amount"] for category in response]

    df = pd.DataFrame({
        'Month': months,
        'Amount': amounts
    })

    df_sorted = df.sort_values(by='Amount', ascending=True, ignore_index=True)

    st.markdown("<h3 style='color:#6A5ACD;'>Monthly Expense Overview</h3>", unsafe_allow_html=True)
    st.bar_chart(data=df_sorted.set_index("Month")["Amount"], use_container_width=True)

    df_sorted['Amount'] = df_sorted['Amount'].map('{:.2f}'.format)
    st.dataframe(df_sorted, use_container_width=True)
