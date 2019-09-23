## Object-Oriented Programming (OOP) with Classes

### Background/Motivation

From [wikipedia](https://en.wikipedia.org/wiki/Object-oriented_programming): Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which are data structures that contain data, in the form of fields, often known as attributes; and code, in the form of procedures, often known as methods.

How does it relate to Python? It turns out that everything in Python is an object. Everything in Python stores data, and has methods that operate on that data. Strings are a perfect example of this. When we have a string, it stores the individual characters that make up the string (these are the data, or **attributes**), and we have **methods** (`lower()`, `upper()`, `replace()`, etc.) that operate on that data.

With knowledge of what an object is, let's discuss how they are related to **classes**. It turns out that a **class** is simply a blueprint that describes the format of an object. It tells us what data an object will store, and what methods that object will have available.  By building different classes (i.e. blueprints), we can create different objects (and then they can interact with each other, which we'll get to). Why use classes, though?

We use classes for much the same reasons that we use functions - *reusability* and *abstraction* (there are actually some additional design principles behind OOP that we'll go into shortly). Classes allow us to build reusable objects while at the same time abstracting away the inner workings of those objects. This way, users of our classes can build objects and then interact with them without really caring how any of it is working under the hood. For example, when we interact with strings using the `replace()` method, we don't have to think about that `replace()` method works; we just have to know that it will work.

### Design Principles

The motivation for object-oriented programming (OOP) is actually heavily rooted in design principles, namely the principles of *inheritance*, *encapsulation*, and *polymorphism*. This terminology is more of an advanced topic in computer programming, and we'll only cover it briefly here (while it is advanced, any treatment of OOP should at least mention these, which is why we do here).

* **Inheritance** - When a class is based on another class, building off of the existing class to take advantage of existing behavior, while having additional specific behavior of its own.
* **Encapsulation** - The practice of hiding the inner workings of our class, and only exposing what is necessary to the outside world. This idea is effectively the same as the idea of **abstraction**, and allows users of our classes to only care about the what (i.e. what our class can do) and not the how (i.e. how our class does what it does).
* **Polymorphism** - The provision of a single interface to entities of different types. This enables us to use a shared interface for similar classes while at the same time still allowing each class to have its own specialized behavior.

While OOP does enjoy the benefits of the above design principles, it also kind of matches how we think about the world. The world is composed of objects, where objects can be people, houses, cars, buildings, etc. These objects have some properties about them (i.e. they contain data), and they can do things (i.e. they have methods that can be applied). Object oriented programming approaches a programming problem by using objects that interact with each other, much like they do in the real world.

### Terminology

Before we get to actually learning how to build a class, it'll be helpful to define some of the terminology surrounding classes/OOP. Often times, the terminology can be the most confusing part of learning OOP.

1. **Class** - Used to refer to the abstract concept of an object.
2. **Object** - An actual instance of a class.
3. **Instance** - What Python returns when you tell it to create a class.
4. **Instantiation** - A fancy way of saying that we're going to create an instance of a class.
5. **Constructor** - What we call to instantiate a class.
6. **self** - Inside of a class, a variable for the instance/object being accessed (i.e. it holds a reference to the instance/object of that class).
7. **attribute**/**field**/**property** - A piece of data that a class has, stored in a variable. Inside of a class definition, all attributes/fields/properties are accessed via `self.<attribute>`, while on an instance, they are accessed via `<variable name>.<attribute>`.
8. **method**/**procedure** - A block of code that is accessible via the class, and typically acts on or with the classes' attributes/fields/properties. Inside of a class definition, all methods/procedures are created via `def` (they are really just functions), and accessible via `self.<method>()`, while on an instance, they are accessed via `<variable name>.<method>()`.

Don't worry if this terminology isn't 100% clear at this point in time. It should become more clear as we work through these notes, and should be a useful reference. From here on out, we'll treat attribute, field, and property as interchangeable, and we'll do the same with method and procedure.

### Defining A Class

Much like defining a function, there is a common syntax when defining a class. It is almost exactly the same as defining a function, but we replace `def` with `class`. That is, we write `class`, then the name of the class that we are defining, followed by a set of parentheses, and finally a colon. After the colon is an indented block of code that we use to define the class attributes and methods. One subtle difference is that with functions, the standard is to name these beginning in lowercase and separating words with underscores (i.e. *snake_case*); with classes, the standard is to name these capitalized, and not separate words at all (i.e. *CamelCase*). For example...

```python
class OurClass():
    # attributes and methods go in here.
```

**Note**: As we'll show below, `OurClass()` is exactly what we'd used to create an instance of this class, and is the **constructor** for this class.

#### Instantiation

Like we mentioned above, **instantiation** is just a fancy word for saying that we're going to create an instance of a particular class. We do this by calling the **constructor** for our class, which is the name that we give our class right after the `class` statement in its definition. Using this **constructor**, we create an instance of our class, and store that instance in a variable.

```python
our_class = OurClass()
```

Okay, cool! Let's revisit some of the terminology that we discussed above. We've shown you how to define a class, and **instantiate** it using a **constructor**. What we've done directly above is created an **instance** of `OurClass` that we've stored in the `our_class` variable. This variable is an object that theoretically has **attributes** and **methods**, which we can use to interact with it (we say theoretically because we didn't actually define any attributes or methods above). Now let's look at how to actually build a class that does something.   

#### Inner Workings (defining attributes and methods)

As review, remember that inside of a class, we can have both attributes and methods. We can then think of these attributes and methods as belonging to the class, and they become accessible via any instances of the class (through dot notation, which we'll get to in a second). Inside of the class, all of these attributes and methods are set and retrieved via `self`. Let's dive in...

##### The `__init__()`

Almost every class you ever write will have an `__init__()` method. This method gets called every time that you create a new instance of a class, and handles any kind of setup that the class may require. Setup typically just involves assigning values to attributes, which we can do with or without values passed in (similar to how we interact with functions). Let's look at defining a class and instantiating a class in both of these cases.

```python
In [1]: class OurClass():
   ...:     
   ...:     def __init__(self):
   ...:         self.name = 'Intro Python'

In [2]: our_class = OurClass()

In [3]: our_class.name
Out[3]: 'Intro Python'
```

How does the `__init__()` method work? As mentioned above, it is called by default whenever we instantiate an instance of `OurClass()` (or whatever class it is a part of). In addition, any arguments that we pass to the `OurClass()` constructor that we use during instantiation are passed to the `__init__()` method. But wait... In the `__init__()` method definition you have it accepting the `self` parameter, but don't pass any arguments during instantiation? The reason for this is that by default, Python passes a reference to the instance (which is what `self` is) as the first argument in any method that is defined within the class. Let's dive into this a little deeper...   

`self` is what we use inside of the class to access attributes or methods of the class. Notice that we do this with dot notation - e.g. by placing a period after `self`, and then the name of the attribute or method that we want to access. When we write `self.name = 'Intro Python'`, then, what we are doing is accessing `self.name` and then assigning it the value of 'Intro Python'. Outside of the class, we access this attribute (or any attribute/method) again via dot notation, but replacing `self` with the variable name that holds a reference our instantiated object (above this is `our_class`).

Let's now take a look at what it looks like to pass arguments into the `__init__()` method.

```python
In [1]: class OurClass():
   ...:
   ...:     def __init__(self, name):
   ...:         self.name = name

In [2]: our_python_class = OurClass('Intro Python')

In [3]: our_ds_class = OurClass('Data Science')

In [4]: our_python_class.name
Out[4]: 'Intro Python'

In [5]: our_ds_class.name
Out[5]: 'Data Science'

In [6]: our_last_class = OurClass()
______________________________________________________________
TypeError                    Traceback (most recent call last)
<ipython-input-6-aa0dd92460> in <module>()
    > 1 our_last_class = OurClass()

TypeError: __init__() takes exactly 2 arguments (1 given)
```

So, what's happening here? In our `__init__()` method, we have included another parameter in addition to `self`. In doing so, when we instantiate our class, the constructor expects an argument (in addition to `self`, which is automatically passed by default). It then takes that expected argument and assigns it to the `name` attribute. Then, we access that `name` attribute via dot notation, prefaced with  `self` inside of the class and the variable name of your object outside of the class.

What happened in that last example, though? Here, we tried to instantiate the class without an argument and got an error. This is because we didn't pass in an argument for the `name` parameter. Methods within classes work exactly like functions (in fact they are functions, we just call them methods since they are inside classes). As a result, we have to pass the expected number of arguments in when we call them (with the caveat that `self` is passed by default, and that `__init__()` is called by default when a class is instantiated).

Let's look at one last example to hammer home the `__init__()` method. Remember that it's just like a function (a kind of special function). This means that we can pass it multiple arguments, and even give parameters default values.

```python
In [1]: class OurClass():
   ...:     
   ...:     def __init__(self, name, location, size=0):
   ...:         self.name = name
   ...:         self.location = location
   ...:         self.size = size

In [2]: our_python_class = OurClass('Intro Python', 'Platte')

In [3]: our_ds_class = OurClass('Data Science', 'Platte', 15)

In [4]: our_python_class.name, our_python_class.location, our_python_class.size
Out[4]: ('Intro Python', 'Platte', 0)

In [5]: our_ds_class.name, our_ds_class.location, our_ds_class.size
Out[5]: ('Data Science', 'Platte', 15)
```

Here, we see the use of multiple parameters in the definition of the `__init__()` method, along with the use of default values for one of those parameters. When we look at the instantiation of the two `OurClass()` objects, we see the realization of these multiple parameters and default values.

As a brief aside before diving into defining other methods inside our functions, the `__init__()` method is a special type of method that we refer to as a **magic method**. We'll go into these in depth in the next class, but for now it's important to note that all **magic methods** begin and end with double underscores (like `__init__()`).  

##### Defining other methods

Defining other methods is going to work exactly like defining the `__init__()` method (except we won't begin or end their names with double underscores, **unless** they are magic methods, which we'll get to). The only difference is in how we access those methods from outside of our object. Whereas the `__init__()` method is called by default when we instantiate an object, we are going to have to explicitly call other methods (that aren't **magic methods**) after the instantiation of the object. Again, we'll call those other methods via dot notation. Let's take a look at defining another method within `OurClass()`.

```python
In [1]: class OurClass():
   ...:     
   ...:     def __init__(self, name, location, size=0):
   ...:         self.name = name
   ...:         self.location = location
   ...:         self.size = size
   ...:         self.questions_asked = []
   ...:
   ...:     def add_question_asked(self, question):
   ...:         self.questions_asked.append(question)

In [1]: our_class = OurClass('Intro Python', 'Platte', 15)

In [2]: our_class.name, our_class.location, our_class.size
Out[2]: ('Intro Python', 'Platte', 15)

In [3]: our_class.questions_asked
Out[3]: []

In [4]: our_class.add_question_asked('Why Python?')

In [5]: our_class.questions_asked
Out[5]: ['Why Python?']

In [6]: our_class.add_question_asked('Why not R?')

In [7]: our_class.questions_asked
Out[7]: ['Why Python?', 'Why not R?']
```

Here, we have now defined another method within our class, `add_question_asked()`. Notice that we call this method *after* we have instantiated an instance of `OurClass()` (stored in the variable `our_class`), and we use dot notation to access it. This `add_question_asked()` method takes in a string (or really anything) and appends it to the object's `questions_asked` attribute. But, how does it know where to find the `questions_asked` attribute if it isn't passed into the `add_question_asked` method? This comes back to the beauty of the `self` reference that is *automatically* passed as the first argument in any method call on an object. That `self` reference holds access to *any* of the object's attributes, no matter where they were defined (in the `__init__()`, in another method, etc.). *As long as* that attribute was assigned via dot notation using `self`, then it will be accessible via `self` in any method of the class.

Note, too, that any method within the class can alter the attributes that are accessible via `self`. Above, we used the `add_question_asked` method to alter the `questions_asked` attribute. However, if we use a variable within a method and don't assign it as a class attribute, then it won't be accessible in other methods of the class (this is because it will be enclosed in the scope of that method only). Let's hammer this home with another example.

```python
In [1]: class OurClass():
   ...:     
   ...:     def __init__(self, name, location, size=0):
   ...:         self.name = name
   ...:         self.location = location
   ...:         self.size = size
   ...:         self.questions_asked = []
   ...:
   ...:     def add_question_asked(self, question):
   ...:         self.questions_asked.append(question)
   ...:     
   ...:     def add_class_members(self, num):
   ...:         self.size += num
   ...:
   ...:         if self.size >= 20:
   ...:             print('Capacity Reached!!')
   ...:             at_capacity = True
   ...:
   ...:     def check_if_at_capacity(self):
   ...:         return self.at_capacity

In [2]: our_class = OurClass('Intro Python', 'Platte', 15)

In [3]: our_class.add_question_asked("What's he going to show?")

In [4]: our_class.add_question_asked('Do you know the answer?')

In [5]: our_class.questions_asked
Out[5]: ["What's he going to show?", 'Do you know the answer?']

In [6]: our_class.add_class_members(3)

In [7]: our_class.size
Out[7]: 18

In [8]: our_class.add_class_members(5)
Capacity Reached!!

In [9]: our_class.size
Out[9]: 23

In [10]: our_class.check_if_at_capacity()
______________________________________________________________________
NameError                           Traceback (most recent call last)
<ipython-input-21-bd556e9468f1> in <module>()
    > 1 our_class.check_if_at_capacity()

<ipython-input-9-f631bd9392f0> in check_if_at_capacity(self)
      13             at_capacity = True
      14     def check_if_at_capacity(self):
    > 15         return at_capacity == True
      16

AttributeError: OurClass instance has no attribute 'at_capacity'
```

Let's highlight a couple of things in our last example here. The main point of this example is to show that any method can access any attribute of the class **that is assigned via `self`**. We see this in two of our methods above - `add_question_asked()` is able to access the `questions_asked` attribute (just as before), and `add_class_members()` is able to access `size`. Both of these attributes are accessed via `self`. When we get to `check_if_at_capacity()`, though, it tries to access `at_capacity`, which was never made an attribute (assigned via `self`), and hence not available via `self`. The way this code is written, `at_capacity` is only ever set and accessible within the `add_class_members()` method itself. Let's fix this by assigning it via `self` and seeing what that does.

```python
In [1]: class OurClass():
   ...:     
   ...:     def __init__(self, name, location, size=0):
   ...:         self.name = name
   ...:         self.location = location
   ...:         self.size = size
   ...:         self.questions_asked = []
   ...:
   ...:     def add_question_asked(self, question):
   ...:         self.questions_asked.append(question)
   ...:     
   ...:     def add_class_members(self, num):
   ...:         self.size += num
   ...:
   ...:         if self.size >= 20:
   ...:             print('Capacity Reached!!')
   ...:             self.at_capacity = True
   ...:
   ...:     def check_if_at_capacity(self):
   ...:         return self.at_capacity

In [2]: our_class = OurClass('Intro Python', 'Platte', 15)

In [3]: our_class.add_class_members(5)
Capacity Reached!!

In [4]: our_class.at_capacity
Out[4]: True

In [5]: our_class.check_if_at_capacity()
Out[5]: True
```

Here we can see that not only can we create attributes in the `__init__()` method, but in other methods as well. Before our line `our_class.add_class_members(5)` was called, there was no `at_capacity` attribute on `our_class` object. After, however, there was! This is because it got created in the `if` block within the `add_class_members()` method. Furthermore, because we assigned it via `self`, it was accessible in the `check_if_at_capacity()` method when we called it.

In our above example, we showed how we could create attributes in methods other than the `__init__()` method. However, this is in general not considered to be good practice. To see why, imagine what would have happened if we called the `check_if_at_capacity` method before `self.at_capacity` was set? It would have thrown an error! Typically, we want to at least define all of the attributes that might ever be accessed on our object in the `__init__()` method. We can give that attribute a default value, or we can simply assign `None` to it. This is actually what we should have done with the `at_capacity` attribute above. Let's see what this looks like:

```python
In [1]: class OurClass():
   ...:     
   ...:     def __init__(self, name, location, size=0):
   ...:         self.name = name
   ...:         self.location = location
   ...:         self.size = size
   ...:         self.questions_asked = []
   ...:         if self.size >= 20:
   ...:             self.at_capacity = True
   ...:         else:
   ...:             self.at_capacity = False
   ...:
   ...:     def add_question_asked(self, question):
   ...:         self.questions_asked.append(question)
   ...:     
   ...:     def add_class_members(self, num):
   ...:         self.size += num
   ...:
   ...:         if self.size >= 20:
   ...:             print('Capacity Reached!!')
   ...:             self.at_capacity = True
   ...:
   ...:     def check_if_at_capacity(self):
   ...:         return self.at_capacity

In [2]: our_class = OurClass('Intro Python', 'Platte', 15)

In [3]: our_class.add_question_asked("What's he going to show?")

In [4]: our_class.add_question_asked('Do you know the answer?')

In [5]: our_class.questions_asked
Out[5]: ["What's he going to show?", 'Do you know the answer?']

In [6]: our_class.add_class_members(3)

In [7]: our_class.size
Out[7]: 18

In [8]: our_class.add_class_members(5)
Capacity Reached!!

In [9]: our_class.size
Out[9]: 23

In [10]: our_class.check_if_at_capacity()
Out[10]: True
```

Now, we won't get any errors no matter when we try to access `self.at_capacity`.

As a final note, you can also perform tab completion on your own objects. If we were to tab complete the last instance of `OurClass()` from directly above, we would have seen this:

```python
In [6]: our_class.
our_class.add_class_memebers    our_class.location
our_class.add_question_asked    our_class.name
our_class.at_capacity           our_class.questions_asked
our_class.check_if_at_capacity  our_class.size
```
