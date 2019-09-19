## More On Python Classes

### Intro

Last class we learned about the programming paradigm known as OOP, and we got some practice writing simple classes in Python. Today, we are going to build on that knowledge and discuss a number of important things regarding classes and their use:

* Python classes magic methods.
* How to analyze when to use classes.
* How everything in Python is actually an object (instantiated class)!

### Magic Methods

There are a number of things that we have been taking for granted in our use of Python so far. Let's dive into an example of where we were using some functionality built into Python, but didn't think too much about how it was working.

```python
In [1]: my_list = [1, 2, 3]

In [2]: my_dict = {1: 'first', 2: 'second'}

In [3]: len(my_list)
Out[3]: 3

In [4]: len(my_dict)
Out[4]: 2
```

Here, we are using the `len()` function (a Python built-in), passing it a list and then a dictionary. This might seem fairly natural now, but if you take a moment to think about how this works, you may run into some logical stops. One question that might come to mind is how we are able to pass two different data structures to `len()`, and have that `len()` function know what we're asking? Furthermore, how does it reason about how "long" these different data structures are? Given our knowledge of how functions work, how does this `len()` function do what it does above?

What's happening under the hood when we pass a data structure to the `len()` function is that Python is going to that object and running its `__len__()` method. Ok, that sounds cool, but what does it all mean? This is an example of a **magic method**, and we will dive into them shortly. For now, know that magic methods allow us to give more robust functionality to our classes in terms of how they interact with Python. So, just as the `__len__()` method was called when both a list and a dictionary were passed to the `len()` function, we can define a `__len__()` method on our custom classes. Then, Python will know what to do when you pass an instance of that class to the `len()` method (the exact implementation of how that `__len__()` works is entirely up to you!)

#### Polymorphism Detour

The above example is a great example of **polymorphism**, an idea we quickly discussed last class. Let's take a moment to get a better handle on this idea. **Polymorphism** is defined as the provision of the same interface for entities of different types.

We see that idea in direct action in the above example. Though we were passing different types of entities to the `len()` function, because it implements the `__len__()` method on whatever object was passed to it, and any object can implement that method, we see this notion of the same interface. And, even further, we see the benefits of setting up a paradigm with this design principle implemented. To make something work with `len()`, all you have to do is make sure it implements the `__len__()` method. And, tada! The general structure of the interface, polymorphism in action, takes care of the rest.

Speaking of which. How do we define these "magic" methods?? End detour.

#### Defining a Magic Method

Defining a magic method is as easy as defining any other method in a class. We actually did it last time with the `__init__()` method. So, all you have to do is start with a `def`, and then the name of the magic method with the double underscores. **Note**: All methods with names beginning and ending with double underscores are magic methods, and this naming convention is reserved for them.

Let's take a look at this with the `OurClass` class we created last time. I'm going to add a `__len__()` implementation to the code from last lecture. Considering that the `len()` function should return a number, it seems reasonable to have it return the number of questions asked. Instead of putting our code directly into IPython, this time we're going to store it in a script, `lecture_code.py` (it will be located in the `misc` folder), and get some practice importing. Let's take a look.

```python
class OurClass():
    def __init__(self, name, location, size=0):
        self.name = name
        self.location = location
        self.size = size
        self.questions_asked = []
        if self.size >= 20:
            self.at_capacity = True
        else:
            self.at_capacity = False

    def __len__(self):
        return len(self.questions_asked)

    def add_question_asked(self, question):
        self.questions_asked.append(question)

    def add_class_members(self, num):
        self.size += num

        if self.size >= 20:
            print('Capacity Reached!!')
            self.at_capacity = True

    def check_if_at_capacity(self):
        return self.at_capacity
```

Now we can have `len()` interact with instances of `OurClass`.

```python
In [1]: from lecture_code import OurClass

In [2]: our_class = OurClass('Intro Python', 'Platte', 15)

In [3]: len(our_class)
Out[3]: 0

In [4]: our_class.add_question_asked("What's he going to show?")

In [5]: our_class.add_question_asked('Do you know the answer?')

In [6]: len(our_class)
Out[6]: 2
```

Just as we'd expect, we get the number of questions when calling `len()`. For reference, check out what would happen if we hadn't defined an implementation for `__len__()`.

```python
In [1]: from lecture_code import OurClass

In [2]: our_class = OurClass('Intro Python', 'Platte', 15)

In [3]: len(our_class)
___________________________________________________________________________
TypeError                                 Traceback (most recent call last)
<ipython-input-3-ae0663a04767> in <module>()
    > 1 len(our_class)

TypeError: object of type 'OurClass' has no len()
```

