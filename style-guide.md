# Style Guide

This code style guide reproduces common conventions for Python programming. While rules can be occasionally bent with justification, most programming work in this course should follow these guidelines.

## Naming

### Variable names

Variable names should be descriptive, concise, and lowercase with words separated by underscores as in `snake_case`. Avoid single letter names for variables because a single letter usually fails to describe the values contained in a variable, with the exception of loop variables. Avoid Python keywords, such as `class`, `print`, `import`, or `return`, or names of built-in functions or types, such as `len`.

:::{hint} Good
:class: code-example

```python
factor
total_weight
data1        # Okay to have a number right after a word
```
:::

:::{error} Bad
:class: code-example

```python
x            # Most likely not descriptive enough,
             # except for something like an (x, y) coordinate
totalWeight  # Not using snake_case
NewImage     # Not using snake_case
newresult    # Not separating words with underscores
return       # Python keyword
len          # Python built-in function
```
:::

### Function names

Function names should be descriptive, concise, and lowercase with words separated by underscores as in `snake_case`. As with variable names, avoid names of built-in Python functions. We usually specify the function names in the specification, so make sure to name your functions accordingly.

:::{hint} Good
:class: code-example

```python
get_height(person)
plot_population(df)
```
:::

:::{error} Bad
:class: code-example

```python
setScore(record)  # not using snake_case
max()             # will overwrite the built-in max function in Python
```
:::

When writing test functions, the name of your test function should clearly indicate which function it is testing. For example, a test for the function `add_two_numbers` might be named `test_add_two_numbers`.

### Class names

Class names should be in `CapitalCase`.

:::{hint} Good
:class: code-example

```python
University
DataFrame
EdPost
```
:::

:::{error} Bad
:class: code-example

```python
dataFrame
ed_post
```
:::

### Constant names

Constant names should be in `ALL_CAPITAL_CASE_WITH_UNDERSCORES`.

**Constants** are values defined outside the function declarations whose values are manually assigned by programmers and infrequently changed. Constants usually replace "magic values" to make code more readable. Constants should only represent simple values, not large objects such as dataframes. Constants are optional in test programs.

:::{hint} Good
:class: code-example

```python
NUM_PARTICIPANTS = "97"
data[:NUM_PARTICIPANTS]
```
:::

:::{error} Bad
:class: code-example

```python
data[:97]
```
:::

### File names

Python (py) files or module names should be in `snake_case`, such as `main.py` or `dataset_analysis.py`.

Jupyter Notebook (ipynb) files do not have a particularly universal naming convention. Course materials use lowercase names with words separated by hyphens as in `kebab-case`.

## Whitespace

### Indentation

Unlike other languages that use explicit delimiters to determine what goes inside a loop or function (such as `{}` in Java), Python only uses indentation. Indentation affects the behavior of programs. `IndentationError: unexpected indent` means there is an error in code indentation.

### Blank lines

Leave two blank lines separating code for different function definitions, class definitions, and other code. The only exception is for methods defined within the same class, in which case a single blank line between methods is preferred.

Within a function definition, avoid introducing more than a single blank line at a time and only for separating complex chunks of code for readability. Careful and consistent of two blank lines can help communicate the start of a significant, new definition.

:::{hint} Good
:class: code-example

```python
def the_first_function():
    # Implementation for the first function


def the_second_function():
    # Implementation for the second function
```
:::

:::{hint} Good
:class: code-example

```python
def compute_avg(x, y, z):
    """
    Sums the given three numbers and returns the average.
    """
    sum_val = x + y + z

    # Compute and return the average value
    result = sum_val / 3.0
    return result
```
:::

### Between operators

Include spaces between operators and other elements in an expression. Mathematical operators include `+`, `-`, `*`, `/`, and `**`. Logical operators include `==`, `<=`, `>=`, `<`, and `>`.  Limit space delimiters to 1 space to avoid unnecessary whitespace. The exception to this is parentheses, which can be directly adjacent to whatever they are enclosing.

:::{hint} Good
:class: code-example

