'''
This script defines a function `get_max_triples(n)` that calculates the number of triples (a[i], a[j], a[k]) in an array `a` of length `n` where i < j < k, and the sum a[i] + a[j] + a[k] is a multiple of 3.
'''
def get_max_triples(n):
    # Step 1: Generate the array a
    a = [i * i - i + 1 for i in range(1, n + 1)]
    # Step 2: Initialize the count of valid triples
    count = 0
    # Step 3: Iterate through all possible triples (i, j, k)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Check if the sum of the triple is a multiple of 3
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    # Step 4: Return the count of valid triples
    return count
# Example usage
if __name__ == "__main__":
    print(get_max_triples(5))  # Output should be 1