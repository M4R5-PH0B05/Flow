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
    def addExpense(self,userID,amount,category,notes=None,recurring=False,recurringDate=None):
        try:
            self.cur.execute("INSERT INTO expenses(userID,amount,category,notes,recurring,recurringDate) VALUES (%s,%s,%s,%s,%s,%s)",(userID,amount,category,notes,recurring,recurringDate))
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

    # Adds an Income
    def addIncome(self, userID, amount, category, notes=None, recurring=False, recurringDate=None):
        try:
            self.cur.execute("INSERT INTO incomes(userID,amount,category,notes,recurring,recurringDate) VALUES (%s,%s,%s,%s,%s,%s)",(userID,amount,category,notes,recurring,recurringDate))
            self.conn.commit()
            # 1 - Succeeded
            return 1
        except Exception as e:
            print(e)
            return 0

    # Returns all of users Incomes
    def showIncomes(self, userID):
        try:
            self.cur.execute("SELECT * FROM incomes WHERE userID = %s", (userID))
            rows = self.cur.fetchall()
            return rows
        except Exception as e:
            print(e)
            return 0
        
    # Returns users details from the email and password
    def userDetails(self, email,password):
        try:
            self.cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email,password))
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