```python
x + y
(total ** 2) + 4 * val - 1
x * (4 + 6)
b + math.sqrt(4 * max_val)
```
:::

:::{error} Bad
:class: code-example

```python
x+y                             # not enough spaces
(total**2)+4*val-1              # not enough spaces
x * ( 4 + 6 )                   # unnecessary spaces around parentheses
b +  math.sqrt( 4 *   max_val)  # inconsistent spacing
```
:::

This does not apply when specifying default parameter values or keyword arguments. Avoid spaces around the assignment operator `=` for those cases.

:::{hint} Good
:class: code-example

```python
def add_three_nums(a, b, c=10):
    return a + b + c


add_three_nums(b=20, a=20, c)
```
:::

### Function calls

Include spaces between arguments in a function call. Avoid space(s) between the function name and its argument list. Adding space(s) incorrectly suggests that the parentheses are for grouping an expression when they actually indicate a function call.

:::{hint} Good
:class: code-example

```python
x = math.sqrt(n)
range_vals = range(n, 4)
```
:::

:::{error} Bad
:class: code-example

```python
x = math.sqrt (n)        # too much space before the parenthesis
range_vals = range(n,4)  # no spaces between parameters
```
:::

## Line length

In general, lines should not exceed 100 characters. Occaisional exceptions are permitted when a longer line would be clearer and easier to understand than two or more shorter lines. Avoid long lines with the following strategies.

Function calls
: ```python
  some_function(first_arg="This is a function",
                second_arg="With many arguments",
                third_arg="indent until everything lines up")
  ```

Expressions
: ```python
  total = (first_num + second_num + third_num
           + fourth_num + fifth_num)
  ```

Strings
: ```python
  print("For very very very very very very long strings, "
        "this is how we might break it up to two lines")
  ```

DataFrames
: ```python
  # This filter is too long and combines multiple steps
  data = data[(data['primary_color'] == 'Magenta') & (data['size'] != 'Large')]

  # Instead, assign names to each step of the filter
  is_magenta = data['primary_color'] == 'Magenta'
  is_not_large = data['size'] != 'Large'

  data = data[is_magenta & is_not_large]
  ```

## Documentation

Each function should contain a docstring describing what the function does right below the function definition. It should describe any parameters the function takes and values it returns (if any). If the code requires handle some special cases (like case sensitivity, or special returns values for a certain input), include that in the comment as well. The `main` method does not require a comment.

Long blocks of particularly complex code can be explained by including a comment `#` on the preceding line(s).

```python
def add_two_numbers(a, b, return_zero=False):
    """
    This function returns the sum of the two given numbers a, b
    if return_zero is False. Otherwise returns 0.
    return_zero has False as its default value.
    """
    if return_zero:
        return 0
    else:
        return a + b
```

Avoid information that is unnecessary or irrelevant to clients (end-users of your work), such as "initialize variable" or "nested for loop" or "increment count". Function comments should describe **what** result the program achieves rather than **how** it achieves that result.

:::{error} Bad
:class: code-example

```python
# Note that the usage of a set and a loop are implementation details,
# as in they describe HOW the method works.
# Returning the length of the set doesn't mean much to the clients.
def count_unique_characters(filename):
    """
    Opens the given file, loops through each character and adds them
    to a set. Returns the length of the set.
    """
    result = set()
    with open(filename) as f:
        content = f.read()
        for c in content:
            result.add(c)
    return len(result)
```
:::

:::{hint} Good
:class: code-example

```python
def count_unique_characters(filename):
    """
    Takes in a filename and returns the number of unique characters within
    the given file.
    """
    result = set()
    with open(filename) as f:
        content = f.read()
        for c in content:
            result.add(c)
    return len(result)
```
:::

Consider what a client would find useful. Documentation should contain all the necessary information needed to use a function. The exact details of how the function solves the problem is irrelevant, but the client needs to know the purpose of the parameters and the expected behavior. Avoid mentioning "the spec" or "the assessment" because clients won't know what this means unless they've also taken this course.

The documentation for test functions can be relatively simple. For example, the test function `test_add_two_numbers` could include the docstring, "Tests the function `add_two_numbers`".

