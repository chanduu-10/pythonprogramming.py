# (basicproject-01) Number guessing game 🔢
"""
import random

number_to_guess = random.randint(1,100)
while True:
  try:
    guess = int(input("Guess the number 1 and 100:"))

    if guess < number_to_guess:
        print("Too Low!")
    elif guess > number_to_guess:
        print("Too High")
    else:
        print("Congratutlations! you guessed the number.")
        break
  except ValueError:
        print("please enter a valid number")"""

# (basicproject - 02) rock_paper_scissor 🗿
"""
import random
choices = ["rock","paper","scissor"]
computer_choice = random.choice(choices)
user_choice = input("choose one of three (rock/paper/scissor/):")
if user_choice == computer_choice :
    print("it's a tie")
elif (user_choice == "rock" and computer_choice == "scissor")or  \
     (user_choice == "paper" and computer_choice == "rock")or  \
     (user_choice == "scissor" and computer_choice == "paper") :
    print("you win! Computer choose",computer_choice)
else:
    print("you Loose! computer choose",computer_choice)"""

# (basicproject - 03) Dice Rolling Simulator ⚂
"""
import random
def roll_dice():
    return random.randint(1,7)
while True:
  roll = input("Roll the dice?(yes/no):" ).lower()
  if roll == "yes":
     print("you rolled",roll_dice())
  else:
     print("thanks for playing")"""

# (basicproject - 04) quiz game 💯
"""
questions = ("How many elements are in the periodic table?:",
             "Which animal lays the largest eggs?:",
             "What is the most abudant gas in the earth's atmosophere?:",
             "How many bones are in the human body?:",
             "Which planet in the solar system in the hottest?:")
options = (("A. 116 ","B. 117 ","C. 118 ","D. 119 "),
           ("A. Whale ","B. Crocodile ","C. Elephant ","D. Ostrich "),
           ("A. Nitrogen ","B. Oxygen ","C. Carbon-Dioxide ","D. Hydrogen "),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Mercury","B. Venus ","C. Earth ","D. Mars"))
answers = ("C","D","A","A","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)


    guess = input("Enter(A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("--------------------------")
print("        RESULTS           ")
print("--------------------------")


print("answers:",end="")
for answer in answers:
    print(answer,end="")
print()

print("guesses:",end="")
for guess in guesses:
    print(guess,end="")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")"""

# (basicproject - 05)money interest
# ✅ 1. Simple Interest (SI) — "Interest only on the original money"
# You earn ₹1.5 per ₹100 per year, so for ₹60,000:

# Year 1 Interest = ₹900,
# Year 2 Interest =₹900
# Year 1 Interest=₹900,Year 2 Interest=₹900
# Total interest = ₹900 + ₹900 = ₹1,800
# Final amount your friend returns = ₹60,000 + ₹1,800 = ₹61,800

# 🧠 Key point: You earn ₹900 every year, because it's always calculated on ₹60,000.


# ✅ 2. Compound Interest (CI) — "Interest on interest"
# In the 1st year, you earn ₹900 (same as SI).

# But in the 2nd year, the interest is calculated on ₹60,900 (₹60,000 + ₹900), not just ₹60,000!

# Let’s see:
# Year 1: ₹60,000 → ₹60,900 (₹900 interest)
# Year 2: ₹60,900 × 1.5% = ₹913.50 interest

# Total CI=₹900+₹913.50=₹1,813.50
# Final amount = ₹60,000 + ₹1,813.50 = ₹61,813.50

# 🧠 Key point: You earn more each year because your interest is added back (compounded).



# (basicproject - 05) Simple Interest Calculator  💵

"""
principal = float(input("Enter your principal amount (₹): "))
rate = float(input("Enter your annual interest rate (%): "))
years = int(input("Enter number of years: "))
months = int(input("Enter number of months: "))
days = int(input("Enter number of days: "))

# Convert total time into years
time = years + (months / 12) + (days / 365)

# Calculate simple interest
simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print(f"\nSimple Interest = ₹{simple_interest:.2f}")
print(f"Total Amount = ₹{total_amount:.2f}")"""


# (basicproject - 06)  compound interest  💵


# Compound Interest Calculator

# Input values
"""
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time in years: "))
n = int(input("Enter the number of times interest is compounded per year: "))

# Convert rate to decimal
rate = rate / 100

# Calculate final amount
amount = principal * (1 + rate / n) ** (n * time)

# Calculate compound interest
compound_interest = amount - principal

# Print results
print(f"\nTotal Amount = ₹{amount:.2f}")
print(f"Compound Interest = ₹{compound_interest:.2f}")"""

# (basicproject - 07) Madlibs game,word game where your create a story by filling in blanks with random words
"""
adjective1 = input("Enter an adjective(description):")
noun1 = input("Enter a noun(person,place,thing):")
adjective2 = input("Enter an adjective(description):")
verb1 = input("Enter a verb ending with'ing'")
adjective3 = input("Enter an adjective(description):")

print(f"Today I went to a {adjective1} zoo.")
print(f'In an exhibit,I saw a {noun1}')
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}")"""

# (basicproject -08) shooping cart  program 🛒
"""
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy(q to quit):")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"enter the price of a {food}:$"))
        foods.append(food)
        prices.append(price)

print("------YOUR CART-------")
for food in foods:
    print(food,end=" ")
for price in prices:
    total += price

print()
print(f"Your total is :${total}")"""

# (basicproject -09)  concession stand program 🍿
"""
menu = {"pizza":90.00,
        "nachos":30.10,
        "popcorn":60.00,
        "fries":45.13,
        "chips":20.00,
        "salad":45.00}
cart = []
total = 0

print("-------MENU---------")
for key,value in menu.items():
    print(f"{key}:${value:2f}")
print("-----------------")

while True:
    food = input("select an item(q to quit):").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("--------YOUR ORDER---------")
for food in cart:
    total += menu.get(food)
    print(food,end=" ")

print()
print(f"Total is :${total:.2f}")"""

# (basicproject -10) Project Title: Personal Expense Tracker App (Console-Based)
"""
import csv
import os

FILENAME = "expenses.csv"

# Initialize CSV if not already present
if not os.path.exists(FILENAME):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Amount", "Description"])

def add_transaction(tr_type, amount, description):
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tr_type, amount, description])
    print("Transaction added successfully!\n")

def view_summary():
    income = 0
    expenses = 0
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row[0] == 'Income':
                income += float(row[1])
            elif row[0] == 'Expense':
                expenses += float(row[1])
    print(f"\nTotal Income: ₹{income:.2f}")
    print(f"Total Expenses: ₹{expenses:.2f}")
    print(f"Balance: ₹{income - expenses:.2f}\n")

def main():
    print("=== Personal Expense Tracker ===")
    while True:
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amt = float(input("Enter income amount: ₹"))
            desc = input("Enter description: ")
            add_transaction("Income", amt, desc)

        elif choice == '2':
            amt = float(input("Enter expense amount: ₹"))
            desc = input("Enter description: ")
            add_transaction("Expense", amt, desc)

        elif choice == '3':
            view_summary()

        elif choice == '4':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()"""

