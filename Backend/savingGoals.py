###REQUIREMENTS
#how much do you want to save
#notes - what are you saving for (but optional)
#what is the saving goal called
#when you want to achieve the goal by
#take info from the current incomes and calculate how much you must save per week to achieve that goal
#if goal is bigger than total income say you cannot save that amount

###IMPORTS
from db import db
import datetime

#INITIALISATION
CurrentUser = 1#This will be changed to the current user ID when the user acctually uses this code
DBconnection = db()


#MAIN
def createSavingGoal():#asks user for details on thier saving goal
    GoalName = input("What would you like your new saving goal to be called? ")
    GoalAmount = int(input("How much would you like to save? "))
    GoalDeadline = datetime.datetime.strptime(input("When do you want to achieve your goal by? "), "%d/%m/%Y")
    calculateSavingGoal(GoalAmount,GoalDeadline)

def calculateSavingGoal(GoalAmount,GoalDeadline):#caclulates if saving goal is possible given current requirements
    ###TEMP
    #this function will need to calculate the total income in the time period specified
    #TotalIncome = GetIncomes(CurrentDate, GoalDeadline)
    #if(GoalAmount > TotalIncome):
    #   print("You do not have enough income to save this amount in this time frame")
    #else:
    #   Total Days = GoalDeadLines - CurrentDate
    #   PerWeekSaving = round((Total Days / 7),2)
    #   PerMonthSaving = round((Total Days / 30),2)

    test = DBconnection.getSpecificIncome(GoalDeadline)
    print(str(test) + "idk")



def main():
    createSavingGoal()

main()
