from backend import db_helper

print(__file__)

def test_fetch_expenses_for_date_aug_15():
    expenses = db_helper.fetch_expenses_for_date('2024-08-15')

    assert len(expenses) == 1
    assert expenses[0]['amount']==10.00
    assert expenses[0]['category'] == 'Shopping'
    assert expenses[0]['notes'] == 'Bought potatoes'

def test_fetch_expenses_for_date_invalid():
    expenses = db_helper.fetch_expenses_for_date('8888-08-15')

    assert len(expenses) == 0

def test_fetch_expense_summary_invalid_date():
    summary = db_helper.fetch_expense_summary('8888-08-15' ,'8888-08-18' )

    assert len(summary) == 0
