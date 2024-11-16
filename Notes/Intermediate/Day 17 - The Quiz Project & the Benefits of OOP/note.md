### How to create your own Class in Python

```python
class Car:
```

- Have the class keyword followed by the name of the class, and then a semicolon
- All of the code that’s in the class will follow this and it will be indented

<br>

```python
class User:
    pass
user_1 = User()
```

- To leave the class (or function) empty, one can use a `pass` keyword
    - `pass` keyword makes the code to continue to the next line of code

<br>

### Naming convention for a class

A name of the class should have the first letter of every word capitalised (PascalCase) 

<br>

- Different to camelCase as camelCase has the first word in lowercase, but every subsequent word has its first letter capitalised
- Also different to snake_case, where all the words are lowercase, but they’re separated by an underscore

<br>

> PascalCase is being used for the class names camelCase is rarely used in Python programming, and snake_case is being used pretty much to name everything else

 <br>

---

### Working with Attributes, Class Constructors and the \__init__ () Function

<br>

```python
class User:
    pass
user_1 = User()

# To create an attribute for the class
# Tap into the object and then add an attribute
user_1.id = "001"
user_1.username = "jisu"

print(user_1.username)
```

```python
jisu
```

<br>

### Constructor

A part of the blueprint that allows one to specify what should happen when one’s object is being constructed

- This is also known in programming as initialising an object
    - to set (variables, counters, switches, etc) to their starting values at the beginning of a programme or subprogramme
    - to clear (internal memory, a disk, etc.) of previous data in preparation for use

<br>

### To create a constructor

```python
class Car:
    def __init__(self):
    # initialise attributes
```

- It is special because it is not just the def keyword and then the name of the function
    - It’s got two underscores either side of the name
- It is a method that the Python interpreter knows about and knows that it has a special function
    - It’s normally used to initialise the attributes
<br>

If inside the class:

```python
class User:
    def __init__(self):
        print("new user being created...")
```

<br>

### Set attributes in the constructor

```python
class Car:
    def __init__(self, seats):
        self.seats = seats
```

- Inside class, there is an init function
    - Inside the init function, in addition to the thing called self, which is the actual object that’s being created or being initialised, in addition one can add as many parameters as one wishes
        - That parameter is going to be passed in when an object gets constructed from the class
            - Once one receives the data, then one can use it to set the object’s attributes
<br>

```python
my_car = Car(5)
```

- Object is created by calling the name of the class and adding the parentheses
    - If inside the init function, one has some additional parameters, one can also pass in data to those parameters, which will be used to set the attributes for the object
- Once this line of code has completed:
    - my_car.seats is going to be equal to five
    - exactly same as when codes:
    
    ```python
    my_car.seats = 5
    ```
    
<br>

e.g.

```python
class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # Can use default value

user_1 = User("001", "Angela") # There should be two parameters as the number of defined parameters is two
print(user_1.followers)
# Output: 0
```
<br>

---

### Adding Methods to a Class

### Method

```python
class Car:
    def enter_race_mode():
        self.seats = 2
```

- Inside the class declaration, there is a function
- When a function is attached to an object, then it is called a method

<br>

### To call a method

```python
my_car.enter_race_mode()
```

<br>

e.g. 

```python
class User:

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Angela")
user_2 = User("002", "Jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

```

<br>

---

### Quiz Project Part 1: Creating the Question Class

1. A question will be asked to the user and they’ll select True or False
2. Then, the programme will tell them if they got it right or wrong and give them a score

<br>

### Creating the Question Class

**Attributes**:

1. The Question Class might have a text attribute for the question text
2. And it might also hold an answer attribute
- These two attributes should be initialised with a value when a new question object is created from this class

<br>

In question_model.py file, create a new class called question — this question class should have an init method which will initialise two attributes the text and the answer

```python
# question_model.py
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

<br>

---

### Quiz Project Part 2: Creating the List of Question Objects from the Data

Create a question bank of questions objects in this format:

```python
question_bank = [
    Question(q1, a1),
    Question(q2, a2),
    Question(q3, a3),
    ...
]
```

<br>

```python
# question_model.py
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

```python
# data.py
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
             "you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, "
             "you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

```

```python
# main.py
from question_model import Question
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)

```

<br>

---

### Quiz Project Part 3: The QuizBrain and the next_question() Method

<br>

TODO:

