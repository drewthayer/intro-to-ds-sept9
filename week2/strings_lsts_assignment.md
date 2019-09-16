# Strings and Lists Exercise

# Instructions

Tonight we'll be working through problems designed to get your hands on everything you learned tonight - strings and lists (and their methods), along with iteration using for loops. The goal of tonight is to get more comfortable with Python, and working with its data structures. We're also going to work on getting more familiar with some of the methods that are available to us for interacting with strings and lists. Remember that from the IPython terminal, we can find any of the methods that are available on an object via tab completion. That should come in handy tonight!

# Warm-up

The first thing you going to do is work through some problems that will get you in the mindset necessary to solve tonight's assignment problems. The starter code for these warm-up questions is located in the `warmups/` folder for this day. Feel free to edit the scripts in that folder in any way you need to solve these problems. Each question will ask you to add, remove, or change the code in the scripts. As you do so, run your scripts in order to test your changes. At the end of each change, your script should run from top to bottom, so make sure your aren't removing any code that it needs to run.

1. String Warm-up
    1. Look at the code in `warmup1.py`. What is the letter at index 14 of `my_str`? Think about this first, then feel free to print just that letter to check your answer.
    2. In line 1 of `warmup1.py`, change the definition of `my_str` to use the contraction "wasn't" instead of "was not". What letter is at index 14 now?
    3. Change `warmup1.py` to print `my_str` with only lowercase letters.
    4. Add a line between lines 1 and 2 that adds the string `"oR wAs it??"` to the end of `my_str`. When you print `my_str` with no uppercase letters now, it should display: `this string wasn't chosen arbitrarily...or was it??`. (**Hint**: use string concatenation with `+=` to redefine `my_str`)
    5. Using indexing, print only the `"oR wAs it"` in `my_str`. You're going to have to use `[start_index:end_index]` notation to do this.
    6. Find a different way to index into `my_str` to print only the `"oR wAs it"`. This time, though, print all the letters in uppercase.
    7. Add the line `user_input = input('Add "oR wAs it??" (y/n)? ')` at the top of `warmup1.py`. This will prompt the user to enter a `y` or an `n`. Now add an `if` statement to your code that only adds the string `"oR wAs it??"` to `my_str` if the user inputs a `y`. If the user inputs an `n`, don't add `"oR wAs it??"` to `my_str`. Print `my_str` at the end of the script.
    8. Change the first line of `warmup1.py` to `user_input = input('String to add to end of my_str: ')`. Add `user_input` to the end of `my_str` instead of `"oR wAs it??"` and print `my_str`. Note, you'll have to remove the `if` you have in your code from the previous question.
    9. Now, only add `user_input` to `my_str` if it's shorter than 10 characters. No matter what, print `my_str`.

