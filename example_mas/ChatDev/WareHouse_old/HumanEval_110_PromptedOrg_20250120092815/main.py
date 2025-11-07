'''
This module contains the implementation of the exchange function which determines
if it is possible to exchange elements between two lists to make the first list
contain only even numbers.
'''
def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    # Check if there are any odd numbers in lst1
    has_odd_in_lst1 = any(x % 2 != 0 for x in lst1)
    # Check if there are any even numbers in lst2
    has_even_in_lst2 = any(x % 2 == 0 for x in lst2)
    # If lst1 has no odd numbers, it's already all even
    if not has_odd_in_lst1:
        return "YES"
    # If lst2 has no even numbers, we cannot make lst1 all even
    if not has_even_in_lst2:
        return "NO"
    # If lst1 has odd numbers and lst2 has even numbers, exchange is possible
    return "YES"