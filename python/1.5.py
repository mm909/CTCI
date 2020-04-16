# Page 91
# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale , pie - > false
# pales , pale - > true
# pale , bale - > true
# pale , bake - > false
# Hints: #23, #97, it 130

from string import ascii_lowercase

def oneEditBrute(base, goal):
    if base == goal: return True

    # Remove time(n)
    for char in base:
        if base.replace(char, '') == goal:
            return True

    # Insert time(26n)
    for letter in ascii_lowercase:
        for i in range(len(base)+1):
            if base[:i]+letter+base[i:] == goal:
                return True

    # Replace time(26n)
    for letter in ascii_lowercase:
        for i in range(len(base)):
            if base[:i]+letter+base[i+1:] == goal:
                return True

    return False

print(oneEditBrute('pale', 'pie'))
print(oneEditBrute('pales', 'pale'))
print(oneEditBrute('pale', 'bale'))
print(oneEditBrute('pale', 'bake'))
