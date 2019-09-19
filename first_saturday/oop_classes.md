# Day 7 Lecture Notes

<br><br><br><br><br><br>
# Functions, OOP and Classes


<br><br><br><br>
## Writing Better Functions
* Add flexibility with `*args` and `**kwargs`
* function atomicity

<br><br><br><br>
## `*args` and `**kwargs`
* used to pass in arbitrary lengthed multiple values
* often seen when writing command line scripts that process files, since these allow passing arguments into the script

<br><br>
### `*args` is essentially a `list` that can contain in-order data to be used by the function
* `*args` is the convention, but can be `*anything`
```python
def human_attribs(age, haircolor, favorite_bird):
    print(age, haircolor, favorite_bird)

human_attribs(123, 'ghostly white', 'dead bird')

# with *args
def human_attribs_flex(name, *args):
    print(name)
    [print(item) for item in args]

human_attribs_flex('Johanne', 123, 'ghostly white', 'dead bird', 'buick', 'hangglide', 31)
```

<br><br>
### `*kwargs` is essentially a `dict` that can contain named parameters to be used by the function
```python
def human_attribs_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}')

human_attribs_kwargs(name='Floyd', age='132', hair_color='ghostly gray', favorite_animal='cat skeleton')
```


<br><br><br><br>
## Function Atomicity
* a function should have a single, simple job
* a function should be reusable

<br><br>
### write `is_prime_and_divides_n()`
* although we could write this as one function, it is generally better to write helper functions.
```python
def is_prime(k):
    for i in range(2,k):
        if k % i == 0:
            return False
    return True

# atomic
def is_divisible(k,n):
    if n % k == 0:
        return True
    else:
        return False

# abstraction from atomic functions
def is_prime_and_divides_n(k, n):
    if is_prime(k) and is_divisible(k,n):
        return True
    else:
        return False
```
    
<br><br><br><br><br><br>
# Classes

<br><br>
## Basics
* Everything in Python is an object, defined by a template known as a 'class'
    * objects have **attributes**
    * objects have **methods**
* Capitalized CamelCase is the naming convention for classes:
    * ex: `class CamelCase: ...`

<br><br>
## Why Classes?
* Better organization and representation of ideas
* Classes translate easily to database table schemas

<br><br>
## Constructing an Object
* `__init__` : we overwrite this dunder method in order to set initial attributes when we **construct** 
    * [dunder ("double underscore" or magic) methods](https://docs.python.org/3/reference/datamodel.html#special-method-names) are default methods for Python classes. We often overwrite these in order to change the behavior of our objects
* Construct an object using this syntax:
    * `some_obj_1 = SomeClass('attrib 1', 'attrib 2')`

<br><br>
### Write the `Bike` class
```python
class Bike:
    
    def __init__(self, make, model): # constructor
        self.make = make
        self.model = model

    def __repr__(self): # add print-ability to the object
        representation = representation = f'make: {self.make}\nmodel: {self.model}'
        return representation

    def brag(self, someone='random stranger'):
        print('I have a {} {} {}!'.format(self.make, self.model, someone))
        return ''

    def bike_to(self, destination='home'):
        print('I am biking toward {} at 1000 mph!'.format(destination))
```

<br><br>
### **Instantiate** the `Bike` class
```python
bike1 = Bike('Peugeot', 'Montreal Express')
bike3 = Bike('Huffy', 'something')
bike2 = Bike('Cannondale', 'm894828')
print(bike1)
```

<br><br>
### invoking a `Bike` class method
```python
bike1.brag()
bike2.brag('Mom')
bike3.brag('my bike nerd friend who will be impressed')
```

<br><br>
### Write and use the `RecurringCustomer` class
```python
class RecurringCustomer:
    
    def __init__(self, cust_id, name):
        self.cust_id = cust_id
        self.name = name
        self.purchase_hist = dict()

    def get_purchase_history(self):
        for k,v in self.purchase_hist.items():
            print(f'{k} : {v}')

    def add_purchase(self, date, item):
        self.purchase_hist[date] = item

cust1 = RecurringCustomer('00000000', 'David Jones')

cust1.get_purchase_history()
cust1.add_purchase('2019-07-17', 'wool socks')
cust1.get_purchase_history()
```