An error! At least Python lets us know that it's related to having no length, a problem that we now know how to fix!

#### Other Magic Methods

It turns out that there are many other magic methods that we can implement on our custom classes. In fact, we've already seen one! The `__init__()` method is a magic method - this is why it is called when the class is constructed and always performs class setup.

Most of the magic methods allow for you to make your classes interact with already existing features in Python. This process is called operator overloading, and implementing magic methods on our classes is how we do it.

For example, let's take a look at what happens if we try printing one of our own custom classes? If we try with an instance of the `OurClass` class, we get something like: `<__main__.OurClass instance at 0x10a157a28>`. This isn't very informative. How do we get a more useful printout of our classes, then? We can use the `__str__()` method! This is the method that is called when you try to cast an object as a string with the `str()` constructor. Non-coincidentally, objects are cast as strings by Python when you call `print()`, as Python only knows how to represent strings on the screen. Let's take a look at what a `__str__()` method could look like. Then, we can use it to print an instance of `OurClass` and get something useful.

```python
class OurClass():
    def __init__(self, name, location, size=0):
        self.name = name
        self.location = location
        self.size = size
        self.questions_asked = []
        if self.size >= 20:
            self.at_capacity = True
        else:
            self.at_capacity = False

    def __str__(self):
        our_class_string = '{}, location: {}'
        return our_class_string.format(self.name, self.location)

    def add_question_asked(self, question):
        self.questions_asked.append(question)

    def add_class_members(self, num):
        self.size += num

        if self.size >= 20:
            print('Capacity Reached!!')
            self.at_capacity = True

    def check_if_at_capacity(self):
        return self.at_capacity
```

Note, the return type from the `__str__()` method must be a string when we implement our own. Now, when we try to print an instance of `OurClass` we actually get something useful.

```python
In [1]: from lecture_code import OurClass

In [2]: our_class = OurClass('Intro Python', 'Platte', 15)

In [3]: print(our_class)
Out[3]: Intro Python, location: Platte
```

#### Magic Methods for the Win

If we can decide if two numbers, or strings, etc. are equal with the equality operator, `==`, why can't we make a custom class do the same? Turns out we can! With the magic `__eq__()` method, we can enable two instances of our class to be compared.

How would our class know that it's getting compared to another object to check equality? If you take a look at the specification for how python will use the magic `__eq__()` method [here](https://docs.python.org/2/reference/datamodel.html#object.__eq__), it specifies that the arguments to be passed look like: `object.__eq__(self, other)`. We already know that `self` is a reference to the instance that the method is being called on. It turns out that `other` is a reference to an instance as well.

