
# def get_all_substrings(string):
  
#   length = len(string)
#   alist = []
#     for i in range(length):
#         for j in range(i,length):
#             alist.append(string[i:j + 1]) 

#     Stuart=[]
#     Kevin=[]
#     vowels=("A","e","I","O","U")
#     for s in alist:
#         if s.startswith(vowels):
#             Kevin.append(s)
#         else:
#             Stuart.append(s)


#     if len(Stuart)>len(Kevin):
#         return Stuart,len(Stuart) 
#     else:
#         return Kevin, len (Kevin)

# string='BANANA'
# res=get_all_substrings(string)
# print(res)


def get_all_substrings(string):
    length = len(string)
    alist = []
    for i in range(length):
        for j in range(i, length):
            alist.append(string[i:j + 1]) 

    Stuart = []
    Kevin = []
    vowels = ("A", "E", "I", "O", "U")
    for s in alist:
        if s.startswith(vowels):
            Kevin.append(s)
        else:
            Stuart.append(s)
    
    print(len (Kevin))
    if len(Stuart) > len(Kevin):
        return f'Stuart {len(Stuart)}'
    else:
        return f'Kevin {len(Kevin)}'
    
string='BANANA'
res=get_all_substrings(string)
print(res)


"""
# However, the issue is that you're not printing the result in the __main__ block. You need to add a print statement to display the output.
def minion_game(string):
    length = len(string)
    alist = []
    for i in range(length):
        for j in range(i, length):
            alist.append(string[i:j + 1]) 

    Stuart = []
    Kevin = []
    vowels = ("A", "e", "I", "O", "U")
    for s in alist:
        if s.startswith(vowels):
            Kevin.append(s)
        else:
            Stuart.append(s)

    if len(Stuart) == len(Kevin):
        print("Draw")
    elif len(Stuart) > len(Kevin):
        print(f'Stuart {len(Stuart)}')
    else:
        print(f'Kevin {len(Kevin)}')

if __name__ == '__main__':
    s = input("Enter a string: ")
    minion_game(s)"""


# def get_all_substrings(string):
#     length = len(string)
#     alist = []
#     for i in range(length):
#         for j in range(i, length):
#             alist.append(string[i:j + 1]) 

#     Stuart = []
#     Kevin = []
#     vowels = ("A", "e", "I", "O", "U")
#     for s in alist:
#         if s.startswith(vowels):
#             Kevin.append(s)
#         else:
#             Stuart.append(s)

#     if len(Stuart) > len(Kevin):
#         return f'Stuart {len(Stuart)}'
#     else:
#         return f'Kevin {len(Kevin)}'


def minion_game(string):
    # your code goes here
    n = len(string)
    comb = ((n)*(n+1))/2
    count_k = 0
    count_s = 0
    count_k = sum([len(string[i:]) for i in range(len(string)) if string[i] in "AEIOU"])
    count_s = comb - count_k
    
    if count_s == count_k:
        print("Draw")
    elif count_s > count_k:
        print("Stuart", int(count_s) )
    else:
        print("Kevin", int(count_k))

if __name__ == '__main__':
    s = input()
    minion_game(s)


#  def minion_game(string):
#     s=len(string)
#     vowel = 0
#     consonant = 0
     
#     for i in range(s):
#         if string[i] in 'AEIOU':
#            vowel+=(s-i)
#         else:
#            consonant+=(s-i)
                
#     if vowel < consonant:
#         print('Stuart ' + str(consonant))
#     elif vowel > consonant:
#         print('Kevin ' + str(vowel))
#     else:
#         print('Draw')   