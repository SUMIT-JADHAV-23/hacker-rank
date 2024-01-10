"""
You are given an integer,N. Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)
The center of the rangoli has the first alphabet letter a,
and the boundary has the N alphabet letter (in alphabetical order).
Function Description
Complete the rangoli function in the editor below.
rangoli has the following parameters:
int size: the size of the rangoli
Returns
string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
Input Format
Only one line of input containing size, the size of the rangoli.
"""

#first generate middle line create
# def print_rangoli(size):
#     l1 ="abcdefghijklmnopqrstuvwxyz"
#     #list=map(chr,range(91,123))
#     x=l1[n-1: :-1]+l1[1:n]
#     width =('-'.join(x))
#     print(width)
# if __name__=='__main__':
#     n=int(input())
#     print_rangoli(n)


#first generate middle line create
# def print_rangoli(size):
#     l1 ="abcdefghijklmnopqrstuvwxyz"
#     #list=map(chr,range(91,123))
#     x=l1[n-1: :-1]+l1[1:n]
#     print(x)
#     print('-'.join(x))

# if __name__=='__main__':
#     n=int(input())
#     print_rangoli(n)


# #create upper part
# def print_rangoli(size):
#     l1 ="abcdefghijklmnopqrstuvwxyz"
#     #list=map(chr,range(91,123))
#     for i in range(size):
#         x=l1[n-1:n-i:-1]+l1[n-i:n]
#         # print(x)
#         print(('-'.join(x)))

# if __name__=='__main__':
#     n=int(input())
#     print_rangoli(n)



# def print_rangoli(size):
#     l1 ="abcdefghijklmnopqrstuvwxyz"
#     #list=map(chr,range(91,123))
#     x=l1[n-1: :-1]+l1[1:n]
#     width = len('-'.join(x))
#     for i in range(1,size):
#         #use of center function 
#         x=('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(width,'-'))
#         print(x)
        

# if __name__=='__main__':
#     n=int(input())
#     print_rangoli(n)




def print_rangoli(size):
    l1 ="abcdefghijklmnopqrstuvwxyz"
    #list=map(chr,range(91,123))
    x=l1[n-1: :-1]+l1[1:n]
    width = len('-'.join(x))
    #for upper part
    for i in range(1,size):
        #use of center function 
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(width,'-'))
    #for lower part
    for i in range(n,0,-1):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(width,'-'))

        

if __name__=='__main__':
    n=int(input())
    print_rangoli(n)



"""
def print_rangoli(size):
    # your code goes here
    alpha = "abcdefghijklmnopqrstuvwxyz"
    data = [alpha[i] for i in range(size)]
    items = list(range(size))
    items = items[:-1]+items[::-1]
    for i in items:
        temp = data[-(i+1):]
        row = temp[::-1]+temp[1:]
        print("-".join(row).center(n*4-3, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

"""

# #solution
# a = "abcdefghijklmnopqrstuvwxyz"
# def print_rangoli(size):
    
#     lines = []
#     for row in range(size):
#         print_ = "-".join(a[row:size])
#         lines.append(print_[::-1] + print_[1:])
#     width = len(lines[0])
    
#     for row in range(size-1, 0, -1):
#         print(lines[row].center(width, '-'))
        
#     for row in range(size):
#         print(lines[row].center(width, '-'))
#     # your code goes here

# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


# #solution

# def print_rangoli(size):
#     # your code goes here
#     import string
#     design = string.ascii_lowercase

#     L = []
#     for i in range(n):
#         s = "-".join(design[i:n])
#         L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
#     print('\n'.join(L[:0:-1]+L))


# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)



    
def print_rangoli(size):
    l1 ="0123456789"
    #list=map(chr,range(91,123))
    x=l1[n-1: :-1]+l1[1:n]
    width = len('-'.join(x))
    #for upper part
    for i in range(1,size):
        #use of center function 
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(width,'-'))
    #for lower part
    for i in range(n,0,-1):
        print('-'.join(l1[n-1:n-i:-1]+l1[n-i:n]).center(width,'-'))

        


if __name__=='__main__':
    n=int(input())
    print_rangoli(n)





# n, m = map(int,input().split())
# for i in range(n//2):
#     j = int((2*i)+1)
#     print(('.|.'*j).center(m, '-'))
# print('WELCOME'.center(m,'-'))
# for i in reversed(range(n//2)):
#     j = int((2*i)+1)
#     print(('.|.'*j).center(m, '-'))