def sum_array(array):
    '''Return sum of all items in array'''

def fibonacci(n):
    '''Return nth term in fibonacci sequence'''
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
    '''Return n!'''
    if n == 1:
        return n
    else:
        lower_fact = factorial(n-1)
        current_fact = n * lower_fact
        return  current_fact

def reverse(word):
    '''Return word in reverse'''
