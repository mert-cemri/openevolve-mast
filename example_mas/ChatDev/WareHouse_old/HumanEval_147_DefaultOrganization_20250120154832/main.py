'''
This module contains the implementation of the function get_max_triples which calculates
the number of triples (a[i], a[j], a[k]) from an array a where i < j < k and the sum
a[i] + a[j] + a[k] is a multiple of 3.
'''
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
    For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
    Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.
    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    # Generate the array a
    a = [i * i - i + 1 for i in range(1, n + 1)]
    # Initialize the count of valid triples
    count = 0
    # Iterate over all possible triples (i, j, k)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Check if the sum of the triple is a multiple of 3
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count