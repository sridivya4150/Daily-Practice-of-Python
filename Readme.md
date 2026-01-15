🐍 Python Basics – Beginner Notes

Python is a high-level, general-purpose programming language.
It is open-source, interpreted, and object-oriented.

Python was created by Guido van Rossum and first released in 1991.

---

WHY PYTHON?

1. Python is close to human language
2. Works on different platforms (Windows, Mac, Linux, etc.)
3. Allows developers to write programs with fewer lines of code
4. Supports procedural, object-oriented, and functional programming styles
5. Provides powerful libraries and frameworks such as Django, Flask (web development) and Pandas (data analysis)

---

APPLICATIONS

Python is used in many top companies:

1. Netflix
2. Spotify
3. YouTube
4. Uber
5. Instagram

---

DISADVANTAGES

1. Python is an interpreted language, so it can be slower than compiled languages like C or Java
2. Python consumes more memory
3. Global Interpreter Lock (GIL) prevents multiple threads from executing Python code at the same time

---

FIRST PROGRAM IN PYTHON

print("Hello, World!")

Explanation:
print() is a built-in function used to display output on the screen
"Hello, World!" is a string (text enclosed in single or double quotes)

---

COMMENTS IN PYTHON

Comments are notes for developers and are ignored by the compiler.

Single-line comment:

# This is a comment

Multi-line comment:
'''
This is a multi-line comment
'''

---

CHECKING PYTHON VERSION

import sys
print(sys.version)

---

SAVING PYTHON FILES

Python files are saved with the .py extension
Example: hello.py

---

INPUT AND OUTPUT IN PYTHON

print() -> used to display output
input() -> used to take input from the user

---

STATEMENTS

A program is a list of instructions called statements.
Python does not require semicolons at the end of statements.
Semicolons are optional and used only when writing multiple statements in one line.

---

VARIABLES

Variables are containers for storing data values.
They are created when a value is assigned.
No need to declare data type explicitly.
Variable names are case-sensitive.

Examples:
a = b = c = 100
a, b, c = 3, 'hi', 4.5

To check variable type:
type(a)

To delete a variable:
del a

---

VARIABLE NAMING STYLES

Camel Case:
myVariableName = "John"

Pascal Case:
MyVariableName = "John"

Snake Case:
my_variable_name = "John"

---

TYPE CASTING

Type casting converts one data type into another.

Example:
x = 5
y = float(x)

---


