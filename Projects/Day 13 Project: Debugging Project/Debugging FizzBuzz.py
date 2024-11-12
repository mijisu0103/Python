# Debugging FizzBuzz

"""
- Read the code in the exercise.py file.
- Find a problem 🐞.
- Fix the problem by modifying the program.
- without a shortcut

- Don't copy and paste the code to replace it completely with a solution that worked before.

The code should print out the answer to the FizzBuzz game.
- The program must output each number from 1 up to the number x entered.
- However, if the number is divided by 3, you should output "Fizz" instead of outputting the number.
- If the number falls by 5, you must output "Buzz" instead of printing the number.
- And if the numbers are separated by both 3 and 5, you have to output "FizzBuzz" instead of outputting the numbers, for example, when it's 15.
"""

# Original code
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 or number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print([number])

# Debugged code
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
