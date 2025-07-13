# 🔹 Step 1: Why divisible by 4?
# Earth takes about 365.25 days to go around the Sun.

# That extra 0.25 day × 4 = 1 extra day every 4 years.

# So we add a day every 4 years ➝ Leap year.

# 🔸 Step 2: Why not divisible by 100?
# 0.25 is not exact — it’s actually 0.242.

# That means, we are adding too many leap years.

# So we skip leap years that are divisible by 100 to fix this mistake.

# Example: 1900 is divisible by 4 and 100 ➝ ❌ Not a leap year

# 🔹 Step 3: Why divisible by 400 is allowed?
# Skipping all years divisible by 100 removes too many leap years.

# To balance, we say: If the year is divisible by 400, it IS a leap year.

# Example: 2000 is divisible by 400 ➝ ✅ Leap year

# 01 write a programm and print leap year
"""
year = int(input("enter a year:"))
if (year % 4 == 0 and year % 100!= 0) or (year % 400 == 0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")"""

# 02 write a programm and print number of vowels and which vowels are been in your str
"""
str = input("enter a name:")
vowels = "aeiouAEIOU"
count = 0
found_vowels = ""
for char in str:
    if char in vowels:
        count += 1
        found_vowels += char
print(f"total {count} vowels in your str ")
print(f"this letters are found in your str '{found_vowels}',")"""
# 03 write a programm and print factorial programm using recursive function
"""
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))"""
#  write a programm and print factorial proramm using  loop
"""
n = int(input("enter a number:"))
product = 1
for i in range (1,n+1):
    product = product * i
print(f"factorial of {n} is {product}")"""
# 04 write a python program and print Remove duplicates from a list without using set().
"""
a = [1,11,2,2,4,3,2,1,11,23,21,45,23]
unique_list = [] 
for item in a:
    if item not in unique_list:
        unique_list.append(item)
print("a:", a)
print("List after removing duplicates:", unique_list)"""

# using set remove duplicate elements
"""
a = [1,11,2,2,4,3,2,1,11,23,21,45,23]
a1 = set(a)
a2 = sorted(a1)
print(a2)"""

"""
a = [1,11,2,2,4,3,2,1,11,23,21,45,23]
a1 = sorted(list(set(a)))

print(a1)"""

# 05 write a programm and print Reverse a string in Python
"""
str = input("enter your string:")
str1 = str[::-1]
print(str1)"""
# write a program and print Reverse a String without using [::-1] slicing.
"""
str = input("enter your string:")
result = ""
for char in str:
    result = char +result
print(result)"""
# write a program Reverse a String without using in-built functions
"""
def reverse_string(s):
    result=""
    for char in s:
        result = char + result
    return result
print(reverse_string("sajja"))"""
# 06 write a programm and print Check if a string is a palindrome.
"""
str = input("enter your string:")
if str == str[::-1]:
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palidrome")"""
# 07 write a programm and print Fibonacci series using (recursive) ,find fibonacci (7)
"""
def fibonacci_recursive(n):
    
    if n <= 0:
        return 0
    eli# 09 calculatorf n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
fibonacci_recursive(5)"""
# finding first 7 elements fibonacci sereis
"""
def fibonacci_series(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)

# Print first 7 numbers
for n in range(8):
    print(fibonacci_series(n), end=", ")"""

# 08 write a programm and print number of vowels in given string
"""
str = input("enter your string:")
vowels = "aeiouAEIOU"
count = 0
for char in str:
    if char in vowels:
        count += 1
print(f"total number of vowels in your str {count} ")"""

# 09 print duplicate elements only 
"""

my_list = [1,2,32,5,4,11,11,1,5,2]
duplicates = []
n = len(my_list)
for i in range(n):
    for j in range(i+1,n):
        if my_list[i] == my_list[j]:
            duplicates.append(my_list[i])
print(duplicates)"""


