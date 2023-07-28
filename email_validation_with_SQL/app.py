import sys
from dbhelper import DBhelper

class Email:
    def __init__():
        #connect to database
        self.db = DBhelper()
        
    def clean_table(self):
        
        response = self.db.clean_table()
        
        if response:
            print("Registration sucessful")
        else:
            print("Registration Failed ")
        self.clean_table()