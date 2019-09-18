
# Weekend Homework
We covered a lot over these first few days. We have a large enough set of tools, at this point, to start writing functions that actually "do things."

I want you to complete as much of this notebook as you can. If you find yourself stuck for more than 10 minutes on any given problem, post the problem and a description of how you're stuck into the Slack channel. Your classmates or I will respond **in a reply within the thread**.

There are multiple ways to solve most of these functions. Feel free to solve these in any way you feel comfortable. You may also include multiple solutions for any given problem.

## We will be writing functions!
This is key to our progress through the course. Almost all of the problems below will have you writing a function. For many of these, we provide you some starting code.

Remember to *test your functions*! You can do this with simple `print()` statements within the same cell. The first few functions have these `print` statements written for you.

Feel free to work on these within the jupyter notebook, or move them to a separate `.py` file.

## NOTE: These are not the only solutions
In most cases below, the solution provided is meant to be explanatory. These are not meant to be optimal solutions, nor are they the only way to solve any of these problems.

<br><br><br>
### `return_float()`
Write a function called `return_float()` that takes a numeric type and returns the `float` of that number.


```python
def return_float(some_num):
    return float(some_num)

print(return_float(89))
print(return_float(False))
print(return_float(978.33))

```

    89.0
    0.0
    978.33


<br><br><br>
### `return_bool()`
Write a function called `return_bool()` that takes a numeric type and returns the `bool` value of that number.


```python
def return_bool(some_num):
    return bool(some_num)

print(return_bool(-42))
print(return_bool(False))
print(return_bool(None))

```

    True
    False
    False


<br><br><br>
### `return_type()`
Write a function called `return_type()` that simply returns the `type` of the data that is passed into it. Use the `str()` function to cast the type to a string.


```python
def return_type(data):
    return str(type(data))

# write your own function calls to check the outcome
print(return_type(True))
print(return_type(0.97))
print(return_type('giraffe'))

```

    <class 'bool'>
    <class 'float'>
    <class 'str'>


<br><br><br>
### `round_up()`
Write a function called `round_up()` that takes a float number and rounds it up to the next digit. This function  should return an integer.

For example:
```python
print(round_up(57.353))
>>> 58
```


```python
def round_up(num):
    return int(num) + 1

# write your own function calls to check the outcome
round_up(7.3)

```




    8



<br><br><br>
### `square_divisible_by_6()`
Write a function called `square_divisible_by_6()` that returns `True` if the square of an `int` passed into it is divisible by 6.


```python
def square_divisible_by_6(some_int):
    if some_int**2 % 6 == 0:
        return True
    else:
        return False

# write your own function calls to check the outcome
squares_div_by_6 = []
for i in range(1, 1000):
    if square_divisible_by_6(i) == True:
        squares_div_by_6.append(i)
    
print(squares_div_by_6)

# consider the pattern in this generated list. What redundant
# operations have been performed?

```

    [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198, 204, 210, 216, 222, 228, 234, 240, 246, 252, 258, 264, 270, 276, 282, 288, 294, 300, 306, 312, 318, 324, 330, 336, 342, 348, 354, 360, 366, 372, 378, 384, 390, 396, 402, 408, 414, 420, 426, 432, 438, 444, 450, 456, 462, 468, 474, 480, 486, 492, 498, 504, 510, 516, 522, 528, 534, 540, 546, 552, 558, 564, 570, 576, 582, 588, 594, 600, 606, 612, 618, 624, 630, 636, 642, 648, 654, 660, 666, 672, 678, 684, 690, 696, 702, 708, 714, 720, 726, 732, 738, 744, 750, 756, 762, 768, 774, 780, 786, 792, 798, 804, 810, 816, 822, 828, 834, 840, 846, 852, 858, 864, 870, 876, 882, 888, 894, 900, 906, 912, 918, 924, 930, 936, 942, 948, 954, 960, 966, 972, 978, 984, 990, 996]


