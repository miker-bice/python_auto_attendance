import requests
import schedule
import time

# this works with google forms that do not require a sign in

# insert here the link of your form
url = 'https://docs.google.com/forms/d/e/1FAIpQLScLrLcx1XnRExDW2ku5eXGoe_iz4rsz8N4XeuCchHuyFBGlFg/formResponse'
# insert here your email
email = 'mrgalindez@ccc.edu.ph'


def get_login_values():
    values = {
        'entry.2082349234': 'Log In',
        'entry.344582317': 'Work-from-Home',
        'emailAddress': email,
    }

    return values


def send_attendance(url, data):
    try:
        requests.post(url, data=data)
        print("Form Submitted.")
        time.sleep(5)
    except:
        print("Error Occured!")


final_data = get_login_values()
send_attendance(url, final_data)
