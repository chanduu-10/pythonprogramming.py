# 01 local vairable and global vairable
#Local Variables:

#1. Defined inside a function or block
#2. Accessible only within that function or block
#3. Exist only during function/block execution

#Global Variables:

#1. Defined outside functions or blocks
#2. Accessible from anywhere in the program
#3. Exist for the entire program duration
"""
x = 10  # Global
def my_function():
    y = 20  # Local
    print(x, y)
my_function()
print(x) """
#This code updates a global variable x from 10 to 77 using the global keyword inside a function.
"""
x = 10  # Global variable 'x' is initialized with value 10

def my_function():
    global x  # This tells Python that we are referring to the global variable 'x'
    x = 77    # The global variable 'x' is updated to 77

my_function()  # Call the function, which updates the global 'x'
print(x)       # Output the value of 'x' """

# 02 print sum of numbers using for loop
"""
user = int(input("enter your number:"))
total = 0
for i in range(1,user+1):
    print(i,end=" ")
    total += i
print()             ##This is just a blank print(), which tells Python:“Okay, now go to the next line.” other wise sum of total also prints in print(i,end = " ") thats only we use normal print()
print(f"sum of total:{total}")"""
#print sum of numbers using while loop
"""
user = int(input("enter your number:"))
total = 0
i = 1
while i <= user:
    print(i,end = " ")
    total += i
    i += 1
print()
print(f"sum of total:{total}")"""

# adding multiple numbers in input
"""
a = input("Enter numbers:")
s = a.split(",")
total = 0

for i in s:
    total += int(i)
print(total)"""
# 03 write a program and print swap two vairable
"""
a = 7
b = 18
temp = a
a = b
b = temp
print(f"a = {a}")
print(f"b = {b}")"""
"""
a = 7
b = 18
a,b = b,a
print(f"a = {a}")
print(f"b = {b}")"""
# 04 print 17 table using for loop
"""
num = int(input("enter your number:"))
total = 0
for i in range(1,11):
    total = num * i
    print(f"{num} * {i} = {total}")"""
# print 17 table using while loop
"""
num = int(input("enter your number:"))
i = 1

while i <= 9:
     i+=1
     print(f"{num}x {i}={num*i}")"""
# 05 Generate Random number
# gives a random integer in specified range
"""
import random
num = random.randint(1,100)
print(num)"""

# gives a random float number between 0 and 1
"""
import random
num = random.random()
print(num)"""

# gives a random float number in specified number
"""
import random
num = random.uniform(1,100)
print(num)"""

# gives a random number in a range with incremental steps
"""
import random
num = random.randrange(0,100,2)
print(num)"""

# gives a sereis of random numbers
"""
import random
numlist = random.sample(range(0,100),3)
print(numlist)"""

# 06 print forward 5 stars patterns
"""
for i in range(1,6):
    print("* " * i)"""
"""
num = int(input("enter your number:"))
for i in range(1,num):
    print(" *" * i)"""

# 07 print reverse 5 stars patterns
"""
for i in range(5,0,-1):
    print(" *" * i)"""
"""num = int(input("enter your number:"))
for i in range(num,0,-1):
    print(" *" * i)"""

# 08 print forward pyramid type in 5 stars
"""
for i in range(1,6):
    spaces = " " *(5-i)
    stars = "* " * i
    print(spaces + stars)"""

# 09 print reverse pyramid type in 5 stars 
"""
for i in range(5,0,-1):
    spaces = " " * (5-i)
    stars = "* " * i
    print(spaces + stars)"""

# print 1 to 5 numbers like pattern only
"""
n = int(input("enter your number:"))
for i in range(1,n+1):
    for j in range(1,x+1):
        print(j,end =" ")
    print()"""

# print 1 to 5 numbers pyramid type
"""
n = 6
for i in range(1,n):
    spaces = (" " * (n-i))
    print(spaces,end= " ")
    for j in range(1,i+1):
        print(j,end = " ")
    print()"""

# print 5 to 1 numbers like pattern only
"""
num = int(input("enter your number:"))  # e.g., 5
for i in range(1,num):           # Starting from 5 down to 1
    for j in range(x,num):         # Print from 5 to x
        print(j, end=" ")
    print()"""

