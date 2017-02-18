"""Source:
    The hacker guide to python
    """
#Generators allow to handle large data set with less memory loads
#yield is used - a stack reference is kept to resume letter when yield  reached
#yield's less commonly used feature is a value to a generator can be passed
#using generator's send() method to the yield (as it retuns value like function)

def shorten(string_list):
    length = len(string_list[0])
    for s in string_list:
        length = yield s[:length]

mystringlist = ['loremipsum', 'dolorsit', 'ametfoobar']
shortstringlist = shorten(mystringlist)
result = []
try:
    s = next(shortstringlist)
    result.append(s)
    while True:
        number_of_vowels = len(filter(lambda letter: letter in 'aeiou', s))
        s = shortstringlist.send(number_of_vowels)
        result.append(s)
except StopIteration:
    pass

print result
"""prints ['loremipsum', 'dolo', 'am'] as 4 and 2 is passed as no of vowels
in yield s[:length] - for length value
"""
