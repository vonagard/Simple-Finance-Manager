import os

from models.expenses import add_expense, get_expense
from models.budgets import set_budget, get_budget
from models.savings import set_goal, get_saving_goals, check_goal_status, update_saving_goals

from reports.report_manager import generate_expense_report


def initial_menu():
    print('Welcome to your personal finance manager made by Vonagard.' +
          '\n  Choose an option:' +
          '\n   1. Add Expense' +
          '\n   2  Get Expense' +
          '\n   3. Set Budget' +
          '\n   4. Get Budget' +
          '\n   5. Set Goal' +
          '\n   6. Update Saving Goals' +
          '\n   7. Get Saving Goals' +
          '\n   8. Check Goal Status' +
          '\n   9. Generate Report' +
          '\n   10. Clear Terminal' +
          '\n   0. Exit\n')


def main_menu():
    initial_bool = False

    while True:
        if not initial_bool:
            initial_bool = True
            initial_menu()

        choice = input('Option: ')

        if choice == '1':
            # 1. Add Expense
            print('* are optional!\n')
            category = input('Category: ')
            amount = float(input('Amount: '))
            description = input('*Description: ')
            add_expense(category, amount, description)
        elif choice == '2':
            # Get Expense
            expenses = get_expense()
            print('All expenses:')
            print('id  |  category  |  amount  |  description')
            for expense in expenses:
                id = expense[0]
                category = expense[1]
                amount = expense[2]
                description = expense[3]
                print(f'{id}  |  {category}  |  {amount}  |  {description}')
        elif choice == '3':
            # 3. Set Budget
            category = input('Category: ')
            limit = float(input('Budget Limit: '))
            set_budget(category, limit)
        elif choice == '4':
            # 4. Get Budgets
            budget = get_budget()
            print('  id  |  category  |  budget_limit  |  timestamp')
            for row in budget:
                print(f'  {row[0]}  |  {row[1]}  |  {row[2]}  |  {row[3]}')
        elif choice == '5':
            # 5. Set Goal
            print('Set a new goal:')
            goal_name = input('Goal Name: ')
            target_amount = float(input('Target Amount: '))
            current_amount = float(input('Current Amount: '))
            deadline = input('// format %d%m%Y // Deadline: ')

            result = set_goal(goal_name, deadline, target_amount, current_amount)

            if result:
                print('Goal set successfully.')
            else:
                print('Something went wrong.')
        elif choice == '6':
            # 6. Update Saving Goals
            id_to_find = int(input('Please choose a goal id: '))
            amount_to_add = float(input('Please choose an amount to add: '))
            print(update_saving_goals(id_to_find, amount_to_add))
        elif choice == '7':
            # 7. Get Saving Goals
            print('test')
            goals = get_saving_goals()
            print('Goals:\n' + goals)
        elif choice == '8':
            # 8. Check Goal Status
            id_to_find = input('Please choose a goal id: ')
            print(check_goal_status(id_to_find))
        elif choice == '9':
            # 9. Generate Report
            print(generate_expense_report())
        elif choice == '10':
            initial_bool = False
            clear = lambda: os.system('cls')
            clear()
        elif choice == '0':
            # 0. Exit
            print('Exiting...')
            initial_bool = False
            break
