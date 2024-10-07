from database.db_manager import connect_db
from database.get_and_format_date import get_current_date


def add_expense(category, amount, description=''):
    connection = connect_db()
    cursor = connection.cursor()

    query = '''
        INSERT INTO expenses (category, amount, description, timestamp)
        VALUES(?, ?, ?, ?)
    '''
    data_tuple = (category, amount, description, get_current_date())
    cursor.execute(query, data_tuple)

    connection.commit()
    connection.close()

    return True


def get_expense():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM expenses
    ''')
    expenses = cursor.fetchall()

    connection.close()

    return expenses
