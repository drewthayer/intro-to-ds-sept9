# create, analyze and modify strings


# strings are like immutable lists

# def iterate_through_str(some_str):
#     for i, char in enumerate(some_str):
#         print(i, char)
#     # some_str_lst = list(some_str)
#     # for char in some_str_lst:
#     #     print(char)

test_str = 'We need to pass something in this function'
# test_str[0] = 'w'


# iterate_through_str(test_str)




# commonly declare strings using the syntax string = 'some text here
# utilize the three types of string bounding characters
# 'some text' : most widely used
# some_string = 'with "single" \'quotes\''
# print(some_string)

# some_string = "with 'double' \"quotes\""
# print(some_string)

# some_string = '''with single quotes
# some more text
# '''

# print(some_string)

# some_string = """with single quotes"""

# "more text" : also used, less often
# ''' multi-line strings''' : used when \n is to be implicitly stated, through 
#  a simple carriage return
# used in function Docstrings

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


# print(count_unique_chars_in_str(test_str))


# in operator
# print('a' in 'plant')
# print(4 in [1,4,7,8,2,4,6,4])

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
# print(find_anagrams(word_list))



# can be used for multi-line comments
# can also be """ like this """
# operating on strings with +
# 'str' + 'ing'
def concatenate_strings(str1, str2):
    return str1 + ' ' + str2

str1 = 'black'
str2 = 'cat'
# print(concatenate_strings(str1, str2))




# casting data to a string with str()
# print(type(str(type(str(43.7)))))
# print(type(concatenate_strings))

# str(['hey', 'you', 'guys']) : might not do what you expect it do do
# print(str(['hey', 'you', 'guys']))

# if you want to combine characters in a string, use 


def create_sentence_from_list(some_list):
    some_list[0] = some_list[0][0].upper() + some_list[0][1:]
    return ' '.join(some_list) + '.'

# 'this'[0] #-> 't'
test_list = ['this', 'will', 'combine', 'words']
# print(create_sentence_from_list(test_list))

# str slicing
print('not all cats hate water'[8:]) #-> 'cats hate water'
print('not all cats hate water'[0:7]) #-> 'not all'


# using for loops to iterate through strings:
# for char in 'some_string': print(char)
# str indexing
# 'some_str'[0] #--> 's'
# 'some string'[0] = 'f' will throw an error








# Write a function that returns 2 parallel lists, based on counts of letters in an input string:
# letters : list of letters in the input string
# counts : parallel list with the counts of each letter
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

# tuples
some_str = 'I am a happy string'

results = get_letter_counts(some_str)

letters = results[0]
counts  = results[1]

# print(results)

animal_tup = ('dog', 'cat', 'badger')
animal_tup = ('plover', animal_tup[1], animal_tup[2])

# hashable
# only immutable types can be used as keys in a dict

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









# Membership in strings
# similar to lists
# 'club' in 'very important club' #-> True
# Important string functions and methods
# len('some string')
# list('splits characters')
# 'split separates on a character'.split(' ')
# 'SoMe StRiNg'.lower()
# 'SoMe StRiNg'.upper()
# 'time tome'.replace('t', 'l')
# String interpolation with format() and fstrings
# '{}x{}x{}'.format(length, width, height)
# f'{length}x{width}x{height}'
# more on formatting for rounding and justification
# Write the is_palindrome() function
# Write the is_anagram() function
# Create and use tuples
# tuples are like immutable lists
# access elements in the tuple using our common indexing approach
# tuple values cannot be changed!
# some_tuple = ('item1', 'item2', 'item3')
# tuple_from_list = tuple([3,4,5])
# functions that return multiple values return tuples!!
# def generic_func(): return 25, 17
# type(generic_func()) #--> tuple
# unpack tuples:
# var1, var2, var3 = (1, 2, 3)
# why tuples?