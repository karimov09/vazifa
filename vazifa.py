import datetime
import calendar
import time

def get_weekday_number(date_string):
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    weekday_number = date_obj.weekday()
    return weekday_number

def display_month(year, month):
    return calendar.month(year, month)

def display_year(year):
    return calendar.calendar(year)

def check_date(date1, date2):
    date_format = "%Y-%m-%d"
    a = datetime.datetime.strptime(date1, date_format)
    b = datetime.datetime.strptime(date2, date_format)
    delta = b - a
    return delta.days

def display_today():
    today = time.strftime("%A %d %B %Y %H:%M:%S")
    date_today = time.strftime("%d.%m.%Y")
    return f":\n{today}\n{date_today}"

def save_calendar_html(year, filename='kalendar.html'):
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    html_calendar = cal.formatyear(year)
    with open(filename, 'w') as file:
        file.write(html_calendar)

def main():
    date_string = '2024-07-17'
    weekday_number = get_weekday_number(date_string)
    print(f"The weekday number for {date_string} is {weekday_number}.")

    print(display_month(2024, 7))
    print(display_year(2024))

    days_between = check_date('2024-01-01', '2024-07-17')
    print(f" {days_between}")

    print(display_today())

    save_calendar_html(2024)
    print("2024 kalendar")

if __name__ == "__main__":
    main()
