# Tuples, Dictionaries, and Sets Exercise

# Instructions

As with your previous assignment, tonight's will get you practice with the data structures that you learned about in lecture. While most of the problems will be centered around tuples, dictionaries, and sets, they will also build on the structures that you've already learned about.

# Warmup

Tonight we'll also begin by working through some problems that will get you in the mindset necessary to solve tonight's assignment problems. The starter code for these warm-up questions is located in the `warmups` folder for this day. Feel free to edit the scripts in that folder in any way you need to solve these problems. Each of the sections below will get you working and interacting with the data structures we learned about tonight - the `tuple`, `dictionary`, and `set`.

1. Tuple warm up:
    1. Look at the code in `warmup1.py`. What do you think this `tuple` is storing? If I tell you it is storing the four suits of a standard card deck, can you tell me why it's appropriate that I use a `tuple` for this?
    2. Run `warmup1.py`, and note what it originally prints.
    3. Now, change the print statement to print out the 1st element in the `tuple` (e.g. `diamond`).
    4. Now, change the print statement to print out every other element.
    5. Why are we able to grab individual elements (or every other element) from the `tuple` just as if it is a `list`?
    4. Now, alter it so that it prints out each of the elements, one at a time on a new line. Use a `for` loop to do this. Why are we able to use a `for` loop on the `tuple` like this?
    5.  Now, say that I want to add a new suit to my card deck. Let's call it `gorilla` (who doesn't like a gorilla suit). How would I do this? Why can't we use `append` on a `tuple` like we can on a `list`?

2. Dictionary warm up:
    1. Don't run the code yet! First, examine the code in `warmup2.py`. What do you think it will print when run? Why does it print this?
    2. Why is it appropriate to use a dictionary in this scenario?
    3. Okay, so you will by now have noticed what it printed. Change the `element` variable that is storing the key through each iteration of the loop to be a more descriptive variable name.
    4. Now, change the loop so that it not only prints the `key` at every iteration, but both the `key` and `value` (i.e. print the state as well as the city in the loop).
    5. Build another dictionary that stores the state and capital of the state you grew up in, as well as the state and capital of the state your neighbor grew up in. Call this `neighbor_dct`, and put it on the second line of the `warmup2.py` script (before the `for` loop).
    6. Now, add a line before the for loop that adds the key-value pairs in `neighbor_dct` to `my_dct`. `my_dct` should now have the contents from it's previous state and also `neighbor_dct`.
    7. Modify `warmup2.py` to take in a user inputted state. Then, take that user inputted state, and if it is in `my_dct`, print out it's capital. If it's not, then print out 'Capital not found!'.
    8. Now, modify `warmup2.py` to ask the user for a state name. If it is not already in `my_dct`, have your script prompt the user for a capital to associate with that state name.

