from datetime import datetime, timedelta

def date_difference(days):
    current_datetime = datetime.now()
    print("Current Datetime  : ", current_datetime)
    date_diff = current_datetime - timedelta(days=days)
    return date_diff


day = int(input("Enter number of days : "))
print("Modified Datetime : ", date_difference(day))