The way that Python evaluates an expression like `x == y` is that it calls the `__eq__()` method on the first argument to the expression (`x`) and passes a reference to that variable as the first argument to the `__eq__()` method. Then, it looks on the other side of the `==` and passes a reference to that variable as the second argument to `__eq__()` (here it's `y`). So, the `other` argument that we see above is just a reference to another instance! Since it's a reference to another instance, we can access attributes and methods of that instance via the name `other`!

For example, we might consider two instances of `OurClass` equal if they have the same name and location. The way that we would have our class implement this behavior is by overloading the `==` via implementing the `__eq__()` method. Let's take a look...

```python
class OurClass():
    def __init__(self, name, location, size=0):
        self.name = name
        self.location = location
        self.size = size
        self.questions_asked = []
        if self.size >= 20:
            self.at_capacity = True
        else:
            self.at_capacity = False

    def __eq__(self, other):
        return self.name == other.name and self.location == other.location

    def add_question_asked(self, question):
        self.questions_asked.append(question)

    def add_class_members(self, num):
        self.size += num

        if self.size >= 20:
            print('Capacity Reached!!')
            self.at_capacity = True

    def check_if_at_capacity(self):
        return self.at_capacity
```

Notice that we easily have access to information about the other instance through dot notation. Also, as we would expect that the `==` operator return a boolean, we should take special care to make sure that we return things from our magic methods that make sense within the context!

#### Tons of Magic Methods

For the most part, any of the seemingly simple functionality that is built into Python data structures can be implemented via a magic method in our custom classes. Take a look at [this](https://docs.python.org/2/reference/datamodel.html#special-method-names) link to get a sense for all the things magic methods can do.

### Using Classes Pragmatically

One question that comes up frequently in languages like Python that don't fall into a single [paradigm](https://en.wikipedia.org/wiki/Programming_paradigm) (such as functional or OOP) is learning when to use the different features of the language. As applied to our current circumstance, when should we be making classes instead of just using functions?

Part of the confusion in answering this question frequently stems from an incomplete understanding of OOP's purpose in life - to take advantage of inheritance, encapsulation, and polymorphism. With this in mind, let's discuss classes at a high level, and see what kinds of problems lend themselves to being solved with functions (e.g. procedurally) vs. with OOP.

Similar to one of the motivations for functions, **abstraction**, we see the idea of **encapsulation** espoused by OOP. Encapsulation is very much like abstraction in that it hides implementation details; however, with it we see the distinction that many functions can be bundled up together in a class. In addition, we also see another aspect of abstraction introduced - abstraction of the data itself. While we can instantiate a class with whatever properties we dictate, often these will specify the nature of the data (though sometimes it wont). We then have our bundled methods that act on the data,  and these methods are designed to keep us from caring about the exact state of that data. Sometimes this can be good, and sometimes not so much.

Consider this example - you have a dictionary with keys as country names, and values as a list of all historical presidents for that country. You want to have the ability to see what presidents names start with a given letter. You could easily write a function for this. Maybe it looks like the following:

```python
def presidents_by_letter(country_pres_dict, letter):
    letter_pres = []
    for pres_list in country_pres_dict.values():
        for pres in pres_list:
            if pres[0].lower() == letter:
                letter_pres.append(pres)
    return letter_pres
```

This seems pretty reasonable. However, we could also make a class for this task. It would contain the dictionary of countries and presidents as an attribute, and have a method that does the same thing as `presidents_by_letter()` above. Maybe it looks like the following:

```python
class CountriesPresidents():
    def __init__(self, country_pres_dict):
        self.country_pres_dict = country_pres_dict

    def presidents_by_letter(self, letter):
        letter_pres = []
        for pres_list in self.country_pres_dict.values():
            for pres in pres_list:
                if pres[0].lower() == letter:
                    letter_pres.append(pres)
        return letter_pres
```

So. Which is better - the function or the class??

#### Function or Class?

In the case outlined above, there is a pretty strong case for not going with the more heavy-weight option of a class, and instead sticking with a simple function. Is there a rule, then, that governs when you should use one over the other? Yes and no. Let's discuss how we make the decision of whether or not to use a class.

Generally, we think of use cases for classes as ones that align with the principles of OOP - **inheritance**, **encapsulation**, and **polymorphism**. If we think that we are in a situation where encapsulation (having multiple layers of abstraction between the user and their data) makes sense, then using classes makes a decent amount of sense. If there is also an opportunity to take advantage of providing a polymorphic interface, then you definitely should think about taking advantage of the OOP features in Python.

This probably all seems a little hand wavy, but hopefully the method of reasoning seems quite sound. In addition, we have access to another amazing tool to make our decision process easier - **refactoring**. **Refactoring** is the process of restructuring your code without changing it's behavior. When we took advantage of function abstraction in the other lecture and changed the internals of `update_counts()`, we were actually refactoring.

Refactoring can also be a more overhauling process, where you change the entire structure of your programs. To illustrate this, lets look at a problem that extends the `create_report()` project that we built when we were learning how to make functions work together. Along the way, we will discuss why the problem should be solved with functions, and then talk about when an extension/refactor to a class would be appropriate.

### Python's Multi-paradigmatic Toolbox For the Win

Let's start this [gedankenexperiment](https://en.wikipedia.org/wiki/Thought_experiment) with a reminder about the `create_report()` project. We had our "boss" come to us and ask for a program that takes the path for a text file, and returns the number of sentences, words, and characters in that file. Below is the code that we came up with for this project.

```python
def update_counts(line, counts_dict):
    for char in line:
        counts_dict['characters'] += 1
        if char == '.':
            counts_dict['sentences'] += 1
        elif char == ' ':
            counts_dict['words'] += 1
    counts_dict['words'] += 1


def create_report(file_path):
    counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
    with open(file_path) as txt_file:
        for line in txt_file:
            update_counts(line, counts_dict)
    return counts_dict
```

We went through a couple of iterations of this project, improving on this code to get it to where it is above. As a result, our boss seemed pleased with the result. Now, he's back. He wants more functionality built into our solution. This time, he asks us to expand our program so that we can easily create reports as it did before, but also do a couple of other things. He also wants our solution to keep an aggregated count of the sentences, words, and characters over all the reports produced. In addition, he wants a library of words from all the documents. Lastly, he wants us to make it easy to get the size of this vocabulary.

Alright! Well, that's certainly a bit more functionality. How are we going to solve this? Simple answer - one step at a time. Ok, that's wasn't particularly specific... what's the first step, then?? As before, we are going to embrace an iterative approach to developing functionality. Our first task, then, will be to build a function that will produce a bunch of reports.

If we want to do the same thing repeatedly while programming, what tool do we use? A loop! Ok, that's awesome. We already have an idea of how we're going to approach this problem, but what are we going to loop over? An obvious answer is a list of file paths. Let's take a look at some [pseudocode](https://en.wikipedia.org/wiki/Pseudocode) that implements a loop like this.

```python
def create_reports(file_paths):
    for file_path in file_paths:
        create_report(file_path)
```

This skeleton makes some sense, since for each file path we want to create a report. However, our current code for `create_report()` returns a dictionary of counts. What are we going to do with these counts? How are we going to collect all the counts together so that we can keep a master count? Further, how are we going to create a library of words contained in all the documents??

These are great questions, and to answer them we need to think hard about the structure of our program. If we want to aggregate all of the counts together, we could have a separate dictionary devoted to that task. Then, we would have to ask ourselves where that dictionary should be created, and where the updates to it should be made?

Questions like this one go a long way in terms of directing decisions on how to structure your programs. One thing to think about when you're answering these questions are that functions should be reusable. This means that a function that creates and returns data structures within it's scope is potentially less general than if it accepts an existing data structure as a parameter. However, another thing to consider is that passing around objects might be unnecessary, since they could just be stored as attributes in a class. Then, the functions that operate on those objects could simply be methods on that class. All of this reads: can you encapsulate the solution to your problem, and do you want to? This brings up an important point - Python allows you to implement both functions and classes, which means that you can choose the one that suits your needs! What's important is that you're aware of both and are consciously weighing the costs and benefits of each when you're writing your programs. Often times, the boundary between choosing one over the other can be a little fuzzy, and so as long as you're actually thinking critically about it, that's a good sign!

How do we apply all of this to our current problem? Well, we know that we're going to want to have some sort of object storing all of our counts and our vocabulary. This is starting to sound like maybe we should create a class. Keep in mind that this decision, to make the jump to class usage, can happen at any time during your process, and you can always go back! (**Note**: Frequently you'll want to try out a change, be it a large change that requires a huge refactor or a small change that requires a tiny implementation change, but not want it to affect all of your current work. This happens so frequently that there is some amazing functionality to solve this exact problem built into your version control system, `git`. It involves the use of **branches**. [Here](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) is a great intro to branching and merging from the git docs if you want to learn about this amazing feature.)

Let's make the jump to classes, then!

#### Functions to Classes

When you're thinking about refactoring your function based code to classes, you frequently have an idea what the methods are going to do and have already written some functions. The next thing to think about is what the class' attributes will look like. For us it's not too bad - we know that we're going to need a dictionary to hold our master counts and a place to store our vocabulary. In this case, a set makes the most sense, since we don't want repeats of words. If instead we wanted to keep track of all the documents a word was found in, we could do that with a dictionary. Let's start setting up the structure of our class, starting with the inclusion of the `create_reports()` function we started with earlier.

```python
class ReportCreator():
    def __init__(self):
        self.vocabulary = set()
        self.master_counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}

    def create_reports(self, file_paths):
        for file_path in file_paths:
            pass
```

Nice and easy. Now we want to transition our functions to methods so that they will be accessible within the class. Remember that we need to pass `self` as the first parameter to methods.

```python
class ReportCreator():
    def __init__(self):
        self.vocabulary = set()
        self.master_counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}

    def create_reports(self, file_paths):
        for file_path in file_paths:
            pass

    def create_report(self, file_path):
        counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
        with open(file_path) as txt_file:
            for line in txt_file:
                self._update_counts(line, counts_dict)
        return counts_dict

    def _update_counts(self, line, count_dict):
        for char in line:
            counts_dict['characters'] += 1
            if char == '.':
                counts_dict['sentences'] += 1
            elif char == ' ':
                counts_dict['words'] += 1
        counts_dict['words'] += 1
```

Now, we've got access to the functionality we had in our old functions, but as methods within the class. Let's talk about two things real quickly. First off, you might have noticed that `update_counts()` was changed to `_update_counts()`. The leading underscore is a signal to users of our class that this particular method is for use internal only, similar to the double underscores we see with the magic methods (**Note**: The single underscore can also be used with attributes, and it means the same thing). It also makes the method hidden when tab completing on instances of this class, unless you start with an underscore (e.g. In IPython type `<instance of ReportCreator>._<tab>`). It makes sense to make this a hidden method, because realistically a user of this class will never need to explicitly use this method. Second, you might also notice that we'll have to change what happens in the `_update_counts()` method in order to keep track of all the words our class has seen.

#### Making Our Class Work with Itself

That second part forces us to rethink how we will loop over each line. Currently, we don't store anything about the characters we're looping over within a line in `_update_counts()`. Now we'll need to store them, and add logic to figure out when to add a word to our vocabulary. Let's see if we can make this work...

```python
class ReportCreator():
    ...

    def _update_counts(self, line, counts_dict):
        word = ''
        for char in line:
            counts_dict['characters'] += 1
            if char in '?.!':
                counts_dict['sentences'] += 1
            elif char == ' ':
                counts_dict['words'] += 1
                self.vocabulary.add(word)
                word = ''
            else:
                word += char.lower()
        counts_dict['words'] += 1
        self.vocabulary.add(word)
```

Notice how this solution isn't robust to random punctuation characters like `@` or `&`, but we can deal with that later if necessary (we're going to put it off for now). At least we're considering other ways for sentences to end with by writing `if char in '?.!'`. Also, it seems that we are actually repeating the lines `counts_dict['words'] += 1` and `self.vocabulary.add(word)` in one of our conditions and at the end of the function. In the name of the DRY methodology, we should consider putting this into a function and calling it twice in place of those 4 lines.

