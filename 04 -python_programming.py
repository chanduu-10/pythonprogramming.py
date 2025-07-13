# 01 input [1,2,3,4,5,6]
#  output[2,1,4,3,6,5]
"""
a =[1,2,3,4,5,6]
a[0],a[1],a[2],a[3],a[4],a[5] = a[3],a[4],a[5] ,a[0],a[1],a[2]
print(a)"""

# 02 input[1,2,3,4,5,6]
#output[4,5,6,1,2,3]
"""
a =[1,2,3,4,5,6]
a[0],a[1],a[2],a[3],a[4],a[5] = a[1],a[0],a[3] ,a[2],a[5],a[4]
print(a)"""

# 03 selection sort
# 👉 “Find the smallest number and put it in the correct place — one by one.”
# It keeps choosing the smallest from the remaining list and placing it at the front.
"""
a = [2,1,3,4,11]
n = len(a)
for i in range(n-1):
    for j in range(i+1,n):
        if a[j] < a[i]:
            a[i],a[j] = a[j],a[i]
print(a)"""

# 04 Bubble sort
# 👉 “Keep comparing neighbors and swap if they are in the wrong order — again and again.”
# Big numbers slowly bubble to the end, like bubbles rising in water.
"""
a = [2,1,3,4,11]
n = len(a)
for i in range(n-1):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)"""

# 05  Linear Search is the simplest way to find an element in a list:
# You check each element one by one until you find the target.
# Time Complexity: O(n)
"""
# 05 Linear search
num = eval(input("enter your list:"))
target = int(input("enter your number:"))
for i in range (len(num)):
    if num[i]==target:
       print("number found at index:",i)
"""

# 06 Binary search
# input [2,5,7,9,10,66]
# target num :- 9
# here we checking 9 is present or not by using  decides which half to eliminate based on the middle value. 
# Binary Search works by repeatedly dividing the sorted list into halves:

# Compare the middle element with the target.

# If equal → target found.

# If target < mid → search in left half.

# If target > mid → search in right half.


#Why Binary Search Requires a Sorted List:
#Binary search divides the list into halves and decides which half to eliminate based on the middle value. This decision is only valid if the list is sorted.
"""
input = eval(input("enter your list:"))
num = int(input("enter your number:"))
begin = 0
end = len(input)-1
while begin <= end:
    mid = (begin + end) // 2
    if num == input[mid] :
        print(num,"is founded at index:",mid)
        break
    elif num>input[mid]:
        begin = mid + 1
    elif  num<input[mid]:
        end = mid - 1
else:
    print("enter valid number")"""

# 07 find first and second largest number in list with using any method
"""
arr = [3,454,345,34,43,54,453,543,454,2]
a = 0
b = 0
c = 0
for i in arr:
    if i > a:
        c = b
        b = a
        a = i
    elif i > b and i != a:
        b = i
    elif i > c and i != b and i != a:
        c = i
print("Largest number:",a)
print("second largestnumber:",b)
print("thrid largestnumber:",c)"""

#  08 Remove all special characters from a string
"""
import re
text = ("Hello@#% World!! 123:")
cleaned_text = re.sub(r'[^A-Za-z0-9]','',text) #r:- before the string — Raw String Notation The r prefix means it's a raw string, so Python will treat backslashes (\) as literal characters rather than escape characters.sub:- substitutr or replace
print(cleaned_text)"""

# 09 Capitalize the first letter of each word in a sentence.
"""
text = "this is chandu from andhrapradesh"
capatalized_text = text.title()
print(capatalized_text)"""

# 10 Use lambda to square all numbers in a list.
"""
numbers = [1,2,3,4,5]
squared = list(map(lambda x:x**2,numbers))#using lambda
print(squared)
numbers = [1,2,3,4,5]
squared = [x**2 for x in numbers]  #list comphersion
print(squared)"""

# 11 print words in reverse order
"""
s = "this is sajja"
words = s.split()
s1 = words[::-1]
print(s1)
"""

