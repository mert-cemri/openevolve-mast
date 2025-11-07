'''
Find how many times a given substring can be found in the original string. Count overlapping cases.
>>> how_many_times('', 'a')
0
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
'''
def how_many_times(string: str, substring: str) -> int:
    count = start = 0
    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += 1  # Move start index by one to count overlapping
    return count