'''
Return True if all numbers in the list l are below threshold t.
'''
def below_threshold(l: list, t: int):
    return all(x < t for x in l)