Now that we have figured out how `_update_counts()` is going to work, we need to decide how `create_reports()` is going to interact with `create_report()`. As mentioned earlier, it's best to keep functions/methods specialized; this means that if we wanted to create reports and update our class with a list of file paths, the functionality should be the same as if we wanted to do this with a single file path. This means that we should be doing updates to `self.master_counts_dict` from within `create_report()`.

Here's what our code might look like if we updated it with those ideas.

```python
from collections import Counter

class ReportCreator():
    def __init__(self):
        self.vocabulary = set()
        self.master_counts_dict = Counter(sentences=0, words=0, characters=0)

    def create_reports(self, file_paths):
        for file_path in file_paths:
            pass

    def create_report(self, file_path):
        counts_dict = Counter(sentences=0, words=0, characters=0)
        with open(file_path) as txt_file:
            for line in txt_file:
                self._update_counts(line, counts_dict)
            self.master_counts_dict += counts_dict
        return counts_dict

    def _update_counts(self, line, counts_dict):

        def update_words(word):
            counts_dict['words'] += 1
            self.vocabulary.add(word)
            return ''

        word = ''
        for char in line:
            counts_dict['characters'] += 1
            if char in '?.!':
                counts_dict['sentences'] += 1
            elif char == ' ':
                word = update_words(word)
            else:
                word += char.lower()
        update_words(word)
```

