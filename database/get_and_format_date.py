from datetime import datetime
from datetime import date


def format_str_to_ddmmyyyy_str(date_to_format, input_format):
    # inputs:
    # mmddyyyy
    # yyyymmdd
    # output: mm-dd-YYYY
    if input_format.lower() == 'mmddyyyy':
        mm_dd_yyyy = date_to_format.split('-')
        formatted_date = date(*list(map(int, mm_dd_yyyy)))
        return f'{formatted_date.day}-{formatted_date.month}-{formatted_date.year}'
    elif input_format.lower() == 'yyyymmdd':
        yyyy_mm_dd = date_to_format.split('-')
        formatted_date = date(*list(map(int, yyyy_mm_dd)))
        return f'{formatted_date.day}-{formatted_date.month}-{formatted_date.year}'
    else:
        print('Wrong input format. Possible formats:\n  mmddyyyy\n  yyyymmdd')


def format_date_to_str(date_to_format):
    return f'{date_to_format.day}-{date_to_format.month}-{date_to_format.year}'


def format_str_to_date(date_str, input_format):
    # yyyymmdd
    # ddmmyyyy
    print(date_str)
    print(str.split('-', date_str))
    print(list(map(int, date_str.split('-'))))
    if input_format.lower() == 'yyyymmdd':
        return date(*(list(map(int, list(date_str.split('-'))))))
    elif input_format.lower() == 'ddmmyyyy':
        return date(*(list(map(int, list(date_str.split('-')))))[::-1])


def get_current_date():
    current_date = datetime.now()
    yyyy = current_date.year
    mm = current_date.month
    dd = current_date.day

    return date(yyyy, mm, dd)


def get_days_left(deadline):
    current_date = get_current_date()
    formatted_deadline = format_str_to_date(deadline, 'yyyymmdd')
    return abs((formatted_deadline - current_date).days)
