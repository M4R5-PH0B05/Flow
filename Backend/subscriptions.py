# IMPORTS
from db import db
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from typing import List
# MAIN BODY


# Create a new subscription
class subscription:
    # Initialise Values
    def __init__(self,userid,name,renewalFrequency,nextDate,amount,category,notes):
        self.userid = userid # User ID that the subscription belongs to
        self.name = name # Name of Subscription
        self.renewalFrequency = renewalFrequency # E.G. Monthly, Weekly, Yearly
        self.nextDate = nextDate # When does it next renew, e.g. 04/10/25
        self.amount = amount # How much does it cost
        self.category = category # Food, Leisure, etc..
        self.notes = notes # Any Notes
        self.dates = [] # All Future Dates


    # Write subscription to the database
    def createSubscription(self):
        try:
            self.calculateRenewalDates()
            # Create a new DB connection
            connection = db() # (self,userid,amount,category,notes,nextDate,dates,name):
            # Add the subscription
            connection.addSubscription(self.userid,self.amount,self.category,self.notes,self.nextDate,self.dates,
                                       self.name,self.renewalFrequency)
            print("Sucessfully created subscription.")
        except Exception as e:
            print(f"Could not create subscription. Exception was: {e}")

    # A function to calculate when subscriptions will be renewed
    def calculateRenewalDates(self):
        # Add the first renewal date
        self.dates = [self.nextDate.strftime("%d/%m/%Y")]
        # Calculate 1 - x dates ( amount of dates ) Default: 12
        for i in range(1,12 +1):
            # Calculate if its for weekly
            if self.renewalFrequency.lower() == "weekly":
                nextDate = self.nextDate + relativedelta(weeks=i)
            # Monthly
            elif self.renewalFrequency.lower() == "monthly":
                nextDate = self.nextDate + relativedelta(months=i)
            # Annually
            elif self.renewalFrequency.lower() == "annually":
                nextDate = self.nextDate + relativedelta(years=i)
            # If monthly annually or weekly were not entered, raise an error
            else:
                raise ValueError("Invalid renewal frequency")

            # Add them to the list of dates
            self.dates.append(nextDate.strftime("%d/%m/%Y"))

        # Return the list of dates
        # return self.dates

    # Converts the string date into a date object
    @staticmethod
    def convertDate(date):
        return datetime.strptime(date, "%d/%m/%Y")


    # Make a new subscription object out of the results of the database
    @staticmethod
    def makeSubscription(new_details):
        sub = subscription(new_details[1],new_details[7],new_details[8],new_details[5],new_details[2],new_details[3],new_details[4])
        return sub




# Testing

# # Create a new subscription
# spotify = subscription(1,"Adobe","Annually",subscription.convertDate("1/09/2025"),250,'Entertainment',None)
# #
# # # Create the subscription
# spotify.createSubscription()

# List the details of a given subscription
connection = db()
details = connection.getSubscriptionDetails("Adobe",1)
object = subscription.makeSubscription(details[0])
print(object.nextDate)