### Namespaces: Local vs. Global Scope

### Local Scope

Variables (or functions) declared inside functions have local scope (also called function scope). They are only seen by other code within the same block of code.

e.g.

```python
def my_function():
    my_local_var = 2

# This will cause a NameErrorr
print(my_local_var)

```

<br>

### Global Scope

Variables or functions declared at the top level (unindented) of a code file have global scope. It is accessible anywhere in the code file.

e.g.

```python
my_global_var = 3

def my_function():
    # This works no problems
    print(my_global_var)
```

<br>

**Example of Local and Global Scope**

```python
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
```

```python
enemies inside function: 2
enemies outside function: 1
```

<br>

**Example 2 of Local and Global Scope**

```python
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength) # This causes an NameError
```

```python
2
NameError: name 'potion_strength' is not defined
```

<br>

---

### Does Python Have Block Scope?

Unlike some other programming languages like C++ or Java, **there is no such thing as block scope in Python**

This means that variables created nested in other blocks of code e.g. for loops, if statements, while loops etc. don't get local scope. They are given function scope if they are within a function or global scope if they are not.

e.g.

```python
# Accessible anywhere
my_global_var = 1

def my_function():
    # Only accessible within my_function()
    my_local_var = 2

for _ in range(10):
    # Accessible anywhere
    my_block_var = 3

```

<br>

**Example 3 of Local and Global Scope**

```python
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]
print(new_enemy)

# vs.
def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)
```

<br>

---

### Prime Number Checker

A prime number is a number divisible by itself and one.

You must write an is_prime() function that verifies that the number taken over is a prime number. This function must return True or False.

For example, 7 is a prime number because it is divisible only by itself and 1.

However, 4 is not a prime number because it can be divided into 1, 2, or 4.

Note: 2 is a prime numbers because it is divisible only by itself and 1.

<br>

Input Example 1

73

Output Example 1

True

Input Example 2

75

Output Example 2

False

<br>

```python
def is_prime(num):
    if num <= 1:
        return False 
    if num == 2:
        return True 

    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True
```

<br>

---

### How to Modify a Global Variable

One can force the code allow one to modify something with global if one uses the global keyword before one uses it.

e.g. This will give one an error

```python
a = 1
def my_function():
    a += 1
    print(a)

```

<br>

But this will work

```python
a = 1
def my_function():
    global a
    a += 1
    print(a)
```

<br>

**Example of Modifying Global Scope**

```python
# Modifying Global Scope

enemies = 1

def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")
```

<br>

<aside align = justify>

  ⭐ It is strongly recommended to avoid modifying global scope, because it is confusing and it’s prone to creating bugs and errors. 
  Because the variable with global scope could have been created anywhere in one’s code, one would be modifying it completely independent of when one created it — It just makes everything more fallible, easier to fail
  One can use it within one’s code, but advised not to try to modify it within a function that has local scope

</aside>

<br>

## How to create a function that changes the global variable without modifying the global scope within the function?

```python
# Modifying Global Scope

enemies = 1

def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")
```

<br>

---

### Python Constants and Global Scope

Global scope can be incredibly useful, especially when one is defining constants

<br>

### **Global constants**

Variables which one defines and one is never planning on changing it ever again

<br>

### Naming Convention

Global constants are normally declared in `ALL_CAPS` with a underscore in between.

e.g.

```python
PI = 3.14159
GOOGLE_URL = "https://www.google.com"
```

<br>

---

### Scope Quiz

**Q1: What is the value that is output to the console when the code is executed?**

**Think you've become a computer without running the code and try to answer it.**

```python
def a_function(a_parameter):
    a_variable = 15
    return a_parameter
 
a_function(10)
print(a_variable)
```

- **NameError**
- 10
- 15
- SyntaxError

A1: **NameError**

<br>

**Q2: What is the value that is output to the console when the code is executed?**

**Think you've become a computer without running the code and try to answer it.**

```python
i = 50
def foo():
    i = 100
    return i
 
foo()
print(i)
```

- 100
- **50**
- 150
- NameError

A2: **50**

<br>

**Q3: What is the value that is output to the console when the code is executed?**

**Think you've become a computer without running the code and try to answer it.**

```python
def bar():
    my_variable = 9
 
    if 16 > 9:
      my_variable = 16
 
    print(my_variable)
 
bar()
```

- 9
- **16**
- NameError
- Nothing is output

A3: **16**

<br>

---
### Introducing the Final Project: The Number Guessing Game
1. Greets users
2. Tells users that the number will be chosen between 1 and 100
3. Asks users to choose difficulty between easy or hard
4. Tells users how many attempts users have remaining
5. Asks users to make a guess
6. Tells users that their chosen number is either too high or too low or correct

<br>