Alright, a lot of stuff happened in that change. Let's list off what was changed and describe those changes quickly. 1) We added a function to `_update_counts()` (called `update_words()`) for DRY purposes. 2) We updated `create_report()` so that it changed the `master_counts_dict` attribute with the count dictionary from `_update_counts()`. 3) We changed the data structure used to keep track of out counts to make (2) easier. One by one, slowly now.

1. As we talked about earlier, we wanted to make a function that updated our words information, since we wrote the same lines for this task twice in our original implementation of `_update_counts()`. Here, we are seeing a function, aptly named `update_words()`, which is defined within the scope of `_update_counts()`. We call functions like these nested functions, or helper functions. Because they are defined within the scope of another function, our `update_words()` has access to all the variables within the scope of its parent function. The upshot of this is that we don't have to pass `_update_counts()`'s `counts_dict` variable to `update_words()`, as it automatically has access to that variable because of the scope it was defined in.

2. We see the update to the `master_counts_dict` attribute on line 17. This happens from within `create_report()` so that the user can call either `create_reports()` to make more than one report, or make a single report with `create_report()`. Both will update the `master_counts_dict` attribute, which is useful functionality for our class.

3. The update that we implemented in (2) was made easier by using the `Counter` class (imported from the collections library). The `Counter` class keeps counts of things. This is exactly what we were doing before with our dictionaries. So, why start using a `Counter`? Well, as you may have guessed, we get some extra functionality when using one. Because the `Counter` class knows that it will only ever have integers stored for its values, it has the built in ability to add the values from two `Counter` objects. It does this by key, and it makes a new Counter. That's what we see happening in line 17. Other functionality of `Counter`s can be found in the [docs](https://docs.python.org/2/library/collections.html#collections.Counter). Here, you can learn that `Counter`s are a subclass of `dict`, meaning they inherit from the dictionary class. This makes sense when you think about it!