### Type annotations

Every function should have its parameter types and return types annotated. Fields of objects should also their types annotated. Annotations are not required for local variables.

```python
def function_example(a: int, b: float) -> str:
    return "example" + str(int) + str(float)


class ClassExample:
    def __init__(self, param1: int, param2: float) -> None:
        self.field1: str = str(param1)
        self.field2: float = param2

    def method(self, param: str) -> int:
        return len(self.field1 + param)
```

If a function doesn't return anything, indicate its return type is `None`. You should annotate every function you write, including test functions.

### Class definitions

Include a docstring comment describing the class right below the class definition.

```python
class Dog:
    """
    Represents a dog with a name.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a Dog object with the given name.
        """
        self._name: str = name

    # Other methods for the Dog class
```

## Logical refactoring

If the same lines of code appear in multiple places, reduce redundancy by refactoring.

### Conditional logic

:::{error} Bad
:class: code-example

```python
# Note that there are repeated lines of logic that actually always happen,
# instead of conditionally like how our structure is set up. We can factor
# these out to simplify and clean our code.
if x % 2 == 0:
    print("Hello!")
    print("I love even numbers too.")
    print("See you later!")
else:
    print("Hello!")
    print("I don't like even numbers either.")
    print("See you later!")
```
:::

:::{hint} Good
:class: code-example

```python
print("Hello!")
if x % 2 == 0:
    print("I love even numbers too.")
else:
    print("I don't like even numbers either.")
print("See you later!")
```
:::

### Boolean zen

Avoid unnecessary comparisons to `True` and `False`. Remember to negate boolean values with the `not` operator.

:::{error} Bad
:class: code-example

```python
if is_sunny:
    return True
else:
    return False
```
:::

:::{hint} Good
:class: code-example

```python
return is_sunny
```
:::

:::{error} Bad
:class: code-example

```python
if is_sunny == True:
    go_hiking()
```
:::

:::{hint} Good
:class: code-example

```python
if is_sunny:
    go_hiking()
```
:::

:::{error} Bad
:class: code-example

```python
return is_sunny == False
```
:::

:::{hint} Good
:class: code-example

```python
return not is_sunny
```
:::

### Loop zen

Choose loop bounds or loop conditions that generalize code the best.

:::{error} Bad
:class: code-example

```python
l = [1, 2, 3]
total += l[0]
for i in range(1, len(l)):
    total += l[i]
```
:::

:::{hint} Good
:class: code-example

```python
for i in range(len(l)):
    total += l[i]
```
:::

Computation that only need to happen once should not be recomputed inside a loop.

:::{error} Bad
:class: code-example

```python
# Note that the mean of the whole list remains unchanged for each loop iteration
# so it should be outside the loop to avoid unnecessary computation
def demean(l):
    """
    Takes in a list of numbers l and returns a new list with the mean
    value of the original list subtracted from each corresponding value
    """
    result = []
    for i in range(len(l)):
        mean = sum(l) / len(l)
        result.append(l[i] - mean)
    return result
```
:::

:::{hint} Good
:class: code-example

```python
def demean(l):
    """
    Takes in a list of numbers l and returns a new list with the mean
    value of the original list subtracted from each corresponding value
    """
    result = []
    mean = sum(l) / len(l)
    for i in range(len(l)):
        result.append(l[i] - mean)
    return result
```
:::

Avoid unnecessary looping.

:::{error} Bad
:class: code-example

```python
# Note that the total score for each sex could be computed at the same time
def get_total_for_each_sex(data):
    """
    Takes in data containing scores of students as a list of dictionaries.
    Returns a tuple containing the total score for each sex in the format
    of (male total, female total).
    """
    for row in data:
        if row['sex'] == 'M':
            male_total += row['score']
    for row in data:
        if row['sex'] == 'F':
            female_total += row['score']
    return male_total, female_total
```
:::

:::{hint} Good
:class: code-example

```python
def get_total_for_each_sex(data):
    """
    Takes in data containing scores of students as a list of dictionaries.
    Returns a tuple containing the total score for each sex in the format
    of (male total, female total).
    """
    for row in data:
        if row['sex'] == 'M':
            male_total += row['score']
        else:
            female_total += row['score']
    return male_total, female_total
```
:::

