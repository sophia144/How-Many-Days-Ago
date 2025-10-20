#importing necessary modules
import numpy as np
import csv

#function for calculating how long ago a given day was and outputting it using an f-string
def basic_date_calculation(reference_date):
    today = np.datetime64('today')
    days_in_past = today - reference_date
    print(f'{reference_date} was {days_in_past} ago')

#function for running the calculation from a user input
def user_input_version():
    user_date = np.datetime64(str(input('Input your desired date in the format YYYY-MM-DD: \n')))
    basic_date_calculation(user_date)

#function for running the calculation from a given csv
def csv_input_calculation(file_name):
    print('\n')
    with open(file_name) as csv_file:
        read_csv = csv.reader(csv_file, delimiter= '\n')
        for row in read_csv:
            basic_date_calculation(np.datetime64(row[0]))
    print('\n')

csv_input_calculation('random_dates.csv')