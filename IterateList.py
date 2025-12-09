def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
 
# Driver Code
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
print(intersection(lst1, lst2))

import re
p= input("Input your password :")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break
if x:
    print("Not a Valid Password")

#Sample Output:

#Input your passwordW3r@1

import random
print( random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))

n=int(input("Enter the number of terms: "))
sum1=0
for i in range(1,n+1):
    sum1=sum1+(1/i)
print("The sum of series is",round(sum1,2))

input_lists= [12,24,35,70,88,120,155]
lists= [x for (i,x) in enumerate(input_lists) if i not in (0,4,5)]
print (lists)
# [24, 35, 70, 155]
lst = [12,24,35,70,88,120,155]
lst = [x for x in lst if x%5!=0 and x%7!=0]
print (lst)
# [12, 24, 88]

a =[4,7,8,9];
for i in a:
    print("Element: " + str(i) + " Index: "+ str(a.index(i)))

#Please write a program which accepts a string from console and print the characters that have even indexes
print("Please enter text to print that have even indexes::")
inputchars = input()

if inputchars:
	outputchars = ""
	for i in inputchars:
		if inputchars.index(i)%2 == 0:
			outputchars += str(i)
	
	print('-------------------')
	print(" Entered:", inputchars)
	print("Result:")
	print(outputchars)
def removeDuplicate( lists):
    newlist=[]
    seen = set()
    for item in lists:
        if item not in seen:
            seen.add( item )
            newlist.append(item)

    return newlist

li=[12,24,35,24,88,120,155,88,120,155]
print ( removeDuplicate(li))	
#Reverse 1
def reverse(string):
    string = string[::-1]
    return string
 
s = "Geeksforgeeks"
 
print("The original string is : ", end="")
print(s)
 
print("The reversed string(using extended slice syntax) is : ", end="")
print(reverse(s))
# Reverse
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
 
s = "rise to vote sir "
 
print("The original string is : ", end="")
print(s)
 
print("The reversed string(using loops) is : ", end="")
print(reverse(s))

#count char
# initializing string
print("Please enter text to count character::")
input_text = input()
 
# using set() + count() to get count
# of each element in string
count_text = {i: input_text.count(i) for i in set(input_text)}
 
# printing result
print("The count of all characters in given input is :\n "
      + str(count_text))
# view formatted
def character_counter(text):
	characters_list = list(text)
	char_count = {}
	for x in characters_list:
		if x in char_count.keys():
			char_count[x] += 1
		else:
			char_count[x] = 1
	return char_count


def dict_viewer(dictionary):
	for x, y in dictionary.items():
		print(f"{x},{y}")


text = input("> ")
dict_viewer(character_counter(text))

