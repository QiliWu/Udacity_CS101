# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.

# replace splitlist-characters(characters in splitlist string) in source string with splitlist[0]
def character_replace(source, splitlist):
    i = 1
    while i < len(splitlist):
        while source.find(splitlist[i]) != -1:
            source = source[:source.find(splitlist[i])] + splitlist[0] + source[source.find(splitlist[i]) + 1:]
        i = i + 1
    return source


def split_string(source, splitlist):
    # split the new source string(character_replace(source,splitlist)) with splitlist[0]
    list = character_replace(source, splitlist).split(splitlist[0])
    # delete the '' element in list
    for e in list:
        if e == '':
            list = list[:list.index('')] + list[list.index('') + 1:]
    return list


out = split_string("This is a test-of the,string separation-code!", " ,!-")
print out
# >>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
# >>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code", ",")
print out
# >>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
























