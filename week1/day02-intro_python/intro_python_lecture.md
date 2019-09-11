# Day 2 Lecture Notes

## `git clone` our classroom repo on the command line and update it using `git pull`
* Unix commands we introduced today:
    * `touch some_filename.py` : creates a new file in the terminal
    * `code some_filename.py` : should open the file in VSCode if you have installed this functionality
* GitHub and git: cloning our repo
    * 1. Open a terminal
        * find out what directory you are in by typing `pwd`
        * navigate to the location where you would like to clone your repository using `cd ..` to go up a directory, `ls` to list files and folders,  and `cd` to enter a directory
    * 2. Once you are in the location where you want to clone your repository
        * Go to the repository on github and click on the green button that says **Clone or download"** and copy the url that is there
        * `git clone <repo .git file>`
    * 3. To keep your repository current, you can always run
        * `git pull`
            * run this often in the terminal to collect any updates to our course repository


## Intro to Markdown
* Markdown is a semi-universal documentation format all over the internet
* Markdown is meant to provide a "pure" text document formatting. `.md` files on GitHub have enough features to provide headers, links, and image rendering.
* You can insert nicely-rendered code blocks in markdown files, as will be seen throughout. Look at the raw text file of this document to learn how to do that.


## Comments in Python
* comment your code with single line (`#`) or block (`''' some comment '''`) comments :
* Reasons for using comments:
    * Send a message to someone reading your code
    * Exclude some bit of code from running
    * Add documentation to functions, ie Docstrings

```python
# This is a single line comment!

'''
This is a block comment! 
We often use these for Function Docstrings!
'''

x = 7
# print(x) # uncomment this to print the value of x
```


## Common Datatypes
* `int` : Integers, aka "whole numbers"
* `float` : Floats, or numbers that have a decimal point
* `bool` : Booleans, can only be `True` or `False
* Check variable types using the `type()` function:

```python
print(type(7)) # -> <class 'int'>

print(type(11.03)) # -> <class 'float'>

print(type(False)) # -> <class 'bool'>
```

### Convert between common data types using "casting"
* "casting functions": `int()`, `float()`, `bool()`
* Try these out and see if they do what you expect:

```python
print(int(True))

print(bool(1))

print(bool(23))

print(bool(0))

print(bool(-3))

print(bool(None))
```


## Common arithmetic operators 
* familiar operations: `+`, `-`, `*`, `/` 
    * consider that the result of the operation will follow the more complex datatype
* others:
    * floor division: `//` : divide, throw away the decimal, convert to integer
    * modulo: `%` : divide and return the remainder `5 % 3` -> `2`
    * to the power of: `**` : note that in most languages, this is performed with the `^` character
* You can't safely cast strings or letter characters to int or float types
* In general, you can follow PEMDAS for order of operations
    * What you would expect, however, always use parens to disambiguate calculation
* Try these out:

### basic arithmetic
```python
print(1 + 7)

print(9 * 33)

print(1.0 * 7)
print(type(1.0 * 7))

print(7 / 5)
print(type(7 / 5))
```

### floor division
```python

print(8 // 3)
print(type(8 // 3))
```

### you can't cast letters to ints or floats
```python

print(float('a'))
```

### HOWEVER!  Try this:
```python
print(bool('a'))
```

### modulo
```python
print(8 % 3)

print(1 % 33)
```

### power operator
```python
print(2**3)
```

### order of operations
```python
print(7 + 3**3 * 9 / 36)
print((7 + 3**3) * 9 / 36)
```

### a gotcha
```python
# what's going wrong here?
print(9(33 + 6))
```


## Declaring variables
* there are other names used to describe variables: namespaces, objects, ...
* a variable is a container that holds a pointer to some data in memory
    * use `id()` to see the the address/memory location
    * the `type()` function will let you know the data type of your variable when it is not immediately obvious
* the `=` symbol can be called the "assignment operator"
    * it is more meaningful to read `x = 7` as "x gets seven" than "x equals 7", since x is only a container for a pointer toward the value in memory.
    * the actual "equality operator" looks like this: `==`

### declare variables
```python
x = 513
y = 723.9

print(type(x))
print(type(y))
```

### using `id()`
```python
x = 513
y = 723.9

print(id(x))
print(id(y)) 
```

### interesting behavior 1
```python
x = 216
z = x

print(x, z)
print(id(x) == id(z))
```

### interesting behavior 2
* Why don't `x` and `frog` have the same id, even though `y` and `dog` do (or probably do)?
```python
x = 513
frog = 513

print(id(y))
print(id(dog))


y = 56
dog = 56

print(id(x))
print(id(frog))
```
**NOTE**: It turns out that Python optimizes for certain `int` values (between -5 and 256), so that their ids are likely the same. This applies to some other data types as well, so feel free to check `id`s. However, this behavior is not necessarily guaranteed, so don't count on *sameness*, look instead to *equality* using the `==` operator.


## Operating on Variables
* we can apply all the same arithmetic operators as above on variables
* in addition, we can use `+=`, `-=`, `*=`, `**=` and `/=` to update the value in a variable
* We've only learned **immutable** types so far: 
    * `int`, `float`, `bool`, `string`
        * `tuple` is also an immutable type we'll learn soon
    * when we update a variable of an immutable value, we get a different `id()` result


### operating on a variable
```python
y = 5
print(y + 2)
print(y)
```

### modifying the value of a variable
* notice that the results of id() change
```python
z = 95
print(id(z))

z = z * 2

print(z)
print(id(z))
```

### let's use our new operators to update values
* use id() to verify that the memory address is changing, in spite of each value being an immutable type
```python
x = 7
print(x)
x += 1 # x = x + 1
print(x) 
x -= 1
print(x)
x *= 3
print(x)
x **= 4
print(x)
x /= 4
print(x)
```

### why doesn't this work?
```python
x = 7

print(x += 1)
print(x -= 1)
print(x *= 3)
print(x **= 4)
print(x /= 4)
```


## Declare simple functions
* functions do things
* functions `return` things
    * by default, functions return `None`
    * can return 1 or more values
* functions can have **parameters**
    * allows passing values (**arguments**) into the function to be processed
* functions are **called**
* we will try to perform MOST operations using functions


### very simple function
```python
# define/declare a function
def return_90():
    return 90

# "call" a function
print(return_90()) 
```


### function with a single parameter
```python
def increment_some_int_by_1(some_int):
    return some_int + 1

print(increment_some_int_by_1(20))
```


### a more complex function
```python
def square_num_div_by_7_make_int(some_value):
    print('initial value of x: ', some_value)

    x = some_value**2
    print('x squared: ', x)

    x2 = x / 7
    print('x squared divided by 7: ', x2)

    x2_int = int(x2)

    return x2_int

print('result: ', square_num_div_by_7_make_int(57))
```


### a function doesn't need to "do" anything
```python
def does_nothing(doesnt_matter):
    pass

print(does_nothing(598))
```