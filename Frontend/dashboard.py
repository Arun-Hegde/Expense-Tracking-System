import streamlit as st
import requests
import pandas as pd

API_URL = 'http://localhost:8000'

def dashboard_tab():
    st.subheader("📈 Expense Summary Dashboard")

    try:
        response_month = requests.get(f'{API_URL}/analytics/month/').json()
        df_month = pd.DataFrame(response_month)
    except:
        st.error("Failed to fetch monthly analytics.")
        return

    try:
        response_cat = requests.post(f'{API_URL}/analytics/category/', json={
            'start_date': '2024-08-01',
            'end_date': '2024-08-31'
        }).json()

        df_cat = pd.DataFrame({
            'Category': list(response_cat.keys()),
            'Total': [response_cat[c]['total'] for c in response_cat],
            'Percentage': [response_cat[c]['percentage'] for c in response_cat]
        })
    except:
        st.error("Failed to fetch category analytics.")
        return

    budget = st.number_input("Set Monthly Budget (₹)", min_value=0, value=10000, step=500)
    total_expense = df_month['total_amount'].sum()

    if total_expense > budget:
        st.warning(f"⚠️ You have exceeded your budget! Spent ₹{total_expense:.2f} out of ₹{budget}")
    else:
        st.success(f"✅ You are within your budget. Spent ₹{total_expense:.2f} out of ₹{budget}")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("💸 Total Spent", f"₹{total_expense:.2f}")
    with col2:
        top_month = df_month.loc[df_month['total_amount'].idxmax()]['month']
        st.metric("📅 Highest Spending Month", top_month)
    with col3:
        top_category = df_cat.loc[df_cat['Total'].idxmax()]['Category']
        st.metric("🏆 Top Category", top_category)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("### 📊 Monthly Trends")
    df_month_sorted = df_month.sort_values(by="month")
    st.line_chart(data=df_month_sorted.set_index("month")["total_amount"], use_container_width=True)

    st.markdown("### 🧮 Category-wise Distribution")
    st.bar_chart(data=df_cat.set_index("Category")["Percentage"], use_container_width=True)