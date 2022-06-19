# Autofill Google Form

import requests
import schedule
import time


# URL to the form you want to fill. formResponse should be used instead of viewform
url = 'https://docs.google.com/forms/d/e/1FAIpQLSeuX4sCwE-2mSUEvIVgs8FVVwaDbsACXzpLamsWy3PQ6sgdIQ/formResponse'


def get_morning_values():
    values = {
        "entry.1283133789": "Onsite",
        "entry.932776810": "Login",
    }

    return values


def get_afternoon_values():
    values = {
        "entry.1283133789": "Work from Home",
        "entry.932776810": "Logout",
    }

    return values

# Function used to submit the data


def send_attendance(url, data):
    try:
        requests.post(url, data=data)
        print("Form Submitted.")
        time.sleep(5)
    except:
        print("Error Occured!")


def execute_morning():
    final_data = get_morning_values()
    send_attendance(url, final_data)


def execute_afternoon():
    final_data = get_afternoon_values()
    send_attendance(url, final_data)


schedule.every(1).minutes.do(execute_afternoon)

while True:
    schedule.run_pending()
    time.sleep(5)
