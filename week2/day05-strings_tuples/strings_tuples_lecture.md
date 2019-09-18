# Day 5 Lecture Notes

<br><br><br><br><br><br>
# `str`ings

<br><br><br><br>
## `str`ings are sort of like immutable lists
* we can use indexing, but we can't change values
```python
'some_str'[0] #--> 's'
'some string'[0] = 'f' # will throw an error
```


<br><br><br><br>
## String declaration
* commonly declare strings using the syntax `string = 'some text here'`
* three types of string bounding characters
    * `'single quotes'`
    * `"double quotes"`
    * `'''triple single quotes'''`
    * `"""triple double quotes"""`

<br><br>
### single line `str`ing declaration
* `\n` has to be explicitly stated
```python
some_string = 'with "single" \'quotes\' \nthis is on a new line'
print(some_string)

some_string = "with 'double' \"quotes\""
print(some_string)
```

<br><br>
### multi-line `str`ing declaration
* used when `\n` (newline) is to be implicitly stated
* used in function Docstrings
* can also be used for multi-line comments
```python
some_string = '''with triple single quotes
some more text
'''
print(some_string)

some_string = """with triple double quotes
this will also print
"""
```

<br><br>
### Docstring example
* use Docstrings in your functions to describe the behavior
* also describe parameters and returns of the function
```python
def count_unique_chars_in_str(some_string):
    '''takes a string and returns a count of that string's
    unique characters, not including empty spaces

    Parameters
    ----------
    some_str: (str)
        we count the characters of this string

    Returns
    -------
    count: (int)
        number of characters in the string
    '''
    output = []
    for char in some_string:
        if char != ' ' and char not in output:
            output.append(char)
    
    return len(output)


print(count_unique_chars_in_str(test_str))
```

<br><br><br><br>
## in operator
* check to see if something is in a collection
* sometimes called the "membership operator"
    * 'club' in 'very important club' #-> True
```python
print('a' in 'plant')
print(4 in [1,4,7,8,2,4,6,4])
```

<br><br>
### String iteration using `in` and `enumerate()`
* similar iteration process to `list`s
```python
def iterate_through_str(some_str):
    for i, char in enumerate(some_str):
        print(i, char)
    
    # # Uncomment to see iteration on a str cast as list
    # some_str_lst = list(some_str)
    # for char in some_str_lst:
    #     print(char)

test_str = 'We need to pass something in this function'
test_str[0] = 'w'

iterate_through_str(test_str)
```

<br><br>
### using `in` inside a conditional
```python
def find_anagrams(list_of_words):
    output = []
    
    for word1 in list_of_words:
        for word2 in list_of_words:
            print(sorted(word1), sorted(word2))
            if word1 != word2:
                if sorted(word1) == sorted(word2):
                    if word1 not in output:
                        output.append(word1)
        
    return output

word_list = ['levis', 'elvis', 'bat', 'tab', 'tab', 'car', 'ark', 'tabb']
print(find_anagrams(word_list))
```

<br><br>
### Write a letter counting function using parallel lists
* `letters` : list of letters in the input string
* `counts` : parallel list with the counts of each letter
```python
def get_letter_counts(some_str):
    letters = []

    for char in some_str:
        if char not in letters and char != ' ':
            letters.append(char.lower())

    some_str_ = some_str.lower()
    counts = [0] * len(letters)

    for i, char in enumerate(letters):
        
        counts[i] = some_str_.count(char)

    return (letters, counts)

some_str = 'I am a happy string'
results = get_letter_counts(some_str)
print(results)
```

<br><br><br><br>
## operating on strings with `+`
* `'str' + 'ing'`
```python
def concatenate_strings(str1, str2):
    return str1 + ' ' + str2

str1 = 'black'
str2 = 'cat'
print(concatenate_strings(str1, str2))

# print(type(concatenate_strings))
```

<br><br><br><br>
## casting data to a string with `str()`
* there are a number of types that seem like `str`ings but you should double-check
```python
print(str(43.7))
print(type(str(43.7)))
print(str(type(str(43.7))))
print(type(str(type(str(43.7)))))
```

<br><br>
### casting `list` to `str`ing might not do what you expect
```python
print(str(['hey', 'you', 'guys']))
```

