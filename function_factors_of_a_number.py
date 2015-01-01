#!/usr/bin/python
# TL;DR: Return the factors of the entered number.
# GOAL: Define a function that creates a list of all the numbers that are factors of the user's number. For example, if the function is called factor, factor(36) should return [1,2,3,4,6,9,12,18,36]. The numbers in your list should be from least to greatest, and 1 and the original number should be included.

error = 'Only integers > 1 are allowed.'

def factor(num):
    print num
    if num > 1:
        start = 3
        if is_even(num):
            start = 2
        for i in range(start, num):
            if num % i == 0: result_list.append(i)
        result_list.append(1)
        result_list.append(num)
        return sorted(result_list[:])
    else:
        print error 

def is_even(x):
    return x % 2 == 0

def flow():
    try:
        num_factor = factor(int(raw_input('Enter a number above 1 to have its factor: ')))
        if num_factor != None: print num_factor
    except:
        print error

if __name__ == '__main__':
    result_list = []
    flow()