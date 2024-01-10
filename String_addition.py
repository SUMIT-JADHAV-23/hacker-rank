"""You are given the firstname and lastname of a person on two different lines. 
Your task is to read them and print
("Hello firstname lastname! You just delved into python.")
Function Description-
Complete the print_full_name function in the editor below.

print_full_name has the following parameters:
string first: the first name
string last: the last name
Prints-
string: 'Hello (firt_name,last_name) ! You just delved into python'
where first_name and last_name  are replaced with first and last.
Input Format

The first line contains the first name, and the second line contains the last name.
"""


# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

"""
if __name__ == '__main__':
    first_name = input()
    last_name = input()
print(first_name)
print(last_name)

"""

"""
def print_full_name(first, last):
    # Write your code here
    print(f'Hello {first,last}! You just delved into python')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

"""

# def print_full_name(first, last):
#     # Write your code here
#     print(f'Hello +first+last+! You just delved into python')

# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

def print_full_name(first, last):
    # Write your code here
    print("Hello " + first, last + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

        
# print("Hello " + first, last + "! You just delved into python.")
# print("Hello "+(first)+" "+(last)+"! You just delved into python")
# print("Hello "+(first),(last)+"! You just delved into python")
# print(f'Hello +first+last+! You just delved into python')
# print(f'Hello {first,last}! You just delved into python')