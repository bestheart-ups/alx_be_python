from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()

    formatted_date = current_date.strftime("%y-%m-%d %H:%M:%S")
    print("current date and time:", foematted_date)

def calculate_future_date():
    while True:
        try:
            days = int(input("enter the number of days to add: "))
            break
        except ValueError:
            print("please enter a valid integer.")

            current_date = datetime.now()
            future_date = current_date + timedelta(days=days)

            formatted_future_date = future_date.strftime("%y-%m-%d")
            print(f"Date after {days} days will be: {formatted_future_date}")

    if __name__ == "__main__":
        display_current_datetime()
        calculate_future_date()