# Page 90, 1.1
# Is Unique:
#   Implement an algorithm to determine if a string has all unique characters.
#   What if you cannot use additional data structures?
# Hints: 44 117 132
from imports.quicksort import *
from imports.heapsort import *

class stringCheck:

    # Brute Force
    # Time : n^2
    # Space: constant
    def isUnique1(str):
        for i, char1 in enumerate(str):
            for j, char2 in enumerate(str):
                if char1 == char2 and i != j:
                    return False
        return True

    # With hash
    # Time : n
    # Space: 26
    def isUnique2(str):
        if(len(str) > 26):
            return False
        hash = {}
        for char in str:
            if char in hash:
                return False
            else:
                hash[char] = 1
        return True

    # Sorting
    # Time: nLog(n)
    # Space: constant
    def isUnique3(str):
        str = heapsort(str)
        for i, char in enumerate(str[:-1]):
            if char == str[i+1]:
                return False
        return True

print(stringCheck.isUnique1("ASDF"))
print(stringCheck.isUnique1("ADAF"))
print(stringCheck.isUnique2("ASDF"))
print(stringCheck.isUnique2("ADAF"))
print(stringCheck.isUnique3("ASDF"))
print(stringCheck.isUnique3("ADAF"))
