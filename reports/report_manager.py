import pandas as pd
import matplotlib.pyplot as plt

from database.db_manager import connect_db


def generate_expense_report():
    connection = connect_db()
    query = 'SELECT * FROM expenses'
    df = pd.read_sql_query(query, connection)

    print(df.groupby('category').sum())

    df.groupby('category').sum()['amount'].plot(kind='bar')
    plt.show()

    connection.close()