#### Magic Methods with Your Classes

We now have a well encapsulated class that not only allows us to create reports, but also keeps track of the word counts and vocabulary over all the documents it's seen. To add additional functionality, we could implement some methods that allow the user to control how a report is printed to the user, or to keep track of the average number of words in each document, etc. Who knows what our boss will want us to do next? Instead, the last bit of functionality that we're going to implement on this class is making it respond to the `len()` function. This seems like an intuitive way to get the size of the classes vocabulary.

As we discussed earlier, we can perform tasks like this (ones that allow custom classes to interact with the Python interpreter in an intuitive way) by using magic methods. In this case, we're going the need the `__len__()` method ([here](https://docs.python.org/2/reference/datamodel.html#object.__len__) are the docs).

It might seem intuitive that Python should be able to figure out the size of the set stored on instances of your new class if you were to pass one of those instances to the `len()` function; it knows how long a list or a dictionary is?? Remember, it's because those classes implement a specific version of the `__len__()` method. This means that when an instance of those classes are passed to `len()`, Python knows how to find the "length".

What do we want to return from the `ReportCreator`'s `__len__()` method, then? We want to return the size of the vocabulary set. To get that, we need to call `len()`! This might seem a little self-defining/cyclic in it's logic. Note, however, that if we call `len(self.vocabulary)`, Python knows how to find the length of the set. If we return that value from `__len__()`, then, we extend that functionality to apply to instances of our class.

```python
from collections import Counter

class ReportCreator():
    ...

    def __len__(self):
        return len(self.vocabulary)
```

Simple enough! Let's take a look at what the entire class we've written looks like when we call `create_report()` from within `create_reports()`.

```python
from collections import Counter

class ReportCreator():
    def __init__(self):
        self.vocabulary = set()
        self.master_counts_dict = Counter(sentences=0, words=0, characters=0)

    def create_reports(self, file_paths):
        for file_path in file_paths:
            self.create_report(file_path)

    def create_report(self, file_path):
        counts_dict = Counter(sentences=0, words=0, characters=0)
        with open(file_path) as txt_file:
            for line in txt_file:
                self._update_counts(line, counts_dict)
            self.master_counts_dict += counts_dict
        return counts_dict

    def _update_counts(self, line, counts_dict):

        def update_words(word):
            counts_dict['words'] += 1
            self.vocabulary.add(word)
            return ''

        word = ''
        for char in line:
            counts_dict['characters'] += 1
            if char in '?.!':
                counts_dict['sentences'] += 1
            elif char == ' ':
                word = update_words(word)
            else:
                word += char.lower()
        update_words(word)

    def __len__(self):
        return len(self.vocabulary)
```

Now that we have all that done and stored in `lecture_code.py`, let's test it out in IPython. We'll use the same test text file that we used last week. This time, though, let's pass the text file's path twice to the `create_reports()` method. As a reminder, the stats from that file when we used our `create_report()` function were `{'words': 16, 'characters': 76, 'sentences': 2}`.

```python
In [1]: from lecture_code import ReportCreator

In [2]: rc = ReportCreator()

In [3]: rc.create_reports(['test_text.txt', 'test_text.txt'])

In [4]: rc.master_counts_dict
Out[4]: Counter({'characters': 152, 'sentences': 4, 'words': 32})

In [5]: len(rc)
Out[5]: 16
```

And if we try to use just the `create_report()` method.

```python
In [6]: rc.create_report('test_text.txt')
Out[6]: Counter({'characters': 76, 'sentences': 2, 'words': 16})

In [7]: rc.master_counts_dict
Out[7]: Counter({'characters': 228, 'sentences': 6, 'words': 48})

In [8]: len(rc)
Out[8]: 16
```

Holy moly, everything works! Trust me, I'm as surprised as you are!

### Everything in Python is an Object!

One a final note, it's important to remember that everything in Python is an object. This means that even seemingly simple data structures have attributes and methods stored on them. In addition, they are great starting places to think about when you're building your own custom classes.
