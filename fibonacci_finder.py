#!/usr/bin/python
# GOAL: Define a function that allows the user to find the value of the nth term in the sequence. To make sure you've written your function correctly, test the first 10 numbers of the sequence. Remember, the 0th term is 0 and the first and second term are both 1.

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