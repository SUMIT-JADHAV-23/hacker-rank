"""
You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.
Input Format
A single line containing the thickness value for the logo.
Constraints
The thickness must be an odd number.
"""
# .ljust(width)
# This method returns a left aligned string of length width.

# width=20
# print('HackerRank'.ljust(width,'-'))

# width =10
# print('hackerRank'.center(width,'|'))

# width =20
# print('Hacker'.rjust(width,'-'))

# width =20
# print('hackerRank'.center(width,"|"))

# thickness = int(input()) #This must be an odd number
# c = 'H'

"""
# enters a loop (for i in range(thickness)) where i takes values from 0 to thickness - 1.
# Inside the loop, it prints a string composed of the character c repeated i times (c * i). This creates a line with a varying number of characters.
# The ljust(thickness) function is used to left-justify the string within a field of width thickness.
# This ensures that all lines have the same width, and the characters are aligned to the left
for i in range(thickness):
    print((c*i).rjust(thickness-1))


#+ c adds one more instance of the character c to the end of each line.
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c)


for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))


"""
# #top cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
"""
               
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).ljust(thickness*2,"-"))

for i in range(thickness+1):
    print((c*thickness).rjust(thickness*2,"-"))          

         
for i in range(thickness):
    print((c*thickness).ljust(thickness)+(c*thickness).rjust(thickness*6))

         
for i in range(thickness):
    print((c*thickness).ljust(thickness*2)+(c*thickness).rjust(thickness*6))


"""

# #top cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
               
# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).ljust(thickness*2)+(c*thickness).rjust(thickness*2,))

"""
#top cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
               
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).rjust(thickness)+(c*thickness).rjust(thickness*3,))


# Middle Bel
for i in range(thickness-2):
    print((c*thickness*4).center(thickness))  


"""
# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).rjust(thickness)+(c*thickness).rjust(thickness*3,))  



# #top cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
               
# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).rjust(thickness)+(c*thickness).rjust(thickness*3,))


# # Middle Bel
# for i in range(thickness-2):
#     print((c*thickness*4).center(thickness))  

# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).rjust(thickness)+(c*thickness).rjust(thickness*3,)) 

"""
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness-1)))

for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness-1))+c)

for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness-1))+c+((c*(thickness-i-1)).ljust(thickness-1)))

for i in range(thickness):
    print((((c*(thickness-i-1)).rjust(thickness-1))+c+((c*(thickness-i-1)).ljust(thickness-1))).center(thickness*5))

"""

# #top cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
               
# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).rjust(thickness)+(c*thickness).rjust(thickness*3,))


# # Middle Bel
# for i in range(thickness-2):
#     print((c*thickness*4).center(thickness))  

# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).rjust(thickness)+(c*thickness).rjust(thickness*3,)) 


# for i in range(thickness):
#     print((((c*(thickness-i-1)).rjust(thickness-1))+c+((c*(thickness-i-1)).ljust(thickness-1))).center(thickness*6+1))




# thickness = int(input()) #This must be an odd number
# c = 'H'

# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).rjust(thickness+2)+(c*thickness).rjust(thickness*4))

# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))    

# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).rjust(thickness+2)+(c*thickness).rjust(thickness*4))    

# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).center(thickness*10))



thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))