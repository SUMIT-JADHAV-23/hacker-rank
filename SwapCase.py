"""You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.
For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
"""

### when we need a swap case there we can use this function
## upper(), lower() casefold() capitalize() and tittle()


#The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

#converts all lowercase characters in a string into uppercase characters and returns it.
text = "lisT Upper"
upper_text = text.upper()
print(upper_text)

#converts all uppercase characters in a string into lowercase characters and returns it.
text1 = "LIST UPPER"
lower_text = text1.lower()
print(lower_text)

#another method casefold() converts all uppercase characters in a string into lowercase characters and returns it
text2 = "Hello My Name Is PETER"
casefolded_text = text2.casefold()
print(casefolded_text)


#capitalize()-converts the first character of a string to uppercase and the rest to lowercase
original_text = "hello My Name Is PETER"
capitalized_text = original_text.capitalize()
print(capitalized_text)

#title()-used to capitalize the first letter of all the words in a string
flexiple = "hello my name is peter"
title_text=flexiple.title()
print(title_text)

"""

def swap_case(s):

    string = ""

    for i in s:

        if i.isupper() == True:

            string+=(i.lower())

        else:

            string+=(i.upper())

    return string


if __name__ == '__main__':

    s = input()

    result = swap_case(s)

    print(result)

"""




#next problem


def solve(s):
    ans = s.split(' ')
    ans1 = (i.capitalize() for i in ans)
    return ' '.join(ans1)

if __name__ == '__main__':
    s = (1, 'w', 2, 'r')
    result = solve(s)
    print(result)




# def solve(s):
#     # Split the input string into a list of words
#     ans = s.split(' ')
#     # Capitalize the first letter of each word
#     ans1 = (i.capitalize() for i in ans)
#     return ' '.join(ans1)

# if __name__ == '__main__':
#     s = input()
#     result = solve(s)
#     print(result)



"""
def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s

if __name__ == '__main__':
    s = input()
    result = solve(s)
"""

"""
def solve(s):
    words = s.split(' ')
    result = ' '.join([word.capitalize() if word.isalpha() else word for word in words])
    return result

if __name__ == '__main__':
    s = input()
    result = solve(s)
"""


# def solve(s):
#     return (" ".join(i.capitalize() for i in s.split(" ")))

# if __name__ == '__main__':
#     s = input()
#     result = solve(s)