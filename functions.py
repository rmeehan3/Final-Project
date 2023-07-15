import sqlite3

connection = sqlite3.connect("inventoryList.db")

cursor = connection.cursor()

def viewSelect():
    print("\n1. View All\n2. View Item\n3. Edit\n")
    choice = int(input("Enter your choice: "))

def viewAudio():
    print("All Audio Equipment\n---------------------\nNumber\tName\tAmount\n---------------------")
    rows = cursor.execute("SELECT * FROM Audio")
    print(rows.fetchall())