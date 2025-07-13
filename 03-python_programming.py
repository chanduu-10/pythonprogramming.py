# 01 What is  Stack?
        # A stack is a linear data structure that follows the LIFO (Last In, First Out) principle:
        #Push: Adding an element to the stack.
        #Pop: Removing the most recently added element from the stack.
        #Peek or Top: Viewing the top element of the stack without removing it
"""
stack = []
# Push elements
stack.append(30)
stack.append(20)

# Pop element
print("Popped:", stack.pop())

# View stack
print("Stack now:", stack)"""

# 02 what is Queue?
   #A queue is a linear data structure that follows the FIFO (First In, First Out) principle. 
"""
queue = []

# Enqueue
queue.append(10)
queue.append(20)

# Dequeue
print("Dequeued:", queue.pop(0))

# View queue
print("Queue now:", queue)"""

# 03 write a python program and print remove duplicates and also print maximum number and minimum number in list
"""
arr = [1,2,2,12,21,12,1,2,12,13,15]
print(list(set(arr)))
print(max(arr))
print(min(arr))"""

# 04  write a program and print first non repeat character in string
"""
sen = input("enter your string:")
for char in sen:
    if sen.count(char) == 1:
        print("first non repesting string is :",char)
        break
else:
    print("No non -repeating characters found")   
    """

# 05 write a progam and print non repeating characters in string
"""
string = input("enter your string:")
for char in string:
    if string.count(char) == 1:
        print(char,end = '')"""
# write a program and print first non repeating number in list
"""
list = [1,1,2,3,5,6,78,56,6]
for numbers in list:
    if list.count(numbers) == 1:
       print("first non repeating number is ",numbers)
       break
else:
    print("there is no non repeating numbers")"""

# write a program and print non repeating numbers in list
"""
list = [1,1,2,3,5,6,78,56,6]
for numbers in list:
    if list.count(numbers) == 1:
        print(numbers)"""

# 06 write a program and print roman numericals to integers
# 1. Roman numerals use letters instead of digits:
    #I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
# 🎯 Main Important Rules:
# 2. Addition rule,Subraction Rule:
    # If smaller number comes before bigger ➔ Subtract it.
    # If smaller number comes after bigger ➔ Add it.
    # Example:
    # IV ➔ I before V ➔ 5 - 1 = 4
    # VI ➔ V before I ➔ 5 + 1 = 6
# 3. Repetition Rule:
    # You can repeat a symbol maximum three times.
    # Example:

     #III = 3
     #XXX = 30
     #❌ Never repeat V, L, or D.
# 4. Placement Rule:
     #Write biggest values first, moving left to right.
     #Example:
     #MCMXCIV = 1000 + (1000-100) + (100-10) + (5-1) = 1994
"""
def roman_to_integer(roman):
    values = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    total = 0
    prev_value = 0

    for char in reversed(roman):  #u use like this, for char in roman [::-1] ,for reversing the function argument
        value = values[char]

        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value
        
    return total

roman_input = input("enter roman numerical:").upper()
result = roman_to_integer(roman_input)
print(f"The integer value of {roman_input} is {result}")"""

# 07 difference between postional arguments(*args) and keyword arguments(**kwargs) and also give example program
    # Positional arguments (*args) collect extra values based on their position into a tuple, while
    
    # Keyword arguments (**kwargs) collect extra values based on keys (name=value) into a dictionary.

    # *args → handles extra positional arguments (order matters)

    # **kwargs → handles extra keyword arguments (key-value pairs, order doesn't matter)  

"""   
def positional_keyword(*args,**kwargs):
    print(args)
    print(kwargs)

positional_keyword(1,2,3,name="chandu",age="22")"""

# 08 write a program and print Find all pairs in a list whose sum is equal to a given number.
"""
def two_num_sum(nums,target):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j] == target:
                result.append((nums[i],nums[j]))
    return result
nums = [1,2,3,3,4,0,5]
target = 6
print(two_num_sum(nums,target))"""

# 09 write a program and print shallow copy
    #    A shallow copy creates a new outer container (like a new list), but the items inside are not copied. 
    #    both the original and the shallow copy share the same inner items
    #    so ,if you change some thing inside these inner items,both will show the change

# Uses of Shallow Copy :-

# Makes a new outer list (or container) fast.
# Saves memory by sharing inner items.
# Good if inner items won’t change (like numbers or strings).

# UnUses of Shallow Copy :-

# If inner items can change (like lists), changing them affects both copies.
# Not good if you want a completely separate copy.
# Can cause mistakes because inner parts are shared.
"""
import copy

# Original list
original_list = [[1, 2],[3,4]]

# Shallow copy
shallow_copy = copy.copy(original_list)

# Modify the original list
original_list[0][0] = 99

# Print the results
print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)"""


# 10 write a programm and print deep copy
    #  A deep copy creates a completely new object — including copies of everything inside it. The copy is totally independent.
    #  So even if you change the original, the deep copy stays safe and unchanged.

# Uses of Deep Copy:-

# Makes a completely separate copy of everything — outer and inner objects.
# Good when you want to change inner items without affecting the original.
# Helps avoid bugs caused by shared inner objects.

# UnUses of Deep Copy:-

