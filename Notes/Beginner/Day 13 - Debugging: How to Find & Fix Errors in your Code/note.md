### Describe the problem

The first step of solving a problem is being able to describe the problem.

<br>

### PAUSE 1

Look at the code in task.py and answer the following questions:

1. What is the for loop doing?
2. When is the function meant to print "You got it"?
3. What are your assumptions about the value of i?

```python
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")

my_function()

# 1. Loops through all the numbers between 1 and 20
# 2. Once that number reaches 20, it's supposed to print "You got it"
# 3. My assumption about the value of i is that the value, i, will definitely reach 20
```

<br>

### PAUSE 2

Fix the code so that the print statement executes

```python
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function()
```

<br>

---

### Reproduce the Bug

Some bugs are sneaky, they only occur under certain conditions. In order to debug them, one needs to be able to reliably reproduce the bug and diagnose one’s problem to figure out which conditions trigger the bug.

<br>

### Occasional Bug Code

```python
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])
```

<br>

### PAUSE 1

Change the code so that it always produces the occasional error.

```python
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = 6
print(dice_images[dice_num])
```

<br>

### PAUSE 2

Fix the code and remove the bug

```python
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])
```

<br>

---

### Play Computer and Evaluate Each Line

Playing computer is an important skill in debugging. One needs to be able to go through one’s code line by line as if one were the computer to help one figure out what is going wrong.

<br>

### PAUSE 1

Play computer and go through the code line by line as if you were executing the code to figure out why 1994 does not work as expected. Then go ahead and fix the code.

```python
year = int(input("What's your year of birth?"))
# For 1994
if year > 1980 and year < 1994: # if True and False => False
    print("You are a millennial.")
elif year > 1994: # False
    print("You are a Gen Z.")

# PAUSE 1
if year > 1980 and year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
```

<br>

---

### Fixing Errors and Watching for Red Underlines

Fix any errors (red underlines) that show up in the editor before one runs one’s code. The warnings (yellow) are optional fixes, sometimes it will cause a problem down the line other times it's fine and the editor just doesn't understand what one is trying to do.

```python
# Original code
age = int(input("How old are you?"))
if age > 18:
print("You can drive at age {age}.")
```

```python
# IndentationError on Console when executed
 print("You can drive at age {age}.")
    ^
IndentationError: expected an indented block after 'if' statement on line 2
```

```python
# Fixed code
age = int(input("How old are you?"))
if age > 18:
    print("You can drive at age {age}.") # Indented
```

<br>

### Catching Exceptions

One can use a try/except block in Python to catch any exceptions that might occur. For example if one imagines there could be a chance of user error. One can prevent it crashing one’s code by anticipating it. One traps the dangerous code inside a try block and use an except block to catch any potential errors. Then one defines what should happen when that error occurs instead of simply just crashing and stopping the code.

e.g.

```python
try:
    print(6 > "five")
except TypeError:
    print("You can't mix integers and strings in a comparison")

```

<br>

### PAUSE 1

Fix the bug so that the print statement displays the correct value of age in the output area.

```python
try: 
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in an invalid number. Please try again with a numerical response such as 15.") 
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.") # Indented
```

<br>

---

### Squash bugs with a print() Statement

`print()` can help expose hidden values while one’s code is running. In a for loop, the loop will follow some rules to perform a repeated block of code. But during the loop it’s difficult to see the intermediate values, that’s a perfect example of how one can use print function to expose those intermediate values and help one debug one’s code.

<br>

### PAUSE 1

The code is supposed to calculate the total number of words given the number pages and the word per page. But it's not currently giving any output. Diagnose the problem using `print()` statements.

```python
# Original Code
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
```

```python
print(f"pages = {pages}".)
print(f"word_per_page = {word_per_page}".) # word_per_page is having a problem
print(total_words)
```

<br>

### PAUSE 2

Fix the code.

```python
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) # Single Equal Sign is needed not Double Equal Sign
total_words = pages * word_per_page
print(total_words)
```

<br>

---

### Bringing out the BIG Gun: Using a Debugger

Most IDEs (Intelligent Development Environments) such as PyCharm will have built-in tools for debugging. This is normally known as the debugger. In many ways, they are like print statements on steroids.

Debuggers allows one to peek into one’s code during execution and pause on chosen lines to figure out what is the inner mechanism and where it's going wrong.

There are a couple of things that are the same in most IDEs which one should be familiar with:

1. **Breakpoint** - One can set a breakpoint by clicking on a line in the gutter of the code (where the line numbers are). This line will be where the program pauses during debug run.
2. **Step Over** - This button will go through the execution of one’s code line by line and allow one to view the intermediate values of one’s variables.
3. **Step Into** - This will enter into any other modules that one’s code references. e.g. If one uses a function from the random module it will show one the original code for that function so one can better understand its functionality and how it relates to one’s problems.
4. **Step Into My Code** - This does the same thing as Step Into, but it limits the scope to one’s own project code and ignores library code such as random.

<br>

### PAUSE 1

Use the PyCharm debugger to figure out what is the issue in the starting code and fix it.

```python
# maths.py
def add(n1, n2):
    return n1 + n2
```

```python
# original.py
import random
import maths

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])
```

<br>

```python
# debugged code
import random
import maths

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])
```

<br>

---

### Final Debugging Tips

1. Take a break in between
2. Ask for a code review
3. Run one’s code often — run it after every little execution
4. Ask StackOverflow — only when one exhausted all other avenues of debugging

<br>

