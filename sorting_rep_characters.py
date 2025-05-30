#  Given a string, sort it in decreasing order based on the frequency of characters. If there are multiple possible solutions, return any of them.

# For example, given the string tweet, return tteew. eettw would also be acceptable.


strings = ["tweet", "success", "balloon", "committee"]

## 1ST VERSION
#  time complexity: O(n2) given the nested count() in the for loop
def sort_rep_char(string):
    indiv_char = list(set(string))
    sorted_repetitions = sorted([char*(string.count(char)) for char in indiv_char], key=len, reverse=True)

    return "".join(sorted_repetitions)


## OTHER VERSION
# time complexity: O(n log(n)) because of sorted()
# space complexity: O(n)

def sort_repeated_characters(s):
    frequency_map = {}
    for c in s:
        if frequency_map.get(c) != None:
            frequency_map[c] += 1
        else:
            frequency_map[c] = 1

    sorted_by_frequecy = sorted(frequency_map.items(), key=lambda item:item[1], reverse=True)
    return "".join([item[0]*item[1] for item in sorted_by_frequecy])


## TEST 

for string in strings:

    # sort_rep_char(string)
    print(sort_repeated_characters(string))
