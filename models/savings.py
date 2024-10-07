from database.db_manager import connect_db
from database.get_and_format_date import (format_str_to_date, format_str_to_ddmmyyyy_str, format_date_to_str,
                                          get_current_date, get_days_left)


def visualize_goal(goal_id, goal_name, target_amount, current_amount, deadline, timestamp):
    db_format = 'yyyymmdd'

    formatted_timestamp = format_str_to_ddmmyyyy_str(timestamp, db_format)

    formatted_deadline = format_str_to_ddmmyyyy_str(deadline, db_format)

    current_date = get_current_date()
    formatted_current_date = format_date_to_str(current_date)

    days_left = get_days_left(deadline)
    percentage_saved = (current_amount / target_amount) * 100

    return f'''
    Goal Name: {goal_name}
    Goal Id: {goal_id}
    Date Added: {formatted_timestamp}
    Deadline: {formatted_deadline}
    Current Date: {formatted_current_date}
    Days Left: {
        f'{days_left} Days Remaining!'
        if format_str_to_date(deadline, db_format) > current_date
        else f'{days_left} Days Overdue!'}
    Target Amount: {target_amount}
    Current Amount: {current_amount}
    Percentage Saved: {percentage_saved}
    '''


def set_goal(goal_name, deadline, target_amount, current_amount=0):
    connection = connect_db()
    cursor = connection.cursor()
    formatted_deadline = format_str_to_ddmmyyyy_str(deadline, )

    query = '''
        INSERT INTO saving_goals (goal_name, target_amount, current_amount, deadline, timestamp)
        VALUES (?, ?, ?, ?, ?)
    '''
    data_tuple = (goal_name, target_amount, current_amount, formatted_deadline, get_current_date())

    cursor.execute(query, data_tuple)

    print("Goal added successfully!")

    connection.commit()
    connection.close()

    return True


def update_saving_goals(goal_id, new_amount):
    connection = connect_db()
    cursor = connection.cursor()

    query = '''
        SELECT current_amount FROM saving_goals WHERE id = ?
    '''
    data_tuple = (goal_id,)

    cursor.execute(query, data_tuple)
    current_amount = cursor.fetchone()[0]
    updated_amount = current_amount + new_amount

    query = '''
        UPDATE saving_goals SET current_amount = ? WHERE id = ?
    '''
    data_tuple = (updated_amount, goal_id)
    cursor.execute(query, data_tuple)

    connection.commit()
    connection.close()

    return f'''
    Old amount: {current_amount}
    Added amount: {new_amount}
    Updated amount: {updated_amount}
'''


def get_saving_goals():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM saving_goals
    ''')
    goals = cursor.fetchall()

    connection.close()

    all_goals = ''
    for goal in goals:
        goal_id, goal_name, target_amount, current_amount, deadline, timestamp = goal
        print(type(timestamp))
        print(type(deadline))
        print(visualize_goal(goal_id, goal_name, target_amount, current_amount, deadline, timestamp))
        all_goals += visualize_goal(goal_id, goal_name, target_amount, current_amount, deadline, timestamp)

    return all_goals


def check_goal_status(goal_id):
    connection = connect_db()
    cursor = connection.cursor()

    query = '''
        SELECT * FROM saving_goals WHERE id = ?
    '''
    try:
        int_id = int(goal_id)
    except:
        return 'Not a valid goal id. Must be a number!'

    cursor.execute(query, (int_id,))
    goal = cursor.fetchone()

    if goal:
        goal_id, goal_name, target_amount, current_amount, deadline, timestamp = goal
        status = visualize_goal(goal_id, goal_name, target_amount, current_amount, deadline, timestamp)

        return status
    return f'Goal not found using the {goal_id} id.'
