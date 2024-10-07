from database.db_manager import connect_db
from database.get_and_format_date import get_current_date


def set_budget(category, limit):
    connection = connect_db()
    cursor = connection.cursor()

    query = '''
        INSERT INTO budgets (category, budget_limit, timestamp)
        VALUES (?, ?, ?)
    '''
    data_tuple = (category, limit, get_current_date())

    cursor.execute(query, data_tuple)

    connection.commit()
    connection.close()

    return True


def get_budget():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM budgets
    ''')
    budgets = cursor.fetchall()

    connection.close()

    return budgets