### Redundant cases

Avoid redundant cases. Before introducing a special case, think about whether a general case could compute the same result.

:::{error} Bad
:class: code-example

```python
# Note the first case is unnecessary since if a == 0 and b != 0, a / b will
# still return 0.
def divide(a, b):
    """
    Takes in two numbers a, b and returns the result of a / b.
    Returns 0 if b == 0.
    """
    if a == 0:
        return 0
    elif b == 0:
        return 0
    else:
        return a / b
```
:::

:::{hint} Good
:class: code-example

```python
def divide(a, b):
    """
    Takes in two numbers a, b and returns the result of a / b.
    Returns 0 if b == 0.
    """
    if b == 0:
        return 0
    else:
        return a / b
```
:::

## Program design

### Global variables

Only constants be defined as global variables in the top level of indentation.

### Argument immutability

Unless an explicit part of the specification, avoid modifying the arguments passed to your functions. While many built-in types like `int`, `float`, `bool`, `str`, `tuple` are immutable, some built-in types are mutable such as lists, dictionaries, `DataFrame`, `numpy` arrays, etc.

:::{error} Bad
:class: code-example

```python
# data is a DataFrame
data['new_col'] = ...   # will modify the input DataFrame

# data is a list of dictionaries
data.append(...)        # will modify the input list

# data is a 2D numpy array
data[:, :] = ...        # will modify the input array
```
:::

:::{hint} Good
:class: code-example

```python
data = ...
```
:::

### Private fields

In class definitions, all fields should be initialized in the `__init__` method. Fields should be declared private by prefixing their names them with an underscore `_`. Rather than`self.field_name`, use `self._field_name`.

Avoid unnecessary fields. The more fields in a class definition, the more difficult it becomes to maintain and reason about code. Additionally, each instance of the class will also consume more memory. Watch for fields that are only used in one public method or recomputed/cleared every call to a specific method. These can likely be simplified to local variables or function parameters. Deciding on what fields to include can be tricky: it might be necessary to make something a field to improve efficiency at the cost of simplicity.

Avoid accessing private fields from outside the class except for testing purposes. To allow client access to a private field, declare a public "getter" method that returns the value of the field and use it instead.

### Private methods

"Helper" methods should be declared private by prefixing their names with an underscore, such as `_private_method`. Avoid calling private methods from outside the class except for testing purposes.

### Pandas zen

When working with `pandas` objects, avoid loops since `pandas` methods are often much faster to run.

:::{error} Bad
:class: code-example

```python
total = 0
for row in data:
    total += row['score']
```
:::

:::{hint} Good
:class: code-example

```python
total = data['score'].sum()
```
:::

### Notebook zen

When working in a Jupyter Notebook, ensure that each code cell represents a logical step in a procedure. Avoid writing all the code in a single code cell and instead spread code out across multiple code cells with Markdown cells to explain each step.

The notebook should be top-to-bottom executable: after restarting the Python kernel, we can reproduce your outputs by running all cells from the top of the notebook to the bottom of the notebook.

### Unnecessary computation

Avoid computing unnecessary values.

:::{error} Bad
:class: code-example

```python
def get_average_score_for_sex(data, sex):
    """
    Takes in a DataFrame data containing scores for students and a sex and
    returns the average score for the given sex as a Series. Assume sex only
    takes the value 'M' (male) and 'F' (female).
    """
    male_avg = data[data['sex'] == 'M']
    female_avg = data[data['sex'] == 'F']
    if sex == 'M':
        return male_avg
    else:
        return female_avg
```
:::

:::{hint} Good
:class: code-example

```python
def get_average_score_for_sex(data, sex):
    """
    Takes in a DataFrame data containing scores for students and a sex and
    returns the average score for the given sex as a Series. Assume sex only
    takes the value 'M' (male) and 'F' (female).
    """
    return data[data['sex'] == sex]
```
:::

### Fit and finish

Remove all debugging print statements and fix all warnings and errors.
