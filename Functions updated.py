import sqlite3

connection = sqlite3.connect("inventoryList.db")
cursor = connection.cursor()

def viewSelect():
    print("\n1. View All\n2. View Item\n3. Edit\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        viewAll()
    elif choice == 2:
        viewItem()
    elif choice == 3:
        # Add/Edit functionality (you can implement it as needed)
        pass
    else:
        print("Invalid choice")

def viewAudio():
    print("All Audio Equipment\n---------------------\nNumber\tName\tAmount\n---------------------")
    rows = cursor.execute("SELECT * FROM Audio")
    print(rows.fetchall())

def viewVisual():
    print("All Visual Equipment\n---------------------\nNumber\tName\tAmount\n---------------------")
    rows = cursor.execute("SELECT * FROM Visual")
    print(rows.fetchall())

def addAudioItem():
    a_id = input('Enter ID: ')
    a_name = input('Audio Item:')
    a_amount = input('Quantity:')
    cursor.execute("""
    INSERT INTO Audio(AudioID, AudioName, AudioAmount)
    VALUES (?,?,?)
    """, (a_id, a_name, a_amount))
    connection.commit()
    print('Data entered successfully.')

def addVisualItem():
    v_id = input('Enter ID: ')
    v_name = input('Visual Item:')
    v_amount = input('Quantity:')
    cursor.execute("""
    INSERT INTO Visual(VisualID, VisualName, VisualAmount)
    VALUES (?,?,?)
    """, (v_id, v_name, v_amount))
    connection.commit()
    print('Data entered successfully.')

def delAudioItem():
    del_id = input('Enter ID to delete: ')
    cursor.execute("""DELETE FROM Audio WHERE AudioID = ?""", (del_id,))
    connection.commit()
    print("Item with ID:", del_id, "successfully deleted.")

def delVisualItem():
    del_id = input('Enter ID to delete: ')
    cursor.execute("""DELETE FROM Visual WHERE VisualID = ?""", (del_id,))
    connection.commit()
    print("Item with ID:", del_id, "successfully deleted.")
