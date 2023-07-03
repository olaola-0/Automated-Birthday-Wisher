import smtplib
from datetime import datetime
import pandas as pd
import random

# Email and email provider generated password for the sender
my_email = 'email@email.com'
my_password = 'generated password'

# Get the current date
today = datetime.now()

# Load the data from the csv file into a dataframe
df = pd.read_csv('birthdays.csv')

# Filter the dataframe for rows where the day and month match today's day and month
birthdays_today = df[(df['month'] == today.month) & (df['day'] == today.day)]

# For each birthday person today
for idx, birthday_person in birthdays_today.iterrows():
    # Randomly select a letter template
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_path) as letter_file:
        # Read the contents of the letter
        contents = letter_file.read()
        # Replace placeholder with the birthday person's name
        contents = contents.replace('[NAME]', birthday_person['name'])

        # Start a secure SMTP connection
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(my_email, my_password)
            # Send the email to the birthday person
            smtp.sendmail(from_addr=my_email,
                          to_addrs=birthday_person['email'],
                          msg=f'Subject: Happy Birthday!\n\n{contents}')
