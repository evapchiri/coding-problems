# Write a function that takes a natural number as input and returns the number of digits the input has.
# Constraint: don't use any loops.


def num_of_digits(num: int):

    return len(str(num))


tests = {2: 1, 23: 2, 453: 3, 72845: 5, 9456237825: 10}

# for number in tests:
#     result = num_of_digits(number)
#     assert result == tests[number]
#     print(result)


# SPACE-TIME complexity analysis

# Time complexity is O(n) where (n) is  the number of digits of 'num'. This is due to str() needing to process each digit from 'num' - len will however retrieve the stored lenght value.
# Space complexity is also O(n), again n being the number of digits, as str() stores the string in memory and this string will increase linearly with the more digits 'num' has.


## O(1) version!!
import math


def count_digits(num):
    return math.floor(math.log10(num)) + 1


for test in tests:
    got = count_digits(test)
    want = tests[test]
    print(f"I got {got} and I wanted {want}")
    assert got == want
