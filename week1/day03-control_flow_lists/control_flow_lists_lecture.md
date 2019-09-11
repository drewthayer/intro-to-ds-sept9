# Day 3 Lecture Notes

## Python Naming Conventions
* properly name things according to conventions in Python, **GIVE IT A GOOD NAME**
    * Described in Pep 8: https://www.python.org/dev/peps/pep-0008/
* **snake case**: using underscores to separate words
    * promotes readability
    * applies to variable names and function names
    * often applies to filenames as well
* Names are appropriately descriptive
    * variable names are descriptive nouns
        * examples: 
            * `mean_of_eagle_flight = 70`
            * `std_of_florida_ages = 14.7`
            * `name_of_cat = 'Chairman Meow'`
    * function names describe actions
        * examples:
            * `def calc_mean_of_eagle_flight(heights): pass`
            * `def display_menu(): pass`
            * `def concatenate_three_strings(string_1, string_2, string_3): pass`
    * Further: `module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name`
    * Be careful not to make exceedingly long names


## Control Flow
* control the flow of your programs using basic logic
    * using `if`, `elif` and `else`
    * with the `==`, `!=`, `>`, `<`, `>=` and `<=` operators

### Basic if/else
```python
num = int(input('Enter a number: '))

if num > 30:
    print(num * 3)
else:
    print(num + 90)

print('We\'re done')
```

### `if/elif/else`
* `else` will execute if no other conditions are met
```python
num = float(input('Enter a float: '))

if num > 10:
    print('{} is greater than 10'.format(num))
elif y <= 10 and y > 5:
    print('{} is less than or equal to 10 and greater than 5'.format(num))
else:
    print('{} is less than or equal to 5'.format(num))
```

### make menus with `if/elif/else`
* you can have as many `elifs` as you need
```python
menu_choice = input('Choose a food item: burrito: (b), pasta: (p), orange: (o): ')

if menu_choice == 'b':
    print('Great, you\'ll get a burrito')
elif menu_choice == 'p':
    print('You\'re going to want some water with that')
elif menu_choice == 'o':
    print('Vitamin C')
else:
    print('We don\'t have that, sorry we\'re a crappy restaurant')
```

### `and`, `or` and `not`
* these are **logical operators** to create compound conditions
* `not` precedes `and` precedes `or` in logical order of operations
    * use parentheses to keep your logic clear
```python
num = int(input('Enter an integer: '))

if num % 2 == 0 and num % 3 == 0:
    print('{} is divisible by both 2 and 3'.format(num))
elif num % 3 == 0:
    print('{} is divisible by 3'.format(num))
elif num % 2 == 0:
    print('{} is divisible by 2'.format(num))
else:
    print('{} is divisible by neither 2 or 3'.format(num))
```

```python
some_string = input('Enter a string of length between 3 and 10 characters: ')

if not (len(some_string) < 3 or len(some_string) > 10):
    print('{} is a good string length'.format(some_string))
else:
    print('{} is not between the appropriate bounds'.format(some_string))
```




## `lists` 
* declare lists using the syntax `some_list = []` or `some_list = list()`
* create lists with values, like `some_list = [3, 2, 9, 18, 34]`
* create lists filled with one value, like `some_list = [7] * 10`
* generate a series of numbers in lists by using `some_list = list(range(a, n))`


### create an empty list
```python
some_list = [] # this is most common
another_list = list() # this works too
```

### create lists with values
* note that a `list` can contain multiple datatypes
```python
list_of_nums = [3, 2, 9, 18, 34]
print(list_of_nums)

list_of_mixed_types = [True, 14, 'cat', [76, 33.3]]
print(list_of_mixed_types)
```

### syntax to create a list of some length with a single value
```python
cat_list = ['cat'] * 3
# cat_list = ['cat'] + ['cat'] + ['cat'] # equivalent
print(cat_list)
```

### generating a `list` with a `range` of numbers
* `range` is a type, but we can cast it as a list using `list()`
* `range(0,n)` is not inclusive of `n`
```python
a = 0
n = 20

num_list = list(range(a, n))
print(num_list)
```


### indices and accessing elements/values in lists
* Python uses zero-indexing (element position numbering starts at 0)
    * `some_list[0]` to access the first element in the list
    * `some_list[-1]` to access the last value of a list
```python
animal_list = ['cat', 'dog', 'bird']

print('the first animal in the list is {}'.format(animal_list[0]))

print('the last animal in the list is {}'.format(animal_list[-1]))
```


### modify list values    
* lists are a **mutable** type
* `some_list[0] = 7` : sets the first value in the list to `7`
```python
animal_list = ['platypus', 'beaver', 'hawk']

animal_list[0] = 'dolphin'

print(animal_list)
```


### list slicing
* `some_list[0:5]` to access the first 5 values in a list
    * this slice is not inclusive of index `5`
* `some_list[-5:-1]` to access the last 4 values in a list
```python
a = 20
n = 40

num_list = list(range(a, n))

print(num_list[0:5])
print(num_list[10:])
print(num_list[7:14])
print(num_list[-7:-2])
```

### create a sublist
* modifying the original list will not affect the sublist, or vice-versa
```python
a = 10
n = 20

num_list = list(range(a, n))

num_sublist = num_list[0:5]

num_sublist[0] = 900
print(num_list[0])
```


### list "unpacking"
* data types that are "collections" tend to be able to be unpacked, where their elements can be placed into variables by using the assignment operator `=`
* we most often see this with `tuple`, but we can do this with lists as well
* the number of variables in which you unpack a collection must be equal to the size of the collection