# 11 Anagram :- it means An anagram is a word  formed by rearranging the letters of a different word , typically using all the original letters exactly once.
#Examples of Anagrams:
#"listen" → "silent"
#"eleven plus two" → "twelve plus one"
#"dormitory" → "dirty room"
# #Anagrams are often used in word games, puzzles, and cryptography for fun or mental challenges
"""
str1 = input("enter your string:")
str2 = input("enter your string:")
if sorted(str1) == sorted(str2):
    print("it is anagram")
else:
    print("it is not anagram")"""
"""
def anagram(str1,str2):
    return sorted (str1) == sorted(str2)
print(anagram("shannu","nnuash"))
print(anagram("chandu","gopi"))"""
# 12 fibonacci:-The Fibonacci sequence is a famous series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
"""
def fibonacci(n):
    if n == 0:
       return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))"""
# 13 Two Sum Problem
#Given a list of numbers and a target number, return indices of the two numbers that add up to the target.
#Input: nums = [1, 3, 2, 3, 4, 5, 6], target = 6 → Output: [0, 1]
# it prints index pairs instead of value pairs
"""
def two_num_sum(nums, target):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                result.append((i,j))
    return result

# Example usage:
nums = [1, 3, 2, 3, 4, 5, 6]
target = 6
print(two_num_sum(nums, target)) """


# 🔥 The Core Difference:
# Situation	Variable Type	What You Want	Correct Method
# Armstrong number check	int	Number of digits	len(str(num))
# List iteration/indexing	list	Number of elements	len(nums)

# it prints value pairs instead of index pairs
"""
def two_num_sum(nums,target):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                result.append((nums[i],nums[j]))
    return result
nums = [1, 3, 2, 3, 4, 5, 6]
target = 6
print(two_num_sum(nums, target))"""

# 14 finiding average 
"""
str = input("enter your name:")
tel = int(input("enter your telugu marks:"))
eng = int(input("enter your english marks:"))
math = int(input("enter your maths marks:"))
scie = int(input("enter your science marks:"))
print("---------------------------------------")
print(f"Report of {str}")
print("----------------------------------------")
totalmarks = tel+eng + math+ scie
average = totalmarks/5
print(average)
print(f"your total msrks is {totalmarks}")
if totalmarks > 70:
    print(f"your marks is {totalmarks},your  grade is A")
else:
    print("your marks is {totalmarks},your  grade is B")
print("-------------------------------------------")"""
# 15 Bill calculation
"""
Bill = int(input("enter your total bills:"))
print("----------Bill Summary------------")
print(f"original Amount{Bill}:")
Discount = Bill * 80/100
Gst = Discount * 10/100
final_amount =  Discount + Gst
print(f"discount on product: {Discount}")
print(f"GST @ 10% on product:{Gst}")
print(f"final_amount :{final_amount}")"""
# Bill calculation program
"""
total_bill = float(input("Enter your total bill: ₹"))
discount = total_bill * 80/100  #0.80
gst = discount * 10/100         #0.10
final_amount = discount + gst

print("------Bill Summary------")
print(f"Original Amount: ₹{total_bill}")
print(f"Discount on product: ₹{discount}")
print(f"GST @ 10% on product: ₹{gst}")
print(f"Final amount: ₹{final_amount}")"""
# 16 prime number
"""
n= int(input("enter your number:"))
if n <= 1:
      print("it is not prime number")
else:
      for i in range(2,n):
          if n % i == 0:
                  print("it is not prime number")
                  break
      else:
          print("it is prime number")"""
# 17 prime number programm # see difference here else is not straight on if block

n= int(input("enter your number:"))
for i in range(2,n):
    if n % i == 0:
            print("it is not prime number")
            break
else:
        print("it is prime number")
# count prime numbers from 1 to 100
"""
count = 0
prime_numbers = []
for num in range(1,101):
    if num < 2:
        continue
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        count += 1
        prime_numbers.append(num)
print(("Total prime numbers from 1 to 100:", count))
print("Prime numbers:", prime_numbers)"""

