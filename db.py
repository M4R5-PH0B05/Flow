import psycopg2
# The database class
class db:
    # Create a new database connection
    def __init__(self):
        self.user = 'mars'
        self.password = 'Morgan1206!'
        self.host = '192.168.0.40'
        self.port = '32768'
        self.database = 'Flow'
        self.conn = psycopg2.connect(user=self.user, password=self.password, host=self.host, port=self.port, database=self.database)
        self.cur = self.conn.cursor()

    # Select statement
    def select(self,statement):
        try:
            self.cur.execute(str(statement))
            rows = self.cur.fetchall()
            return rows
        except:
            # 0 - Failed
            return 0

    # Insert statement
    def insert(self,statement):
        try:
            self.cur.execute(str(statement))
            self.conn.commit()
            # 1 - Succeeded
            return 1
        except:
            # 0 - Failed
            return 0

    # Adds an Expense
    def addExpense(self,userID,amount,category_id,notes=None,recurring=False,recurringDate=None,recurringFrequency=None):
        try:
            self.cur.execute("INSERT INTO expenses(userID,amount,category_id,notes,recurring,recurringDate,"
                             "recurringFrequency) VALUES (%s,"
                             "%s,%s,%s,%s,%s,%s)",(userID,amount,category_id,notes,recurring,recurringDate,
                                                recurringFrequency))
            self.conn.commit()
            # 1 - Succeeded
            return 1
        except Exception as e:
            print(e)
            # 0 - Failed
            return 0

    # Returns all of users expenses
    def showExpenses(self,userID):
        try:
            self.cur.execute("SELECT * FROM expenses WHERE userID = %s",(userID))
            rows = self.cur.fetchall()

            return rows
        except Exception as e:
            print(e)
            return 0

    # Adds a new income
    def addIncome(self,userID,amount,category_id,notes=None,recurring=False,recurringDate=None,recurringFrequency=None):
        try:
            self.cur.execute("INSERT INTO incomes(userID,amount,category_id,notes,recurring,recurringDate,"
                             "recurringFrequency) VALUES (%s,"
                             "%s,%s,%s,%s,%s,%s)",(userID,amount,category_id,notes,recurring,recurringDate,
                                                recurringFrequency))
            self.conn.commit()
            # 1 - Succeeded
            return 1
        except Exception as e:
            print(e)
            # 0 - Failed
            return 0

    # Returns all of users incomes
    def showIncomes(self,userID):
        try:
            self.cur.execute("SELECT * FROM incomes WHERE userID = %s",(userID))
            rows = self.cur.fetchall()

            return rows
        except Exception as e:
            print(e)
            return 0

    # Returns users details from the email and password
    def userDetails(self, email,password = None):
        if password != None:
            try:
                self.cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email,password))
                rows = self.cur.fetchall()
                if len(rows) <= 0:
                    return 0
                return rows
            except Exception as e:
                print(e)
                return 0
        else:
            try:
                self.cur.execute("SELECT * FROM users WHERE email = %s", (email,))
                rows = self.cur.fetchall()
                if len(rows) <= 0:
                    return 0
                return rows
            except Exception as e:
                print(e)
                return 0

    # Registers a user
    def registerUser(self, first_name,second_name,email,password):
        try:
            self.cur.execute("INSERT INTO users(first_name,second_name,email,password) VALUES (%s, %s, "
                             "%s,%s)", (first_name,second_name,email,password))
            self.conn.commit()
            # 1 - Succeeded
            return 1
        except Exception as e:
            print(e)
            return 0

    # Changes a password
    def changePassword(self,email,newPassword):
        try:
            self.cur.execute("UPDATE users SET password = %s WHERE email = %s", (newPassword,email))
            self.conn.commit()
            # 1 - Succeeded
            return 1
        except Exception as e:
            print(e)
            return 0

    # Gets the password from the Email
    def selectPassword(self, email):
        try:
            self.cur.execute(f"SELECT password FROM users WHERE email = %s", (email,))
            data = self.cur.fetchone()
            if data == None:
                return 0
            return data
        except Exception as e:
            print(e)
            return 0

    # Adds a new category
    def addCategory(self,userid,category_name,type):
        try:
            self.cur.execute("INSERT INTO categories(userid,category_name,type) VALUES (%s, %s, %s)", (userid,
                                                                                                   category_name,type))
            self.conn.commit()
            # 1 - Succeeded
            return 1
        except Exception as e:
            print(e)
            return 0

    # Removes a category
    def removeCategory(self,category_id):

            try:
                self.cur.execute("DELETE FROM categories WHERE category_id = %s", (category_id,))
                self.conn.commit()
                return 1
            except Exception as e:
                print(e)
                return 0

    # Lists all categories for that user
    def listCustomCategories(self,userid,type):
        try:
            result = self.cur.execute("""
                SELECT * FROM categories
                WHERE (userid = 0 OR userid = %s)
                  AND type = %s
                ORDER BY userid
            """, (userid, type))

            result = self.cur.fetchall()
            return result
        except Exception as e:
            print(e)
            return 0

    # Gets category ID
    def getCategoryID(self,category_name,userid):
        try:
            self.cur.execute(f"SELECT category_id FROM categories WHERE category_name = %s AND userid = %s",
                             (category_name,userid))
            data = self.cur.fetchall()
            return data[0][0]
        except Exception as e:
            print(e)
            return 0

# TESTING