1. Asking the questions
2. Checking if the answer was correct
3. Checking if one is at the end of the quiz

<br>

QuizBrain class will have two attributes:

1. question_number = 0
2. questions_list

<br>

QuizBrain class will have a method:

1. next_question — which will pull up the next question from the list

<br>

Inside the quiz_brain.py file, create the QuizBrain class. Add those two attributes; one is the question number which starts out with default value and the other is the question list which is going to be initialised when creating a new QuizBrain. Then, the question bank will be passed to question_list when new QuizBrain is initialised. After then, create a method called next_question inside the QuizBrain.  This method needs to retrieve the item at the current question number from the question list. Once item is there, use the input function to show the user the question text and ask for the user’s answer.

<br>

```python
# question_model.py
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

```python
# data.py
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
             "you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, "
             "you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

```

```python
# main.py
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()
```

```python
# quiz_brain.py
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q{self.question_number}: {current_question.text} (True / False): ")
```

<br>

---

### Quiz Project Part 4: How to continue showing new Questions

<br>

Create another method called still_has_questions() that returns a boolean depending on the value of question_number. Then use the while loop to show the next question until the end

<br>

```python
# question_model.py
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

```

```python
# data.py
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
             "you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, "
             "you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

```

```python
# main.py
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
```

```python
# quiz_brain.py
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q{self.question_number}: {current_question.text} (True / False): ")
```

<br>

---

### Quiz Project Part 5: Checking Answers and Keeping Score

For QuizBrain class, add one more method, check_answer(), for the ability to check the answer that the user inputted and see if it was correct — this means that the programme needs to keep track of the user’s score. Also, add score attribute which has a default value of zero to begin with — this will increase every time users get a question right.

<br>

```python
# question_model.py
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

```

```python
# data.py
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
             "you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, "
             "you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

```

```python
# main.py
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score} / {len(question_bank)}")
```

```python
# quiz_brain.py
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True / False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

```

<br>

---

### The Benefits of OOP: Use Open Trivia DB to Get New Questions

<br>

To get new questions, one can use [Open Trivia Database](https://opentdb.com/), which is a free-to-use user contributed trivia question database. It has over 3000 verified questions to pick from.  

<br>

1. Take a look at their API to see how one can generate some questions
2. Select the number of questions, category, difficulty, type, and encoding then generate API URL
3. After getting API URL, open up a new tab and go to that location
4. Copy data generated in a JSON format (JavaScript Object Notation)
5. Paste it in data.py

<br>

```python
question_data = [
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "The common software-programming acronym 'I18N' comes from the term 'Interlocalization'.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "hard", "category": "Science: Computers",
     "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "Linux was first created as an alternative to Windows XP.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "To bypass US Munitions Export Laws, the creator of the PGP published all the source code in book form. ",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "The logo for Snapchat is a Bell.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "'HTML' stands for Hypertext Markup Language.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "The very first recorded computer 'bug' was a moth found inside a Harvard Mark II computer.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "The HTML5 standard was published in 2014.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "Ada Lovelace is often considered the first computer programmer.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "The first computer bug was formed by faulty wires.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "MacOS is based on Linux.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "hard", "category": "Science: Computers",
     "question": "DHCP stands for Dynamic Host Configuration Port.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "RAM stands for Random Access Memory.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "Linus Sebastian is the creator of the Linux kernel, which went on to be used in Linux, Android, and Chrome OS.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "FLAC stands for 'Free Lossless Audio Condenser'&#039;",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "'Windows NT' is a monolithic kernel.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "AMD created the first consumer 64-bit processor.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "The last Windows operating system to be based on the Windows 9x kernel was Windows 98.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "The first dual-core CPU was the Intel Pentium D.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "The Windows ME operating system was released in the year 2000.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "Early RAM was directly seated onto the motherboard and could not be easily removed.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "A Boolean value of '0' represents which of these words?",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "The open source program Redis is a relational database server.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "hard", "category": "Science: Computers",
     "question": "The T-Mobile Sidekick smartphone is a re-branded version of the Danger Hiptop.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "Time on Computers is measured via the EPOX System.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science: Computers",
     "question": "Android versions are named in alphabetical order.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "The Windows 7 operating system has six main editions.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
     "question": "The programming language 'Python' is based off a modified version of 'JavaScript'.",
     "correct_answer": "False", "incorrect_answers": ["True"]}
]

```

<br>

