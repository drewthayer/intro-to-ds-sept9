# Day 4 Lecture Notes
<br><br><br><br><br><br>
# Loops
* we can use loops to perform repeated operations and solve numeric problems
* often we use **accumulators** to store/collect values that we alter or generate through the course of a loop
* use `for` loops when you know how many times to do something
* use `while` loops when the number of iterations needed to solve a problem is unknown
    * also for menus, sessions, "wait states"
    * watch out for **infinite loops**


<br><br><br><br>
## `for` loops
* if you "know how many times" you need to do something, you likely want to use a `for` loop.
* We will explore 2 forms of the `for` in Python:
    * using range values: `for i in range(n): print(i)`
    * traversing items: `for element in some_list: print(element)`


<br><br><br><br>
## Accumulators
* simply, an accumulutor is an object used to collect or store the results of operations within a loop
* declare the accumulator before the loop, and do something with it after the loop
* here we'll see them of types `int`, `float`, `boolean` and `list`, but accumulators can also be `dict` or `set`

<br><br>
### `int` accumulators
* here we're just summing all values from 0 and 19
* recall, we could just use `sum(list(range(20)))` to do this

```python
x = 0

for i in range(20):
    x += i
    print(x)

print(x)
```

<br><br>
### `float` accumulators
* When would you use a `float` for accumulation instead of an `int`?
    * monetary, or other calculations involving floating point values
    * consider exponential growth/decay

```python
x2 = 1.0

for i in range(1,20):
    x2 /= i
    print(x2)
print(x2)
```

<br><br>
#### "underflow"
As a sidenote, I want to mention the concept of "underflow" as it relates to the `float` data type. Underflow can occur when we attempt to calculate a number smaller than what we are able to store in memory. As I alluded before, `int` or "integers" are stored differently than "floats". 

An integer is more or less a direct representation of its binary form. For example, here are binary representations for integers from 0 to 16, if we are assuming only positive numbers (greater than or equal to 0):
```
0000 : 0
0001 : 1
0010 : 2
0011 : 3
0100 : 4
0101 : 5
0110 : 6
0111 : 7
1000 : 8
1001 : 9
1010 : 10
1011 : 11
1100 : 12
1101 : 13
1110 : 14
1111 : 15
```

