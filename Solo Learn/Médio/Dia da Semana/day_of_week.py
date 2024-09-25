from datetime import datetime

def get_day_of_week(date_str):
    try:
        # First, try parsing the "MM/DD/YYYY" format
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
    except ValueError:
        try:
            # If the first format fails, try "Month Day, Year" format
            date_obj = datetime.strptime(date_str, "%B %d, %Y")
        except ValueError:
            return "Invalid date format. Please use 'MM/DD/YYYY' or 'Month Day, Year'."

    # Get the day of the week and return it
    return date_obj.strftime("%A")

# Sample Input
date_input = input()
print(get_day_of_week(date_input))