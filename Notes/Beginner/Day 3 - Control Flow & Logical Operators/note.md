### Control Flow with if / else & Conditional Operators

Depending on a particular condition, one would do either A or B

e.g. **rollercoaster**

```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height < 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")
```
<br>

**Comparison Operators**

| Operator | Meaning |
| --- | --- |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |
| == | Equal to |
| != | Not equal to |

<br>

**Usage of equal sign(s)**

`=` — Value assignment

`==` — Check Equality

<br>

***
### Introducing the Modulo
An operator is a symbol in programming that has a specific function

**Modulo operator (%)** looks a bit like a percentage sign that goes in between two numbers (hence a binary operator) and **works out what is the remainder after the division**

- 10 % 5 = 0
- 6 % 2 = 0
- 6 % 5 = 1
- 6 % 4 = 2

<br>

### PAUSE 1 - What is 10 % 3?

What do you think this will output?

```python
print(10 % 3)
```

```python
1 # 3 with 1 remaining
```

<br>

### **PAUSE 2 - Check Odd or Even**

Write some code using what you have learnt about the modulo operator and conditional checks in Python to check if the number in he input area is odd or even. If it's odd print out the word "Odd" otherwise printout "Even".

```python
number_to_check = int(input("What is the number you want to check? "))

if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")
```

<br>

***
### Nested if statements & elif statements
Represent extra condition that one needs to check for in one’s code

- Once the first condition has passed, one can check for another condition and then one can have another if else statement inside this if condition
- Essentially the computer first looks at the larger picture, which is the first condition, and decides on whether if it should go into the else block or if it should go into the nested block

```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
```

<br>

Instead of having a simple if else statement where there’s only one condition, one can add as many elif conditions as one wants.

```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
```

<br>

***
### BMI Calculator with Interpretations

Add an if/elif/else statement to the BMI calculator to interpret the calculated BMI values.

- If bmi is less than 18.5, output "underweight".
- If bmi is greater than 18.5 and less than 25, output "normal weight".
- If bmi is above 25, output "overweight".

```python
weight = 85
height = 1.85
 
bmi = weight / (height ** 2)
 
if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")
```

<br>

***
### Multiple If Statements in Succession
**if / elif / else vs. multiple if**

- **if / elif / else**:
    1. Only one of code under if or elif or else will be carried out 
    - Only one code will be executed
- **multiple if**:
    1. If the first condition is true, then execute the relevant code
    2. Then, the code moves to the next case and check if the second condition is also true, in which case the relevant code will be executed
    3. Moving to the next case, if the final condition is also true, the relevant code will be executed
    - All of the cases are checked and if it happens that all of the cases are true, then all of the codes will be executed
    
<br>

**Multiple if use case**

```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == "y":
        bill += 3 # same as bill = bill + 3
    
    # No need for else statement here as if the answer is no, the code simply is going to do nothing to the bill
    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
```

<br>

***
### Pizza Order Practice

Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

- Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.
    - Small pizza (S): $15
    - Medium pizza (M): $20
    - Large pizza (L): $25
    - Add pepperoni for small pizza (Y or N): +$2
    - Add pepperoni for medium or large pizza (Y or N): +$3
    - Add extra cheese for any size pizza (Y or N): +$1

```python
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size choice
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")

# todo: work out how much to add to their bill based on their pepperoni choice
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# todo: work out their final amount based on whether if they want extra cheese
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
```

<br>

***
### Logical Operators

- `and`: when one combines two different conditions using an and operator, they both have to be true ,both A and B, for the entire line of code to be true
    - If just one of them is true, say A is true and B is false, or A is false and B is true, then the overall thing evaluates to false
    
    ```python
    a = 12
    
    a > 10 and a < 13 # True
    a > 15 & a < 13 # False
    
    True and True # True
    False and True # False
    True and False # False 
    ```

<br>

- `or`: if one only needs one of the conditions to be true, then one can use the or operator instead
    - If just one of them is true, say C or D is true, or both of them are true, then it will evaluate to true
    - It is only when both C and D are false thus this statement actually become false
    
    ```python
    a = 12
    
    a > 10 or a < 10 # True
    
    True or True # True
    True or False # True
    False or True # True
    False or False # False
    ```

<br>

- `not`: not operator basically reverses a condition
    - If the condition is false, then it becomes true
    - If the condition is true, then it becomes false
    
    ```python
    a = 12
    
    not a < 0 # False --> True
    
    not False # True
    not True # False
    ```
    
<br>

### PAUSE 1 - Age 45 to 55 Modifier

Update the code so that people age 45 to 55 (inclusive of both ages) ride for free. Use logical operators to check that the age is greater than 45, and it's also less than 55.

```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55: # also can write elif 45 <= age <= 55
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == "y":
        bill += 3 # same as bill = bill + 3
    
    # No need for else statement here as if the answer is no, the code simply is going to do nothing to the bill
    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
```

<br>

***
### Logical Operators Quiz

**Q1: What is the following code calculated by?**

```python
not 5 == 5
```

- True
- **False**

A1: **False**

<br>

**Q2: What is the following code evaluated as?**

```python
False or True or False
```

- **True**
- False
- Syntax Error

A2: **True**

<br>

**Q3: What does the following code output?**

```python
a = 5
b = 7
 
if a >= b and a != b:
    print("A")
elif not a >= b and a != b:
    print("B")
else:
    print("C")
```

- A
- **B**
- C

A3: **B**

<br>

