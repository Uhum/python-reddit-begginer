#!/usr/bin/python
# GOAL: Define a function that allows the user to find the value of the nth term in the sequence. To make sure you've written your function correctly, test the first 10 numbers of the sequence. Remember, the 0th term is 0 and the first and second term are both 1.

def get_fibonacci(num):
    fibonacci_array = const_start
    for i in range(1, num):
        i_num = fibonacci_array[i] + fibonacci_array[(i-1)]
        const_start.append(i_num)
    return fibonacci_array[-1]

def flow():
    try:
        user_input = int(raw_input('Enter the nth fibonacci number to be calculated: '))
        print get_fibonacci(user_input)
    except:
        print error

if __name__ == '__main__':
    const_start = [0, 1]
    error = 'Must be integer > 1'
    flow()