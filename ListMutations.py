"""
We have seen that lists are mutable (they can be changed), 
and tuples are immutable (they cannot be changed).
Let's try to understand this with an example.
You are given an immutable string, and you want to make changes to it.

"""

# string = "abracadabra"
# l = list(string)
# l[5] = 'k'
# string = ''.join(l)
# print (string)


# k = string[:5] + "k" + string[6:]
# print (k)

"""
def mutate_string(string, position, character):
    li=list(string)
    # print(li)
    li[position] = character
    # print(li1)
    string ="".join(li)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
"""


# def mutate_string(string, position, character):
#     lst = list(string)
#     lst[position] = character
#     string = "".join(lst)
#     return string

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()

#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

"""
def mutate_string(string, character):
    string=string[:5]+character+string[5:]
    return string

if __name__ == '__main__':
    s = input()
    c = input()
    s_new = mutate_string(s,  c)
    print(s_new)
"""
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


def mutate_string(string, position, character):
    return string[:position]+character+string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


 def mutate_string(string,pos,charac):
    x = [i for i in string]#list comprehension
    x[pos] = charac 
    return ''.join(x)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)  