<br><br><br>
### `square_divisible_by_n()`
Write a function called `square_divisible_by_n()` that returns `True` if the square of an `int` passed into it is divisible by another int.


```python
def square_divisible_by_n(some_int, divisor):
    if some_int**2 % divisor == 0:
        return True
    else:
        return False

squares_div_by_n = []
for i in range(1, 1000):
    if square_divisible_by_n(i, 7) == True:
        squares_div_by_n.append(i)
    
print(squares_div_by_n)

# By plugging in various integer values, we can see that 
# we can simply check divisibility and that the squaring is
# redundant

```

    [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175, 182, 189, 196, 203, 210, 217, 224, 231, 238, 245, 252, 259, 266, 273, 280, 287, 294, 301, 308, 315, 322, 329, 336, 343, 350, 357, 364, 371, 378, 385, 392, 399, 406, 413, 420, 427, 434, 441, 448, 455, 462, 469, 476, 483, 490, 497, 504, 511, 518, 525, 532, 539, 546, 553, 560, 567, 574, 581, 588, 595, 602, 609, 616, 623, 630, 637, 644, 651, 658, 665, 672, 679, 686, 693, 700, 707, 714, 721, 728, 735, 742, 749, 756, 763, 770, 777, 784, 791, 798, 805, 812, 819, 826, 833, 840, 847, 854, 861, 868, 875, 882, 889, 896, 903, 910, 917, 924, 931, 938, 945, 952, 959, 966, 973, 980, 987, 994]


<br><br><br>
### `calc_fourth_order_polyn()`
Write a function called `calc_fourth_order_polyn()` that returns the result of a 4th order polynomial of the form:

$$
y = Ax^4 + Bx^3 + Cx^2 + Dx + E
$$


```python
def calc_fourth_order_polyn(A, B, C, D, E, x):
    return A*x**4 + B*x**3 + C*x**2 + D*x + E


print(calc_fourth_order_polyn(1, 2, 3, 4, 5, 3))

```

    179


<br><br><br>
### `discuss_favorite_number()`
Write a function called `discuss_favorite_number()` that asks the user for their favorite number between 0 and 100. Print different messages depending on in which quartile the favorite number falls. Make up your own messages:

for example
```
< 25 : "I used to think numbers less than the 1st quartile were cool"
> 25, < 50 : "something else"
...
```

If you want to get fancy, print "Number out of range!" if the favorite number is not between 0 and 100.


