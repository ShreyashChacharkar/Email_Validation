import mysql.connector
import sys

class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host= "localhost", user="root", password="", database = "flipkart_demo")
            self.mycursor = self.conn.cursor()
        except:
            print("Some error occured. Could not connect to database")
            sys.exit(0)
        else:
            print("Connected to database")
            
    def clean_table(self):
        try:
            query = """
            SELECT * FROM user WHERE email LIKE 
            """

            self.mycursor.execute(query)
            self.conn.commit()
        except:
            return -1
        else:
            return 1