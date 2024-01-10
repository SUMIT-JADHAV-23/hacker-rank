"""
You are given a string n and width w.
Your task is to wrap the string into a paragraph of width w.
Function Description - Complete the wrap function in the editor below.
wrap has the following parameters:
string string: a long string
int max_width: the width to wrap to
Returns-
string: a single string with newline characters ('\n') where the breaks should be
Input Format
The first line contains a string, .
The second line contains the width, .
"""
#firstly import textwrap this is builtin function
import textwrap
#def wrap that contain string and max_width to wrap the string into a paragraph of width 
def wrap(string, max_width):
    #textwrap having a parameter fill that takes two argumenrts string and index
    text=textwrap.fill(string,max_width)
    #return the text
    return text

if __name__ == '__main__':
    #takes input 1.defult string 2.int input
    string, max_width = input(), int(input())
    #call the def function to print
    result = wrap(string, max_width)
    print(result)

#another method
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


#another method 
import textwrap

def wrap(string, max_width):
    for i in range(0,len(string)+1,max_width):
        result = string[i:i+max_width]
        if len(result) == max_width:
            print(result)
        else:
            return(result)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)