# 18  write a programm on  == and is
#== → checks value equality (do the objects have the same value?)
#is → checks identity (are they the same object in memory?)
"""
a = [1,2,3]
b = a
c = [1,2,3]

print(a == c)   # True (same content)
print(a is c)   # False (different memory)
                # True (same memory) 
print(a is b) """  
#19

#✅ 1. What is HCF/GCD? (Highest Common Factor)/(Greatest Common Divisior)
#🧠 Definition:
#HCF is the largest number that can divide both numbers without leaving a remainder.

#📌 Example:lets take 12 and 18
#Factors of 12 = 1, 2, 3, 4, 6, 12
#Factors of 18 = 1, 2, 3, 6, 9, 18
#Common factors = 1, 2, 3, 6
#👉 HCF = 6 (the biggest one)

#HCF(a,b) = HCF(b,a%b)

#✅ 2. What is LCM? (Least Common Multiple)
#🧠 Definition:
#LCM is the smallest number that is a multiple of both numbers.

#📌 Example: lets Take 12 and 18
#Multiples of 12 = 12, 24, 36, 48, ...
#Multiples of 18 = 18, 36, 54, ...
#👉 LCM = 36 (the smallest common one)

#LCM(a,b)= a * b/HCF(a,b)

"""
def HCF(a,b):
    if b != 0:
        return HCF(b,a%b)
    else:
        return a
print(HCF(12,18))"""
"""
def HCF(a, b):
    if b != 0:
        return HCF(b, a % b)
    else:
        return a
def LCM(a, b):
    hcf = HCF(a, b)
    lcm = (a * b) // hcf
    return lcm

print("LCM is:", LCM(12, 18))"""


# 20 print first largest number and  second largest number using methods

"""
def largest_and_secondlargest(nums):
    nums = list(set(nums))           #set(nums) → remove duplicates
    nums.sort()                      #list(set(nums)) → make it sortable,Because after removing duplicates, we want to 👉 And sort() only works on a list, not on a set.
   
    largest = nums[-1]
    second_largest = nums[-2]
    return largest,second_largest


largest,second_largest = largest_and_secondlargest([21,23,544,677,899,433,2,45,45,2,7])
print("Largest:",largest)
print("Second_largest:",second_largest)"""


# print largestnumber and second largestnumber with out using any methods
"""
arr = [21,32,54,67,34,43,12,43,2,1,54,45,65,54,78,76,87,87,54,31,128]
a = 0   # largest number
b = 0   # second largestnumber

for i in arr:
    if i > a:
        b = a   # If i is greater than a (the current largest), we update b to be a (because the old largest becomes the second largest), and then update a to i (the new largest).
        a = i
    elif i > b and i != a:
        b = i
print("Largest number is",a)
print("second largest number is",b)"""


# EXAMPLE OF ELIF CONDITION
# Imagine it like this:
# You have two boxes:

# Box A holds the largest number
# Box B holds the second largest number

# You look at a new number i.

# First, if i is bigger than Box A, you move Box A’s number to Box B, and put i into Box A (that’s the if part).

# But if i is NOT bigger than Box A, you check if i can go into Box B:

# Is it bigger than what’s currently in Box B?
# And is it not the same as what’s in Box A?

# If yes, put it into Box B (this is your elif).





# AIM OF ELIF CONDITION IS MANILY
# ✅ Yes — the elif i > b and i != a: condition helps:

# Skip duplicate values of the largest number
# Find the second largest number




#  print largestnumber and second largestnumber and thrid largest  with out using any methods
"""
arr = [1,2,2,12,21,12,1,2,12,13,15,38,45,36,63,36,45,45,39]
a = 0
b = 0
c = 0
for i in arr:
    if i > a:
        c = b
        b = a
        a = i
        
    elif i > b  and i != a:
        b = i
    elif i > c and i != a and i != b:
        c = i
print(a,"first largest number")
print(b,"second largest number")
print(c,"thrid largest number")"""