3. Set warm up:
    1. Run `warmup3.py`. Why are we able to use a `for` loop to print out the elements of `my_set`?
    2. On the second line, create a new set (you'll have to move the `for` and everything below it down one line). Call it `my_fav_primes`, and enter 3 of your favorite prime numbers.
    3. Now, move everything down one more line, and create a third set that gives the numbers that `my_set` and `my_fav_primes` have in common. Alter the `for` loop to print out the numbers in this new `set`.  
    4. Change your code to get only the numbers that are in `my_set` but aren't in `my_fav_primes`. Store these in a third set, and alter the `for` loop to print out the numbers in this third set.
    5. Create a new set with the elements from both `my_fav_primes` and `my_set`, and name it `my_tot_primes`. Alter the `for` loop to print out its values.
    6. Now, modify `warmup3.py` to take in a user inputted prime, and then add it to `my_tot_primes`.

# Assignment Questions

### Part 1 - Practice with Tuples

1. Write a script that prompts the user to input numbers separated by commas. Your script will then take these inputted numbers and store them as a list of tuples, two at a time. Finally, your script will print that list of tuples to the user. If the user inputs an odd number of numbers, then only make a list of the largest number of pairs of two that are possible.

 Example: If you inputted the numbers `1, 2, 3, 4, 5, 6`, your script should print `[(1, 2), (3, 4), (5, 6)]`. If you inputted the numbers `1, 2, 3, 4, 5`, your script should print `[(1, 2), (3, 4)]`.

 **Hint**: Check out the [zip](https://docs.python.org/3/library/functions.html#zip) function. While you don't have to use it, it could make things easier.

### Part 2 - Practice with Dictionaries

1. Write a script that prompts the user to input numbers separated by dashes ( - ). Your script will take those numbers, and print a dictionary where the keys are the inputted numbers, and the values are the squares of those numbers.

 Example: If you inputted the numbers `1 - 5 - 8 - 10`, your script should print `{8: 64, 1: 1, 10: 100, 5: 25}` (remember that dictionaries are unordered, which is why the script might print out the key-value pairs in a different order than the user inputted the numbers).

2. Write a script that prompts the user for a state name. It will then check that state name against the dictionary below to give back the capital of that state. However, you'll notice that the dictionary doesn't know the capitals for all the states. If the user inputs the name of a state that isn't in the dictionary, your script should print that the capital is unknown.

 ```python
    state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento',
                        'Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                        'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}
 ```

 Example: If you inputted the state name `Kansas`, your script should print `Topeka`. If you inputted the state name `Washington`, your script should print `Capital unknown`.

  How could you make it so that your script isn't sensitive to the case of the inputted state? (**Hint**: one of the easiest ways is by changing the state dictionary slightly and using a method on your input string.)

3. Write a script that will continually prompt the user for a set of three things to be separated by commas. The first two things will be (x, y) coordinates of the word that follows (the word will be the third thing). So the user will input a string that is formatted like `x, y, word`. Your script will use the string to build a dictionary with the first two inputs (i.e. the (x, y)) from each string as keys to a dictionary, and the third input (the word) as the value for that key. The script will continually prompt the user to input strings in this format until the user inputs nothing (i.e. hits enter with no input).

 After building the dictionary, your script should allow the user to query the dictionary it built by accepting strings of the format `x, y`. It should check if the coordinate is in the dictionary, and if it is return the corresponding word. If it isn't, it should print `Coordinate not found`. This should continue until the user inputs the letter `q`, at which point the script should exit.

 Example usage:
 ```
 Please enter a coordinate-word pair in the format (x, y, word): 1, 2, hello
 Please enter a coordinate-word pair in the format (x, y, word): 2, 3, world
 Please enter a coordinate-word pair in the format (x, y, word):
 Please enter a coordinate to look up: 2, 3  
 world
 Please enter a coordinate to look up: 3, 4
 Coordinate not found
 Please enter a coordinate to look up: q
 ```

### Part 3 - Practice with Sets

1. Write a script that prompts the user to input numbers separated by commas, and then does so again. It should then print those numbers that were common in both entries.

 Example: If you inputted the numbers `1, 2, 3, 5, 6` first, and `2, 3, 4, 6, 7` second, your script should print `2, 3, 6`. Make sure to use sets, as they are optimal for this problem.

 **Hint**: For the output to be formatted in the prescribed way, you could use the `join()` method available on strings.

2. Write a script that prompts a user to input a list of words separated by commas, and then prints out the unique words in the list.

 Example: If you inputted the words `hello, there, how, are, you, hello, you`, your script would print `how, you, there, hello, are`.

3. Write a script that continually accepts a word from the user. As it does, it should add the word to a set. If the user enters the letter `v`, your script should display all the known words, it's vocabulary. This will continue until the user enters the letter `q`, which should quit the program.

 Example usage:
 ```
 Enter a word to add to the vocabulary: thing
 Enter a word to add to the vocabulary: stuff
 Enter a word to add to the vocabulary: v
 thing stuff
 Enter a word to add to the vocabulary: hello
 Enter a word to add to the vocabulary: v
 thing stuff hello
 Enter a word to add to the vocabulary: q
 ```
