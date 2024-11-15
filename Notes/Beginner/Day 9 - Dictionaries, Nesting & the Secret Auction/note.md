### The Python Dictionary: Deep Dive

Dictionary in Python is a data structure that allows one to associate a key to a value and pair the two pieces of data together

<br>

### Dictionary format

> {Key: Value}

<br>


## Creating a dictionary in Python

```python
colours = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow"
}
```

<br>

### Retrieving items from a dictionary

```python
print(colours["pear"])
# Output: "green"
```

<br>

### Creating an empty dictionary

```python
my_empty_dictionary = {}
```

<br>

### Adding new items to an existing dictionary

```python
colours["peach"] = "pink"
```

<br>

### Editing an existing value in a dictionary

```python
colours["apple"] = "green"
```

<br>

### Looping through a dictionary and print all the keys

```python
for key in colours:
    print(key)
```

<br>

### Looping through a dictionary and print all the values

```python
for values in colours:
    print(colours[values])
```

<br>

### Example of dictionary usage

```python
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# Retrieve an item from the dictionary
print(programming_dictionary["Bug"])
# Output: An error in a program that prevents the program from running as expected.

# Add a new entry in the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)
# Output: {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# Output: {"Bug": "A moth in your computer.","Function": "A piece of code that you can easily call over and over again.","Loop": "The action of doing something over and over again"}
# If one makes a typo thus key does not exist in the dictionary, then the new key:value pair will be created and added to the existing dictionary

# Loop through a dictionary
for thing in programming_dictionary:
    print(thing) # print keys
    print(programming_dictionary[thing]) # print values
# Output:
# Bug
# A moth in your computer.
# Function
# A piece of code that you can easily call over and over again.
# Loop
# The action of doing something over and over again.

```

<br>

---

### Grading Program

You can access the student_scores database, which contains students' test scores. The key in student_scores is the students' name and the value is their test score.

Please write a program that converts your scores into grades.

At the end of the program, you must have a new dictionary called student_grads, which must have the student name as a key and the rated grade as a value.

The final version of the student_graders dictionary will be verified.

- *Never ** modify lines 1-7 to avoid changing the existing student_scores dictionary.

The following are based on scores:

- 91 - 100 points: Grade = "Outstanding"
- 81 - 90 points: Grade= "Exceeds Expectations"
- 71 - 80 points: Grade = "Acceptable"
- 70 points or less: Grade = "Fail"

<br>

```python
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
 
student_grades = {}

for student in student_scores:

    score = student_scores[student]

    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
```

<br>

---

### Nesting Lists and Dictionaries

One can mix and match various data types to achieve one’s desired structure.

Instead of a String value assigned to a key, one can replace it with a List or Dictionary. That is, one can nest a List or Dictionary in a Dictionary like this:

```python
{
    Key: [List],
    Key2: {Dict}
}
```

<br>

### Nested List in Dictionary

```python
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}
```

<br>

### PAUSE 1

Print “Lille” from travel_log list

```python
print(travel_log["France"][1])
```

<br>

### Nested List inside another list

```python
nested_list = ["A", "B", ["C", "D"]]
```

<br>

### PAUSE 2

Print “D” from nested_list list

```python
print(nested_list[2][1])
```

<br>

### Nested Dictionary inside a Dictionary

### Pause 3

Print “Stuttgart ” from travel_log list

```python
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
print(travel_log["Germany"]["cities_visited"][2])
```

<br>

---

### Python Dictionaries Quiz

**Q1: What is the code to change starting_dictionary to final_dictionary?**

```python
starting_dictionary = {
    "a": 9,
    "b": 8,
}

final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}
```

- final_dictionary = starting_dictionary.append({”c” : 7})
- final_dictionary = starting_dictionary += {”C”: 7}
- final_dictionary = starting_dictionary[”c” ]: 7
- final_dictionary = starting_dictionary[”c”] = 7
- **starting_dictionary[”c”] = 7**
    
    **final_dictionary = starting_dictionary**
    

A1: **5th code**

<br>

**Q2: Where is the code that causes the error?**

```python
dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
```

- dict[”c”] = [1, 2, 3]
- for key in dict:
    
        dict[key] += 1
    
- dict[1] = 4
- **print(dict[1])**

A2: **4th code**

<br>

**Q3: What is the code that outputs "Steak"?**

```python
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
```

- print(order[”main”][2])
- print(order[”dessert” -1][2][0])
- print(order[main][2][0]
- **print(order[”main”][2][0]**

A3: **4th code**

<br>

