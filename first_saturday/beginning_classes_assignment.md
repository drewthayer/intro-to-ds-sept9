# Instructions 

Tonight we'll work through building classes and getting practice with their syntax. We'll begin by having you complete class constructors that are already written, and then move on to having you write class constructors for some code that is already written. After that, we'll move on to building a class or two of your own!

For each of the classes you build tonight, you should test them out. Try instantiating a couple of different instances of each class you build, and make sure they work the way that you would expect. A couple of questions to ask yourself are: 

* If I tab complete, do I see the attributes/methods that I would expect?
* If I examine an attribute of my instantiated class/object, is it's value what you would expect?
* Do the methods that you've defined in your class work as expected for your instantiated class/object?

# Warmup

### Part 1

For the first set of problems, we'll give you a class constructor and ask that you fill it in according to some specifications. 

1. Let's make a `Dog` class. In this dog class, we've gone ahead and given the skeleton for the `__init__` method, as well as a `wag_tail` method. We want you to fill these in such that: 

 * In the `__init__` method, we assign to our `Dog` class a `name` attribute and a `happiness_level` attribute. 
 * In the `wag_tail` method, the `Dog` "wags it's tail" for the inputted `n` number of times, and each time it wags it's tail, it's `happiness_level` increases by 5. 

 ```python 
class Dog(): 
    """This docstring will discuss how to interact with our Dog class. 

    Our Dog class will have two attributes - a name and happiness_level. 
    It's one method, wag_tail, will simulate the dog wagging it's tail 
    some number of times, and increasing it's happiness level. 

    Parameters: 
    -----------
        name: str
        happiness_level: int
    """
    
    def __init__(self, name, happiness_level=5): 
        pass

    def wag_tail(self, n): 
        """Wags the dogs tail n times, and each time increase 
        happiness level by 5. 

        Args: 
            n: int
        """
        pass
```

 * What does it mean for me to have put an `=5` after the `happiness_level` parameter in the `__init__` method?
 * Why do I have to pass self as the first argument in both the `__init__` method and the `wag_tail` method?

2. Now, let's build a `Cat` class. In this cat class, we've again given you the skeleton for the `__init__` method, as well as a method called `sense_earthquake` (I just read in Reader's Digest that cat's can sense earthquakes - who knew?). We want you to fill these in such that: 

 * In the `__init__` method, we assign to our `Cat` class a `name` attribute, a `laziness_level` attribute, and a `location` attribute. See the docstring for a description of the specific information that each attribute should contain. 
 * In the `sense_earthquake` method, if there is an earthquake, the cat's `location` attribute changes to the string `'gone dark'` and we print the string `<name> has gone dark!` (where `<name>` is equal to the `name` attribute of the cat). If there is no earthquake, then we print the current location and name of the cat (e.g. `<name> is at <location>`). 

 ```python 
class Cat(): 
    """This docstring will discuss how to interact with our Cat class. 

    Our Cat class will have three attributes - a name, laziness level,  
    and a location. It's one method, sense_earthquake, will change 
    the cats location based on whether or not there is an earthquake. 

    Parameters
    ----------
        name: str 
        laziness_level: int
            This holds how lazy the cat is on a scale of 1 to 10. 
        location: str
            This holds where the cat is currently located at. 
    """

    def __init__(self, name, laziness_level, location): 
        pass

    def sense_earthquake(self, earthquake): 
        """Checks if the cat senses an earthquake, and if so changes the cat's
        location to 'gone dark'. 

        Args: 
            earthquake: boolean
                Holds a True or False as to whether there was an earthquake. 
        """
        pass
```

 * Can you change your definition of the `__init__` method so that any instances of our cat have a `laziness_level` of 5 and a `location` of "home" if arguments for those parameters are not passed in at instantiation? 

### Part 2

For the second set of problems, we'll give you blocks of code that we want you to place into methods within a class definition. After building up each of your class definitions, use them to instantiate a couple of instances of your class. Play around with those instances, and make sure that everything is working like you would expect. 

