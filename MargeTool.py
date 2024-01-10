"""
Consider the following:
A string S,of length N.
An integer,K , where K is a factor of N.

We can split S into N/K substrings where each subtring ti,
consists of a contiguous block of K characters in S.
Then, ti use each to create string ui such that:
The characters in ui  are a subsequence of the characters in ti.
Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once.

Given S and K , print N/K lines where each line i denotes string ui. 

Example
string="AABBCADDE"
k=3
There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'.
The first substring is all 'A' characters, so u1="A". 
The second substring has all distinct characters, so u2="BCA".
The third substring has  different characters, so u3="DE".
Note that a subsequence maintains the original order of characters encountered. 
The order of characters in each subsequence shown is important.

Function Description
Complete the merge_the_tools function in the editor below.
merge_the_tools has the following parameters:

string s: the string to analyze
int k: the size of substrings to analyze
Prints

Print each subsequence on a new line. There will be N/K  of them. No return value is expected.

Input Format
The first line contains a single string, .
The second line contains an integer, , the length of each substring.

"""


"""string="AABBCADDE"
k=3

def merge_tools(string,k):
    n=len(string)
    sub_string_len=int(n/k)
    # print(sub_string_len)
    l1=[]
    for i in range(0,len(string),k):
        if(string[i:i+k]):      
            l1.append(string[i:i+k])
        print(l1)
    return l1
        
resilt=merge_tools(string,k)
print(resilt)

"""
"""
string = "ABCDEFGH"
k = 2

#range(0,len(string),k)-start from 0 to upto len of string and step size k
for i in range(0, len(string), k):
    print(i, string[i:i + k])
"""

# string = "AABBCADDE"
# k = 3

# def merge_tools(string, k):
#     n = len(string)
#     sub_string_len = int(n / k)
#     l1 = []
#     for i in range(0, n, k):
#         if (string[i:i + k]):
#             l1.append(string[i:i + k])
#     return l1

# result = merge_tools(string, k)
# print(result)


# string = "AABBCADDE"
# k = 3

# def merge_tools(string, k):
#     n = len(string)
#     sub_string_len = int(n / k)
#     result = []
#     for i in range(0, n, sub_string_len):
#         if string[i:i + sub_string_len]:
#             result.append(string[i:i + sub_string_len])
#     return result

# result = merge_tools(string, k)
# for substring in result:
#     print(substring)

"""string="AABBCADDE"
k=3

def merge_tools(string,k):
    n=len(string)
    sub_string_len=int(n/k)
    # print(sub_string_len)
    l1=[]
    l2=[]
    for i in range(0,len(string),k):
        if(string[i:i+k]):      
            l1.append(string[i:i+k])
            print(l1)
        for char in l1:
            if char in l1:
                    pass
            else:
                    l2.append(char)
            print(l2)
                    
result=merge_tools(string,k)
print(result)"""



string="AABBCADDE"
k=3

def merge_tools(string,k):
    n=len(string)
    sub_string_len=int(n/k)
    # print(sub_string_len)
    l1=[]
    for i in range(0,len(string),k):
        if(string[i:i+k]):      
            l1.append(string[i:i+k])
            # print(l1)
    l2=[]
    for j in l1:
        character_set=set()
        chars=''
        for char in j:
            if char not in character_set:
                character_set.add(char)
                # print(character_set)
                chars += char
                # print(chars)
        l2.append(chars)
    return l2
                    
result=merge_tools(string,k)
for substring in result:
    print(substring)



# l1 = ['AAB', 'BCA', 'DDE']

# def remove_duplicates_from_strings(lst):
#     result = []
#     for s in lst:
#         unique_chars = set()
#         unique_string = ''
#         for char in s:
#             if char not in unique_chars:
#                 unique_chars.add(char)
#                 unique_string += char
#         result.append(unique_string)
#     return result

# result = remove_duplicates_from_strings(l1)
# print(result)


# list_no_dupl = []
#             for item in list_till_k:
#                 if item in list_no_dupl:
#                     pass
#                 else:
#                     list_no_dupl.append(item)
#             print(''.join(list_no_dupl))


# def fix(string):
#     s = set()
#     list = []
#     for ch in string:
#         if ch not in s:
#             s.add(ch)
#             list.append(ch)
    
#     return ''.join(list)        

# string = "Protiijaayiiii"
# print(fix(string))


# string = "geeksforgeeks"
# p = ""
# for char in string:
#     if char not in p:
#         p = p+char
# print(p)
# k = list("geeksforgeeks")


"""
from textwrap import wrap
def merge_the_tools(string, k):
    string_word = string
    string_len = len(string_word)
    parts = k
    interval = int(string_len/parts)
    list_of_string_word = wrap(string_word,parts)
    #print(list_of_string_word)
    new_list = []
    p =''
    for i in list_of_string_word:
        for char in i:
            if char not in p:
                p= p + char
        new_list.append(p)
        p = ''

    #printing the list
    for i in new_list:
        print(i)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

-----------------

import textwrap
def merge_the_tools(string, k):
    list1 = textwrap.wrap(string, k)
    for a in list1:
        u = ""
        for n in range(k):
            if a[n] not in u:
                u += a[n]
        print(u)



--------------------

def merge_the_tools(string, k):
    j=k
    result=''
    for i in range(0,len(string),k):
        tmp=''
        for l in string[i: j]:
            if l not in tmp:
                tmp+=l
        if j==k:
            result+=tmp
            j+=k
        else:
            result+=('\n'+tmp)
            j+=k
    print(result)

------------------------------------
def merge_the_tools(string, k):
    list1 = []
    for i in range(len(string)):
        list1.append(string[i])
    for j in range(len(list1)) :
        if (j+1) % k == 0:
            x = int((j+1) / k)
            list_till_k = list1[(k*(x-1)):(k*x)]
            list_no_dupl = []
            for item in list_till_k:
                if item in list_no_dupl:
                    pass
                else:
                    list_no_dupl.append(item)
            print(''.join(list_no_dupl))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)"""