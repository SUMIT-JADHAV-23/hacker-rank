"""Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n.
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of (i+j+k)  is not equal to n.
Here, 0 < i < x, 0 < j < y, 0 < k < z
Please use list comprehensions rather than multiple loops, as a learning exercise"""

"""
example: x=1  y=1  z=1  n=2
# A permutation is the number of ways a set can be arranged or the number of ways things can be arranged.
all posiible permutations[i,j,k]=[[]]

from itertools import permutations
l = list(permutations(range(1, 4)))
print(l)
d=list(permutations([1, 2, 3]))
print(d)
"""
"""
x = int(input())
y = int(input())
z = int(input())
n = int(input())

# Initialize an empty list to store combinations
li= []

# Nested loops to iterate over all possible combinations of i, j, and k
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            # Check if the sum of i, j, and k is not equal to n
            if i + j + k != n:
                # If the condition is met, create a list [i, j, k] and append it to yx
                inner = [i, j, k]
                yx.append(inner)

# Print the list containing all valid combinations
print(yx)
"""
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# l=[] 
# for i in range(x+1):
#      for j in range(y+1):
#           for k in range(z+1):
#              if(i+j+k)!=n :
#                  l.append([i,j,k])
#                  print(l)

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
# code = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]

# print(code)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range (z+1) if (i+j+k)!=n]

    print(list)
