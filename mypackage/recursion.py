def sum_array(array):
    '''Return sum of all items in array'''
    if len(array) == 0:
        return 0
    else:
        return array[-1] + sum_array(array[:-1])

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
    elif n == 0:
        return 1
    else:
        lower_fact = factorial(n-1)
        current_fact = n * lower_fact
        return  current_fact

def reverse(word):
    '''Return word in reverse'''
    if len(word) == 0:
        return word
    else:
        new_word = word[-1]
        return new_word + reverse(word[:-1])
