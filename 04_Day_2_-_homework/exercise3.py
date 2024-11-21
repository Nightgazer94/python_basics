
def format_date(day, month, year):
    months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if not (1 <= month <= 12):
        return None
    if not (1 <= day <= days_in_month[month]):
        return None

    return f"{day} {months[month]} {year}"

print(format_date(29, 2, 2020))