### Why do we need OOP and how does it work?

### Procedural Programming

Programming where we set up procedures of functions that do particular things

- One procedure leads to another procedure, and all in all, the computer’s mostly working from top to bottom and then jumping out into a function as needed
- One of the earliest paradigms of programming

<br>

### Object Oriented Programming

Programming that simplifies the relationships in one’s code and make it scalable for a larger and more complex project

- **Modularisation** — Using OOP, larger task can be split into smaller pieces, and each of those pieces can be worked on by separate teams, separate people
- **Reusability** — Each of those pieces become reusable if one needs the same functionality in the future

<br>

---

### How to use OOP: Classes and Objects

OOP tries to model a real-life objects and those object have things and they also can do things

- What the object has — **attributes**
    - modeled by a variable that’s attached to a particular object
- What the object does — **methods**
    - modeled by functions that a particular modeled object can do

<br>

> An object is just a way of combining some piece of data and some functionality altogether in the same thing

<br>

One can generate multiple versions of the same object

- `Blueprint` = a class that defines the attributes and methods of an object
- `Class` = a template that defines the data attributes and functions that an object can have
- `Object` = an instance of a class that defines the data attributes and functions that an object can have
- `Attributes` = the data that defines the state of an object
- `Methods` = The functions that describe the behaviour of an object

<br>

---

### Constructing Objects and Accessing their Attributes and Methods

### Blueprint for a car

- Specifies:
    - what the colour of the car is
    - how many wheels it should have
    - what its mileage is
    - how much fuel it has
    - the ability to drive
    - the ability to stop and break

<br>

### Class for a car

That blueprint which models a real-life car is known as the class — it is from the blueprint, the class, that one can generate as many object as one wants

<br>

### Object for a car

The actual thing that one is going to be using in one’s code

<br>

### Creating an object from a blueprint

1. Give the object a name 
2. Set it equal to the name of the class
3. Add the parentheses after the classname

<br>

```python
car = CarBlueprint()
```

- `CarBlueprint()` is a **class**, written with the first letter of each word capitalised (known as Pascal case)
- `Car` is the **object**, and it gets created from this CarBlueprint()

<br>

### Turtle Graphics

Turtle Graphics is a Python module that allows one to create graphics and animations by controlling a virtual “turtle” on the screen

- It is preloaded with every download of Python

<br>

[Python documentation turtle — Turtle Graphics](https://docs.python.org/3/library/turtle.html)

<br>

### Constructing Objects with Turtle

```python
# main.py
# To construct a new object
from turtle import Turtle
timmy = Turtle()
print(timmy)
```

```python
# Output
<turtle.Turtle object at 0x10e0dc050>
```

<br>

### Object Attributes

### Accessing attributes

```python
car.speed
```

- Identifies the object (car) and then it says, from this object get the speed attribute
    - Represent the speed of this particular car object

<br>

### Object Attributes with Turtle

```python

# To construct a new object
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)

# Using Screen blueprint to represent the window in which the turtle is going to show up
my_screen = Screen()
print(my_screen.canvheight)

#my_screen is the object
#canvheight is an attribute associated with that screen
```

```python
<turtle.Turtle object at 0x1083d71a0>
300
```

<br>

### Object Methods

```python
car.stop()
```

- Getting hold of the car object and then calling the stop function that’s associated the object

<br>

### Object Methods with Turtle

```python

# To construct a new object
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)

# Change the shape of timmy
timmy.shape("turtle")
# Change the colour of timmy
timmy.color("DarkGreen")
# Move timmy by 100 spaces
timmy.forward(100)

# Using Screen blueprint to represent the window in which the turtle is going to show up
my_screen = Screen()
print(my_screen.canvheight) #my_screen is the object #canvheight is an attribute associated with that screen

# exitonclick() function will allow one's programme to continue running until one clicks on the screen,
# then it exists one's code
my_screen.exitonclick()

```

```python
<turtle.Turtle object at 0x108827230>
300
```

<br>

<div align = center>
  <img src = "https://file.notion.so/f/f/a468339a-fa06-46af-a19a-112cfa0c051b/cc74c47a-e8c4-485e-8c0b-1c5f95837120/turtle.gif?table=block&id=13f5e786-f1f1-80a7-8eca-e8a94f1ab2f6&spaceId=a468339a-fa06-46af-a19a-112cfa0c051b&expirationTimestamp=1731801600000&signature=yomG1MfSkJ62Izf8NzP-yQfs8aqAJi91fWiGwFLPpJo&downloadName=turtle.gif">
</div>

<br>

---

### How to add Python Packages and use PyPi

### Python Packages

A package differs from a module in the sense that it is actually a whole bunch of code that other people have written lots and lots of files, all packaged together to achieve some sort of goal or purpose

<br>

### Pypi

Pypi is a bunch of software for the Python programming language that is developed and shared by the Python community

<br>

[PyPI PyPi · The Python Package Index](https://pypi.org/)

<br>

### Installing a package (Mac)

1. Go to preferences menu under Pycharm 
2. Select the Project tab on the left side
3. Go to Project Interpreter
4. Click the + button to install any package
5. On the PyPi website, note the name of the package that one wants to install
6. Coming back to Pycharm, search the package name inside the available packages
7. Once one finds it, select it then click install

<br>

e.g.

```python
import prettytable # import name_of_the_package
```

- To see the source code of the package, hover over the name of the package, then right click on it, then select go to implementation — this will take one to the Python file where this entire package is implemented

<br>

All one needs to do is look at the documentation for the package on PyPi and see how one can implement it into one’s project

<br>

---

### Practice Modifying Object Attributes and Calling Methods
<br>

```python
from prettytable import PrettyTable
table = PrettyTable()

# Print out your table and nicely format it in an ASCII style
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Change the alignment of the table from center to left
# Check the current alignment
print(table.align)

# Change the alignment
table.align = "l"

# Print the table
print(table)
```

```python
{'base_align_value': 'c', 'Pokemon Name': 'c', 'Type': 'c'}
+--------------+----------+
| Pokemon Name | Type     |
+--------------+----------+
| Pikachu      | Electric |
| Squirtle     | Water    |
| Charmander   | Fire     |
+--------------+----------+
```

<br>

---

### Python Objects Quiz

**Q1: What is the name of the Blueprint for creating objects in OPP?**

- Attribute
- Method
- **Class**
- Instance

A1: **Class**

<br>

**Q2: When the attributes and methods of the Class Blueprint for Car are as follows, what code is causing the error in the answer?**

```python
# Attributes:
num_of_seats
speed

# Methods:
drive()
brake()
```

- car.drive()
- car.num_of_seats = 2
- **car.brake = 0**
- print(car.speed)

A2: **car.brake = 0**

<br>

**Q3: What are the words that describe what goes inside my_toyota and my_fiat?**

```python
my_toyota = Car()
my_fiat = Car()
```

- Class
- Attribute
- Variable
- **Object**
- Method

A3: **Object**

<br>

