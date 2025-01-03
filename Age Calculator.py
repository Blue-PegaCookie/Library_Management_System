from calendar import month
from datetime import datetime


def Age_Calculator():



    def date_of_birth():
        current_year = datetime.now().year
        while True:
            try:
                dob = input("Enter your date of birth (dd/mm/yyyy): ")
                day, month, year = map(int, dob.split('/'))
                if month < 1 or month > 12:
                    raise ValueError("Month must be between 1 and 12.")
                if year < 1 or year > current_year:
                    raise ValueError(f"Year must be between 1 and {current_year}.")
                if day < 1 or day > 31:
                    raise ValueError("Day must be between 1 and 31.")
                datetime(year, month, day)  # This will raise an error if the date is invalid
                if datetime(year, month, day) > datetime.now():
                    raise ValueError("Date of birth cannot be in the future.")
                print(f"Day: {day}, Month: {month}, Year: {year}")
                break
            except ValueError as e:
                if "invalid literal for int()" in str(e):
                    print("Invalid date format. Please enter the date in dd/mm/yyyy format.")
                else:
                    print(f"Invalid date: {e}. Please enter the date in dd/mm/yyyy format.")
            except Exception:
                print("Invalid input. Please enter the date in dd/mm/yyyy format.")

        return year, month, day



    year, month, day = date_of_birth()



    def year_calc(year, month, day):
        current_year = datetime.now().year
        if month > datetime.now().month:
            return current_year - year - 1
        elif month == datetime.now().month and day > datetime.now().day:
            return current_year - year - 1
        else:
            return current_year - year



    def month_calc(year, month, day):
        current_month = datetime.now().month
        if month > current_month:
            return 12 - month + current_month
        else:
            return current_month - month



    def day_calc(year, month, day):
        current_day = datetime.now().day
        if day > current_day:
            return 30 - day + current_day
        else:
            return current_day - day



    years = year_calc(year, month, day)
    months = month_calc(year, month, day)
    days = day_calc(year, month, day)

    print(f"You are {years} years, {months} months, and {days} days old.")


Age_Calculator()
#
# import tkinter as tk
#
# window = tk.Tk()
# window.title("Age Calculator")
#
# # Create and place the widgets
# tk.Label(window, text="Enter your date of birth (dd/mm/yyyy):").pack(pady=10)
# entry = tk.Entry(window)
# entry.pack(pady=5)
#
# tk.Button(window, text="Calculate Age", command=Age_Calculator()).pack(pady=10)
# result_label = tk.Label(window, text="")
# result_label.pack(pady=10)
#
# # Run the application
# window.mainloop()

