### Python Primitive Data Types

1. `Strings` (e.g. `“Hello”`): comprised of characters strung together — have to create with double quote with them
    - Because they are a string of characters one can actually pull out each character individually by subscripting — a method of pulling out a particular element from a string
    
    e.g. H from “Hello”
    
    ```python
    # Subscripting
    # The number in between the square brackets determines which character one is going to pull out
      # The number just goes up from zero to 1 to 2, and so on and so forth
    
    print("Hello"[0])
    ```
    
    ```python
    H
    ```
    
    - Programmers always start counting from zero because they work with binary zeros and ones
        - Whenever they want to get hold of the first character or the first of anything, it always is at zero
        - Can also use negative number in indices
        ```python
        print("Hello"[-1])
        ```
        
        ```python
        o
        ```
        
        ```python
        print("Hello"[-2])
        ```
        
        ```python
        l
        ```
<br>

- Concatenating numbers in strings — won’t give us the result of mathematical calculation

  ```python
  # String
  print("123" + "456")
  ```
  
  ```python
  123456
  ```

<br>

2. `Integers`: Data type for whole numbers — numbers without any decimal places
    
    ```python
    print(123 + 456)
    ```
    
    ```python
    468
    ```
    
    Numbers are being calculated because one got actual numbers instead of strings
    
    - **Large integer**: 123,456,789
    
    ```python
    print(123_456_789)
    ```
    
    ```python
    # The computer actually removes those underscores and ignores it
    # The benefit is just for us humans to be able to visualise it more easily
    123456789
    ```
    <br>
3. `Floats(short for floating point number)`: Numbers in decimal places
    
    ```python
    print(3.14159)
    ```
    
    ```python
    3.14159
    ```
    <br>
4. `Booleans`: Data type which is used to test if something is true or if something is false, and for one’s programme to respond accordingly
    - Only two values — True, False
        - These values always begin with a capital letter T, F without any quotation marks around them
    ```python
    print(True)
    ```
    ```python
    print(False)
    ```
    <br>
***
### Data Types Quiz

**Q1: What is the wrong explanation?**

- 932 is an integer
- **“False” is a boolean value**
- 857.25 is a floating point number
- “523” is a string

A1: **“False” is a boolean value**

<br>

Q2: **What is the data type of the variable Mystery?**

`mystery = 734_529.678`

- Integers
- Strings
- Qurtle
- **Floats**

A2: **Floats**

<br>

**Q3: What are the values that you're going to print out in the next code?**

```python
street_name = "Abbey Road"
print(street_name[4] + street_name[7])
```

- eR

```python
"Abbey Road"
"Abbey Road"
"Abbey Road"
"Abbey Road"

"Abbey Road"
"Abbey Road"
"Abbey Road"
"Abbey Road"
"Abbey Road"
"Abbey Road"
"Abbey Road"
```

- en
- **yo**

A3: **yo**
    
<br>

***
### Type Error, Type Checking & Type Conversion

### Type Error

```python
len(12345)
```

```python
TypeError: object of type 'int' has no len()
```

- len() function’s argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set)
- len() function cannot take an integer or any other number data type as its argument
    
    **∴ Causing a type error**

<br>

### PAUSE 1. Fix the len() function so it has no more warnings or errors.

```python
len("12345")
```

```python
5
```

<br>

### Type Checking
One can check the data type of any value or variable in Python using the type() function.
<br>

### type()
Type functions returns the data type
```python
print(type("abc"))
```

```python
<class 'str'>
```
<br>

### PAUSE 2. Write out 4 type checks to print all 4 data types
- To see the type
    
    ```python
    print(type("Hello"))
    ```
    
    ```python
    <class 'str'>
    ```
    
    - The function checked the data type of the given data inside of the parentheses and returned a string as its data type

    <br>

    ```python
    print(type(123))
    ```
    
    ```python
    <class 'int'>
    ```
    
    <br>

    ```python
    print(type(3.14))
    ```
    
    ```python
    <class 'float'>
    ```
    <br>
    
    ```python
    print(type(True))
    ```
    
    ```python
    <class 'bool'>
    ```

<br>
  
### Type Conversion (Type Casting)

Type conversion, also known as type casting in Python is a process of converting one data type to another

e.g.

**Before**: Concatenate strings instead of performing a mathematical operation

```python
print("123" + "456")
```

```python
123456
```

**After conversion**: Strings are treated as numbers and added together to perform a mathematical operation

```python
print(int("123") + int("456")) 
```

```python
579
```
<br>

### Type Conversion functions for major primitive types

```python
int()
float()
str()
bool()
```

Sometimes, one cannot convert things into a different data type