2. List Warm-up
    1. Look at the code in `warmup2.py`. What is going to be printed to the console? Change the print statement so that the first element in `my_list`, `1`, is printed. What's the reason that we have to make this change?
    2. Now change the print statement so that only the words `"hello"`, `"there"`, and `"list"` are grabbed from `my_list` and printed. You should do this with indexing. What do you expect the type of the thing that is printed to be?
    3. Put a line between lines 1 and 2 that adds the number `4` to the end of `my_list`.
    4. Change the print statement so that only the numbers in `my_list` are printed. Again, do this with indexing.
    5. Add another line after the one with `append()` that [removes](https://docs.python.org/3/tutorial/datastructures.html) the word "list" from `my_list`. What do you think `my_list` looks like now? Print it to check.
    6. Now, using indexing, print only the elements in `my_list` at odd indices. You should see: `['hello', 'there', 4]` Is this what you'd expect? If not, consider how you've transformed `my_list`, and convince yourself that this makes sense.
    7. Remove the lines that modify `my_list`. Now add the line `user_input = input('Add the number 4 to mylist (y/n)? ')` at the top of `warmup2.py`. Modify the rest of `warmup2.py` so that if the user inputs a `y`, it will add the number 4 to the end of `my_list`, and otherwise it will do nothing. At the end, print `my_list`. Play around with different inputs. Do they work the way you'd expect?
    8. Modify `warmup2.py` so that it will accept any user inputted string. If the length of that string is less than 8, your script should add it to `my_list`, and other wise it should add the number 4 to the list. Print `my_list` at the end to see what it is.

3. For Loop Warm-up
    1. Look at the code in `warmup3.py`. As in `warmup2.py`, we are printing a list. This time, though, it is displayed differently. What do you think will be printed to the console? Why does it look like this, as opposed to the format we saw in `warmup2.py`?
    2. Change the code in `warmup3.py` so that it also prints the indices of the elements in `my_list`.
    3. Add an `if` to the for loop so that only the elements at odd indices are printed, along with their index.
    4. Change your if statement to only print the elements that are longer than 4 characters, again along with their index. Why can you just `len()` to do this?
    5. Now, instead of just printing the elements to the console, change the script so that it adds the elements that are longer than 4 characters to a new list, called `longer_elements`. This means that you will have to create an empty list with that name before the list. Print `longer_elements` at the end of the script.
    6. Try printing `longer_elements` inside the for loop you created above. What do you expect to see when you run your script? Make sure you understand why you're getting this output.
    7. Add the line `user_number = int(input('Min length to be printed: '))` to the top of `warmup3.py`. Now, change your script so that it only adds words that are longer than a user inputted number to `longer_elements`. You can include the statement printing `longer_elements` inside the loop if you want. Print `longer_elements` after the loop.

# Assignment Questions

### Part 1 - Practice with `For` Loops

For the first part here, take a couple of the scripts we wrote in the `intro_python_assignment.md` in Week 1, Day 2, and change them from using `while` loops to using `for` loops. Start out and just do the first two (for extra practice you could do this with the rest of the problems we worked through):  

1. Write a script that computes and prints the factorial of a user inputted number.
2. Write a script that determines whether or not a user inputted number is a prime and prints 'The number you inputted is a prime/ not a prime number.' depending on what your script finds.

Remember, the goal is to write these by using `for` loops.

### Part 2 - Practice with Strings

Now you're going to work with strings, along with your knowledge of `for` loops and iteration. Remember that you can tab complete to find helpful methods that you can use to operate on strings! For some of these problems, you may not use anything new, but for others, there may be a helpful string method. As a last note, just like with many programming problems, there will be multiple ways to solve these problems.

1. Write a script that counts the occurrences of a user inputted letter in a string that is also inputted by the user. (**Hint**: Use `input()` twice to get both of the user inputs). Make sure to build this in such a way that it ignores the case of the inputted string and letter. For example if the user inputs `c`, and the string `Chelsea likes candy` your script should print 2.
2. Write a script that checks if a user inputted string ends in an exclamation point. **If it does**, then print the string in all capital letters. **If it doesn't**, print the string in all lowercase letters.  
3. Write a script that removes all of the vowels in a user inputted string.
4. Write a script that makes every other letter of a user inputted string capitalized.

### Part 3 - Practice with Lists

1. Write a script that creates a list of only the even numbers between 0 and a user inputted number.
2. Write a script that creates a list of only numbers divisible by a user inputted number that are between 0 and a user inputted number (**Hint**: Use `input()` twice to get both of the user inputs).
3. Given the list `[0, 3, 6, 9, 10, 2, 5]` and `[2, 6, 4, 7, 8, 1, 15]`, write a script that finds the common elements between them. Store them in a list, and print that list, sorted, as the final output (if you'd like you can go ahead and hard code those lists in your script).  
4. For a user inputted number, write a script that outputs a list of multiples of that number from 0 up to another user inputted number. For example, given the numbers 4 and 20, your script should print the numbers 4, 8, 12, and 16.

### Extra Credit

Alter your script in Part 3, Question 3 to accept arbitrary lists. Build it such that the user has to enter 7 numbers (each separated by an enter at the command line) for each list.
