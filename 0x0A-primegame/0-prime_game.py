#!/usr/bin/python3
"""ALX SE Prime Game"""


def prime_nums_in_range(start, end):
    """Finds and returns all the prime numbers in a range"""
    prime_numbers = []

    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)

    return prime_numbers


def isWinner(x, nums):
    """Returns the name of the winner that won the most rounds"""
    maria, ben = 0, 0
    for i in range(x):
        result = prime_nums_in_range(1, nums[i])
        if len(result) % 2:
            maria += 1
        else:
            ben += 1
    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    else:
        return None
