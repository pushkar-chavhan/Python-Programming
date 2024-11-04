import calendar
from colorama import Fore, Style, init

# Initialize colorama for cross-platform color support
init(autoreset=True)

def display_calendar():
    try:
        # User input for year and month
        year = int(input("Enter the year : "))
        month = int(input("Enter the month (1-12): "))
        
        # Set the start day to Monday
        calendar.setfirstweekday(calendar.MONDAY)

        # Display the header
        title = f"{calendar.month_name[month]} {year}"
        print("\n" + "─" * 29)
        print(Fore.CYAN + Style.BRIGHT + title.center(29) + Style.RESET_ALL)
        print("─" * 29)

        # Display the days of the week with Sunday in red
        weekday_headers = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
        for i, day in enumerate(weekday_headers):
            if i == 6:  # Highlight Sunday
                print(Fore.RED + Style.BRIGHT + f" {day} ", end="")
            else:
                print(f" {day} ", end="")
        print()

        # Horizontal line between headers and days
        print("─" * 29)

        # Get the calendar matrix for the month
        month_cal = calendar.monthcalendar(year, month)

        # Loop through each week in the month to display days
        for week in month_cal:
            for i, day in enumerate(week):
                if day == 0:
                    # Empty spaces for days not in the month
                    print("    ", end="")
                elif i == 6:
                    # Print Sundays in red
                    print(Fore.RED + Style.BRIGHT + f" {day:2} ", end="")
                else:
                    # Print weekdays in default color
                    print(f" {day:2} ", end="")
            print()  # New line after each week

        # Footer line
        print("─" * 29)

    except ValueError:
        print("Invalid input. Please enter numeric values for year and month.")

# Run the calendar display function
display_calendar()
