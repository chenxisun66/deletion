# Find number of times a string occurs as a subsequence in given string
def count(a,b,m,n):
    # if both strings are empty/second string is empty, return 1
    if ((m == 0 and n == 0) or n == 0):
        return 1
    # If only first string is empty and second string is not empty, return 0
    if (m == 0):
        return 0

    # If last characters are same
    # Recur for remaining strings by
    # 1. considering last characters of both strings
    # 2. ignoring last character of first string
    if (a[m - 1] == b[n - 1]):
        return count(a, b, m - 1, n - 1) + count(a, b, m - 1, n)
    else:
        # If last characters are different, ignore
        # last char of first string and recur for
        # remaining string
        return count(a, b, m - 1, n)

# examples
substr = "0101"
fullstr  = "01010101"
fullstr1 = "00101011"
fullstr2 = "00101101"
fullstr3 = "01100101"
fullstr4  = "00110101"
fullstr5  = "00110011"

'''print(count(fullstr,substr, len(fullstr), len(substr)))
print(count(fullstr1,substr, len(fullstr1), len(substr)))
print(count(fullstr2,substr, len(fullstr1), len(substr)))
print(count(fullstr3,substr, len(fullstr1), len(substr)))
print(count(fullstr4,substr, len(fullstr1), len(substr)))
print(count(fullstr5,substr, len(fullstr1), len(substr)))'''
