### Defining and Calling Python Functions

> Functions perform different pieces of functionality

A function in its simplest form is just a wrapper name for a block of code. One gives it name and then when one calls the function by that name, all the code within the function block will be executed. It can help one save time and reduce repeated code.

<br>

### Python Built-in Functions

[Python documentation Built-in Functions](https://docs.python.org/3/library/functions.html)

<br>

### Customised Functions

### Defining a new Function

```python
def <function name>():
    print("Hello")
    # Do something else
    # Do something else ...
```
<br>

### Calling a Function

Calling a function just means triggering the function. We can call a function at any point in our code in Python.

```python
<function name>()
```
<br>

### Defining & Calling a Function

```python
#Creating the function
def get_user_name():
    name = input("What is your name? ")
    print("Hello, " + name)
    # Inside the function

#Outside the function
print("Hello")
get_user_name() # Calling the function
```

```python
Hello
What is your name? Jisu # Typed Jisu for the input
Hello, Jisu

```

<br>

**e.g. Defining & Calling a Function**

```python
def my_function():
    print("Hello")
    print("Bye")

my_function()
```

```python
Hello
Bye
```

<br>

---

### The Hurdles Loop Challenge

[André Roberge Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)

**Hurdle #1 — Jumping over 6 hurdles that are positioned at a constant distance**

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for step in range(6):
    jump()
```

<br>

<div align = center>
    <img src = "H1.gif" width = 600>
</div>

<br>

---

### Indentation in Python

In Python, it is really important to be aware of indentation

- Indentation means that something is shifted to the right by four spaces
- Similar to file structure on Finder / File explorer

<br>

---

### Code Indentation Quiz

**Q1: What code causes IndentationError when running?**

```python
def my_function():
  print("Hello")
```

```python
def my_function():
print("Hello")
```

```python
def my_function():
    print("Hello")
```

```python
def my_function():
  print("Hello")
print("Bye"
```

A1: **2nd code**

<br>

**Q2: What is the code that outputs "This will run"?**

```python
# This is my program.
  print("This will run")
```

```python
def my_function():
    print("This will run")
```

```python
def my_function():
    #This is my function
    print("This will run")
    my_function()
```

```python
def my_function():
    #This is my function
    print("This will run")
    my_function()
```

A2: **4th code**

<br>

**Q3:** **What is the code that outputs "This will run"?**

```python
def my_function():
    a = 3
    if a > 2:
    print("This will run")
my_function()
```

```python
def my_function():
a = 3
    if a > 2:
        print("This will run")
my_function()
```

```python
def my_function():
    a = 3
    if a > 2:
        print("This will run")
    my_function()
```

```python
def my_function():
    a = 3
    if a > 2:
        print("This will run")
my_function()
```

A3: **4th code**

<br>

---

### While Loops

While Loops executes codes under it repeatedly while the particular condition is true — it is only when the something becomes false does the loop stop

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
# for step in range(6):
#    jump()

number_of_hurdels = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
```
<br>

### While Loop Syntax

```python
while something_is_true:
    # Do this
    # Then do this
    # Then do this
```

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal != True:
    jump()
    
# OR
# while not at_goal():
#    jump()
```

<br>

### For Loops vs. While Loops

For Loops have set time to be executed — how many times something is going to run. It is going to stop once it reaches the end of the list of items or the upper bound of the range

<br>

While Loops will continue running until the particular condition switches to false — if one has some sort of condition that actually never becomes false, then one’s while loop becomes something known as an infinite loop 

**e.g. Infinite Loop**

```python
while 5 > 3:
    # Do this
    # Then do this
    # Then do this
```

- This is basically going to stop only once it is crashed and timed out

<br>

---

### Hurdles Challenge using While Loops

[André Roberge Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)

<br>

**Hurdle #3 — Jumping over hurdles using while loop**

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal:
    if wall_in_front():
        jump()
    else:
        move()
```

<br>

<div align = center>
    <img src = "H3.gif">
</div>

<br>

---

### Jumping over Hurdles with Variable Heights

[André Roberge Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)

<br>

**Hurdle #4 — Jumping over hurdles with variable heights that are located in different distance**

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal:
    if wall_in_front():
        jump()
    else:
        move()
```

<br>

<div align = center>
    <img src = "H4.gif">
</div>

<br>
