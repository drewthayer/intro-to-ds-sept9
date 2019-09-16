# write loops to solve numeric problems
# describe simple accumulators and the roles they play in loopage

# for loops using the range() function
# # int accumulators
# x = 0

# for i in range(20):
#     x += i
#     print(x)
# print(x)


# # float accumulators
# x2 = 1.0

# for i in range(1,20):
#     x2 /= i
#     print(x2)
# print(x2)

# ## mention underflow


# # bool "accumulators", aka "Flags"

# exit_condition = True
# x3 = 1.

# for i in range(1,20):
#     x3 *= i
#     print(x3)

#     if x3 > 10000:
#         exit_condition = False

#     if exit_condition == False:
#         break # exit current loop level

# print(x3)

# # Loop Levels : 4
# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             for l in range(2):
#                 print(i,j,k,l)

# for hrs in range(24):
#     for minutes in range(60):
#         for secs in range(60):
#             print(f'{hrs}:{minutes}:{secs}')

# image = [
#         [255,0,0,0,0,0],
#         [0,255,0,0,0,0],
#         [0,0,255,0,0,0],
#         [0,0,0,255,0,0],
#         [0,0,0,0,255,0]
#         [0,0,0,0,0,255]
#         ]

# for row in image:
#     # print(row)
#     for val in row:
#         print(val)


# # list accumulators, or "collectors"
# accum = []

# for i in range(30, 60):
#     if i % 3 == 0:
#         accum.append(i)

# print(accum)



# # for loops that traverse items in a list
# list_of_names = ['bob', 'cathy', 'george', 'dino', 'tom']

# long_names = []

# for name in list_of_names:
#     if len(name) > 4:
#         long_names.append(name)

# print(long_names)



# display values in a list

# mixed_list = ['word', [1,2,3,4,5], 43, 90.0]
# unpacked_list = []

# for item in mixed_list:
    
#     if type(item) == list:
#         for nested in item:
#             unpacked_list.append(nested)
#     else:
#         unpacked_list.append(item)

# print(unpacked_list)


# # access and mutate values in a list
# animal_list = ['dog', 'cat', 'dolphin', 'bear', 'eagle']

# for i, animal in enumerate(animal_list):
#     if animal[0] == 'd':
#         animal_list[i] = 'ant'

# print(animal_list)


# animal_list = ['dog', 'cat', 'dolphin', 'bear', 'eagle']

# for i in range(len(animal_list)):
#     if animal_list[i][0] == 'd':
#         animal_list[i] = 'ant'

# print(animal_list)



# accumulate from list values
# into an int or float



# filtering into another list



# # creating parallel lists

# list_of_names   = ['bob', 'tom', 'don', 'larry']
# list_of_heights = [72   ,  68  ,  63  ,   76   ]
# how_many_cats   = [3, 1, 2, 23]

# for i, name in enumerate(list_of_names):
#     print('{} is {} inches tall'.format(name, list_of_heights[i]))
#     print('   he has {} cats'.format(how_many_cats[i]))



# for loops that traverse items in parallel lists
# nested for loops


# while loops using a conditional check
# infinite 
# def get_menu_item():
#     menu = '''Choose an item:
#             (1) broccoli
#             (2) carrots
#             (3) cabbage
#            '''

#     choice = int(input(menu))
#     items = ['broccoli', 'carrots', 'cabbage']
#     return items[choice-1]

# # print(get_menu_item())
# orders = []

# # order_max = 7
# cont = 'y'
# while cont == 'y':
#     orders.append(get_menu_item())

#     # order_max -= 1
#     cont = input('order more? ')

# print(orders)



# for solving "open-ended" problems
# for delivering menus
# using break, continue or pass when appropriate
# break to avoid or exit infinite loops when using while
# break to exit a for or while loop when further computation is no longer necessary
# continue to conditionally skip an operation
# pass as a placeholder in an unfinished function

# list comprehensions, a brief introduction
# [i for i in some_list]
# create functions that execute common mathematical operations
# write the factorial() function

def factorial(k):
    result = 1
    while k > 0:
        result = result * k
        k -= 1
    return result

print(factorial(5))

def factorial(k):
    result = 1

    for i in range(k+1):
        if i == 0:
            continue    
        result = result * i    

    return result

print(factorial(5))


def factorial(k):
    result = 1

    for i in range(1,k+1):  
        result = result * i    

    return result

print(factorial(5))


# write the is_prime() function

def is_prime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num/2), 2):
            if num % i == 0:
                return False

    return True
    
primes = []
for i in range(2, 100):
    if is_prime(i):
        primes.append(i)

print(primes)



# write the get_anagrams() function
# write the poisson_pmf() function