1. Using the following code snippets, we want you to define a `Car` class. We've given you the code for an `__init__` method and a `drive` method. We want you to build the class definition, as well as the definitions for these two methods. 

 * `__init__` method code  

 We want there to be three parameters passed in - `model`, `color`, 
and `tank_size`. 

 ```python 
self.model = model 
self.color = color
self.tank_size = tank_size
self.gallons_of_gas = self.tank_size # We're assuming its tank is full. 
```

 * `drive` method code 

 We want there to be one parameter passed in - `miles_driven`. 

 ```python
self.gallons_of_gas -= miles_driven / 10. 
```

 * Note that for each of these methods above, I didn't include a certain parameter that is passed **by deafult** to any method within a class - what is that parameter? Can you describe exactly what it is used for?

2. Using the following code snippets, we want you to define a `Plane` class. We've given you the code for an `__init__` method and a `fly` method. We want you to build the class definition, as well as the definition for these two methods.   

 * `__init__` method code

 We want there to be three parameters passed in - `destination`, `departure_city`, and `trip_distance`. 

 ```python
 self.destination = destination 
 self.departure_city = departure_city
 self.trip_distance = trip_distance
 ```

 * `fly` method code 

 We don't want any parameters to be passed in. 

 ```python 
 self.departure_city, self.destination = self.destination, self.departure_city
 ```
 
 In looking at the code for the `fly` method, can you take a guess at what it is doing? It turns out that this is a special way that we can do simultaneous variable assignment so that we don't have to use a placeholder. If we were to try to do the above via the following, we would not get the intended result:  

 ```python
 self.departure_city = self.destination
 self.destination = self.departure_city
 ```

 This would result in us with `departure_city` and `destination` being equal to the exact same thing! A way to get around this would be to use a placeholder for the `departure_city` value **before** it gets changed: 

 ```python 
 placeholder = self.departure_city
 self.departure_city = self.destination
 self.destination = placeholder 
 ```

 The one line of code that we gave above for the `fly` method is just shorthand for this same thing. It allows us to do a swap **in place** so that we can avoid having to use a placeholder. 

### Assignment Questions 

Below, we want you to build up some classes from scratch. We'll describe the attributes and methods that each class should have available, and ask that you dive in!

1. Let's build a `Company` class, used to represent some company (Denver Beer Co., Qdoba, Chipotle, etc.). 

    1. In this class, we'll have the following attributes: 

        * `name` - `str` holding the name of the company 
        * `industry_type` - `str` holding what industry the company belongs to
        * `num_employees` - `int` holding the number of employees the company has
        * `total_revenue` - `float` holding the total revenue of the company 

    2. Instances of the `Company` class will have the following methods: 

        * `serve_customer` - this method will take in a `float` that is equal to the cost of serving some customer, and then adjust the `total_revenue` by that cost. 
        * `gain_employees` - this method will take in a `list` that contains new employees that the company has just brought on, and will update the `num_employees` attribute to take account of that. 

2. Let's build a `TV` class, used to represent a television. 

    1. In this class, we'll have the following attributes: 

        * `brand` - `str` holding the brand of the television ('Sony', 'LG', etc.)
        * `on_status` - `bool` holding whether or not the television is on. This should default to False (e.g. off). 
        * `current_channel` - `int` holding the current channel number. If the television is off, then the `current_channel` should be 0. Given that `on_status` defaults to off, what does that mean the `current_channel` should default to?
        * `life_perc` - `float` holding the percentage of life left in the TV. This should start out at 100% (i.e. default to 100). 

    2. Instances of the `TV` class will have the following methods: 

        * `hit_power` - this will turn the television on/off, depending on whether it's already on/off (if its on it'll switch it off, and vice versa). We'll add a couple of stipulations with this one: 
            * Each time the television is turned off, it loses a little bit of life - decrease the `life_perc` by 0.01 each time the television is turned off. 
            * Each time the television is turned off the channel should be set to 0. 
        * `change_channel` - this will take in an `int` to change the channel to a new one. We'll add a stipulation to this as well: 
        * If the television is not on, but the `change_channel` method is called, print 'Television is not on!'. Otherwise, change the channel to the inputted channel. 
