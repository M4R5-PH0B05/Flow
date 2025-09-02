#REQUIREMENTS
#-what income would you like to manage
#-what category is this Income
#-add option to select an already existing category or create a new category

# IMPORTS
from db import db

#DB connection
CurrentUser = 0#This will be changed to the current user ID when the user acctually uses this code
DBconnection = db()
DBListCurrentCategories = DBconnection.listCustomCategories(userid=CurrentUser,type=0)

#INITIALISATION
Categories = []
for item in DBListCurrentCategories:#takes items in CurrentUser's database and appends them to local Categories List
    Categories.append(item[2])
Categories.append("")

#MAIN
class Income:
    def __init__(self, name, category, price, notes, recurring ,recurringDate,recurringFrequency):#initialse Income class
        self.name = name
        self.category = category
        self.price = price
        self.notes = notes
        self.recurring = recurring
        self.recurringDate = recurringDate
        self.recurringFrequency = recurringFrequency


def CreateIncome():#allows the user to input a new Income
    RecurringDate = None
    RecuranceFrequency = None
    Name = input("Please State the name of your Income : ")
    Category = DisplayCategories()
    DBgetCategoryID = DBconnection.getCategoryID(Category, CurrentUser)
    Price = input("How much is your Income?")
    Recurring = input("Does your Income repeat? (Y/N)")
    if(Recurring.upper() == "Y"):
        RecuranceFrequency, RecurringDate = Recurrence()
    WantsToRemoveCategory = input("Would you like to remove a category? (Y/N)")
    if(WantsToRemoveCategory.upper() == "Y"):
        CategoryName = input("What category would you like to remove?")
        RemoveCategory(CategoryName)
    Notes = input("Anything notes that you want to add? ")
    Income(name = Name, category=Category, price=Price,notes=Notes,recurring=Recurring,recurringDate=RecurringDate,recurringFrequency= RecuranceFrequency)#adds an Income to the Incomes class
    DBaddIncome = DBconnection.addIncome(userID=CurrentUser, amount=Price, category_id=DBgetCategoryID, notes=Notes,
                                           recurring=Recurring, recurringDate=RecurringDate,recurringFrequency= RecuranceFrequency)#adds an Income to the database

def DisplayCategories():#displays categories and returns the place in the array chossen by the user
    global Categories
    for i in range (len(Categories)): # displays all current created categories for this user
        if(Categories[i] != ""):
            print(Categories[i] + " (" + str((i+1)) + ")")
        else:
            print("Create New Category (" + str((i+1)) + ")")#gives the create category option
    Category = int(input("Please Select an option : "))
    if(Category == len(Categories)):#at the end of the categories list there is always an empty slot for create
        # category, when a new one is created the old empty category is removed, the new category is added,
        # and the empty is readded
        CategoryName = CreateCategory()
        Categories.pop()
        Categories.append(CategoryName)
        Categories.append("")
    return Categories[Category-1]

def Recurrence():#deals with repeating Incomes
    RecuranceFrequency = input("How often does your Income repeat? e.g weekly monthly, e.t.c")
    RecurringDate = input("When does your Income repeat? (DD/MM/YYYY)")
    return RecuranceFrequency,RecurringDate


def CreateCategory():#when user creates a new category it will be created here and added to the database for that user
    CategoryName = input("What will this new category be called?")
    DBaddCategory = DBconnection.addCategory(CurrentUser,CategoryName,type=0)
    return CategoryName

def RemoveCategory(CategoryName):#allows the user to remove one of the displayed categories from the database and from next time they list the categories
    DBgetCategoryID = DBconnection.getCategoryID(CategoryName, CurrentUser)
    DBremoveCategory = DBconnection.removeCategory(DBgetCategoryID)

def main():# needs to return -  userID amount category notes recurring recurringDate
    CreateIncome()

main()

