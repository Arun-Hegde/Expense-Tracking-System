import streamlit as st
from datetime import datetime
import requests

API_URL = 'http://localhost:8000'

def add_update_tab():
    selected_date = st.date_input('', datetime(2024, 8, 1), label_visibility='collapsed')
    response = requests.get(f'{API_URL}/expenses/{selected_date}')
    if response.status_code == 200:
        existing_expenses = response.json()
    else:
        st.error('Failed To Retrieve')
        existing_expenses = []

    categories = ['Rent', 'Food', 'Shopping', 'Entertainment', 'Other']

    st.markdown("<h3 style='color:#6A5ACD;'>Enter Expenses</h3>", unsafe_allow_html=True)

    with st.form(key='expense_form'):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<b>Amount</b>", unsafe_allow_html=True)
        with col2:
            st.markdown("<b>Category</b>", unsafe_allow_html=True)
        with col3:
            st.markdown("<b>Notes</b>", unsafe_allow_html=True)

        expenses = []

        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i]['amount']
                category = existing_expenses[i]['category']
                notes = existing_expenses[i]['notes']
            else:
                amount = 0.0
                category = 'Other'
                notes = ''

            col1, col2, col3 = st.columns(3)
            with col1:
                number_input = st.number_input('', min_value=0.0, step=1.0, value=amount, key=f'Amount_{i}', label_visibility='collapsed')
            with col2:
                category_input = st.selectbox('', options=categories, index=categories.index(category), key=f'Category_{i}', label_visibility='collapsed')
            with col3:
                notes_input = st.text_input('', value=notes, key=f'Notes_{i}', label_visibility='collapsed')

            expenses.append({
                'amount': number_input,
                'category': category_input,
                'notes': notes_input
            })

        submit_button = st.form_submit_button("Save Expenses")
        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]
            post_response = requests.post(f'{API_URL}/expenses/{selected_date}/add', json=filtered_expenses)
            if post_response.status_code == 200:
                st.success('Expenses Updated Successfully')
            else:
                st.error('Failed To Update')
