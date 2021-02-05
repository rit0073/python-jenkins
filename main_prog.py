import datetime


def return_today_date():
    return datetime.datetime.now().strftime('%d/%m/%Y')


# print(return_today_date())
# python -m pytest tests/test_main_prog.py
