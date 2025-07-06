# 💸 Expense Management Tracking System

A simple, modular, and visually enhanced Python-based Expense Tracking System that helps users manage daily spending with category-wise analytics and budget monitoring. Useful for personal finance or as a base for advanced financial tools.

## 📌 Features

- Add, edit, and track daily expenses
- Categorize transactions (Rent, Food, Shopping, Entertainment, etc.)
- Monthly and category-wise analytics with charts
- Dashboard with budget alert system
- Streamlit-based interactive UI
- FastAPI backend with MySQL
- Modular code structure for easy scaling

## 🛠️ Technologies Used

- **Frontend:** Streamlit
- **Backend:** FastAPI, Pydantic
- **Database:** MySQL
- **Data Handling:** Pandas
- **Testing:** pytest

## 📁 Project Structure
```
Project-Expense-Tracking-System/
├── backend/
│   ├── server.py (FastAPI server)
│   ├── db_helper.py
│   ├── logging_setup.py
│   ├── server.log
├── frontend/
│   ├── app.py (Streamlit main UI)
│   ├── add_update.py
│   ├── analytics_by_category.py
│   ├── analytics_by_month.py
│   ├── dashboard.py
├── test/
│   ├── conftest.py
│   ├── backend/ test_db_helper.py
│   └── frontend/
├── Screenshots/
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- MySQL Server running locally or remotely

### Installation
```bash
git clone https://github.com/arunhegde_18/expense-tracker.git
cd Project-Expense-Tracking-System
pip install -r requirements.txt
```

### Starting the App
1. **Start Backend (FastAPI):**
```bash
uvicorn server:app --reload
```

2. **Start Frontend (Streamlit):**
```bash
cd frontend
streamlit run app.py
```

> ⚠️ Make sure to always run the frontend using `streamlit run app.py`, not `python app.py`.

## ✍️ Usage

- Use the **Add/Update** tab to record expenses
- Use the **Analytics** tabs to see trends by category or month
- Use the **Dashboard** to:
  - Monitor top categories
  - Set monthly budget and receive alerts
  - View summary metrics and trends

## 📄 Requirements
Install these packages via `pip install -r requirements.txt`
```
fastapi
uvicorn
pydantic
mysql-connector-python
streamlit
pandas
requests
pytest
```

## 🖼️ Screenshots

### ➕ Add / Update Tab
### 📊 Category-wise Analytics
### 📅 Monthly Analytics
### 📋 Dashboard with Budget Alert


## 📬 Contact
- **GitHub:** [Arun-Hegde](https://github.com/Arun-Hegde)
- **Email:** arunhegde697@gmail.com
