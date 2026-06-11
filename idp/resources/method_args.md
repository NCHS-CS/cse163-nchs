---
title: Arguments
---

# Arguments
When you visit online API sites (like Pandas), you will see documentation for methods that consists of something like the following:  
```python
    my_method(*args, **kwargs)
```
This is frustrating when there is no mention of what `args` or `kwargs` can be. We can't solve
that problem, but we can at least understand what `*args`, `**kwargs` means and how to use them.  This article aims to help with that.

In short:  
* `*args` means that the method can take any number of **positional arguments**.  
* `**kwargs` means that the method can take any number of **named arguments**.  

Let's define a couple of terms.   
### Important Terms

|Term|Definition|  
|----|----------|  
|_Positional Argument_|Required method arguments that must appear in a specific order|  
|_Named Argument_|Optional method arguments that are given a default value in the prototype (method declaration). They will appear as `name=value`. They can appear in any order after all the positional arguments are provided.|

## Start with Print
Let's first explore the method `print` to see how it works. Note that you can get help on `print` by
using the following inside of Jupyter: `help(print)`. Here is the help printed:

Help on built-in function print in module builtins:
```python
print(...)
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```
    
Prints the values to a stream, or to sys.stdout by default.

Optional keyword arguments:
- **file**:  a file-like object (stream); defaults to the current sys.stdout.
- **sep**:   string inserted between values, default a space.
- **end**:   string appended after the last value, default a newline.
- **flush**: whether to forcibly flush the stream.


The `...` above should be replaced with `*args`. It should look like:  
```python
print(*args, sep=' ', end='\n', file=sys.stdout, flush=False)
```
In short, `print` accepts as many position arguments as you want and it has four named arguments.
You will likely want to set `end=''` at times to behave like Java's `System.out.print` (no
new line printed). And, if you want to print a list of values separated with commas, you could easily
override `sep=', '`. 

## Packing & Unpacking Arguments
When someone calls a method using `*args` in the arguments (e.g. `foo(*args)`) it unpacks the Tuple
and calls the method with each element in the Tuple as an argument (e.g. `foo(1,2,3)`).  

The same things happens when a method is called with `**kwargs` syntax, except that the names are
also unpacked. In this case, kwargs is a `dictionary`.

Here is some code to illustrate:  
```python
args = (1, 2, 3)
foo(*args)    # Same as below
foo(1, 2, 3)  # Same as above

kwargs = { 'a':1, 'b':'yes!', 'c':3 }
bar(**kwargs)             # same as below
bar(a=1, b='yes!', c=3)   # same as above
```
What this means is that you can technically define every method as follows:  
```python
def foo(*args, **kwargs):
    # args behaves like a tuple. Just dereference elements.
    # kwargs behaves like a dictionary.
    # note: perhaps len(args) == 0. Your code should check!
    if len(args) > 0:
        print(args[0])
    if 'name' in kwargs:
        print(kwargs['name'])
    # repack and pass along all named arguments to foo()
    foo(**kwargs)
```
## Examples
Let's say that we want to have a method with 7 arguments where 3 of them have default values. 
We'd define this method as shown below. Note that the three named arguments have default values.

```python
# Example prototype with 4 positional arguments and 3 named arguments
def example_a(value1, value2, value3, value4, named1=1, named2=2, named3=3):
    '''
    value1, value2, value3 & value4 must be present when calling method()
    named1, named2 & named3 are optional because they have default values.
    '''
    print(value1, value2, value3, value4, named1, named2, named3)
```

We can call `example_a` in the following ways:
```python
# we can call example_a in the following ways
example_a(3, 1, 4, 1)                                  # output: 3 1 4 1 1 2 3
example_a('a', 'b', 'c', 'd', named2='foo')            # output: a b c d 1 foo 3
example_a(0, 0, 'a', 'b', named3='bar', named1='foo')  # output: 0 0 a b foo 2 bar
```
In every call, values for every positional argument is required.  

In the first call, all the named arguments retain their default values: 1, 2, 3.  
In the second call, we override the value for `named2` only.  
In the third call, we override `named1` and `named2` only.  

Let's get a little more complicated. In the following code, we are creating
a method that allows for an arbitrary number of position arguments, zero or 50!
The method has exactly two named arguments.  
```python
# example prototype with 1 required positional argument, any number of
# optional positional arguments, and two optional named arguments
def example_b(value1, *args, named1=1, named2=2):
    '''
    value1 is a required, positional argument
    args is basically a Tuple that represents any number of un-named argments that appear
        before all named arguments
    named1 & named2 are optional named arguments that are given default values
    '''
    # when we put the '*' in front of args, we unpack the positional arguments
    print(value1 + 10, *args, named1, named2)
```
The only line of code calls `print` with 3 or more arguments. The first argument
to `print` is `value1 + 10`. It then will pass in zero or more arguments that were
passed into `example_b`.  

Let's examine a few examples:
```python
# we can call example_b in the following ways:
example_b(5, 10, 15, 20)        # output: 15 10 15 20 1 2
example_b(0, named2='override') # output: 10 1 override
```
In the first call, we pass in 4 positional arguments. `value1` will have the value 5.
Then, `*args` will accept the next 3 arguments. `args` is actually a `Tuple`. In order
to pass all these values into `print` as separate arguments, we have to `unpack` the tuple
by using the `*`.  

In the second call, we pass in only 1 positional argument and then override only one
named argument.  

One more example:
```python
def example_c(value1, *args, named1=1, named2=2, **kwargs):
    '''
    value1 is a required, positional argument
    args is basically a Tuple that represents any number of un-named argments that appear
        before all named arguments
    named1 & named2 are optional, named arguments that are given default values
    kwargs is basically a dictionary that represents any number of named argument
        that appear after all the positional arguments
    '''
    # unpack args to all positional arguments
    # unpack **kwargs to be all named arguments
    print(value1 + 20, named1, named2, *args, **kwargs)
    
example_c(0, named1=10)                 # output: 20 10 2
example_c(2, 'foo', named2=0, sep='-')  # output: 22-1-0-foo
named_args = { 'named1':2, 'named2':1, 'sep':':', 'end':'end_of_line' }
example_c(4, 3, **named_args)           # output: 24:2:1:3end_of_line
```
**First call**  
In the first call, `value1=0` and `named1=10`.   

**Second call**  
In the second call, `value1=2` and `'foo'` is put into the `*args` argument. `named1` retains its default
value of `1` and `named2` is overridden to have the value `0`. The named argument `sep` is not found in 
the `example_c` prototype--not as a named argument--so it gets put into the `**kwargs` argument and is subsequently unpacked and passed along to print. The API
`print` has a named argument `'sep'` which is printed between each argument. This is why each value is
separated by `'-'`.  In summary, the code effectly calls print like this:  
```python
    # print(value1+20, named1, named2, *args, **kwargs)
    print(       2+20,      1,      0, 'foo', sep='-')
```

**Third call**  
In the third call things get even more complicated. here we create a `dictionary` that is a map of
named arguments with values. It contains four named arguments, two of which are explicitly named
in the `example_c` prototype, and other two are defined in the `print` prototype. So, the call results in:  
```python
value1 = 4
*args = (3, )
named1 = 2
named2 = 1
**kwargs = { 'sep':':', 'end':'end_of_line' }

# with the above values, the actual print statement is equivalent to:
print(4+20, 2, 1, 3, sep=':', end='end_of_line')
```
