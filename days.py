import numpy as np

def calculate_days_ago():
    user_date = np.datetime64(str(input('Input your desired date in the format YYYY-MM-DD: \n')))
    today = np.datetime64('today')

    days_in_past = today - user_date
    print('\n')
    print(f'{user_date} was {days_in_past} ago')

calculate_days_ago()