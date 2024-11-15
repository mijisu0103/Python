### Functions with Inputs

### PAUSE 1 - Review

- Create a function called `greet()`.
- Write 3 print statement inside the function
- Call the `greet()` function and run your code

<br>

```python
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice?")
    
greet()
```

<br>

### Functions with Inputs

```python
def my_function(something):
    # Do this with something
    # Then do this
    # Finally do this

my_function(123)

#something = parameter -- the name of the data that's being passed in
#123 = argument -- the actual value of the data
```

- Functions can do something different depending on the input that users give them
- If users change that input, then functions will provide a different piece of data
- The **argument** is the actual piece of **data that’s going to be passed over to this function** **when it’s being called**
- The **parameter** is **the name of that data (argument)** — use the parameter **inside the function to refer to it and to do things with it**

<br>

```python
# Functions that allows for inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Jisu")
```

<br>

---

### Life in Weeks

I realised how little time we actually had after reading an article called Tim Urban's Your Life in Weeks.

If you live to the age of 90, create a life_in_weeks() function using math and f-Strings that tells us how many weeks we have left.

Use the current age as an input and output a message indicating the time we have left in the following format:

<br>

> There are now x weeks left.

<br>

```python
def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")
 
 
life_in_weeks(23)
```

<br>

---

### Positional vs. Keyword Arguments

### PAUSE 1

Create a function with multiple inputs 

```python
# PAUSE 1 - Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
greet_with("Jisu", "London")
```

<br>

### Positional Arguments

By default, when one creates a function in Python, it will keep the order of arguments in the function definition.

<br>

e.g. In the function below, the first argument that goes in will always be printed before the second one. a = 2, b = 1

```python
def my_function(a, b)
  print(a)
  print(b)
  
 my_function(2, 1)
 #It will print:
 # 2
 # 1
 
 # However
 my_function(1,2)
 # will print:
 # 1
 # 2
```

<br>

### Keyword Arguments

One can use keywords when one provides the arguments when one calls a function so that there is less confusion which value is assigned to which input parameter.

<br>

### PAUSE 2

Modify the function so that it prints the expected values.

```python
def my_function(a, b, c):
    #Do this with a
    #Then do this with b
    #Finally do this with c

my_function(a=1, b=2, c=3)

# When one actually change the order around, it does not matter how one orders it
my_function(c=3, a=1, b=2)
# It's still going to abide by these bindings
# c will still be 3 and a will still be 1
```

<Br>

### PAUSE 3

Call the greet_with() function using keyword arguments.

```python
greet_with(name="Jisu", location="London")
greet_with(location="London", name="Jisu")
```

<Br>

---

### Love Calculator

You will create a calculate_love_score() function to test compatibility between two names. To calculate the love score between two people:

1. Take the names of two people and check the number of appearances of the word 'TRUE' in each word.
2. Then, check how many times each alphabet in the word "LOVE" appears.
3. Please combine these numbers to create a 2-digit number and print it out.

e.g.

name1 = "Angela Yu" 

name2 = "Jack Bauer"

- T 0 occurrences

- R 1 occurrence

- U 2 occurrences

- E occurs twice

Total = 5

<br>

- L 1 occurrence

- O 0 occurred

- V 0 occurrences

- E 2 occurrences

Total = 3

<br>

Love Score = 53

<br>

```python
def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    
    true_count = sum(combined_names.count(char) for char in "true")
    love_count = sum(combined_names.count(char) for char in "love")
    
    love_score = print(f"{true_count}{love_count}")

    return love_score
```

<br>

---

### Caesar Cipher Part 1 — Encryption

```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount

        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

encrypt(original_text=text, shift_amount=shift)

```

<br>

---

### Caesar Cipher Part 2 — Decryption

```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.

# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
```

<br>

