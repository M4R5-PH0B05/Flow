# IMPORTS
from db import db


#Requirements
#-what expense would you like to manage
#-what category is this expense (eventually making own category
#-add option to select an already existing category or create a new category

#variables
Categories = ["Food","Rent","Clothing", "Toiletries","Electronics","Entertainment", ""]

class Expense:
    def __init__(self, name, category, price, notes, recurring ,recurringDate):#initialse Expense class
        self.name = name
        self.category = category
        self.price = price
        self.notes = notes
        self.recurring = recurring
        self.recurringDate = recurringDate


def CreateExpense():#allows the user to input a new expense
    Name = input("Please State the name of your expense : ")
    DisplayCategories()
    Price = input("How much is your expense?")
    Recurring = input("Does your expense repeat? (Y/N)")
    RecurringDate = input("When does your expense repeat? (DD/MM/YYYY)")# Notes = input("Anything notes that you want to add? ")
    Expense(Name,Category,Priceotes,Recurring,Recurring)#add para names here


def DisplayCategories():
    global Categories
    for i in range (len(Categories)): # displays all current created categories for this user
        if(Categories[i] != ""):
            print(Categories[i] + " (" + str((i+1)) + ")")
        else:
            print("Create New Category (" + str((i+1)) + ")")
    Category = input("Please Select an option : ")
    if(Category == str(len(Categories))):#at the end of the categories list there is always an empty slot for create
        # category, when a new one is created the old empty category is removed, the new category is added,
        # and the empty is readded
        CategoryName = CreateCategory()
        Categories.pop()
        Categories.append(CategoryName)
        Categories.append("")


def CreateCategory():#when user creates a new category it will be created here
    CategoryName = input("What will this new category be called?")
    return CategoryName


def main():# needs to return -  userID amount category notes recurring recurringDate
    CreateExpense()

main()



### Morgan random database commands I need to use later

# Make DB object - connection = db()
# Add a new expense - addExpense = connection.addExpense(userID, amount, category, notes, recurring, recurringdate)
# Show all expenses - expenses = connection.showExpenses(str(userID))

