import datetime


def tomorrow():
    return datetime.date.today() + datetime.timedelta(days=1)

print(tomorrow())