# Slower and uses more memory because it copies everything.
# Not needed if you don’t have nested or mutable inner objects.
# Can be overkill for simple objects without inner objects.


"""
import copy

# Original list with a nested list inside
original_list = [[1,2],[3,4]]

# Deep copy of the list
deep_copy = copy.deepcopy(original_list)

# change deep_copy
deep_copy[0][0] = 99

# Print both lists
print("Original List:", original_list)
print("Deep Copy:", deep_copy)"""

# 11 Find the missing number in a given list of consecutive numbers
"""
def find_missing_number(nums):
    n = len(nums) + 1  # Expected length if no number was missing
    total = n * (n + 1) // 2  # Sum of first n natural numbers
    return total - sum(nums)

# Example usage
numbers = [1, 2, 3, 5, 6, 7]  # Missing 4
print("Missing number:", find_missing_number(numbers))"""

# find the multiple missing numbers in a give list of  consecutive numbers
"""
def find_missing_numbers(nums,full_range_end):
    missing_numbers = []
    for i in range(1,full_range_end+1):
        if i not in nums:
            missing_numbers.append(i)
    return missing_numbers
print(f"missing numbers:",find_missing_numbers([1,2,4,5,8,12],12))"""

# 12 Find common elements between two lists.
"""
a = [1,2,3,4,2,5,6]
b = [2,4,6,8,3,6,7]
c = []
for item in a:
    if item in b and item not in c:
        c.append(item)
print(c)"""

# 13 Check if Two Lists are Identical
"""
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
list3 = [4, 3, 2, 1]

print(list1 == list2)  
print(list1 == list3) """
"""
list1 = [1, 2, 3, 4]
list2 = [4, 3, 2, 1]

print(sorted(list1) == sorted(list2))"""

# 14 Use map() and filter() ,reduce(),with Lambda Functions

# 🗺️ map()
# ✅ Use: To change every item in a list.
# 💡 Think: "Do something to each item."

# 🧹 filter()
# ✅ Use: To keep only items that match a condition.
# 💡 Think: "Keep only what passes the test."

# ➕ reduce()
# ✅ Use: To combine all items into one value.
# 💡 Think: "Add or merge everything into one."


"""
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

from functools import reduce
nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, nums) 
print(total)"""

# 15 find duplicates in array
"""
def find_duplicates(nums):
    return list(set([num for num in nums if nums.count(num) > 1]))

# Example usage:
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(nums))  """

"""
nums = [4, 3, 2, 7, 8, 2, 3, 1]
dup_nums = []
n = len(nums)
for i in range(n):
    for j in range(i+1,n):
        if nums[i] == nums[j]:
            dup_nums.append(nums[i])
print(dup_nums,"duplicate numbers")"""


# 16 write a python program to find  the longest word in sentence

sentence = input("enter a sentence:")
s = sentence.split()
new_sen = ""
for i in s:
    if len(i) > len(new_sen):
        new_sen = i
print(f"{new_sen} is longestword")

# 17 perfect numbers up to 10000:-
# A perfect number is a number where the sum of its divisors (except the number itself) is equal to the number.

# 👉 Example:
# Let's take 6:

# Divisors of 6 (excluding 6): 1, 2, 3

# Sum = 1 + 2 + 3 = 6

# ✅ So, 6 is a perfect number
# 28 → Divisors: 1, 2, 4, 7, 14 → 1 + 2 + 4 + 7 + 14 = 28 ✅
# *Why Initialize result Inside the Loop?*
# 1. Resetting the Sum: By initializing result inside the loop, you reset the sum to 0 for each new number i. This ensures that you're calculating the sum of divisors specifically for each number.
# 2. Accurate Calculation: If you initialize result outside the loop, it would retain its value from the previous iteration, leading to incorrect calculations.


"""
for num in range(1,10000):
    sum = 0
    for i in range (1,num):
        if num % i == 0:
            sum += i
    if num == sum:
        print(f"{num} perfect numbers" )"""
# 17 check if a number is perfect number or not
"""
num = int(input("enter a number:"))
sum = 0
for i in range(1,num):
    if num % i == 0:
        sum += i
if sum == num:
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect numbers")"""
# 18 check if a number is strong number
# A strong number is a number in which the sum of the factorials of its digits equals the number itself.

# For example:
# 145 is a strong number because:
# 1! + 4! + 5! = 1 + 24 + 120 = 145
"""
n = int(input("Enter number: "))
temp = n
sum = 0
while temp > 0:
    d = temp % 10
    f = 1
    for i in range(1, d + 1): f *= i
    sum += f
    temp //= 10
print("Strong Number" if sum == n else "Not a Strong Number")"""

# 19  remove duplicates in list
"""
a = [10,20,10,30,10,10,20,30,10,30]
print(list.set(a))"""# output prints on curly brackets
"""
a[] = [10, 20, 10, 30, 10, 10, 20, 30, 10, 30]
unique = []
for i in a:
    if i not in unique:
        unique.append(i)
print(unique)"""# output prints on square brackets

# 20 Remove duplicates in string
"""
str = input("enter your string:")
s1 = ""
for char in str:
    if char not in s1:
        s1 += char
print(s1)"""



