
haystack = input()
needle = input()

haystack *= 2

#print("Yes" if haystack.count(needle) > 0 else "No")
print("Yes" if needle in haystack else "No")