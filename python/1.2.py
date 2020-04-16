#1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
#other.

def checkPerm(str1, str2):
    if len(str1) != len(str2): return False
    checksum = 0
    for char1, char2 in zip(str1, str2):
        checksum = checksum ^ ord(char1) ^ ord(char2)
    return not checksum

print(checkPerm('Mikian', 'Mikiak'))
print(checkPerm('Mikian', 'Mikina'))
