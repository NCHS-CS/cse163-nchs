---
title: f-strings
---

# Formatted Strings

[RealPython Reference](https://realpython.com/python-f-strings/)  
[Python docs Reference](https://docs.python.org/3/library/string.html#format-string-syntax)  

- [Formatted Strings](#formatted-strings)
  - [%-formatting (old)](#-formatting-old)
  - [format method](#format-method)
  - [f-string](#f-string)
  - [Examples](#examples)

## %-formatting (old)
This style of formatted print is old and not recommended. But, you may see it somewhere. The `%` acts
like a "escape sequence" similar to how it is done in Java's `System.out.printf`.  

The string literal is the format string. After the string literal the arguments to the string
is separated by `%`. I find this odd. Apparently, so did many other programmers which is why this
formatting isn't used very much these days.

```python
print("Hello, %s. You are %s." % (name, adjective))
```

## format method
There is a method named `format` on the string object. The string contains formatting information inside
of curly braces. This formatting is described below. The string can contain many curly braces and
other text to be printed.  

Once again, this method of formatting strings is not used very much these days.  
```python
n = 2.154327
format_float = "{:.2f}".format(n)
print(format_float)

print("text {0}".format('value'))
```

## f-string
This is the most recent and popular way to format a string and values. 
Python's string <a href="https://docs.python.org/3/library/string.html#format-string-syntax" 
target="_blank">formatting</a> functionality is built into Python's <a href="https://realpython.com/python-f-strings/" 
target="_blank">f-string</a>. The API is a bit complicated to understand. It is similar
to the way Java implements `printf`, only it has different escape sequences and specifics. In short, when a
string literal is preceded with `'f'` then the string is expecting to have some
formatting sequence in it. A formatting sequence is embedded inside curly braces `{}` and the text
inside the curly braces is interpreted. It would contain identifiers, method calls, and possibly
formatting options following a colon. Here is the syntax for printing a floating point number with some text label:  

    f'text{<identifer>:.<integer>f}'
    
For example, let's say we do the following:  

    gpa = 3.899
    print(f'GPA={gpa:.2f}')

That code results in printing, `GPA=3.90` (due to rounding to 2 decimal places).

There are lots and lots of options that you can find in [Python docs Reference](https://docs.python.org/3/library/string.html#format-string-syntax). 

## Examples
```python
n = 30
print(f'Hex     = {n:05x}')
print(f'Decimal = {n:5d}')
print(f'SciNota = {n:e}')
print(f'Percent = {n:%}')

# assume foo()=8
from math import sqrt
print(f'Foo = {foo()} and squirt 2 = {sqrt(2):.3f}')
```

**Output**:  
```
Hex     = 0001e
Decimal =    30
Sci Not = 3.000000e+01
Percent = 3000.000000%
Foo = 8 and squirt 2 = 1.414
```