# 12 multipying two lists
"""
num1 = eval(input("enter your list:"))
num2 = eval(input("enter your list"))
for i in num1:
    result = [i * j for j in num2]
    print(f"{i} multipled with{num2}=>{result}")"""

# 13 Pick 3 random items from a list without repetition.
"""
import random
items = ['apple', 'banana', 'mango', 'grapes', 'orange']
print(random.sample(items, 3))

import random
students = ['Ankit', 'Priya', 'Ravi', 'Sneha', 'Mohan']
print(random.choice(students))"""

# 14  Generate a list of 5 unique random even numbers between 1 and 100.
"""
import random
even_numbers = random.sample([i for i in range(2, 101, 2)], 5)
print(even_numbers)"""
 
# 15 lift program
"""
current_floor = 0
target_floor = int(input(" enter floor number you want to go:"))

if 0 <= target_floor <= 9:
    print(f"Elevator is at floor{current_floor}.")
    
    # if target floor is above
    if target_floor > current_floor:
        for floor in range(current_floor +1,target_floor +1):
            print(f"Going up.... now at floor{floor}")
    
    # if target floor is below
    elif target_floor < current_floor:
        for floor in range(current_floor -1,target_floor-1,-1):
            print(f"Going down.... now at floor{floor}")
    else:
        print("You are already on the target floor.")
    
    print(f"Elevator has arrived at floor{target_floor}.Doors opening.")
else:
    print("Invalid floor! please enter a number between 0 and 9.")"""

# 16 lift program
"""
# Initial positions
elevator_floor = 0  # Elevator starts on floor 0
person_floor = 3    # Person starts on floor 3 (can be changed)
target_floor = -1   # This will be set by the person later

# Function to move the elevator
def move_elevator(current_floor, target_floor):
    if current_floor < target_floor:
        print(f"Elevator is going up... now at floor {target_floor}")
    elif current_floor > target_floor:
        print(f"Elevator is going down... now at floor {target_floor}")
    else:
        print(f"Elevator is already at floor {current_floor}")

# Elevator goes to the person's floor
print(f"Elevator is at floor {elevator_floor}.")
print(f"Person is at floor {person_floor}.")
print("Elevator is moving to the person's floor...")
move_elevator(elevator_floor, person_floor)

# Person enters the elevator
print(f"Person entered the elevator at floor {person_floor}.")

# Person selects their destination floor
target_floor = int(input("Enter the floor number you want to go to (0 to 9): "))

# Check if the target floor is valid
if 0 <= target_floor <= 9:
    # Elevator moves to the selected target floor
    print(f"Elevator is now at floor {person_floor}.")
    print(f"Person pressed the button for floor {target_floor}.")
    print("Elevator is moving to the target floor...")
    move_elevator(person_floor, target_floor)

    # Elevator reaches the target floor
    print(f"Elevator has arrived at floor {target_floor}. 🚪 Doors opening.")
else:
    print("❌ Invalid floor! Please enter a number between 0 and 9.")"""

# 17 print Floyd's triangle
"""
rows = 5
num = 1

for i in range(1,rows+1):
    for j in range(i):
        print(num,end=" ")
        num += 1
    print()"""

# 18 merge two dictionaries
"""
dict1 = {'a' : 1,'b' : 2}
dict2 = {'b' : 3,'c' : 4}
dict1.update(dict2)
print(dict1)"""

# 19 convert a string to lowecase and uppercase,remove spaces from a string
"""
text = " Hello Amma! How are you? "
lowercase_text = text.lower()
print("Lowercase:",lowercase_text)
uppercase_text = text.upper()
print("Uppercase",uppercase_text)
no_spaces_text = text.replace(" ","")
print("No spaces",no_spaces_text)"""

# 20 sort a list of tuples by the second element
"""
list_of_tuples = [(1,3),(2,2),(3,1)]
sorted_list = sorted(list_of_tuples,key=lambda x:x[1])
print(sorted_list)"""


