import numpy as np

def calculate_days_since():
    user_date = np.datetime64(str(input('Input your desired date in the format YYYY-MM-DD: \n')))
    today = np.datetime64('today')

    days_in_past = today - user_date
    print(days_in_past)

calculate_days_since()