# print 5 to 1 pyramid type
"""
n = 6
for i in range(1,n):
    spaces = (" " * (i-1))
    print(spaces,end = " ")
    for j in range(i,n):
        print(j,end = " ")
    print()"""


# 10 Write a Python program to print the first 10 natural numbers.
"""
for i in range(1,11):
    print(i)"""

# 11 Create a Python function to calculate the area of a rectangle.
"""
class rectangle:
    @staticmethod
  # def Box(self,len,wid):#if you didnot use self, u must and should give @staticmethod
    def Box(len,wid):
        return len * wid
per = rectangle()
print(per.Box(3,4))"""
"""
def rectangle(length,width):
    return (length * width)
print(rectangle(3,4))"""

# 12 Create a Python list and perform basic operations like append, insert, and delete.
"""
list =[0,1,2,4,5,6]
list.append(7) # element append only last
list.insert(3,3)# element instert in spcefic postion or location based on index postion
list.remove(6) # its removing specific number
list.extend([8,9]) # we can extend multiple numbers in the end of list
list.pop(6) # it removes specific number by using index postion
print(list.count(4)) #  prints how many times 4 appears in the list
list
"""
# 13 create a python tuple and perform all operations like concentation(+),len(),in,[index],[start:end],count(x),index(x)
     # + → Concatenation: Combines two tuples into one.
# len() → Length: Returns the number of elements in the tuple.
# in → Membership Test: Checks if an element exists in the tuple.
# [index] → Indexing: Access elements by their position (positive or negative index).
# [start:end] → Slicing: Extracts a part of the tuple using range of indices.
# count(x) → Count: Returns how many times element x appears in the tuple.
# index(x) → Index: Returns the first index where element x is found.

"""
def tuple(t1,t2):
    concatenated = t1 + t2
    lenght_t1 = len(t1)
    contains_check = 30 in t1
    first_element = t1[0] if t1 else None
    last_element = t1[-1] if t1 else None
    sliced = t1[1:4]
    count_10 = t1.count(10)
    index_20 = t1.index(20) if 20 in t1 else "Not Found"

    return concatenated,lenght_t1,contains_check,first_element,last_element,sliced,count_10,index_20
result = tuple((10,20,30,10,40),(50,60))
print("concatenated:",result[0])
print("length of t1:",result[1])
print("Is 30 in t1?:",result[2])
print("First Element of t1:", result[3])
print("Last Element of t1:", result[4])
print("Sliced t1[1:4]:", result[5])
print("Count of 10 in t1:", result[6])
print("Index of 20 in t1:", result[7])"""


# 14 Create a Python set and perform all operations intersection(&),union(|),subset,superset,Difference(-),symmetric difference(^)
     # & → Intersection,Finds elements common to both sets.
     # | → Union,Combines all elements from both sets
     # subset,A set A is a subset of set B if all elements of A are also in B.
     # superset,A set B is a superset of set A if B contains all elements of A.
     #  - → Difference,Finds elements in A but not in B.
     # ^ → Symmetric Difference,Finds elements in either A or B, but not in both (no common elements).
"""
def letters(str1,str2):
    s1 = set(str1)
    s2 = set(str2)

    intersection = s1 & s2
    union = s1 | s2
    is_subset = s1.issubset(s2)
    is_superset = s1.issuperset(s2)
    difference = s1 - s2
    sym_diff = s1 ^ s2

    return intersection,union,is_subset,is_superset,difference,sym_diff

result = letters("durgabhavani","Mohan chandu")
print("intersection (&):",result[0])
print("union(|):",result[1])
print("is_subset:",result[2])
print("is_superset:",result[3])
print("difference(-):",result[4])
print("symmetric_diff(^):",result[5])"""

