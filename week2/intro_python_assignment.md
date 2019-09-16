# Time to do Python

## Workflow
There's no better way to learn a programming language than to try and solve real problems with it. To that end, this assignment will present a good workflow for working with IPython to iteratively test code while you create your scripts in a text editor.

Let's walk through an example. You should make sure to follow along so you get some hands on practice. Consider the problem:

    Write a script that prints the sum of the whole numbers between 1 and a user inputted number.

Alright, first we want to open up IPython and our favorite text editor (Atom if you followed our advice from day 1). I prefer to have these two side by side so that it's easy to look at and work in each.

We're going to have to start a new file in our text editor to store our script. You should give your script a short name that quickly describes what it does. Python scripts are appended with the file extension `.py`. So, for this problem I would name my script something like `sum_whole_numbers.py`. Now we're off to the races.

At this point, I start thinking about how I'm going to solve my problem. Most of the time this means that I want to experiment with potential solutions/approaches. This is exactly what IPython is great for. It allows you to interact with Python one step at a time and remembers what you've done for the entire time the *session* has been open.

With that in mind, I want to give myself a variable to play with as I solve this problem. Let's call it `my_num` and set it to 7 in IPython.

**Note**: If you want to look at the variables currently in the namespace of your IPython session, simply type the command `whos` into the console.

```python
In [1]: my_num = 7

In [2]: whos
Variable   Type    Data/Info
============================
my_num     int     7
```

Now that I have a number to work with, it's time to think about how to solve the problem. I know that I'm going to need a variable to store my sum result in and another to keep track of the number I'm going to add to that sum result. I'll call these `sum_result` and `current`, respectively.

```python
In [3]: sum_result = 0

In [4]: current = 1
```

I know that I'm going to need a while loop that terminates when `current` is greater than `my_num` (i.e. keeps running while `current` is less than or equal to `my_num`).

```python
In [5]: while current <= my_num:
   ...:
```

Notice that when we start a `while` loop IPython knows that we're going to want to write the `while` block, so it prompts for that with the `...:`. What is this `while` going to do at each iteration? Well, we need to add the value of `current` (remember we will only make it into the loop if `current` is less than or equal to `my_num`) to `sum_result`, and then increment `current` by one. Let's let IPython know what we want to do now!

```python
In [5]: while current <= my_num:
   ...:     sum_result += current
   ...:     current += 1
   ...:
```

Ok, so, what happened? IPython didn't show us anything, did it even work?? It did, actually! We just have to check `sum_result` to see what we got.

```python
In [6]: sum_result
Out[6]: 28
```

### Tying it All Together

This is great! Now that we know how we're solving our problem in Python, we can go back to writing our script. Let's take what we've written and put it in our text file, `sum_whole_numbers.py`.

```python
my_num = 7
sum_result = 0
current = 1
while current <= my_num:
    sum_result += current
    current += 1
```

But wait, weren't we asked to take input from the user? And didn't we need to print the result? These aren't hard fixes; remember the `input()` function to get numbers from the user? Let's use that. All we need to do to print the value we computed is pass `sum_result` to `print()`.

```python
my_num = int(input('Enter a number to find the sum up to: '))
sum_result = 0
current = 1
while current <= my_num:
    sum_result += current
    current += 1
print(sum_result)
```

Now we can simply run our new script from IPython. Know that IPython needs to know where the script you wrote is in your file structure. If you open IPython from the same directory that your script is saved in, there should be no problem. Otherwise, you'll need to give IPython a path to the script.

```python
In [7]: run sum_whole_numbers.py
Enter a number to find the sum up to: 7
28

In [8]: run sum_whole_numbers.py
Enter a number to find the sum up to: 9
45
```

This is awesome! We now have a script that will solve a problem for arbitrary input! Congratulations, you've written your first dynamic program! The process we worked through above is generally iterative; as you test and find chunks of code that you know work in IPython, you iteratively add them to your script.

## Assignment Questions

1. Write a script that takes a user inputted number and prints whether it is positive, negative or zero, with "The inputted number is (positive/negative/zero)" depending.

