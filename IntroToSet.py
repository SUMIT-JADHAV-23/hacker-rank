"""A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.
Task
Now, let's use our knowledge of sets and help Mickey.
Ms. Gabriel Williams is a botany professor at District College.
One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
Function Description
Complete the average function in the editor below.
average has the following parameters:
int arr: an array of integers
Returns
float: the resulting float value rounded to 3 places after the decimal

Here, set is the set containing the distinct heights. Using the sum() and len() functions, we can compute the average.
10                                          arr[] size N = 10
161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]
Sample Output
169.375
"""
# def average(array):
#     # your code goes here
#     a=set(array)
#     b=len(a)
#     s=sum(a)
#     avg=s/b
#     return avg
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)

"""
If we want to add a single element to an existing set, we can use the .add() operation.
Task
Apply your knowledge of the .add() operation to help your friend Rupal.
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection.
She asked for your help. You pick the stamps one by one from a stack of N country stamps.
Find the total number of distinct country stamps.
Input Format
The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from.
"""
# n = int(input())
# a=set()
# for _ in range(n):
#     a.add(input())
# print(len(a))
"""
Task
The students of District College have subscriptions to English and French newspapers.
Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
You are given two sets of student roll numbers. 
One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. 
The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.
Input Format
The first line contains an integer, , the number of students who have subscribed to the English newspaper.
The second line contains  space separated roll numbers of those students.
The third line contains , the number of students who have subscribed to the French newspaper.
The fourth line contains  space separated roll numbers of those students.
"""
# E = int(input())
# english = set(map(int,input().split()))
# b = int(input())
# french = set(map(int,input().split()))
# s=set(english.union(french))
# print(len(s))
"""
Task
The students of District College have subscriptions to English and French newspapers. 
Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.
You are given two sets of student roll numbers.
One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to both newspapers.
Input Format
The first line contains , the number of students who have subscribed to the English newspaper.
The second line contains  space separated roll numbers of those students.
The third line contains , the number of students who have subscribed to the French newspaper.
The fourth line contains  space separated roll numbers of those students.
"""
# E = int(input())
# english = set(map(int,input().split()))
# b = int(input())
# french = set(map(int,input().split()))
# s=set(english.intersection(french))
# print(len(s))

"""Task
Students of District College have a subscription to English and French newspapers.
Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.
You are given two sets of student roll numbers.
One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper.
Your task is to find the total number of students who have subscribed to only English newspapers.
Input Format
The first line contains the number of students who have subscribed to the English newspaper.
The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
The third line contains the number of students who have subscribed to the French newspaper.
The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.
"""
# E = int(input())
# english = set(map(int,input().split()))
# b = int(input())
# french = set(map(int,input().split()))
# s=set(english.difference(french))
# print(len(s))

"""Task
Students of District College have subscriptions to English and French newspapers. 
Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers.
One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

Input Format

The first line contains the number of students who have subscribed to the English newspaper.
The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
The third line contains the number of students who have subscribed to the French newspaper.
The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper."""
# E = int(input())
# english = set(map(int,input().split()))
# b = int(input())
# french = set(map(int,input().split()))
# s=set(english.symmetric_difference(french))
# print(len(s))
"""Task
Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist  in either  M or N  but do not exist in both.

Input Format

The first line of input contains an integer,M .
The second line contains M space-separated integers.
The third line contains an integer,N .
The fourth line contains N space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line."""
# M = int(input())
# set1 = set(map(int,input().split()))
# N= int(input())
# set2 = set(map(int,input().split()))
# A=set(set1.symmetric_difference(set2))
# b=sorted(A)
# for i in b:
#     print(i)
jadhav 