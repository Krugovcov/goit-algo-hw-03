from datetime import datetime


def get_days_from_today(date):
    try:
        return (datetime.strptime(date, "%Y-%m-%d").date() - datetime.today().date()).days
    except ValueError:
        raise ValueError("Використовуйте формат РРРР-ММ-ДД")
print(get_days_from_today("2020-10-09"))