2. Write a script that takes two user inputted numbers and prints "The first number is larger" or "The second number is larger" depending on which is larger. (**Hint**: you'll need to use `input()` twice.)

3. Write a script that computes the sum from 0 to a user inputted number. This time though, start at the user inputted number and work down. This answer will look very much like the example above, you'll just need to change a couple of things.

4. Write a script that computes the factorial of a user inputted number. If you don't know what a factorial is or need a review, check [this](https://en.wikipedia.org/wiki/Factorial) link out. Again, your solution is going to look a lot like the code above. Things you should think about:
    * What is the process of computing a factorial if you were to compute it by hand?
    * What is the common starting place when trying to compute the factorial of any number?<br><br>

5.  Write a script that computes and prints all of the divisors of a user inputted number. If you don't know what a divisor is or need a review, check out [this](https://en.wikipedia.org/wiki/Divisor) link. Things to think about:
    * How do you determine if a single number is a divisor of another?
    * How do you do this multiple times (**Hint**: it involves a while loop)?
    * When do you stop the loop?<br><br>

6.  Write a script that computes the greatest common divisor between two user inputted numbers. If you don't know what a greatest common divisor is, check out [this](https://en.wikipedia.org/wiki/Greatest_common_divisor) link. Things to think about:
    * How do you get two numbers from the user?
    * Where should you start your search for the GCD?
    * Where/how should you end your search?<br><br>

7.  Write a script that computes the least common multiple between two user inputted numbers. If you don't know what a least common multiple is or want a review check [this](https://en.wikipedia.org/wiki/Least_common_multiple) out. Things to think about:
    * How do you get two numbers from the user?
    * Where should you start your search for the LCM?
    * Where/how should you end your search?<br><br>

8. Write a script that determines whether or not a user inputted number is a prime number and prints `'The number you inputted is (not) a prime number.'` depending on what your script finds. If you don't know what a prime number is or need a review, check out [this](https://en.wikipedia.org/wiki/Prime_number) link. Things to think about:
    * How do you check if a number is divisible by another number?
    * What numbers are a prime number divisible by?
    * How do you check all of the numbers a number could be divisible by (**Hint**: use a loop)?
    * When do you stop the loop?<br><br>

9.  One can use loops to compute the elements of a mathematical series. Series can be defined recursively with the value of each element depending on the one that comes before it. Consider the series created by the rules:

    ![series](misc/series_pic.png)

    Write a script that prints the `nth` element in the series as determined by input from the user. e.g. If the user inputs the number `3`, your script should print the 3rd element in the series, `15`. You're welcome to check the math! Things to think about:
    * You know you're going to use a loop to solve this problem, how?
    * How do you store each of the elements as you calculate them with the loop?
    * How many elements do you need to keep track of at any one time?
    * How do you know when to stop the loop?<br><br>

10. Challenge: solve the equation:

    `(a + (b - c) * d - e) * f = 75`

    where a, b, c, d, e, and f are unique integers in the range [1, 6].

    Hints:
      - Computers are so fast that your program can simply try all possible valid values of a, b, c, d, e, and f until it finds one permutation of 1-6 that solves the challenge! (Btw, there is only *one* permutation that will solve it.)
      - Use 6 nested for-loops to enumerate all ways of setting each of a, b, c, d, e, and f to the values 1-6.
      - Use if-statements to ensure all values of a, b, c, d, e, and f are valid. (I.e. to ensure that each value is unique)
      - Use an if-statement to test if the current permutation solves the challenge.<br><br>

    Want more? Modify your program to solve all these (very similar) equations:

    ```
    (a + (b - c) * d - e) * f = 22
    (a + (b - c) * d - e) * f = 38
    (a + (b - c) * d - e) * f = 46
    (a + (b - c) * d - e) * f = 57
    (a + (b - c) * d - e) * f = 78
    (a + (b - c) * d - e) * f = 80
    (a + (b - c) * d - e) * f = 81
    (a + (b - c) * d - e) * f = 88
    (a + (b - c) * d - e) * f = 92
    (a + (b - c) * d - e) * f = 100
    (a + (b - c) * d - e) * f = 102
    (a + (b - c) * d - e) * f = 104
    (a + (b - c) * d - e) * f = 105
    ```
