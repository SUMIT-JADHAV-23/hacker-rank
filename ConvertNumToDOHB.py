"""
Given an integer, , print the following values for each integer i from n to :
Decimal
Octal
Hexadecimal (capitalized)
Binary
Function Description
Complete the print_formatted function in the editor below.
print_formatted has the following parameters:
int number: the maximum value to print
Prints
The four values must be printed on a single line in the order specified above for each i from 1 to num.
Each value should be space-padded to match the width of the binary value of num and 
the values should be separated by a single space.
Input Format
A single integer denoting .
"""
#for int number
# def formated(num):
#     for i in range(1,num+1):
#         deci=str(i)
#         print(deci)
# if __name__=='__main__':
#     n=int(input())
#     print(formated(n))

#for Octal number
# def formated(num):
#     octal=set()
#     for i in range(1,num+1):
#         octa = oct(i)[2:]
#         octal.add(octa)
#     return octal
# if __name__=='__main__':
#     n=int(input())
#     print(formated(n))

"""def formated(num):
    for i in range(1, num + 1):
        #[2:] use for the 'O012' it returns '12'
        octa = oct(i)[2:]
        print(octa)

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    formated(n)
"""
#for hexa Number hex( ) function used
# def formated(num):
#     for i in range(1, num + 1):
#         #[2:] use for the 'O012' it returns '12'
#         hexa = hex(i)[2:].upper()
#         print(hexa)

# if __name__ == '__main__':
#     n = int(input("Enter a number: "))
#     formated(n)



#for Binary number bin() function used
"""    
def formated(num):
    for i in range(1, num + 1):
        #[2:] use for the 'O012' it returns '12'
        bina=bin(i)[2:]
        print(bina)

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    formated(n)"""

#now print side by side using rjust,ljust
#Each value should be space-padded to match the width of the binary value
# def print_formatted(number):
#     width = len(bin(number)[2:])
#     for i in range(1, number+1):
#         deci = str(i)
#         octa = oct(i)[2:]
#         hexa = hex(i)[2:].upper()
#         bina= bin(i)[2:]
#         print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))
#     # your code goes here

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)

"""


def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)"""


#without using function convert decimal to binary

# def binary_num(number):
#     if number >=1:
#         binary_num(number//2)
#     print(number % 2,end='')

# if __name__=='__main__':

#     n=int(input())

#     print(binary_num(n))


"""def binary_num(number):
    if number >= 1:
        binary_num(number // 2)
    print(number % 2, end='')

if __name__ == '__main__':
    n = int(input())
    #in last because of print function it gives None 
    binary_num(n)"""

n=int(input("Enter a number: "))
a=[]
while(n>0):
    dig=n%2
    a.append(dig)
    n=n//2
a.reverse()
print("Binary Equivalent is: ")
for i in a:
    print(i,end=" ")