# Day 8: 

<br><br><br><br><br><br>
# FileIO, csv's and Pandas first look

<br><br>
#### Use `file.readlines()` and `file.write()`


* Write to a text file using `with open('demo.txt', 'w') as f: ...`
> ```python
> lines = ['I am a line', 'So am I', 'I am not a line, wait, yes I am']
> with open('demo.txt', mode='w') as f:
>     f.write(str(lines[0]) + '\n')
>     for line in lines[1:]:
>         f.write(str(line) + '\n')
> ```

* Read from a text file using `with open('demo.txt', 'r') as f: ...`
	* Using `with open` means we don't need to `.close()` the file
		* can verify with `f.closed #--> True`
	* Understand the `open` tags:
		* `'r'` : read only
		* `'w'` : write only, overwrites the file
		* `'a'` : read, and append to the end
> ```python
> with open('demo.txt', mode='r') as f:
>     line = f.readline()
>     while line:
>         print(line)
>         line = f.readline()
> ```

<br><br>
#### Read from a CSV file using the `csv` module
* You don't need this for reading CSV's, but it has some nice simple features
* Read a CSV
> ```python
> import csv
> results = []
> with open('demo.csv', 'r') as f:
>	lines = csv.reader(f, delimiter=',')
>	
> 	for line in lines:
>		results.append(line)
> ```

<br><br>
#### Write to a CSV file using the `csv` module
* You don't need this for reading CSV's, but it has some nice simple features
* Read a CSV
> ```python
> # given some data
> with open('demo_out.csv', 'w') as f:
>	writer = csv.writer(f)
>	writer.writerows(some_list)
> ```

<br><br>
#### Read from a CSV using `pandas` `read_csv`
* `df = pd.read_csv('something.csv')`