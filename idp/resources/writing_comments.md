---
title: Writing Comments
---

# Writing Effective Comments

Comments in Java are essential for making your code understandable to both yourself and others. They serve as documentation and explanations for the code you've written. However, writing good comments requires balance. In this lesson you’ll learn the clear and concise way of writing comments, with examples of too little, just right, and too many comments.

- [Writing Effective Comments](#writing-effective-comments)
  - [Doc-String Comments](#doc-string-comments)
  - [Inline Comments](#inline-comments)
  - [Too Little](#too-little)
    - [No Comments](#no-comments)
    - [Doc-String Comments](#doc-string-comments-1)
    - [Inline Comments](#inline-comments-1)
  - [Goldilocks](#goldilocks)
    - [Doc-String Comments](#doc-string-comments-2)
    - [Inline Comments](#inline-comments-2)
  - [Too Much](#too-much)
    - [Doc-String Comments](#doc-string-comments-3)
    - [Inline Comments](#inline-comments-3)
  - [Quality Inline Comments](#quality-inline-comments)

## Doc-String Comments
Doc-strings are multi-line strings enclosed in triple-quotes (either single or double). They are used to document classes and functions. Here is what makes a strong Doc-String comment:
1. State WHAT the function does. NOT how. And NOT why.
2. Mention by name all the arguments. Types can be inferred (or it is explicitly stated) for each argument.
3. Describe all the return values and special cases.

Doc-strings should not be used anywhere else except as the method descriptor.
Note that they always belong `under` the prototype, not above the prototype (as they are in Java).

## Inline Comments 
Inline comments are single-line comments that appear within the code, providing clarifications or explanations for specific lines or blocks of code. Inline should explain `WHY, HOW, WHAT.` Here is what makes a strong inline comment:
1. All comments should add real value while letting the code speak for itself. Avoid trivial comment such as: this adds one to x
2. The BEST comments state WHY things are happening, such as: we subtract one because we must exclude the last value that is unused in this case
3. Short, tight and efficient code can sometimes be very hard to read. This is when a WHAT comment is vital to have.

When the “what” is obvious, a “how” may not be necessary in the final submission. “How” comments are initially used to help the developer decompose the problem when writing a solution. Developers often write out a few comments that state the steps to take to solve a problem. These can remain as explanations of WHAT if they still add value after the code is complete. 

But, avoid comments like: “loop through each element in the list” if the code is easy to read. However, if the code is sufficiently complicated, “how” comments can truly add value.

It should be clear where vertical spacing belongs, `above` the inline comment (except if it is the first line in the method).

## Too Little
### No Comments
In this example, there are no comments at all. While the code may be simple to understand, it lacks context and explanations. It may be difficult for someone else (or even yourself in the future) to understand the purpose and behavior of these methods.
```python 
def calculate_total(list):
    total = 0
    for element in list:
        total += element
    return total
```
### Doc-String Comments
This example includes a comment, but it does not sufficiently provide the three required parts: the explanation is ambiguous; the argument is not named and its type cannot be inferred; the return types and special cases are not mentioned. One might want to know the functionality when there are capital letters. What is the return type when x is empty? What are the exceptions? Lastly, the single variable names are too minimal.
```python
def count_letters(x):
    ''' 
    Returns the occurrences of each character.
    '''
    d = {}
    for c in x:
        if c in d:
            d[c] = 1
        else:
            d[c] += 1

    return d

def main():
  print(count_letters("How much wood could a wood chuck chuck?"))

```
### Inline Comments
This example includes a comment for every line, yet an unfamiliar reader would still have no idea what's going on or WHY it is happening. The comments state the obvious and are unhelpful. 
```python
def multi_bar(data):
    # create a filter
    filtered = data[(data['small'] == 'low') & (data['Year'] == 2000) ]

    # select some columns
    races = df.loc[:, 'Size':].columns

    # do a melt
    melted = pd.melt(filtered, id_vars='height', var_name='Swim', value_vars=races, value_name='Percent')

    # now plot
    sns.barplot(data=melted, x='Swim', y='Percent', hue='height')
```


## Goldilocks

### Doc-String Comments
This example includes comments at the function level. The comments explain what the function does, what arguments it expects, and what it returns. This level of commenting provides clear and useful information without being excessive.
```python 
def find_largest(numbers):
    '''
    Find the largest value in numbers, an unsorted list of real values. 
    Return as an integer the largest number found. Return None if the list is empty.
    '''
    return None if len(numbers) else int(max(numbers))
```
### Inline Comments
In this example the comments focus on WHY things are done. The comments adds clarity by explaining a little bit of HOW it works because not that many developers know bitwise operations. The comments are concise and enhance code readability. They aren't redundant and offer clarifications. However, the seasoned developer could make an argument that these comments are still a bit too much. (No pun intended.)
```python
def split_to_nibbles(value):
    '''
    This functions takes a 32-bit, positive integer value and returns as a tuple
    the 8 nibbles that comprises the value. Recall that a nibble is 4 bits.
    The high-order nibble will be the last item in the tuple.
    '''
    # construct a list to start, since tuples can't quickly be built one item at a time
    nibbles = []

    # use 0xF as our 4-bit mask. 0xF (hex) == 1111 (binary)
    # We do a bitwise AND operator to collect the rightmost 4 bits, then shift by 4 bits.
    for nib in range(8):
        nibbles.append(value & 0xF)
        value >>= 4

    return tuple(nibbles)
    
def main():
    # will print (3, 0, 2, 4, 1, 10, 0, 0)
    print(split_to_nibbles(0xA14203))
```


## Too Much

### Doc-String Comments
**Excessive comments in doc-string are not penalized, but they cost you a lot of effort.**
This example contains excessive comments that provide redundant or unnecessary information. Comments should not restate the obvious. Over-commenting can clutter the code and make it harder to read.
```python 
class Main:
    '''
    This is the main module of the application.
    It does a lot of things, like managing user input and performing calculations.
    '''
    def add(a, b):
        '''
        This method adds two numbers together. It takes two parameters, a and b, and returns their sum.
        This method cannot be successfully called if both parameters are not provided.
        There are no named parameters and no default arguments.
        Args: 
          - a : (int), the first number to be added
          - b : (int), the second number to be added
        Returns: 
          - The integer sum of a and b as an integer. 
          - If either a or b are not integers, an integer value is still returned.
          - If either a or b are NaN, then this will return NaN.
          - If either a or b are not numbers, or their sum cannot be cast to an int,
            then a type exception may be thrown.
        '''
        return int(a + b)
```

### Inline Comments
It is not appropriate to use comments to describe the obvious. It simply is not professional, it needlessly takes up vertical real estate, and it actually makes the code harder to read. This example code and commenting style drives most engineers nuts! Don't do it!
```python
def calc_avg(numbers):
    '''
    Returns the average of all the values in the list, numbers.
    If the count is zero, return None.
    '''
    # Initialize the total sum to zero
    total = 0

    # Initialize our count to zero
    count = 0

    # Loop through the list of numbers and calculate the total sum.
    # This loop iterates over each element in the list, numbers.
    for num in numbers:

        # Inside the loop, we add the current number to the total sum
        total += num

        # increment our count
        count += 1 

    # if our count is zero, return None
    if count == 0:
        return None

    # Return the average by dividing the sum by the count
    return total / count 
```

## Quality Inline Comments
The most important comments in code are those that explain _WHY_! Other important comments include _HOW_ the code works. In some circumstances, _WHAT_ the code does can be helpful at times, particularly as you decompose the problem. You should focus on _WHY_ commenting.  

To add quality _WHY_ comments ask yourself the following:  
* What happens if we eliminate or modify the code?  
* Why is this data structure the correct choice?  
* Why are we using these constant values?  
* Why is the code in this specific order?  

Avoid comments that are blatantly obvious from reading the code. The future programmer reading your code will know how to code, but will not necessarily know what was in your head when you wrote the code.   
```python
def demo(words, fn):
    '''
    Returns the magical math on words using a function, fn.
    words is a string of words.
    '''
    # calculate the sum before making changes to words
    # to assure we have consistent summation methods on 
    # the original user input. Operate on non-empty tokens 
    # only by splitting on whitespace, not " ".
    s = sum([mystery(term) for term in words.split()])

    # We split using " " because want to include
    # "empty" words where multiple consecutive spaces appear.
    # Sorted gets us a list and the first/last alphabetic word.
    # Avoid first casting to a list() for better performance.
    words = sorted(map(fn, words.split(" ")))
    bounds = [fn(words[0]), fn(words[-1])]

    # subtract two so that we ignore the first and last word
    return (len(words) - 2) * s - sum(bounds)
```
