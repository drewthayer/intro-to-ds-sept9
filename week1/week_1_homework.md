
# Weekend Homework
We covered a lot over these first few days. We have a large enough set of tools, at this point, to start writing functions that actually "do things."

I want you to complete as much of this notebook as you can. If you find yourself stuck for more than 10 minutes on any given problem, post the problem and a description of how you're stuck into the Slack channel. Your classmates or I will respond **in a reply within the thread**.

There are multiple ways to solve most of these functions. Feel free to solve these in any way you feel comfortable. You may also include multiple solutions for any given problem.

## We will be writing functions!
This is key to our progress through the course. Almost all of the problems below will have you writing a function. For many of these, we provide you some starting code.

Remember to *test your functions*! You can do this with simple `print()` statements within the same cell. The first few functions have these `print` statements written for you.

Feel free to work on these within the jupyter notebook, or move them to a separate `.py` file.

<br><br><br>
### `return_float()`
Write a function called `return_float()` that takes a numeric type and returns the `float` of that number.


```python
def return_float(some_num):
    pass

print(return_float(89))
print(return_float(False))
print(return_float(978.33))
```

<br><br><br>
### `return_bool()`
Write a function called `return_bool()` that takes a numeric type and returns the `bool` value of that number.


```python
def return_bool(some_num):
    pass

print(return_bool(-42))
print(return_bool(False))
print(return_bool(None))
```

<br><br><br>
### `return_type()`
Write a function called `return_type()` that simply returns the `type` of the data that is passed into it. Use the `str()` function to cast the type to a string.


```python
def return_type(data):
    pass

# write your own function calls to check the outcome
```

<br><br><br>
### `round_up()`
Write a function called `round_up()` that takes a float number and rounds it up to the next digit. This function  should return an integer.

For example:
```python
print(round_up(57.353))
>>> 58
```


```python
def round_up():
    pass

# write your own function calls to check the outcome
```

<br><br><br>
### `square_divisible_by_6()`
Write a function called `square_divisible_by_6()` that returns `True` if the square of an `int` passed into it is divisible by 6.


```python
def square_divisible_by_6(some_int):
    pass

# write your own function calls to check the outcome
```

<br><br><br>
### `square_divisible_by_n()`
Write a function called `square_divisible_by_n()` that returns `True` if the square of an `int` passed into it is divisible by another int.


```python
def square_divisible_by_n(some_int, divisor):
    pass


```

<br><br><br>
### `calc_fourth_order_polyn()`
Write a function called `calc_fourth_order_polyn()` that returns the result of a 4th order polynomial of the form:

$$
y = Ax^4 + Bx^3 + Cx^2 + Dx + E
$$


```python
def calc_fourth_order_polyn(A, B, C, D, E, x):
    pass


```

<br><br><br>
### `discuss_favorite_number()`
Write a function called `discuss_favorite_number()` that asks the user for their favorite number between 0 and 100. Print different messages depending on in which quartile the favorite number falls. Make up your own messages:

for example
```
< 25 : "I used to think numbers in the 1st quartile were cool"
> 25, < 50 : "something else"
...
```

If you want to get fancy, print "Number out of range!" if the favorite number is not between 0 and 100.


```python
def discuss_favorite_number():
    num = int(input('Enter your favorite number: '))
    # write your code below
```

<br><br><br>
### `select_department()`
Write a function called `select_department()` that asks the user for the department they want to reach. Return the phone number for each department. Feel free to make these up. `return` the string `Erroneous Choice` if they make a choice not in the list:


```python
def select_department():
    menu = '''
            Select a Department:
            (1) Shipping and Receiving
            (2) Customer Service
            (3) Human Resources
            (4) IT
           '''

    selection = int(input(menu))
    # write your code below

```

<br><br><br>
### `get_range_from_list()`
Write a function called `get_range_from_list` that takes a list and returns the range of the values in that list.

for example:
```
list1 = [1, 4, -6, 39, 23]
get_range_from_list(list1)
>>> 45
```


```python
# It's time for you to define and test your own functions
```

<br><br><br>
### `get_mean_of_list()`
Write a function called `get_mean_of_list` that takes a list and returns the mean of the values in that list.

for example:
```
list1 = [1, 4, -6, 39, 23]
get_mean_of_list(list1)
>>> 12.2
```

<br><br><br>
### `get_median_of_list()`
Write a function called `get_median_of_list` that takes a list and returns the median of the values in that list.

Make sure you account for the case where the list has an even number of values in it!


```python

```

<br><br><br>
### `get_below_median_avg()`
Write a function called `get_below_median_avg` that takes a list and returns the median of the values in that list that are below the median. Do not include the median value in your calculation.

Make sure you account for the case where the list has an even number of values in it!


```python

```

<br><br><br>
### `create_boolean_mask()`
Write a function called `create_boolean_mask` that takes a `list` as an argument and returns another list of boolean values indicating whether or not those values are considered `True` or `False` by Python. Do not account for nested lists.




```python

```

<br><br><br>
### `apply_boolean_mask()`
Write a function called `apply_boolean_mask` that takes two lists of the same length: a `list` of values (any type) and another list containing only booleans. Your function should return a new list containing only the items in the values list that correspond to `True` in the boolean list.


```python

```

<br><br><br>
### `get_differences()`
Write a function called `get_differences` that takes two lists of numbers (floats or ints) of the same length. `return` a new list that contains the differences between corresponding indices in the two lists.


```python

```

<br><br><br>
### `get_mse()`
Write a function called `get_mse` that takes two lists of numbers (floats or ints) of the same length. Calculate the mean squared error between the two lists. This is the sum of all differences between the two lists, squared, and divided by the length of one of the lists.

$$
MSE(a, b) = \frac{1}{m}\sum_{i=1}^m (a - b)^2
$$


```python

```

<br><br><br>
### `get_mae()`
Write a function called `get_mae` that takes two lists of numbers (floats or ints) of the same length. Calculate the mean absolute error between the two lists. This is the sum of all absolute valued differences between the two lists, divided by the length of one of the lists.

$$
MAE(a, b) = \frac{1}{m}\sum_{i=1}^m \left| (a - b) \right|
$$


```python

```

<br><br><br>
### `create_trinary_numbers()`
Write a function called `create_trinary_numbers` that returns two lists that are parallel to each other:

`list_of_trinary`: in order, string representations of length-3 trinary numbers, represented as strings
* `list_of_trinary = ['000', '001', '002', '010', '011', ...]

`list_of_base10`: in order, integer representations of the values in `list_of_trinary`

hint: to create the string representations, you can use the `.format()` function that appears throughout the lecture notes:

```python
str_repr = '{}{}{}'.format(0,3,1)
```


```python

```

<br><br><br>
### `increment_towards_n(target, starting_point, incr=10)`
Write a function called `increment_towards_n` that takes three numbers as arguments.
* `target` : the number that you want to move the starting_point toward
* `starting_point` : the value you want to move toward the target. You may not perform mathematical operations that directly involve `target` and `starting_point`.
* `incr` : a multiplier that you can apply to the `starting_point` in order to move it toward `target`. However, within your function, you may only change `increment` by multiplying or dividing it by 10.

Note: it is bad practice to modify the names of parameters. For that reason, we provide some starter code for you, where we rename the two parameters that will change.


```python
def increment_towards_n(target, starting_point, increment=10):
    starting_point_ = starting_point
    increment_ = increment
    # write your code below
```