e.g. 

```python
print(int("abc"))
```

```python
ValueError: invalid literal for int() with base 10: 'abc'
```

<br>

### PAUSE 3. Make this line of code run without errors
```python
print("Number of letters in your name: " + len(input("Enter your name")))
```

```python
name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: ")) # str
print(type(length_of_name)) # int

print("Number of letters in your name: " + str(length_of_name))
```

<br>

***
### Mathematical Operations in Python

**Addition**

```python
print(123 + 456)
```

```python
579
```

<br>

**Subtraction**

```python
print(7 - 3)
```

```python
4
```

<br>

**Multiplication**

```python
print(3 * 2)
```

```python
6
```

<br>

**Division**

```python
print(6 / 3)
```

```python
2.0
```

- Division results always come out with a floating point number
- Default Python behaviour
    - Implicit typecasting because Python is implicitly converting the result here into a floating point number

<br>

**Division (Removing the decimal places of the division result)**

```python
print(5 // 3)
```

```python
1 # Not 1.6666666666666667 -- Watch out when working with scientific numbers
```

<br>

**Raise a number to a power**

```python
print(2 ** 3)
```

```python
8
```

- Having the exponent being built into the language is one of the reasons why Python is really being loved by a lot of data scientists and mathematicians, because it is really optimised towards manipulating and handling numbers

<br>

### Order of priority in mathematical operation

- **PEMDASLR**
  1. Parentheses `()`
  2. Exponents `**`
  3. Multiplication & Division `*` or `/`
  4. Addition & Substraction `+` or `-`
  5. from Left to Right

<br>

### PAUSE 1. What is the output of this code?
```python
print(3 * 3 + 3 / 3 - 3)
```

```python
7
```

<br>

### PAUSE 2. Change the code so it outputs 3?
```python
print(3 * (3 + 3) / 3 - 3)
```

```python
3
```

<br>

***
### BMI Calculator

Body mass index (BMI) is a measurement used in medicine, which is used to check whether someone is underweight or obese. The formula used to calculate it is as follows:

BMI is the weight of the person divided by the square of the person's height.

```python
height = 1.65 
weight = 84
 
bmi = weight / height ** 2
 
print(bmi)
```
<br>

***
### Number Manipulation & F Strings in Python

```python
bmi = 84 / 1.65 ** 2
print(bmi)
```

```python
30.85399449035813
```

<br>

```python
print(int(bmi))
```

```python
30 # 30.85399449035813
```

- Converting float to integer floors the number — removing all of the remaining decimal places numbers, flooring it to the lowest whole number

<br>

### round()

Round function performs the rounding in the traditional mathematical sense, where when it is 0.5, it rounds up to the next whole number, and when it’s below that, it rounds up to the lower whole number

```python
print(round(bmi))
```

```python
31 # 30.85399449035813
```
<br>

```python
print(round(number, ndigits)) # number is the number one wants to round, and the second one, ndigits, is the number of digits one wants to round it to
```

e.g. **Rounding BMI to two decimal places**

```python
print(round(bmi, 2))
```

```python
30.85
```
<br>

### Assignment operator

Accumulate the results of one’s calculations

- +=
- -=
- *=
- /=

e.g.

```python
score = 0

# User scores a point
score += 1 # same as score = score + 1

print(score)
```

```python
1
```
<br>

### F strings

Makes it really easy to mix strings and different data types

**Without F strings**: conversion needed

```python
print("Your score is " + str(score))
```
<br>

**With F strings**

```python
score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")
```

- Add the character `f` in front of the string
- Put variable inside a set of curly braces

```python
Your score is = 0, your height is 1.8. You are winning is True
```

- All of these different data types got combined into a string by using an F in front of the string, and then using these curly braces to place one’s variables into the string
<br>

Using f strings, one can cut down on a lot of manual labour of inserting different data types into a string

<br>

***
### Mathematical Operations Quiz

**Q1: What are the values that you're going to print out with this code?**

```python
print(6 + 4 / 2 - (1 * 2))
```

- 3
- **6.0**
- 8.0
- 5

A1: **6.0**

<br>

**Q2: What is the data type of the resulting value of variable a in the following code?**

```python
a = int("5") / int(2.7)
```

- int
- **float**
- str
- bool

A2: **float**

<br>

**Q3: Where is the code that causes the error?**

```python
name = input("What is your name?")
print(f"Hello, {name}")
```

```python
name = input("What is your name?")
print("Hellow, " + name)
```

```python
age = 12
print(f"You are {age} years old")
```

```python
age = 12
print("You are " + age + " years old")
```

A3: **The fourth code**

<br>

