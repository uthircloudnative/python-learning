# Python Basics Learning Repository

> **Note:** This content is auto-generated based on the available program files in this repository.

Welcome to the Python Basics Learning Repository! This comprehensive guide covers fundamental Python programming concepts through practical examples and exercises. Each topic builds upon the previous one, making it perfect for entry-level learners.

## 📚 Table of Contents

1. [Print Function](#1-print-function)
2. [Math Operators](#2-math-operators)
3. [Built-in Functions](#3-built-in-functions)
4. [Formatting](#4-formatting)
5. [String Operations](#5-string-operations)
6. [Number Operators](#6-number-operators)
7. [Type Conversion](#7-type-conversion)
8. [Comparison Operators](#8-comparison-operators)
9. [Conditional Statements](#9-conditional-statements)
10. [Ternary Operator](#10-ternary-operator)
11. [Logical Operators](#11-logical-operators)
12. [For Loops](#12-for-loops)
13. [Nested Loops](#13-nested-loops)
14. [Iterables](#14-iterables)
15. [While Loops](#15-while-loops)
16. [Even Number Example](#16-even-number-example)
17. [Functions](#17-functions)
18. [Function Keyword Arguments](#18-function-keyword-arguments)
19. [Function Default Arguments](#19-function-default-arguments)

---

## 1. Print Function

**File:** `1_print_function.py`

### Theory

The `print()` function is one of the most fundamental functions in Python. It outputs data to the console, making it essential for displaying results, debugging, and user interaction.

### Key Concepts

- **Purpose**: Display output to the console
- **Syntax**: `print(value1, value2, ...)`
- **Default behavior**: Adds a newline character after output

### Example

```python
print("Hello Python")
```

### Learning Objectives

- Understand basic output in Python
- Learn the syntax of the print function
- Practice displaying text and variables

---

## 2. Math Operators

**File:** `2_math_operator.py`

### Theory

Python provides various arithmetic operators for performing mathematical calculations. These operators work with numeric data types and follow standard mathematical precedence rules.

### Key Concepts

- **Addition (`+`)**: Adds two numbers
- **Subtraction (`-`)**: Subtracts the second number from the first
- **Multiplication (`*`)**: Multiplies two numbers
- **Division (`/`)**: Divides and returns a float result
- **Exponentiation (`**`)\*\*: Raises a number to a power

### Example

```python
print(2+8)     # Addition: 10
print(10-8)    # Subtraction: 2
print(2*8)     # Multiplication: 16
print(10/7)    # Division: 1.4285714285714286
print(10**4)   # Exponentiation: 10000
```

### Learning Objectives

- Master basic arithmetic operations
- Understand operator precedence
- Practice mathematical calculations in Python

---

## 3. Built-in Functions

**File:** `3_builtin_function.py`

### Theory

Python provides many built-in functions that perform common operations without requiring additional imports. The `max()` and `min()` functions are essential for finding extreme values in datasets.

### Key Concepts

- **max()**: Returns the largest value from given arguments
- **min()**: Returns the smallest value from given arguments
- **Multiple arguments**: Both functions can accept multiple parameters
- **Expression evaluation**: Functions can evaluate expressions as arguments

### Example

```python
print(max(19, -7, 28, 78))           # Returns: 78
print(max(19, -7, 28, 78, (10*10)))  # Returns: 100
print(min(19, -7, 28, 78))           # Returns: -7
```

### Learning Objectives

- Understand built-in function usage
- Learn to find maximum and minimum values
- Practice function calls with multiple arguments

---

## 4. Formatting

**File:** `4_formatting.py`

### Theory

Code formatting is crucial for readability and maintainability. Python emphasizes clean, readable code structure.

### Key Concepts

- **PEP 8**: Python's style guide for code formatting
- **Indentation**: Use 4 spaces (not tabs)
- **Variable naming**: Use descriptive, lowercase names with underscores
- **IDE Integration**: VS Code's "Format on Save" feature

### Example

```python
x = 1
length = 5
width = 10
```

### Learning Objectives

- Understand Python formatting standards
- Learn proper variable naming conventions
- Practice clean code writing

---

## 5. String Operations

**File:** `5_string.py`

### Theory

Strings are sequences of characters enclosed in quotes. Python provides extensive string manipulation capabilities, making text processing powerful and intuitive.

### Key Concepts

- **String creation**: Single or double quotes
- **Indexing**: Access characters by position (0-based)
- **Negative indexing**: Access from the end (-1 is last)
- **Slicing**: Extract substrings using `[start:end]`
- **String methods**: Built-in functions for manipulation

### Common String Methods

- `len()`: Get string length
- `upper()`: Convert to uppercase
- `lower()`: Convert to lowercase
- `index()`: Find substring position
- `find()`: Find substring (returns -1 if not found)
- `replace()`: Replace substrings
- `split()`: Split string into list

### Example

```python
language_name = "Python Language"
print(len(language_name))        # Length: 15
print(language_name[0])          # First character: 'P'
print(language_name[-1])         # Last character: 'e'
print(language_name[0:6])        # Slice: 'Python'
print(language_name.upper())     # Uppercase: 'PYTHON LANGUAGE'
```

### Learning Objectives

- Master string creation and manipulation
- Understand indexing and slicing
- Practice common string operations

---

## 6. Number Operators

**File:** `6_number_operators.py`

### Theory

Python supports various numeric operations and mathematical functions. The `math` module provides additional mathematical capabilities beyond basic operators.

### Key Concepts

- **Floor Division (`//`)**: Integer division (discards remainder)
- **Modulus (`%`)**: Returns remainder of division
- **Absolute value (`abs()`)**: Returns positive value
- **Rounding (`round()`)**: Rounds to specified decimal places
- **Math module functions**: Advanced mathematical operations

### Example

```python
import math

number1, number2 = 10, 20
print(number1 + number2)    # Addition: 30
print(number2 % number1)    # Modulus: 0
print(number2 // number1)   # Floor division: 2
print(abs(-number1))        # Absolute: 10
print(round(3.14159, 2))    # Rounded: 3.14
print(math.ceil(3.14))      # Ceiling: 4
```

### Learning Objectives

- Learn advanced arithmetic operations
- Understand the math module
- Practice numeric calculations

---

## 7. Type Conversion

**File:** `7_type_conversion.py`

### Theory

Type conversion (casting) is the process of converting one data type to another. Python provides built-in functions for explicit type conversion, which is essential when working with user input.

### Key Concepts

- **Implicit conversion**: Python automatically converts types when safe
- **Explicit conversion**: Manual conversion using built-in functions
- **Common conversions**: `int()`, `float()`, `str()`, `bool()`
- **User input**: Always returns string type by default

### Example

```python
x = input("Enter a number: ")    # User input is always string
print(type(x))                   # <class 'str'>
y = int(x) + 1                   # Convert to integer before arithmetic
print("Result:", y)
```

### Learning Objectives

- Understand data type concepts
- Learn type conversion functions
- Handle user input properly

---

## 8. Comparison Operators

**File:** `8_comparision_operators.py`

### Theory

Comparison operators compare values and return Boolean results (True/False). They are fundamental for decision-making in programs and work with various data types.

### Key Concepts

- **Greater than (`>`)**: Checks if left value is larger
- **Less than (`<`)**: Checks if left value is smaller
- **Equal to (`==`)**: Checks if values are equal
- **Not equal to (`!=`)**: Checks if values are different
- **String comparison**: Based on lexicographical order
- **Type sensitivity**: Different types are never equal

### Example

```python
print(10 > 8)           # True
print(10 == "10")       # False (different types)
print("apple" > "banana")  # False (lexicographical order)
print("apple" == "Apple")  # False (case sensitive)
```

### Learning Objectives

- Master comparison operations
- Understand Boolean logic
- Learn string comparison rules

---

## 9. Conditional Statements

**File:** `9_conditional_operator.py`

### Theory

Conditional statements allow programs to make decisions based on different conditions. The `if-elif-else` structure enables branching logic and multiple condition checking.

### Key Concepts

- **if statement**: Execute code when condition is True
- **elif statement**: Check additional conditions
- **else statement**: Execute when all conditions are False
- **Indentation**: Python uses indentation to define code blocks
- **Multiple conditions**: Use logical operators to combine conditions

### Example

```python
age = 15

if age <= 5:
    print("You are a toddler.")
elif age > 5 and age <= 14:
    print("You are a kid.")
elif age > 14 and age <= 19:
    print("You are a teenager.")
else:
    print("You are an adult.")
```

### Learning Objectives

- Understand conditional logic
- Learn proper indentation
- Practice decision-making in code

---

## 10. Ternary Operator

**File:** `10_terinary_operator.py`

### Theory

The ternary operator (conditional expression) provides a concise way to write simple if-else statements in a single line. It's useful for simple conditional assignments.

### Key Concepts

- **Syntax**: `value_if_true if condition else value_if_false`
- **Readability**: Best for simple conditions
- **Assignment**: Often used for conditional variable assignment
- **Evaluation**: Condition is evaluated first

### Example

```python
age = int(input("Enter user age: "))
message = "You are a toddler." if age <= 5 else "You are not a toddler."
print(message)
```

### Learning Objectives

- Learn concise conditional syntax
- Understand when to use ternary operators
- Practice one-line conditionals

---

## 11. Logical Operators

**File:** `11_logical_operators.py`

### Theory

Logical operators combine multiple Boolean expressions and are essential for complex conditional statements. They follow Boolean algebra rules.

### Key Concepts

- **and operator**: Returns True if both conditions are True
- **or operator**: Returns True if at least one condition is True
- **not operator**: Reverses the Boolean value
- **Short-circuit evaluation**: Python stops evaluating when result is determined
- **Precedence**: `not` > `and` > `or`

### Example

```python
age = 44
salary = 10
is_retired = False

if age >= 18 and salary > 0 and not is_retired:
    print("You are eligible for the job.")
else:
    print("You are not eligible for the job.")
```

### Learning Objectives

- Master logical operators
- Understand Boolean logic
- Practice complex conditional statements

---

## 12. For Loops

**File:** `12_for_loop.py`

### Theory

For loops provide a way to repeat code execution for a specific number of times or iterate over sequences. They are fundamental for automation and data processing.

### Key Concepts

- **range() function**: Generates number sequences
- **break statement**: Exits loop prematurely
- **else clause**: Executes when loop completes without break
- **Loop variables**: Track current iteration
- **Condition checking**: Control loop execution flow

### Example

```python
# Simple for loop
for i in range(5):
    print("Executing for loop: ", i)

# For loop with break
for i in range(10):
    if i == 5:
        print("Breaking at: ", i)
        break
else:
    print("Loop completed without break.")
```

### Learning Objectives

- Understand loop concepts
- Learn break and else usage
- Practice iterative programming

---

## 13. Nested Loops

**File:** `13_nested_loops.py`

### Theory

Nested loops are loops inside other loops. They are useful for working with multi-dimensional data structures and creating complex patterns.

### Key Concepts

- **Inner and outer loops**: Each loop maintains its own iteration
- **Execution pattern**: Inner loop completes entirely for each outer loop iteration
- **Coordinate systems**: Often used for 2D grid operations
- **Performance**: Consider efficiency with large datasets

### Example

```python
for i in range(3):
    for j in range(4):
        print(f"({i}, {j})")
```

**Output:**

```
(0, 0) (0, 1) (0, 2) (0, 3)
(1, 0) (1, 1) (1, 2) (1, 3)
(2, 0) (2, 1) (2, 2) (2, 3)
```

### Learning Objectives

- Understand nested loop structure
- Learn multi-dimensional iteration
- Practice pattern generation

---

## 14. Iterables

**File:** `14_iterables.py`

### Theory

Iterables are objects that can be looped over. Python's for loops can iterate over various data types, making data processing flexible and powerful.

### Key Concepts

- **Iterable types**: Strings, lists, tuples, dictionaries, sets
- **String iteration**: Access each character
- **List iteration**: Access each element
- **Dictionary iteration**: Access keys, values, or both
- **Tuple iteration**: Similar to lists but immutable

### Example

```python
# String iteration
for char in "Python":
    print(char)

# List iteration
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Dictionary iteration
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
```

### Learning Objectives

- Understand iterable concepts
- Learn different iteration patterns
- Practice data structure traversal

---

## 15. While Loops

**File:** `15_while_loop.py`

### Theory

While loops continue executing as long as a condition remains True. They are useful when the number of iterations is unknown beforehand.

### Key Concepts

- **Condition-based**: Continues while condition is True
- **Infinite loops**: Risk when condition never becomes False
- **Loop control**: Modify variables to eventually break condition
- **Pretest loop**: Condition checked before each iteration

### Example

```python
number = 0
while number < 100:
    print("Number is", number)
    number += 10
print("While loop execution completed.")
```

### Learning Objectives

- Understand condition-based loops
- Learn loop control techniques
- Practice while loop patterns

---

## 16. Even Number Example

**File:** `16_even_number.py`

### Theory

This practical example demonstrates loop usage, conditional statements, and mathematical operations to solve a real problem: counting even numbers.

### Key Concepts

- **Modulus operator**: `%` for checking remainders
- **Even numbers**: Numbers divisible by 2 (remainder 0)
- **Counter variables**: Track occurrences
- **Practical application**: Combining multiple concepts

### Example

```python
even_number_count = 0

for i in range(1, 11):
    print("Actual number is:", i)
    if i % 2 == 0:
        print("Even number found:", i)
        even_number_count += 1

print("Total even numbers found in range 1 to 10:", even_number_count)
```

### Learning Objectives

- Apply multiple concepts together
- Practice problem-solving approach
- Understand practical programming patterns

---

## 17. Functions

**File:** `17_functions.py`

### Theory

Functions are reusable blocks of code that perform specific tasks. They promote code organization, reusability, and modularity in programming.

### Key Concepts

- **Function definition**: `def` keyword creates functions
- **Function call**: Execute function by name with parentheses
- **Parameters**: Input values functions can accept
- **Return values**: Output functions can provide
- **Code reusability**: Write once, use multiple times

### Example

```python
# Function without parameters
def greet():
    print("Hello, Welcome to Python Basics!")

greet()  # Function call

# Function with parameters and return value
def get_greeting(first_name, last_name):
    return f"Hello, {first_name} {last_name}! Welcome to Python Basics."

message = get_greeting("John", "Doe")
print(message)
```

### Learning Objectives

- Understand function concepts
- Learn function definition and calling
- Practice parameter passing and return values

---

## 18. Function Keyword Arguments

**File:** `18_fun_keyword_arg.py`

### Theory

Keyword arguments allow passing arguments to functions by parameter name rather than position. This improves code readability and reduces errors.

### Key Concepts

- **Keyword arguments**: Specify parameter name when calling function
- **Order independence**: Arguments can be passed in any order
- **Clarity**: Makes function calls more readable
- **Error reduction**: Less likely to mix up parameter order

### Example

```python
def increment(number, by):
    return number + by

# Using keyword arguments
value = increment(number=5, by=5)
print(value)  # Output: 10
```

### Learning Objectives

- Learn keyword argument syntax
- Understand benefits of named parameters
- Practice clear function calling

---

## 19. Function Default Arguments

**File:** `19_fun_keyword_default_args.py`

### Theory

Default arguments provide default values for function parameters, making functions more flexible and easier to use by reducing required parameters.

### Key Concepts

- **Default values**: Parameters can have preset values
- **Optional parameters**: Can be omitted when calling function
- **Override capability**: Default values can be replaced
- **Parameter order**: Default parameters must come after required ones

### Example

```python
def increment(number, by=10):  # 'by' has default value of 10
    return number + by

value1 = increment(5)      # Uses default: 5 + 10 = 15
value2 = increment(5, 20)  # Overrides default: 5 + 20 = 25

print(value1)  # Output: 15
print(value2)  # Output: 25
```

### Learning Objectives

- Understand default parameter concepts
- Learn function flexibility techniques
- Practice optional parameter usage

---

## 🚀 Getting Started

1. **Prerequisites**: Python 3.x installed on your system
2. **Running Examples**: Execute each file using `python filename.py`
3. **Learning Path**: Follow the numbered sequence for progressive learning
4. **Practice**: Modify examples and create your own variations
