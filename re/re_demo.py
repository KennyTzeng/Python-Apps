import re

test_str = "11tem22ple"
pattern = "[a-z]+"
pat = re.compile(pattern)

print("the pattern is '{}' and the testing string is '{}'".format(pattern, test_str))
print("the result of match() is : ", end = "")
m = pat.match(test_str)
if m:
    print(m.group())
else:
    print()

print("the result of search() is : ", end = "")
s = pat.search(test_str)
if s:
    print(s.group())
else:
    print()

print("the result of findall() is : ", end = "")
f = pat.findall(test_str)
for str in f:
    print(str, end = " ")

print()


'''
the pattern is '[a-z]+' and the testing string is '11tem22ple'
the result of match() is :
the result of search() is : tem
the result of findall() is : tem ple
'''