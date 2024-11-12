### **print()**
Print function outputs the content inside of parentheses on one’s console

__Strings__ - A string of characters

- When using strings for print function, strings go inside the parentheses
- Strings should be wrapped with double quote

e.g. 
Use what you learnt to print out the words "Hello world!" with Python code.
Then click the run button to execute your code.
```python
print("Hello World!")
```
```python
Hello World!
Process finished with exit code 0
```
<br>

***
### Printing Practice
Write a program to print the following recipe on the output console. The text you want to print has already been provided, and it must be made into code. Your code must print five lines exactly the same as the example output. Be careful not to modify the existing text, as all text, punctuation, and case letters must match!
```python
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")
```
<br>

***
### String Manipulation & Code Intelligence

> `\n`  creates a new line

e.g.
### 1. Use \n to add another line of "Hello world".
So the resulting output looks like this:
```
Hello world!
Hello world!
Hello world!
```
<br>

```python
print("Hello world!\nHello world!\nHello world!")
```

```
Hello world!
Hello world!
Hello world!

Process finished with exit code 0
```
<br>

> `+` concatenates strings

<br>

e.g.
### PAUSE 2. Add a space between the strings

So there is a space between the string Hello and Angela when the print statement runs.

The output should look like this:
```
Hello Angela
```

<br>

```python
print("Hello" + " " + "Angela")
```
```
Hello Angela

Process finished with exit code 0
```

<br>

***
### Debugging Practice
Look at the code in the code editor. Every 5 lines of the code has errors. Fix the code so it runs without errors.
Run each line and try debugging each line using error messages and feedback.
```python
print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")
```

<br>

***
### The Python Input Function
### **input()**

Input function asks a user for a data 
Inside of the parentheses, one should give a prompt — the prompt is the text that goes into the input command
The prompt gives the user a hint as to what kind of data one wants
When the code is run, it will print out the prompt being ready for a user to type in some piece of data

e.g.
**PAUSE 1. Update the code to add an exclamation mark** 
Using what you have learnt in this lesson and previous, can you figure out how take user input and slot it in between 2 strings?
You are looking to print a sentence like this:

```
Hello Name!
```

e.g. 
```
Hello Angela!
```

<br>

```python
print("Hello " + input("What is your name?") + "!")
```
```
What is your name?Jisu
Hello Jisu!

Process finished with exit code 0
```

<br>

`#` is used for a comment that the computer will completely ignore — it won’t be executed
- **Shortcut**: highlight the text that one wants to turn into a commend then press `Cmd (or Ctrl on Windows) + /`

<br>

***
### Python Variables
The value that can be changed or can be varied
```python
name = "Jack"
print(name)
```
```
Jack
```
```python
name = "Angela"
print(name)
```
```
Angela
```

<br>

### len()
The len() function returns the length of a string
e.g. **PAUSE 1. Check the length of the user input** Using what you have learnt about the len() function and the input() function. Try to print out the number of characters in the user input. Write everything in just 1 line of code.
```python
print(len(input ("What is your name?")))
```
```
6
```
<br>

OR: **PAUSE 2. Split everything into variables.**

Split each step in the previous exercise into a separate variable. One variable called username and one called length. Use the variable username in the len calculation.
```python
username = input("What is your name?")
length = len(username)
print(length)
```
```
6
```
<br>

***
### Variables Practice
We have two variables, glass1 and glass2. Glass1 has milk and glass2 has juice. Write the code on the 3 lines that exchange the contents of the variables. Do not enter the words "milk" or "juice." You can only use variables to solve this exercise.

<br>

```python
glass1 = "milk"
glass2 = "juice"

temp = glass1
glass1 = glass2
glass2 = temp
```

<br>

***
### Variable Naming

The name of the variable has to be **one single unit** — In order to separate words in Python one can use the underscore(_)
- One can actually have multiple words in the name of one’s variable separating them using underscore(_)
    - space between them are not allowed as that will cause a syntax error <br>
    e.g. user_name
- One can use numbers in the name of one’s variable but they cannot be at the beginning of the name of the variable
- It is usually good practice to not use the names of the functions like print and input as the names of one’s variables — syntax highlighting gets messed up — can lead to confusion
- The most important one is to make one’s code readable <br>
    e.g. N and L are not going to have a lot of meaning — better to name variables that makes sense to all
- The name that is associated with a certain piece of data should be consistent through one’s code — ensure that data names are consistent <br>
    e.g. for a variable called name, if one types nama instead (mistyping), this will not be recognised as the same variable anymore — thus will display a name error for this specific line of code for this specific variable with a name error
    - As long as the spellings for the specific piece of data are identical everywhere in the document, the computer does not care at all even if it is not an existing word

<br>

***
### Variable Naming Quiz

**Q1: What is the correct Python code?**

- var a =12
- **a = 12**
- a: 12
- 12 = a

A1: **a = 12**

<br>

**Q2: What would be the most appropriate variable name for player 1's username?**

- p1 user name = “jackbauer”
- 1_player_username = “jackbauer”
- **player1_username = “jackbauer”**
- plu = “jackbauer”

A2: **player1_username = “jackbauer”**

<br>

**Q3: Which code is causing the error? Please tell me the type of error that will occur if you want to score extra points.**
```python
time_until_midnight = "5"
print("There are " + time_until_Midnight + " hours until midnight")
```
```python
input = "5"
print("There are " + input + " hours until midnight")
```
```python
time_until_midnight = "5"
print("There are " + time_until_midnight + " hours until midnight")
```
A3: **the first code — because the time_until midnight variable’s name does not match with its name on the second line of the code, time_until_Midnight — thus will display a name error**

