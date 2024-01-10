'''
# Step 1: First, n will take input for a total number of students.

# Step 2: then, we created a dictionary to store the name and marks of students.

# Step 3: After this, we created a for loop.

# Step 4: inside for loop, we have taken an input of the name.

# Step 5: we have also taken the input of scores and stored them in a list.

# Step 6: then we stored names and scores in the dictionary.

# Step 7: in the next step we had taken the input of query_name i.e, the name of the student whose percentage we want to print. And, in the next step, we created the list of query_name marks.

# Step 8: After this, we added all the scores to our list. Then we divided our total sum by the length of the list.

# Step 9: in the last step we had printed the result.

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()

'''
# # The * is being used to grab additional returns from the split statement.
# # fisrst char get separeted and rest is seprated
# first, *rest = input().split()
# print(first)
# print(*rest)

# s = 'a b c d e f'
# name, *line = s.split()
# print(name)
# print(line)

'''
>>> a, b, *rest = range(5)
>>> a, b, rest
(0, 1, [2,3,4])

>>> a, *middle, c = range(4)
>>> a, middle, c
(0, [1,2], 3)

>>> name
'a'
>>> line
['b', 'c', 'd', 'e', 'f']
'''
# name, *line = "foo 23 34 45".split()
# scores = list(map(float, line))
# print(scores)

'''
name, *line = "foo 23 34 45".split()
assert(name == "foo");
assert(line == ["23", "34", "45"])

scores = list(map(float, line))
assert(scores == [23.0, 34.0, 45.0])


# Sample line containing numerical values as strings
line = ['1.5', '2.3', '3.7']

# Applying the expression to convert the strings to floats and create a list
result = list(map(float, line))

print(result)
'''

'''
# Associates the student's name with their scores in the student_marks dictionary
# student_marks[name] = scores
#     query_name = input()





# addition_of_marks=sum(query_name = input())
# length_of_marks=len(query_name = input())

# perc= addition_of_marks/length_of_marks
# print(perc)
'''

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
    
#     # stu_name=(student_marks[query_name])

#     # addition_of_marks=sum(stu_name)
#     # length_of_marks=len(stu_name)
    
#     # perc= addition_of_marks/length_of_marks
#     # print(perc)

#     l1 = list(student_marks[query_name]) 

#     addition = sum(l1)

#     result = addition/len(l1)
#     # ('%.2f'% ) used for decimal 20.00
#     print('%.2f'% result)

"""
Format codes	Description
d	            for integers
f	            for floating point numbers
b	            for binary numbers
o	            for octal numbers
x	            for octal hexadecimal numbers
s	            for string
e	            for floating point in exponent format

"""

floatNumber = 1.9876

print("%f" % floatNumber)

float = 1.9876

print("%d" % float)


floatNumber = 1.9876

print("%.02f" % floatNumber)

floatNumber = 1.9876

print("%.07f" % floatNumber)