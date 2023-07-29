from dbhelper import DBhelper

class Email_validation:
    def __init__(self):
        #connect to database
        self.db = DBhelper()
        
    def clean_table(self):
        response = self.db.clean_table()
        if response:
            print("Cleaning of dataset complete")
        else:
            print("Some error occured")
            
obj = Email_validation()
obj.clean_table()