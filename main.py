# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.

def hello_name():
    user_name = input('Please enter your name: ')
    print('hello_' + user_name + '!')

hello_name()

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for i in range(1, 100, 2):
        print(i)

first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    return max(a_list)

list_1 = [1, 4, 13, 2]
print(max_num_in_list(list_1))


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year():
    print('\nI will check if the year you enter is a leap year.')
    a_year = int(input('What year would you like to check? '))
    if a_year % 400 == 0:
        print(True)
    elif a_year % 100 == 0:
        print(False)
    elif a_year % 4 == 0:
        print(True)
    else:
        print(False)

is_leap_year()
    

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type.

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

newlist = [1,2,3,4,5]
badList = [2,5,5,7]
print(is_consecutive(newlist))
print(is_consecutive(badList))