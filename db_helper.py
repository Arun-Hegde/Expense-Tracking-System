import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password ="root123",
        database="expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor

    connection.commit()

    cursor.close()
    connection.close()

def fetch_all_records():
    logger.info(f"fetch_all_records called with All Records")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)

def insert_expense(expense_date,amount,category,notes):
    logger.info(f"insert_expense called with date:{expense_date},amount:{amount},category:{category},notes:{notes}")
    with get_db_cursor() as cursor:
        cursor.execute("INSERT INTO expenses(expense_date,amount,category,notes) VALUES (%s,%s,%s,%s)",
                       (expense_date,amount,category,notes)               )

def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with date:{expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("SELECT * FROM expenses where expense_date =%s",(expense_date,))
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)
        return expenses

def fetch_expense_summary(start_date,end_date):
    logger.info(f"fetch_expense_summary called with start:{start_date},end:{end_date}")
    with get_db_cursor() as cursor:
        cursor.execute('''SELECT category,sum(amount) as total
                                FROM expenses
                                Where expense_date
                                between %s and %s
                                group by category;''',
                       (start_date,end_date))
        data = cursor.fetchall()
        return data


def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with date:{expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses where expense_date =%s",(expense_date,))

def analytics_by_month():
    logger.info(f"analytics_by_month called with all months")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute('''SELECT 
	                    date_format(expense_date,'%Y-%m') As month,
                        SUM(amount) as total_amount
                        From expenses
                        group by date_format(expense_date,'%Y-%m')
                        order by month;''')
        data = cursor.fetchall()
        return data

if __name__ == "__main__":
   expenses = fetch_expenses_for_date('2024-09-20')
   print(expenses)
   # delete_expenses_for_date('2024-08-25')
   summary = fetch_expense_summary('2024-08-15','2024-08-18')
   for record in summary:
       print(record)
