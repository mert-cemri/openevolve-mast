'''
Given a positive integer n, you have to make a pile of n levels of stones.
The first level has n stones.
The number of stones in the next level is:
    - the next odd number if n is odd.
    - the next even number if n is even.
Return the number of stones in each level in a list, where element at index
i represents the number of stones in the level (i+1).
Examples:
>>> make_a_pile(3)
[3, 5, 7]
'''
def make_a_pile(n):
    stones = [n]
    for _ in range(1, n):
        stones.append(stones[-1] + 2)
    return stones
# Example usage
if __name__ == "__main__":
    print(make_a_pile(3))  # Output: [3, 5, 7]