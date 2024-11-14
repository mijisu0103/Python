### Random Module

**Randomisation**: a concept that is important when one wants to create computer programs that have a degree of unpredictability — randomness

**Deterministic**: performs repeatable actions in a fully predictable way

<br>

> Python uses Mersenne Twister to create pseudo random number

<br>

**Module** — each module is responsible for a different bit of functionality of one’s programme

```python
# Random module
import random

random_integer = random.randint(1, 10)
print(random_integer)
```

<br>

> Random module = random variable generators

<br>

- uniform bytes (values between 0 and 255)
- uniform within range
- pick random element pick random samplepick weighted random sample generate random permutation
- uniform triangular normal (Gaussian( lognormal negative exponential gamma beta pareto Wellbull circular uniform von Mises
- General notes on the underlying Mersenne Twister core generator:
    - The period is 2**19937-1
    - It is one of the most extensively tested generators in existence
    - The random() method is implemented in C, executes in a single Python step, and is, therefore, threadsafe

<br>

### Create and use a module

1. Create a Python file (.py) and name it
2. Inside the module, write a code 
3. Go back to main entry point file — usually a primary file that one uses where one write most of one’s starting and core code
4.  On one’s main entry point file, on the top of the code, add:
    
    ```python
    import module_name
    
    #e.g.
    print (module_name.variable)
    ```

<br>

### Use case of Random module

```python
import random

random_integer = random.randint(1, 10)
print(random_integer)

# 0 <= number < 1
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

# 0 <= number < 10
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

# 0 <= number in float <= 10
random_float = random.uniform(1, 10)
print(random_float)
```

<br>

### PAUSE 1 - Heads or Tails

```python
import random

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
	  print("Heads")
else:
    print("Tails")
```
<br>

---

### Understanding the Offset & Appending Items to Lists

> **List** = A data structure — a way of organising and storing data in Python
> 

```python
# Components inside of square brackets can be in any data type, and they can have different data types to each other
fruits = [item1, item2]
```

<br>

**States of America in a List**

```python
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kensas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
```

- One can use lists to store many pieces of related data, but also have an order
    - The order is determined by the order in the list

<br>

**Querying a data based on its order**

```python
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kensas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america[0])
```

- Index (number in square bracket) — starts from zero
    - Instead of being the position, actually being an offset or a shift from the start of the list
        - Delaware is right at the beginning of the list, so it has an offset or a shift of zero
        - Pennsylvania is shifted from the beginning by one pair, is shifted from the beginning by two

- Negative Index — starts from -1, starting from the end of list and ending at the beginning of the list

<br>

**Editing a data in a list**

```python
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kensas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

states_of_america[1] = "Pencilvania"

print(states_of_america[1])
# Pencilvania
```

<br>

**Add a data in list (append())**

```python
# Add a data at the end of the list
states_of_america.append("Angelaland")
```

<br>

**Add a list in an existing list (extend())**

```python
# Add a list at the end of an existing list
states_of_america.extend(["Angelaland", "Jack Bauer Land"])
```

<br>

---

### Who will pay the bill?

Russian roulette for the bill

```python
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st Option
print(random.choice(friends))

# 2nd Option
random_index = random.randint(0, 4)
print(friends[random_index])
```
<br>

---

### IndexErrors & Working with Nested Lists

```python
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(len(states_of_america))

num_of_states = len(states_of_america) # 50

print(states_of_america[num_of_states - 1])

# dirty_dozen
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
# [['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'], ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]
```
<br>

---

### List & IndexError Quiz

**Q1: Please check the following list.**

```python
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
```

**What is the code that outputs "Apples"?**

- fruits[3]
- fruits[4]
- fruits.Apples()
- **fruits[-5]**
- fruits[-4]

A1: **fruits[-5]**

<br>

**Q2: Please check the code below.**

```python
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)
```

**What is the output is output?**

```python
["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Lemons"]
```

```python
["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Lemons"]
```

```python
["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Melons", "Lemons"]
```

```python
["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Melons", "Lemons"]
```

A2: **4th code**

<br>

**Q3: Please check the code below.**

```python
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1])
```

**What is the output value?**

- “Spinach”
- “Strawberries”
- **“Kale”**
- [”Spinach”, “Kale”, “Tomatoes”, “Celery”, “Potatoes”]
- “Nectarines”

A3: **“Kale”**

<br>
