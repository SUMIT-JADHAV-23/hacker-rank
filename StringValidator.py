"""Python has built-in string validation methods for basic data. 
It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).
str.isdigit()
This method checks if all the characters of a string are digits (0-9).
str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).
str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).

"""

# #for each char
# if __name__ == '__main__':
#     s = input()
    
# for i in s:
#     if s.isalnum:
#         print (True)
#     else:
#         print(False)

# for i in s:
#     if s.isalpha:
#         print (True)
#     else:
#         print(False)

# for i in s:
#     if s.isdigit:
#         print (True)
#     else:
#         print(False)

# for i in s:
#     if s.islower:
#         print (True)
#     else:
#         print(False)

# for i in s:
#     if s.isupper:
#         print (True)
#     else:
#         print(False)


if __name__ == '__main__':
    s = input()

res = False
for i in s:
    if i.isalnum():
        res = True
        break
print(res)

res = False
for j in s:
    if j.isalpha():
        res = True
        break
print(res)

res = False
for k in s:
    if k.isdigit():
        res = True
        break
print(res)

res = False
for l in s:
    if l.islower():
        res = True
        break
print(res)

res = False
for l in s:
    if l.isupper():
        res = True
        break
print(res)
            


if __name__ == '__main__':
    s = input()

# (i.isalnum() for i in s)
print(any(i.isalnum()for i in s))
print(any(i.isalpha()for i in s))
print(any(i.isdigit()for i in s))
print(any(i.islower()for i in s))
print(any(i.isupper()for i in s))


    