The structure of a float is significantly different. Read this [wiki article](https://en.wikipedia.org/wiki/Single-precision_floating-point_format) if you're curious about how to convert from float representation to decimal. For now, the key takeaway is that we can't just "count" binary for a float, and the fraction cannot become infinitely small. At some point, we will "underflow" because we can't represent a number that small. We can encounter issues when comparing two float values to each other. I bring this up here because we can also encounter "unexpected behavior" when we decrease the size of floats toward infinitely small values, say, in a loop.

##### format of 32-bit (single-precision) float
```
     biased      
+/-  exponent    fraction
0    01010010    01000100010010000000000

```

<br><br>
### `bool` "accumulators", aka **flags**
We very often use flags in `while` loops, as an exit condition. Here we see a use of a flag in a `for` loop, however where we `break` as soon as the flag changes to `False`. The `break` keyword exits the current level of the loop.

Recall, `bool`s can only be `True` or `False`. This is convenient for us, as we can notice when the "state" of something changes. We can encounter a moment where it no longer makes sense for us to be in a loop.

Here, we'll use two accumulators. `x3` will become large quickly. If we are exploring how `x3` grows, but are not interested in any `x3` values larger than 10,000, we can define a condition for our loop to exit.

```python
exit_condition = True
x3 = 1.

for i in range(1,20):
    x3 *= i
    print(x3)

    if x3 > 10000:
        exit_condition = False

    if exit_condition == False:
        break # exit current loop level

print(x3)
```

<br><br>
### Loop Level
Another brief aside...

We have the ability to "nest" loops, or put them inside each other. The inner loop will run to completion for every single iteration of the loop that contains it. To illustrate this, try out these counting processes below:

<br><br>
#### Generate 4-bit binary and corresponding decimal
* Loop Levels : 4
    * e.g. 3 nested loops
```python
dec_val = 0

for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                print(i,j,k,l, ' : ', dec_val)
                dec_val += 1
```

<br><br>
#### Output a representation of time
* uncomment the `time` statements to have sort-of a running timer
    * it will be a little off
    * if you run this from terminal, press CTRL+c to exit the timer
```python
# import time
 
for hrs in range(24):
    for minutes in range(60):
        for secs in range(60):
            print(f'{hrs}:{minutes}:{secs}')
            # time.sleep(1) # uncomment for 1 sec delay
```

<br><br>
#### Traverse a nested list
When we get to `numpy`, we'll be able to perform matrix operations. For now, since we're dealing with `list` type storage, we will use nesting to traverse the contents of a list. 

```python
image = [
        [255,0,0,0,0,0],
        [0,255,0,0,0,0],
        [0,0,255,0,0,0],
        [0,0,0,255,0,0],
        [0,0,0,0,255,0]
        [0,0,0,0,0,255]
        ]

for row in image:
    # print(row)
    for val in row:
        print(val)
```

<br><br>
### list accumulators, or "collectors"
These follow the general principle that we've seen so far for accumulators. Now we are just `.append()`ing to some list we created prior to the loop.

In this procedure, we are only appending values to the list if they are divisible by 3.
```python
accum = []

for i in range(30, 60):
    if i % 3 == 0:
        accum.append(i)

print(accum)
```

<br><br>
### for loops that traverse items in a list
So far, we have used `range()` to define the number of times a `for` loop runs. Python provides a very convenient way of going through a list as many times as there are elements in that list.

```python
list1 = ['item1', 3, 9.7 ,[1, 2, 3], 'item5']

for item in list1:
    print(item)
```

<br><br>
#### filtering into another list
Here we traverse a list of names and collect only the names that are longer than 4 characters. Notice that `len()` applies not only to `list` types, but to strings as well.

```python
list_of_names = ['bob', 'cathy', 'george', 'dino', 'tom']

long_names = []

for name in list_of_names:
    if len(name) > 4:
        long_names.append(name)

print(long_names)
```

<br><br>
#### Unpack values from a single-nested list
The `list` data type can store any other type. As such, we can have a list contain another list. Here we show a simple way to check the data type of the item in the list, and, if it is a `list`, collect the items from the nested list into a list accumulator, using a nested `for` loop.

```python
mixed_list = ['word', [1,2,3,4,5], 43, 90.0]
unpacked_list = []

for item in mixed_list:
    
    if type(item) == list:
        for nested in item:
            unpacked_list.append(nested)
    else:
        unpacked_list.append(item)

print(unpacked_list)
```

<br><br>
#### `enumerate()` and mutating values in the list we are traversing
We can use the `enumerate()` function when we need to attach an index to the item at which we are looking. One use case for this is when we are scanning through a list and we wish to change values in that list based on some condition.

Notice that we can use some ideas from the `list` datatype when we are dealing with strings. The condition in this for loop checks if the first letter of each string is "d". If so, it replaces that animal with "ant".

```python
# access and mutate values in a list
animal_list = ['dog', 'cat', 'dolphin', 'bear', 'eagle']

for i, animal in enumerate(animal_list):
    if animal[0] == 'd':
        animal_list[i] = 'ant'

print(animal_list)
```

We can perform the same operation without using `enumerate()` as seen below. However, it's up to you to decide which approach you prefer. The yield the same result.

```python
animal_list = ['dog', 'cat', 'dolphin', 'bear', 'eagle']

for i in range(len(animal_list)):
    if animal_list[i][0] == 'd':
        animal_list[i] = 'ant'

print(animal_list)
```

<br><br>
#### accumulate from list values
Often we will traverse a list and gather values from that list into an `int` or `float` accumulator

Here we simply multiply all values in the list.
```python
x = 1

list_of_multipliers = [3, 7, 1, -3, 72, 22]

for mult in list_of_multipliers:
    x *= mult

print(x)
```

Here we divide `x` by all values in the list, one by one.
```python
x = 1.0

list_of_multipliers = [3, 7, 1, -3, 72, 22]

for mult in list_of_multipliers:
    x /= mult

print(x)
```

<br><br><br><br>
## Parallel `list`s
When two lists are the same length and have associated data at every index, we can consider them to be "parallel". Parallelism can occur between many types of data. Parallelism in lists is an easy way to start understanding the behavior that we'll see in dictionaries (`dict`).

If we have parallel `list`s, then we can use the same index to access the associated data across the lists.

<br><br>
### A simple example
```python
list_of_names   = ['bob', 'tom', 'don', 'larry']
list_of_heights = [  72 ,  68  ,  63  ,   76   ]
how_many_cats   = [   3 ,   1  ,   2  ,   23   ]

for i, name in enumerate(list_of_names):
    print('{} is {} inches tall'.format(name, list_of_heights[i]))
    print('   he has {} cats'.format(how_many_cats[i]))
```


<br><br><br><br>
## `while` loops
* use a while loop when the number of iterations of the loop is not known
* be careful of infinite loops

<br><br>
### an infinite `while`
```python
while True
    print('I can run forever')
```


<br><br>
### `while` loop using a conditional check
* a menu example
Here we use a `while` to build a `list`. After every order, we check to see if another order should be made.


```python
def get_menu_item():
    menu = '''Choose an item:
              (1) broccoli
              (2) carrots
              (3) cabbage
              choice:  '''

    choice = int(input(menu))
    items = ['broccoli', 'carrots', 'cabbage']
    return items[choice-1]

orders = []

cont = 'y'
while cont == 'y':
    orders.append(get_menu_item())

    # order_max -= 1
    cont = input('order more? ')

print(orders)
```

<br><br>
### `while` for solving "open-ended" problems
Here we use a while loop nested in a for loop to take 100 random integer samples, between 1 and 100. We record the number of times it takes for us to achieve a sample below a threshold. We record these in a list accumulator. We then use another accumulator to analyze the distribution of number of trials.

I provide functions here to demonstrate this procedure. I then print our output as a distribution in the terminal. Try to pick through this code and understand what is happening. I'm happy to explain it further.

```python
from random import choice

def get_sample(lower=1, upper=100):
    return choice(range(1, upper+1))

def get_sample_counts(m, threshold):
    output = []

    for _ in range(m):
        num_trials = 1
        while True:
            sample = get_sample()

            if sample < threshold:
                output.append(num_trials)
                break
            else:
                num_trials += 1

    return output


sample_trials = get_sample_counts(100, 25)

# we will make the index of counts correspond with the
# number of trials
counts = [0]*(max(sample_trials) + 1)

for trial in sample_trials:
    counts[trial] += 1

# we'll make a simple terminal graphic to display the distribution of number of trials needed to achieve a value below a given threshold.
for i, count in enumerate(counts):
    if i == 0:
        continue
    print('{:4d}: {}'.format(i, '*' * count))
```


<br><br><br><br>
## `break`, `continue`, and `pass`

<br><br>
### `break`
* use `break` to avoid or exit infinite loops when using while
* use `break` to exit a `for` or `while` loop when further computation is no longer necessary

#### `break`ing a `while
```python
while True: # note, infinite loop
    input = input('Do you want to continue looking at this message? Spell "committment" correctly in order to exit, otherwise we\'re doing this forever... ')    

    if input == 'commitment':
        break
```

<br><br>
### `continue`
* use `continue` to conditionally skip an operation
Here we will use `continue` to separate squares from non-squares. We could easily write this another way, without using `continue`.

```python
not_squares = []

def is_square(num):
    for i in range(2,num):
        if i**2 == num:
            return True
        if i**2 > num:
            break

    return False


for i in range(2, 101):
    if is_square(i) == True:
        continue
    not_squares.append(i)

print(not_squares)
```


<br><br>
### `pass`
* for now, use `pass` as a placeholder in an unfinished function, that you have yet to figure out.

```python
def grow_up():
    pass

def get_enough_sleep():
    pass

def do_the_dishes():
    pass
```



<br><br><br><br>
## list comprehensions, a brief introduction
* comprehensions generate lists
* they are more performant than `for` loops, generally.
* basic form: `list_of_items = [item for item in some_list]`

Comprehensions deserve more than this cursory glance. That said, all functionality of list comprehensions can be solved using `for` loops, so it is much more important to learn `for` loops at this point. To this end, I will give you some templates for performing basic operations using comprehensions. 

<br><br>
### Comprehensions to perform casting across elements in a list

```python
list_of_ints = [0, 1, 2, 3, 4, 5, 6, 7]

list_of_int_strings = [str(num) for num in list_of_ints]

list_of_floats = [float(num) for num in list_of_ints]

list_of_bools = [bool(num) for num in list_of_ints]
```

<br><br>
### Comprehensions to filter elements in a list
Note here that we are using `range` within the comprehensions

```python
divisible_by_7_and_12 = [num for num in range(1, 1000) if num % 7 == 0 and num % 12 == 0]
```

<br><br>
### Nested Comprehensions
Although we'll solve an `is_prime()` function below, let's demonstrate a slick piece of code to generate a list of prime numbers up to 1000, using a nested comprehension.

```python
primes = [num for num in range(2, 1000) if all(num % num2 != 0 for num2 in range(2, int(num/2)+1))]
```


<br><br><br><br>
## Let's Write some Functions!

<br><br>
### the `factorial()` function

#### using a `while` loop
```python
def factorial(k):
    result = 1
    while k > 0:
        result = result * k
        k -= 1
    return result

print(factorial(5))
```


#### `for` loop 1
```python
def factorial(k):
    result = 1

    for i in range(k+1):
        if i == 0:
            continue    
        result = result * i    

    return result

print(factorial(5))
```

#### `for` loop 2
```python
def factorial(k):
    result = 1

    for i in range(k+1):  
        result *= i    

    return result

print(factorial(5))
```

<br><br>
### the `is_prime()` function

```python
def is_prime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num/2), 2):
            if num % i == 0:
                return False

    return True
    
primes = []
for i in range(2, 100):
    if is_prime(i):
        primes.append(i)

print(primes)
```
