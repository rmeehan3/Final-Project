import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import sv_ttk
import sqlite3

# Creating main window
window = tkinter.Tk()
window.title("Aux Inventory")
window.iconbitmap('companylogofavicon.ico')
window.resizable(width = False, height = False)
frame = tkinter.Frame(window)
frame.pack()
# Theme
sv_ttk.set_theme("light")
# DB connection
connection = sqlite3.connect("inventoryList.db")

#Inventory display frame
inventory_frame = ttk.LabelFrame(frame, text="Inventory")
inventory_frame.grid(row=1, column=0, padx=20, pady=25)

inventory_tree = ttk.Treeview(inventory_frame, columns=("ID", "Name", "Amount", "Type"), show="headings", height=5)
inventory_tree.grid(row=0, column=0, padx=10, pady=10)

inventory_tree.heading("ID", text="ID")
inventory_tree.heading("Name", text="Name")
inventory_tree.heading("Amount", text="Amount")
inventory_tree.heading("Type", text="Type")

inventory_scrollbar = ttk.Scrollbar(inventory_frame, orient=tkinter.VERTICAL, command=inventory_tree.yview)
inventory_scrollbar.grid(row=0, column=1, sticky="ns")
inventory_tree.config(yscrollcommand=inventory_scrollbar.set)

# View Item inventory
def viewItem():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Item")
    data = cursor.fetchall()

    if view_Item_button.cget("text") == "View Inventory":
    
        inventory_frame.grid(row=1, column=0, padx=20, pady=25)
        view_Item_button.config(text="Close Inventory")

        #Clears existing data from the table
        inventory_tree.delete(*inventory_tree.get_children())
        for item in data:
            inventory_tree.insert("", "end", values=item)
    else:
        inventory_frame.grid_forget()
        view_Item_button.config(text="View Inventory")

# Hide inventory on start
def hideItemInventory():
    inventory_frame.grid_remove()

# Refresh inventory to display new data
def refreshInventory():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Item")
    data = cursor.fetchall()

    # Clear existing data from display
    inventory_tree.delete(*inventory_tree.get_children())
    for item in data:
        inventory_tree.insert("", "end", values=item)

# Add Item inventory
def addNewItem():
    cursor = connection.cursor()
    ItemID = int(item_id_entry.get())
    ItemName = item_name_entry.get()
    ItemAmount = int(item_count_spinbox.get())
    ItemType = clicked.get()

    if item_name_entry.get() == '':
        messagebox.showerror("Invalid", "Please fill out all fields.")
    elif ItemAmount <= 0:
        messagebox.showerror("Invalid", "Please fill out all fields.")
    elif clicked.get() == "Select":
        messagebox.showerror("Invalid", "Please fill out all fields.")
    else:
        cursor.execute("""INSERT INTO Item(ItemID, ItemName, ItemAmount, ItemType) VALUES (?,?,?,?)""", (ItemID, ItemName, ItemAmount, ItemType))
        connection.commit()
        messagebox.showinfo("Aux Inventory", "Item added to inventory.\nRefresh to view.")

# Edit Item inventory
def editItemAmount():
    cursor = connection.cursor()
    ItemID = int(item_id_entry.get())
    ItemAmount = int(item_count_spinbox.get())
    cursor.execute("""UPDATE Item SET ItemAmount = ? WHERE ItemID = ?""", (ItemAmount, ItemID))
    connection.commit()
    messagebox.showinfo("Aux Inventory", "Amount updated.\nRefresh to view changes.")

# Remove Item inventory
def removeItem():
    cursor = connection.cursor()
    del_id = int(item_id_entry.get())
    cursor.execute("""DELETE FROM Item WHERE ItemID = ?""", (del_id,))
    connection.commit()
    messagebox.showinfo("Aux Inventory", "Item deleted.\nRefresh to view changes.")

def changeItemName():
    cursor = connection.cursor()
    change_ID = int(item_id_entry.get())
    ItemName = item_name_entry.get()
    cursor.execute("""UPDATE Item SET ItemName = ? WHERE ItemID = ?""", (ItemName, change_ID))
    messagebox.showinfo("Aux Inventory", "Item name changed.\nRefresh to view changes.")

#Calling the hide function to hide the inventory table when the program is first opened (not sure if this is the best way to do this feel free to change)
hideItemInventory()

# View inventory frame and button
view_inv_frame = ttk.LabelFrame(frame, text = "Inventory")
view_inv_frame.grid(row = 0, column = 0)
view_Item_button = ttk.Button(frame, text="View Inventory", command=viewItem)
view_Item_button.grid(row=0, column=0, sticky = "news", padx=10, pady=10)

# Edit inventory frame
inventory_Item_frame = ttk.LabelFrame(frame, text = "Inventory")
inventory_Item_frame.grid(row = 2, column = 0, padx = 20, pady = 20)
item_info_frame = ttk.LabelFrame(frame, text = "Edit Inventory")
item_info_frame.grid(row = 2, column = 0, padx = 20, pady = 20)

# Product ID label
item_id_label = ttk.Label(item_info_frame, text = "Product ID")
item_id_label.grid(row = 2, column = 0)
# Get ID
item_id_entry = ttk.Entry(item_info_frame)
item_id_entry.grid(row = 3, column = 0, padx = 15, pady = 5)

# Item name label
item_name_label = ttk.Label(item_info_frame, text = "Item Name")
item_name_label.grid(row = 2, column = 1)
# Get name
item_name_entry = ttk.Entry(item_info_frame)
item_name_entry.grid(row = 3, column = 1, padx = 15, pady = 5)

# Item amount label
item_count_label = ttk.Label(item_info_frame, text = "Amount")
item_count_spinbox = ttk.Spinbox(item_info_frame, from_ = 1, to = 1000)
item_count_label.grid(row = 2, column = 2)
# Get amount
item_count_entry = ttk.Entry(item_info_frame)
item_count_spinbox.grid(row = 3, column = 2, padx = 15, pady = 5)

# Add Item item button
add_Item_button = ttk.Button(item_info_frame, text = "Add New Item", command = addNewItem)
add_Item_button.grid(row = 4, column = 0, sticky = "news", padx = 15, pady = 10)

# Change Item item amount button
edit_Item_button = ttk.Button(item_info_frame, text = "Change Amount", command = editItemAmount)
edit_Item_button.grid(row = 4, column = 1, sticky = "news", padx = 15, pady = 10)

change_Item_name_button = ttk.Button (item_info_frame, text = "Change Name", command = changeItemName)
change_Item_name_button.grid(row = 4, column = 2, sticky = "news", padx = 15, pady =10)

# Delete Item item button
del_Item_button = ttk.Button(item_info_frame, text = "Delete Item", command = removeItem)
del_Item_button.grid(row = 4, column = 3, sticky = "news", padx = 15, pady = 10)

clicked = StringVar()

clicked.set("Select")

type_options = ["Select", "Audio", "Visual", "Other"]

item_type_label = ttk.Label(item_info_frame, text = "Type")
item_type_label.grid(row = 2, column = 3)
item_type_dropdown = ttk.OptionMenu(item_info_frame, clicked, *type_options)
item_type_entry = ttk.Entry(item_info_frame, text = "Type")
item_type_dropdown.grid(row = 3, column = 3, sticky = "news", padx = 15, pady = 10)

# Refresh button
refresh_button = ttk.Button(inventory_frame, text="Refresh", command = refreshInventory)
refresh_button.grid(row=1, column=0, padx=5, pady=10)

# Main loop
window.mainloop()

# Close DB connection
connection.close()