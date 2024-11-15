### Using the for loop with Python Lists

**Loops** allows one to execute the same line(s) of code multiple times — used for things that have to happen over and over and over again

<br>

### PAUSE 1- Be a Computer

Predict what will be printed from the code below:

```python
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
 # Once loop is finished execute the following code
 print(fruits)
```

```python
Apple
Apple pie
Peach
Peach pie
Pear
Pear pie
["Apple", "Peach", "Pear"]
```
<br>

---

### Highest Score

```python
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

total_exam_score = sum(student_scores)

sum = 0
for score in student_scores:
    sum += score

print(sum)
```
<br>

### PAUSE 1 - Max

There are also a built-in Python methods called max() and min(), which allow you to pass in a List of numbers, and it will give you the highest number or the lowest number.

Your job is to figure out how the Python programmers might have built this functionality using loops and conditionals.

```python
# PAUSE 1 - Max
print(max(student_scores))
```

<br>

### Complete this challenge without using max()

```python
# Without using Max
exam_scores = [8, 65, 89, 86, 55, 91, 64, 89]
max_score = 0
for score in exam_scores:
    if score > max_score:
        max_score = score

print(max_score)
```
<br>

---

### for Loops & the range() function

### **range()**

Range function is helpful if one wants to generate a range of numbers to loop through — range() does not do anything alone, that is, it has to be used in conjunction with another function

<br>

```python
# Range Function with For Loop
# The end number won't be included
for number in range(1, 10):
    print(number)
```

```python
1
2
3
4
5
6
7
8
9
```

```python
# Adding a step
for number in range(1, 11, 3):
    print(number)
```

```python
1
4
7
10
```

<br>

### PAUSE 1 — The Gauss Challenge

Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.

```python
# PAUSE 1 - The Gauss Challenge
total = 0
for number in range(1, 101):
    total += number
print(total)
```

```python
5050
```
<br>

---

### FizzBuzz

You will automatically print out the answers to the FizzBuzz game by writing the program. The rules of the FizzBuzz game are as follows:

- The program must output each number from 1 to 100 in turn, and must include the number 100.
- However, if the number is divided by 3, you should output "Fizz" instead of outputting the number.
- If the number falls by 5, you must output "Buzz" instead of printing the number.
- And if the numbers are separated by both 3 and 5, you have to output "FizzBuzz" instead of outputting the numbers, for example, when it's 15.
- For example, it could start as follows:
    
    ```python
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
    ...etc
    ```
    

```python
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
```
<br>