```python
cat_list = ['cat'] * 3

cat1, cat2, cat3 = cat_list # unpacking

print('{} {} {}'.format(cat1, cat2, cat3))
```


### `in` and `not in`
* check if a value is in a collection (`list` in this case)
* resolves to a `bool` value
* ex: `if 7 not in some_list: print('dang')`

```python
a = 10
n = 20

new_list = list(range(a, n))

fifteen_ness = 15 in new_list
print(fifteen_ness)

if fifteen_ness:
    print('yay, 15')

non_fifteen_ness = 15 not in new_list
print(non_fifteen_ness)

if not non_fifteen_ness:
    print('boo, 15')
```

```python
def check_dolphin(string_list):
    if 'dolphin' in string_list:
        print('dolphins swim good')
    else:
        print('no dolphins here')

animal_list = ['platypus', 'beaver', 'hawk']

check_dolphin(animal_list)

animal_list[0] = 'dolphin'

check_dolphin(animal_list)
```


### common list functions:
* the difference between functions and methods is subtle. For our purposes, functions are like boxes that we put things into in order to get something else out.
* the functions below don't alter the list
    

### `len(some_list)` 
* Len is your best and oldest functional friend, you'll spend a lot of time with Len.
```python
a = 10
n = 20

num_list = list(range(a, n)) # not inclusive of n
print(len(num_list))
```

### `sum(some_list)`
* adds all values in the list
```python
a = 10
n = 20

num_list = list(range(a, n))
print(sum(num_list))
```

### `sorted(some_list)`
* sorts a list ascending
```python
str_list = ['z','l', 'j', 'q']
print(sorted(str_list))
```

### `list(reversed(sorted(str_list)))`
* sorts a list descending
* note that `reversed()` does not return a list, it returns a generator that we can cast as a `list`
```python
str_list = ['z','l', 'j', 'q']
print(list(reversed(sorted(str_list))))
```

### `max(some_list)`
* returns the maximum element value
```python
a = 30
n = 90

num_list = list(range(a, n))
print('max: ', max(num_list))
```

### `min(some_list)`
* returns the minimum element value
```python
a = 30
n = 90

num_list = list(range(a, n))
print('min: ', min(num_list))
```

### `any(some_list)`
* `True` if ANY values in some_list are "truthy" 
```python
bool_list = [True, False, True, True, False]
print(any(bool_list))

a = 10
n = 20

num_list = list(range(a, n))
print(any(num_list))
```

### `all(some_list)`
* `True` if ALL values in some_list are "truthy" 
```python
bool_list = [True, False, True, True, False]
print(all(bool_list))

a = 10
n = 20

num_list = list(range(a, n))
print(all(num_list))

num_list[0] = 0
print(all(num_list))
```

### common list methods
* some of these methods may alter/mutate the list
* we can think of the methods below as belonging to the `list` data type


### `some_list.append(x)`
* places a new value at the end of the list
```python
a = 10
n = 20

num_list = list(range(a, n))
print(num_list)
num_list.append('duck')
print(num_list)
```

### `some_list.extend(another_list)`
* puts the contents of `another_list` into `some_list`
```python
a = 10
n = 20

num_list = list(range(a, n))
print(num_list)

other_list = [7, 3, 55]

# num_list.append(other_list)
num_list.extend(other_list)
```

### `some_list.pop()`
* removes and **returns** the last item in the list
```python
a = 10
n = 20

num_list = list(range(a, n))

print(num_list)
print(num_list.pop())
print(num_list)
```

### `some_list.reverse()`
* reverses the list
```python
a = 10
n = 20

num_list = list(range(a, n))

num_list.reverse()
print(num_list)
```

### `some_list.sort()`
* sorts the list, ascending by default
```python
fruit_list = ['apple', 'pear', 'peach', 'mango']

fruit_list.sort()

print(fruit_list)
```

### `some_list.remove(x)`
* remove a specific value from the list
```python
fruit_list = ['apple', 'pear', 'peach', 'mango']

fruit_list.remove('pear')
print(fruit_list)
```

### `some_list.count(x)`
* counts the number of occurrences of a specific value in the list
```python
yet_another = [7] * 5
print(yet_another.count(7))
```


### list copying    
* make a real, unique copy of a list with the same values as the original
* there are multiple ways to do this
```python
some_list = [1, 4, 3, 6, 8, 4]

some_new_list = some_list.copy()
some_new_list = some_list[:]
some_new_list = list(some_list)
```

### lists are an **iterable** type
* meaning we can traverse them with some type of loop or function mapping (we'll do this soon)
* consider the error message that `list(27)` produces when run:
```python
list(27)
```


## WRITE FUNCTIONS

### write the `is_divisor(num1, num2)` function
* a function to check if one number is divisible by another number
* TRY TO WRITE THIS YOURSELF!


### write the `sum_to_n()` function using a function on a list
```python
def sum_to_n(n):
    return sum(list(range(0,n+1)))

print(sum_to_n(4))
```

### write the `sum_range(a, b)` function
* a function to sum all values in the range a to b, including b
* TRY TO WRITE THIS YOURSELF!


### write the `sum_range_divisible_by_a()` function
* for example: sum from 0 to 20 of values divisible by 3
```python
def sum_range_divisible_by_a(n, d):
    num_list = list(range(0,n+1, d))
    # print(num_list)
    return sum(num_list)

print(sum_range_divisible_by_a(20, 3))
```