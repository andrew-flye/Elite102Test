import mysql.connector

cnx = mysql.connector.connect(user = 'root', database = 'banking_app', password = 'password')

cursor = cnx.cursor()

#query = ("SELECT * FROM banking_info")

#cursor.execute(query)

add_account = ("INSERT INTO banking_info"
                "(LName, FName, Account, Pin, Username, Password, Checking, Savings)"
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

account_dave = ('Lopez','David','148134',9876, 'dMoney$$','dragon',0.0,0.50)

#for item in cursor:
#    print(item)

cursor.execute(add_account, account_dave)

cnx.commit()

cursor.close()
cnx.close()
