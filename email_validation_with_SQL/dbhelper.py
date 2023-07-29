import mysql.connector
import sys

class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="email")
            self.mycursor = self.conn.cursor()
        except mysql.connector.Error as e:
            print("Some error occurred. Could not connect to the database:", e)
            sys.exit(0)
        else:
            print("Connected to the database")
            
    def clean_table(self):
        try:
            query = """
            SELECT * FROM user WHERE LOWER(EMAIL_ADDR) REGEXP '^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,}$'
            """

            self.mycursor.execute(query)
            data = self.mycursor.fetchall()

            with open("output_file.sql", 'w') as f:
                for row in data:
                    values = ', '.join("'" + str(value) + "'" for value in row)
                    sql_insert_statement = f"INSERT INTO user VALUES ({values});\n"
                    f.write(sql_insert_statement)

            # Close cursor and connection
            self.mycursor.close()
            self.conn.close()
            
        except mysql.connector.Error as e:
            print("MySQL error:", e)
            return -1
        else:
            print("Data retrieved successfully")
            return 1
