'''
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def divisible_by_under(limit, divs):
    return (i for i in  range(limit) if any(i % div == 0 for div in divs))
print(sum(divisible_by_under(1000, (3,5))))
