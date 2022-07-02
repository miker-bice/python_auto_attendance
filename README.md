
# Python Auto Attendance

A simple code which can fill and submit response to 
Google Forms built using python. You know what this
means? Yep, you can automate your Google Forms 
attendance 👌.



## Tech Stack

**Python3.xx latest** 


## Requirements
* [requests](https://pypi.org/project/requests/)
* [schedule](https://pypi.org/project/schedule/)

To install these packages, just run
```bash
  pip install package_name
```
## Run Project
* Clone the project
* Create your virtual environment using pipenv
* Run pip install for the packages
* Execute the code

## Variables

These are the variables that you need to modify

`url`

For the **url** you need to supply the google form link
and replace the 'viewform' with 'formResponse'

**Note:** This only works on google forms which **do not 
require** a sign in first

---

`values`

For the **values** you need to replace them with the
exact input names that your form contains as well as values
that you want to supply to your form. This goes for both
of the **key** and the **value**.

---

`schedule`

For the **schedule**, you need to replace this with the
schedule that you want your python code to execute. Refer
to [schedule](https://pypi.org/project/schedule/) docs.



