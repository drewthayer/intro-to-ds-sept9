# Week 1:
## Our Environments, Basic Python, Control Flow and Lists, Loops


<br><br><br><br><br><br>
### Day 1: Environments and Setup

* utilize a working Python environment on your local machine
	* installed with [Anaconda](https://anaconda.com)
* explore [GitHub](https://github.com) and access our [classroom repository](https://github.com/clownfragment/dsi-python-fundamentals)
* begin practicing Python in a real code editor (such as [VSCode](https://code.visualstudio.com/)) installed on your local machine
* open a terminal and utilize the **ipython** environment that ships with Anaconda
	* on a Mac, press *COMMAND* + *SPACE BAR* to open spotlight, type "terminal" and hit return. Then, type `ipython` in the terminal
	* in Linux, open a terminal and type `ipython`
	* on Windows, options vary, see the Anaconda and IPython documentation
* perform simple navigation in the terminal
	* `cd` and `cd ..` to navigate between directories
	* `ls` to list directory contents


<br><br><br><br><br><br>
### Day 2: Basic Python

* `git clone` our classroom repo on the command line and update your local copy using `git pull`
	* use `touch filename` to create new files in the terminal
	* rename files using `mv old_filename.py new_filename.py` syntax in the terminal
* describe markdown (`*.md` files) and maybe even start writing them?
* comment your code with single line (`#`) or block (`''' some comment '''`) comments 
* perform operations on common variable types
	* such as `int`, `float` and `bool`
	* with common arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
* declare variables and operate on them
	* analyze **mutability** using the `id()` function
	* check the `type()` of the variable
	* modify the value of a variable using basic increment operations:
		* like `+=`, `-=`, `*=`, `**=` and `/=`
* declare simple functions with one parameter
	* that `return` things
	* that perform math operations


<br><br><br><br><br><br>
### Day 3: Control Flow and Lists

* practice problems on [CodeWars](https://codewars.com)
	* consider this to be something like "Programmer Sudoku", to keep you sharp
* properly name things according to conventions in Python
* control the flow of your programs using basic logic
	* using `if`, `elif` and `else`
		* with the `==`, `!=`, `>`, `<`, `>=` and `<=` operators
	* using `and`, `or` and `not`
* create, analyze and modify lists
	* declare lists using the syntax `some_list = []` or `some_list = list()`
		* create lists with values, like `some_list = [3, 2, 9, 18, 34]`
		* create lists filled with one value, like `some_list = [7] * 10`
	* generate series of numbers in lists by using `some_list = list(range(a, n))`
	* understand indices and access elements/values in lists
		* `some_list[0]` to access the initial index
		* `some_list[0:5]` to access the first 5 values in a list
		* `some_list[-1]` to access the last value of a list
		* `some_list[-5:-1]` to access the last 4 values in a list
	* modify specific elements in a list
		* `some_list[0] = 7` : sets the first value in the list to `7`
	* understand `in` and `not in` in regards to lists:
		* ex: `if 7 not in some_list: print('dang')`
	* use common list functions:
		* these functions don't alter the list
		* `len(some_list)`: Len is your best and oldest functional friend, you'll spend a lot of time with Len.
		* `sum(some_list)`: adds all values in the list
		* `sorted(some_list)`: sorts
		* `max(some_list)` : returns the maximum element value
		* `min(some_list)` : returns the maximum element value
		* `any(some_list)` : `True` if ANY values in some_list are "truthy" 
		* `all(some_list)` : `True` if ALL values in some_list are "truthy" 
	* use common list methods
		* these methods may alter the list
		* `some_list.append(x)` : places a new value at the end of the list
		* `some_list.extend(another_list)` : puts the contents of `another_list` into `some_list`
		* `some_list.pop()` : removes and **returns** the last item in the list
		* `some_list.reverse()` : reverses the list
		* `some_list.sort()` : sorts the list, ascending
		* `some_list.remove(x)` : remove a specific value from the list
		* `some_list.count(x)` : counts the number of occurrences of a specific value in the list
	* make a real, unique copy of a list with the same values as the original:
		* `some_new_list = some_list.copy()`
		* `some_new_list = some_list[:]`
		* `some_new_list = list(some_list)`
	* understand the error message that `list(27)` produces when run
		* hint: **iterable** types
* create functions that execute simple math operations
	* write the `is_divisor()` function using two parameters
	* write the `sum_to_n()` function using a function on a list
	* write the `sum_range()` function
	* write the `sum_range_divisible_by_a()` function
		

<br><br><br><br><br><br>
### Day 4: Loops


* create and push to your own branch in our Classroom repo:
	* create your branch using `git checkout -b your_name` in the terminal
	* make sure you are adding changes to your own branch using `git status`
	* add your changes using `git add filename`
	* commit your changes using `git commit -m 'make a good message'`
	* push those changes to your remote branch using `git push`
	* switch between branches using `git checkout branch_name`
	* to synchronize your branch with master
		* `git checkout master`
		* `git pull`
		* `git checkout your_branch_name`
		* `git merge master`
* create new folders in the terminal using `mkdir`
* write loops to solve numeric problems
	* describe simple accumulators and the roles they play in loopage
		* `int` accumulators
		* `float` accumulators
		* `bool` "accumulators", aka "Flags"
		* `list` accumulators, or "collectors"
	* `for` loops using the `range()` function
	* `for` loops that traverse items in a list
		* display values in a list
		* access and mutate values in a `list`
		* accumulate from `list` values
			* into an `int` or `float`
			* filtering into another list
			* creating parallel lists
	* `for` loops that traverse items in parallel lists
	* nested `for` loops
	* `while` loops using a conditional check
		* for solving "open-ended" problems
		* for delivering menus
	* using `break`, `continue` or `pass` when appropriate
		* `break` to avoid or exit **infinite loops** when using `while`
		* `break` to exit a `for` or `while` loop when further computation is no longer necessary
		* `continue` to conditionally skip an operation
		* `pass` as a placeholder in an unfinished function
	* list comprehensions, a brief introduction
		* [i for i in some_list]
* create functions that execute common mathematical operations
	* write the `factorial()` function
	* write the `is_prime()` function
	* write the `get_anagrams()` function
	* write the `poisson_pmf()` function