<br><br>
### Use `.join()` if you want to combine `list` items into a string
* we use `.join()` **a lot!**, so memorize it
```python
def create_sentence_from_list(some_list):
    # upper-case the first word in the list
    # 'this'[0] #-> 't'
    some_list[0] = some_list[0][0].upper() + some_list[0][1:]
    return ' '.join(some_list) + '.'

test_list = ['this', 'will', 'combine', 'words']
print(create_sentence_from_list(test_list))
```

<br><br><br><br>
## `str`ing slicing
* same as `list`s
```python
print('not all cats hate water'[8:]) #-> 'cats hate water'
print('not all cats hate water'[0:7]) #-> 'not all'
```

<br><br>
### `n_chars()` function
* the need may arise to know every possible occurrence of a sequence of letters of length `n` from some input string
```python
def n_chars(list_of_chars, n=2):
    all_n_chars = []

    for i in range(len(list_of_chars)-n+1):
        if list_of_chars[i:i+n] not in all_n_chars:
            all_n_chars.append(list_of_chars[i:i+n])

    return all_n_chars

char_list = 'oiarsntoienwfeianrstienwfoiarste'
print(n_chars(char_list, n=3))
```

<br><br>
### `slice_at_n()` function
* similarly, we can slice a string every given number of characters
```python
def slice_at_n(list_of_chars, n=2):
    slices_of_n = []

    for i in range(0, len(list_of_chars), n):
        slices_of_n.append(list_of_chars[i:i+n])

    return slices_of_n

char_list = 'oiarsntoienwfeianrstienwfoiarste'
print(slice_at_n(char_list, n=3))
```


<br><br><br><br>
## `str`ing functions to know!

<br><br>
### `list()`
```python
print(list('splits on characters'))
```

<br><br>
### `.split()`
```python
print('split separates on a character'.split(' '))
```

<br><br>
### `.lower()`
```python
print('SoMe StRiNg'.lower())
```

<br><br>
### `.upper()`
```python
python('SoMe StRiNg'.upper())
```

<br><br>
### `.replace()`
```python
print('time tome'.replace('t', 'l'))

# and on substrings
'abclipesnckiwiabcosefnabc'.replace('abc', 'xyz')
```

<br><br><br><br>
## String interpolation with format() and fstrings
```python
length = 3
width = 5
height = 7

print('{}x{}x{}'.format(length, width, height))
print(f'{length}x{width}x{height}')
```

<br><br><br><br><br><br>
# `tuple`s
* are hashable
    * only immutable types can be used as keys in a dict

<br><br><br><br>
## Functions that return multiple items are returning `tuple`s
* use the `get_letter_counts()` function defined above:
```python
results = get_letter_counts(some_str)
print(type(results))

# unpack a tuple:
letters = results[0]
counts  = results[1]
```

<br><br><br><br>
## `tuple`s are immutable
* We can reconstruct them, but we cannot modify them
```python
animal_tup = ('dog', 'cat', 'badger')
# animal_tup[0] = 'plover # this will fail
# instead:
animal_tup = ('plover', animal_tup[1], animal_tup[2])
```

<br><br><br><br>
## Often, we build `tuple`s from lists
```python
tuple_from_list = tuple([3,4,5])
print(tuple_from_list)
```

<br><br><br><br>
## Or, we just declare tuples outright
```python
some_tuple = ('item1', 'item2', 'item3')
```

<br><br>
### Using `in` to construct all possible 3-note chords 
* within an octave of standard western music
* no repeat notes
* notice the use case for `tuple`s, and imagine that we can build a distribution of chord occurrences by analyzing a piece of music, where the chord is a `dict`ionary `key` and the count of occurrences is the `value`
```python
def get_three_note_perms():
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G','G#', 'A', 'A#', 'B']

    chords = []

    for note1 in notes:
        for note2 in notes:
            if note1 == note2:
                continue
            for note3 in notes:
                if note1 != note2 and note1 != note3 and note2 != note3:
                    chords.append(tuple(sorted([note1, note2, note3])))
    return sorted(chords)

print(len(get_three_note_perms()))
print(get_three_note_perms())
```