# 15 Create a Python dictionary and perform all operations like get,keys,values,items,insert, update, and delete.
"""
student = {
    "Name"  : "Mohanchandu",
    "Age"   : 21,
    "Branch":"computerscience"
}
# Access value using get()
print("Name:",student.get("Name"))
print("Roll Number(not present)",student.get("roll","Not Found"))

# Get all keys
print("Keys:",student.keys())

# Get all values
print("values:",student.values())

# Get all items(key-valur pairs)
print("Items:",student.items())

# Insert a new key - value pair
student["University"] = "Paruluniversity"
print("After insert:",student)

# update an existing key
student["Age:"] = 22
print("After update:",student)

# Delete a key
del student["Branch"]
print("After delete:", student)
"""


# 16 Write a Python program to find the sum of all elements in a list.
"""
list = [1,2,34,4,5]
print(sum(list))"""


# 17 write a python program to count the frequency of words appering in a string
     #set(words) removes duplicates just for looping once per word
     #words.count(word) still checks full original list, so you get total accurate counts.

sentence = input("enter a sentence:")
words = sentence.split()
for word in set(words):
    print(f"{word} appears {words.count(word)} times")

#  write a python program to convert two lists in to one dictionary
"""
keys = ["renu","chandu","jagathi","gopi","nani"]
values= [96,83,85,98,99]
d = dict(zip(keys,values))
print(d)"""

# 18 Remove duplicate characters in a string
"""
str = input("enter your string:")
str1 = set(str)
print(str1)"""

# 19 write a program and print Sort a list of tuples by the second element
"""
data = [(1,3),(2,1),(3,2)]
sorted_data = sorted(data,key=lambda x:x[1])
print(sorted_data)"""


# 20 print armstrong number up to  your wish

# Arm strong numbers means which numbers have the property that the sum of the cubes of their digits equals the number itself. 
"""
for i in range (100,10000):
    s = i
    total = 0
    order = len(str(i))
    while s > 0:
        d = s % 10
        sum = total + d ** order
        s = s // 10
    if i == total:
        print("arm strong number are:",i)"""

# 🧠 Example of Armstrong number: Let’s check the number 9474 by hand!
# i = 9474
# s = 9474, total = 0
# order = 4 (since 9474 has 4 digits)

# 🔁 Loop 1:
# d = 9474 % 10 = 4 (last digit)
# 4^4 = 256
# total = 0 + 256 = 256

# Remove last digit: s = 9474 // 10 = 947

# 🔁 Loop 2:
# d = 947 % 10 = 7
# 7^4 = 2401
# total = 256 + 2401 = 2657

# Remove last digit: s = 947 // 10 = 94

# 🔁 Loop 3:
# d = 94 % 10 = 4
# 4^4 = 256
# total = 2657 + 256 = 2913

# Remove last digit: s = 94 // 10 = 9

# 🔁 Loop 4:
# d = 9 % 10 = 9
# 9^4 = 6561
# total = 2913 + 6561 = 9474

# Remove last digit: s = 9 // 10 = 0

# ✅ Final Check:
# Now s = 0, so we exit the loop
# Check if i == total:
# 9474 == 9474 → True
# ✅ So, 9474 is printed as an Armstrong number


# Example of arm strong number: Let’s check the number 153 by hand!
# i = 153
# s = 153, sum = 0

# Loop 1:
# last digit d = 153 % 10 = 3
# cube of 3 = 27
# sum = 0 + 27 = 27
# remove last digit: s = 153 // 10 = 15

# Loop 2:
# last digit d = 15 % 10 = 5
# cube of 5 = 125
# sum = 27 + 125 = 152
# remove last digit: s = 15 // 10 = 1

# Loop 3:
# last digit d = 1 % 10 = 1
# cube of 1 = 1
# sum = 152 + 1 = 153
# remove last digit: s = 1 // 10 = 0
# Now s is 0, so stop looping.

# Check if i == sum:
# 153 == 153 → True
# So, 153 is printed as an Armstrong number!



# it tells you that number is armstrong or not,any number you should wish to enter
"""
num = int(input("enter a number:"))
s = num
sum = 0
order = len(str(num))

while s > 0:
    d = s % 10
    sum = sum + d ** order
    s = s // 10
if num == sum:
    print(f"{num} is arm strong number")
else:
    print(f"{num} is not arm strong number ")"""
