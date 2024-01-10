"""
In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.
"NOTE": String letters are case-sensitive.
Input Format
The first line of input contains the original string. The next line contains the substring.
Constraints
Each character in the string is an ascii character.
Output Format
Output the integer number indicating the total number of occurrences of the substring in the original string.
"""

# s = 'arunununghhjj'
# sb = 'nun'
# results = 0
# sub_len = len(sb)
# for i in range(len(s)):
#     print(i)
#     if s[i:i+sub_len] == sb:
#         results += 1
# print (results)




def count_substring(string, sub_string):
    count=0
    len1=len(sub_string)
    for i in range(0,len(string)):
        if string[i:i+len1]== sub_string:
            count += 1      
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)





# def count_substring(string,sub_string):
#     count=0
#     for i in range(len(string)-len(sub_string)+1):
#         if(string[i:i+len(sub_string)] == sub_string ):      
#             count+=1
#     return count  



# def count_substring(string, sub_string):
#     total = 0
#     for i in range(len(string)):
#         if string[i:len(string)].startswith(sub_string):
#             total += 1
#     return total

# s = 'arunununghhjj'
# sb = 'nun'
# results = 0
# sub_len = len(sb)
# for i in range(len(s)):
#     if s[i:i+sub_len].startswith(sb):
#         results += 1
# print (results)


print(sum("GCAAAAAGH"[i:].startswith("AAA") for i in range(len("GCAAAAAGH"))))


# return(sum(string[i:].startswith(sub_string)for i in range(len(string))))