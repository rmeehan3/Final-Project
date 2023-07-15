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

def addAudioItem():
    a_id = input('Enter ID: ')
    a_name = input('Audio Item:')
    a_amount = input('Quantity:')
    cursor.execute("""
    INSERT INTO Audio(AudioID, AudioName, AudioAmount)
    VALUES (?,?,?)
    """, (a_id, a_name, a_amount))
    connection.commit ()
    print ( 'Data entered successfully.' )