# Debugging Leap Year

"""
- Read the code in the exercise.py file.
- Find a problem 🐞.
- Fix the problem by modifying the program.

Modify the code to make it work. If you submit, you must pass all the tests.
This is how to check if a particular year is a leap year.

- It corresponds to any year that falls by 4 without the rest.
- Exclude all years that fall by 100 without the rest.
- However, the year should be divided into 400 without the rest.

You can copy and paste the code to PyCharm to help with debugging.
"""

# Original code
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        
# Debugged code
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:  # Change 4000 to 400
                return True
            else:
                return False
        else:
            return True
    else:
        return False