```python
def discuss_favorite_number():
    num = int(input('Enter your favorite number: '))
    # write your code below
    if num < 0 or num > 100:
        print('Number out of range!')
    elif num < 25:
        print('less than 25')
    elif num < 50:
        print('greater than or equal to 25, less than 50')
    elif num < 75:
        print('greater than or equal to 50, less than 75')
    else:
        print('greater than or equal to 75, less than or equal to 100')
        
discuss_favorite_number()

```

    Enter your favorite number: 50
    greater than or equal to 50, less than 75


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
            \n
           '''

    selection = int(input(menu))
    # write your code below
    if selection == 1:
        return '517-723-2120'
    elif selection == 2:
        return '586-283-5911'
    elif selection == 3:
        return '105-328-8484'
    elif selection == 4:
        return '987-482-3858'
    else:
        return 'Erroneous Choice'
    
select_department()

```

    
                Select a Department:
                (1) Shipping and Receiving
                (2) Customer Service
                (3) Human Resources
                (4) IT
                
    
               9





    'Erroneous Choice'



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
def get_range_from_list(some_list):
    return max(list1) - min(list1)

list1 = [1, 4, -6, 39, 23]
get_range_from_list(list1)

```




    45



<br><br><br>
### `get_mean_of_list()`
Write a function called `get_mean_of_list` that takes a list and returns the mean of the values in that list.

for example:
```
list1 = [1, 4, -6, 39, 23]
get_mean_of_list(list1)
>>> 12.2
```


```python
def get_mean_of_list(some_list):
    return sum(some_list) / len(some_list)
    
list1 = [1, 4, -6, 39, 23]
get_mean_of_list(list1)

```




    12.2



<br><br><br>
### `get_median_of_list()`
Write a function called `get_median_of_list` that takes a list and returns the median of the values in that list.

Make sure you account for the case where the list has an even number of values in it!


```python
def get_median_of_list(some_list):
    sorted_list = sorted(some_list)
    
    if len(some_list) % 2 == 1:
        return some_list[int(len(some_list) / 2)]
    else:
        return (some_list[int(len(some_list) / 2)-1] 
                + some_list[(int(len(some_list) / 2))]) / 2
    
list1 = [1,3,4,6,8,9,21,23,33,45,67] # odd list
list2 = [1,3,4,6,8,9,21,23,33,45,67,68] # even list

get_median_of_list(list2)

```




    15.0



<br><br><br>
### `get_below_median_avg()`
Write a function called `get_below_median_avg` that takes a list and returns the median of the values in that list that are below the median. Do not include the median value in your calculation.

Make sure you account for the case where the list has an even number of values in it!


```python
def get_below_median_avg(some_list):
    below_median_list = []
    median = get_median_of_list(some_list)
    
    for num in some_list:
        if num < median:
            below_median_list.append(num)
            
    return get_median_of_list(below_median_list)

list1 = [1,3,4,6,8,9,21,23,33,45,67] # odd list
list2 = [1,3,4,6,8,9,21,23,33,45,67,68] # even list

get_below_median_avg(list2)

```




    5.0



<br><br><br>
### `create_boolean_mask()`
Write a function called `create_boolean_mask` that takes a `list` as an argument and returns another list of boolean values indicating whether or not those values are considered `True` or `False` by Python. Do not account for nested lists.




```python
def create_boolean_mask(some_list):
    output = []
    
    for item in some_list:
        output.append(bool(item))
    
    return output

list1 = [None, 1, 0, 365, 42, "hey"]

create_boolean_mask(list1)

```




    [False, True, False, True, True, True]



<br><br><br>
### `apply_boolean_mask()`
Write a function called `apply_boolean_mask` that takes two lists of the same length: a `list` of values (any type) and another list containing only booleans. Your function should return a new list containing only the items in the values list that correspond to `True` in the boolean list.


```python
def apply_boolean_mask(orig, mask):
    output = []
    
    for i, boolean in enumerate(mask):
        if boolean:
            output.append(orig[i])

    return output

list1 = [None, 1, 0, 365, 42, "hey"]
mask = create_boolean_mask(list1)

apply_boolean_mask(list1, mask)

```




    [1, 365, 42, 'hey']



<br><br><br>
### `get_differences()`
Write a function called `get_differences` that takes two lists of numbers (floats or ints) of the same length. `return` a new list that contains the differences between corresponding indices in the two lists.


```python
def get_differences(list1, list2):
    differences = []
    for i in range(len(list1)):
        differences.append(list1[i] - list2[i])
    return differences

list1 = [9,3,5,2,3,4,6]
list2 = [7,2,7,1,2,6,8]

get_differences(list1, list2)

```




    [2, 1, -2, 1, 1, -2, -2]



<br><br><br>
### `get_mse()`
Write a function called `get_mse` that takes two lists of numbers (floats or ints) of the same length. Calculate the mean squared error between the two lists. This is the sum of all differences between the two lists, squared, and divided by the length of one of the lists.

$$
MSE(a, b) = \frac{1}{m}\sum_{i=1}^m (a - b)^2
$$


```python
def get_mse(list1, list2):
    differences = get_differences(list1, list2)
    sq_differences = []
    
    for num in differences:
        sq_differences.append(num**2)
    

    return sum(sq_differences) / len(sq_differences)

list1 = [9,3,5,2,3,4,2]
list2 = [7,2,7,0,2,6,8]

get_mse(list1, list2)

```




    7.714285714285714



<br><br><br>
### `get_mae()`
Write a function called `get_mae` that takes two lists of numbers (floats or ints) of the same length. Calculate the mean absolute error between the two lists. This is the sum of all absolute valued differences between the two lists, divided by the length of one of the lists.

$$
MAE(a, b) = \frac{1}{m}\sum_{i=1}^m \left| (a - b) \right|
$$


```python
def abs_value(n):
    if n > 0:
        return n
    else:
        return -n

def get_mae(list1, list2):
    differences = get_differences(list1, list2)
    abs_differences = []
    
    for num in differences:
        abs_differences.append(abs_value(num))

    return sum(abs_differences) / len(abs_differences)
        
list1 = [9,3,5,2,3,4,2]
list2 = [7,2,7,0,2,6,8]

get_mae(list1, list2)

```




    2.2857142857142856



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
def create_trinary_numbers():
    dec = 0
    list_of_base10 = []
    list_of_trinary = []
    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                list_of_trinary.append('{}{}{}'.format(i,j,k))
                list_of_base10.append(dec)
                dec += 1
                
    return list_of_base10, list_of_trinary

base10, trinary = create_trinary_numbers()

for i,num in enumerate(base10):
    print(f'{num}: {trinary[i]}')
    
```

    0: 000
    1: 001
    2: 002
    3: 010
    4: 011
    5: 012
    6: 020
    7: 021
    8: 022
    9: 100
    10: 101
    11: 102
    12: 110
    13: 111
    14: 112
    15: 120
    16: 121
    17: 122
    18: 200
    19: 201
    20: 202
    21: 210
    22: 211
    23: 212
    24: 220
    25: 221
    26: 222


<br><br><br>
### `increment_towards_n(target, starting_point, incr=10)`
Write a function called `increment_towards_n` that takes three numbers as arguments. Assume that these numbers will always be positive.
* `target` : the number that you want to move the starting_point toward
* `starting_point` : the value you want to move toward the target. You may not perform mathematical operations that directly involve `target` and `starting_point`.
* `incr` : a multiplier that you can apply to the `starting_point` in order to move it toward `target`. However, within your function, you may only change `increment` by multiplying or dividing it by 10.

There are many solutions to this problem. There are solutions that will work for a given range. There are other, more generalizable solutions that should work for a reasonably arbitrary range, including negatives. 

Note: it is bad practice to modify the names of parameters. For that reason, we provide some starter code for you, where we rename the two parameters that will change.


```python
# What I have here is a very simple algorithm. 
# It will only work for a limited domain of 
# targets and starting points. This is an exercise
# in inventing an algorithm to solve a problem. See
# how you can improve/expand on the solution below!

def increment_towards_n(target, 
                        starting_point, 
                        increment=10.0):
    estimate = starting_point
    increment_ = increment
    
    # write your code below
    num_iters = 1
    estimation_values = []
    
    
    while int(estimate) != target:
        
        if estimate < target:
            if target - estimate > estimate:
                estimate += estimate
            else:
                estimate += estimate * (increment_/10/10)
            
            
        else:
            if estimate - target > increment_:
                estimate -= estimate // increment
            else:
                estimate -= estimate * (increment/10/10)
                
        estimation_values.append(estimate)
        num_iters += 1

        # safety
        if num_iters >= 1000:
            break
            
    return num_iters, estimation_values       

increment_towards_n(target=1000, starting_point=93)

```




    (26,
     [186,
      372,
      744,
      818.4,
      900.24,
      990.264,
      1089.2904,
      981.2904000000001,
      1079.4194400000001,
      972.4194400000001,
      1069.6613840000002,
      963.6613840000002,
      1060.0275224000002,
      954.0275224000002,
      1049.43027464,
      945.4302746400001,
      1039.9733021040001,
      936.9733021040001,
      1030.6706323144,
      927.6706323144001,
      1020.4376955458401,
      918.4376955458401,
      1010.2814651004242,
      909.2814651004242,
      1000.2096116104666])




```python

```
