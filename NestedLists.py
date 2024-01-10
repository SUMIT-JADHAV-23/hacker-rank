"""Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

"""
"""
#example of nsted list -list inside list
# creating list
nestedList = [1, 2, ['a', 1], 3]

# indexing list: the sublist has now been accessed
subList = nestedList[2]

# access the first element inside the inner list:
element = nestedList[2][0]

print("List inside the nested list: ", subList)
print("First element of the sublist: ", element)

"""
"""
L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']

print(L[2])
# Prints ['cc', 'dd', ['eee', 'fff']]

print(L[2][2])
# Prints ['eee', 'fff']

print(L[2][2][0])
# Prints eee
"""

name_list=[]
score_list=[]
nested_list=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        #append use for add the input in nested_list
        name_list.append(name)
        score_list.append(score)
        nested_list.append([name,score])
print(nested_list)
print(name_list)
print(score_list)
#set remove duplicate and sort make it as in order asecending
score_list= list(set(score_list))
score_list.sort()
print(score_list)
#use of list while achiveng index
second_low=score_list[1]
print(second_low)


#now we have secound lowest but we have to print with name only
stud_name=[i[0] for i in nested_list if i[1]== second_low]
# print(stud_name)
stud_name.sort()
print(stud_name)
for i in stud_name:
    print(i)



"""
if __name__ == '__main__':
    alist = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        alist.append([name, score])
second_highest = sorted(set([score for name, score in alist]))[1]
print('\n'.join(sorted([name for name, score in alist if score == second_highest])))
"""

"""
Result =[]
scorelist = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Result+=[[name,score]]
        scorelist+=[score]
    b=sorted(list(set(scorelist)))[1] 
    for a,c in sorted(Result):
        if c==b:
            print(a)
"""