import sqlite3


def create_tables():
    connection = connect_db()
    cursor = connection.cursor()

    # creating expenses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        category TEXT,
        amount REAL,
        description TEXT,
        timestamp DATE DEFAULT (datetime('now'))
        )
    ''')

    cursor.execute('''
            SELECT * FROM expenses
        ''')
    # expenses_column_names = list(map(lambda x: x[0], cursor.description))

    # creating budgets table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS budgets (
        id INTEGER PRIMARY KEY,
        category TEXT,
        budget_limit REAL,
        timestamp DATE DEFAULT (datetime('now'))
        )
    ''')

    cursor.execute('''
            SELECT * FROM budgets
        ''')
    # budgets_column_names = list(map(lambda x: x[0], cursor.description))

    # creating saving_goals table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS saving_goals (
        id INTEGER PRIMARY KEY,
        goal_name TEXT,
        target_amount REAL,
        current_amount REAL DEFAULT 0,
        deadline DATE,
        timestamp DATE DEFAULT (datetime('now'))
        )
    ''')

    cursor.execute('''
            SELECT * FROM saving_goals
        ''')
    # saving_goals_column_names = list(map(lambda x: x[0], cursor.description))

    connection.commit()
    connection.close()

    # print(f'''
    # Database: finance.db
    # Tables and Columns:
    # Table    |    Columns
    # budgets: {budgets_column_names}
    # expenses: {expenses_column_names}
    # saving_goals: {saving_goals_column_names}
    # ''')


def connect_db():
    return sqlite3.connect('finance.db')


def initialize_db():
    create_tables()
    print()
