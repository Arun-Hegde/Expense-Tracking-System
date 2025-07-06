import streamlit as st
import requests
import pandas as pd

API_URL = 'http://localhost:8000'

def analytics_by_month_tab():
    response = requests.get(f'{API_URL}/analytics/month/')
    response=response.json()

    months = [category["month"] for category in response]
    amounts = [category["total_amount"] for category in response]
    result={
        'Month' :months,
        'Amount':amounts
    }

    df = pd.DataFrame(result)
    df_sorted = df.sort_values(by='Amount', ascending=True,ignore_index=True)

    st.title('Expense Breakdown By Month')

    st.bar_chart(data=df_sorted.set_index("Month")['Amount'],width=0, height=0, use_container_width=24)
    df_sorted['Amount'] = df_sorted['Amount'].map('{:.2f}'.format)

    st.table(df_sorted)
