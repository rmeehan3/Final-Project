import tkinter
from tkinter import ttk
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

inventory_tree = ttk.Treeview(inventory_frame, columns=("ID", "Name", "Amount"), show="headings", height=10)
inventory_tree.grid(row=0, column=0, padx=10, pady=10)

inventory_tree.heading("ID", text="ID")
inventory_tree.heading("Name", text="Name")
inventory_tree.heading("Amount", text="Amount")

inventory_scrollbar = ttk.Scrollbar(inventory_frame, orient=tkinter.VERTICAL, command=inventory_tree.yview)
inventory_scrollbar.grid(row=0, column=1, sticky="ns")
inventory_tree.config(yscrollcommand=inventory_scrollbar.set)

# View audio inventory
def viewAudio():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Audio")
    data = cursor.fetchall()

    if view_audio_button.cget("text") == "View Inventory":
    
        inventory_frame.grid(row=1, column=0, padx=20, pady=25)
        view_audio_button.config(text="Close Inventory")

        #Clears existing data from the table
        inventory_tree.delete(*inventory_tree.get_children())
        for item in data:
            inventory_tree.insert("", "end", values=item)
    else:
        inventory_frame.grid_forget()
        view_audio_button.config(text="View Inventory")

# Hide inventory on start
def hideAudioInventory():
    inventory_frame.grid_remove()

# Refresh inventory to display new data
def refreshInventory():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Audio")
    data = cursor.fetchall()

    # Clear existing data from display
    inventory_tree.delete(*inventory_tree.get_children())
    for item in data:
        inventory_tree.insert("", "end", values=item)

# Add audio inventory
def addNewAudio():
    cursor = connection.cursor()
    AudioID = int(item_id_entry.get())
    AudioName = item_name_entry.get()
    AudioAmount = int(item_count_spinbox.get())
    cursor.execute("""INSERT INTO Audio(AudioID, AudioName, AudioAmount) VALUES (?,?,?)""", (AudioID, AudioName, AudioAmount))
    connection.commit()

# Edit audio inventory
def editAudioAmount():
    cursor = connection.cursor()
    AudioID = int(item_id_entry.get())
    AudioAmount = int(item_count_spinbox.get())
    cursor.execute("""UPDATE Audio SET AudioAmount = ? WHERE AudioID = ?""", (AudioAmount, AudioID))
    connection.commit()

# Remove audio inventory
def removeAudio():
    cursor = connection.cursor()
    del_id = int(item_id_entry.get())
    cursor.execute("""DELETE FROM Audio WHERE AudioID = ?""", (del_id,))
    connection.commit()

#Calling the hide function to hide the inventory table when the program is first opened (not sure if this is the best way to do this feel free to change)
hideAudioInventory()

# View inventory frame and button
view_inv_frame = ttk.LabelFrame(frame, text = "Inventory")
view_inv_frame.grid(row = 0, column = 0)
view_audio_button = ttk.Button(frame, text="View Inventory", command=viewAudio)
view_audio_button.grid(row=0, column=0, sticky = "news", padx=15, pady=15)

# Edit inventory frame
inventory_audio_frame = ttk.LabelFrame(frame, text = "Inventory")
inventory_audio_frame.grid(row = 2, column = 0, padx = 20, pady = 20)
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

# Add audio item button
add_audio_button = ttk.Button(item_info_frame, text = "Add New Item", command = addNewAudio)
add_audio_button.grid(row = 4, column = 0, sticky = "news", padx = 15, pady = 10)

# Change audio item amount button
edit_audio_button = ttk.Button(item_info_frame, text = "Change Amount", command = editAudioAmount)
edit_audio_button.grid(row = 4, column = 1, sticky = "news", padx = 15, pady = 10)

# Delete audio item button
del_audio_button = ttk.Button(item_info_frame, text = "Delete", command = removeAudio)
del_audio_button.grid(row = 4, column = 2, sticky = "news", padx = 15, pady = 10)

# Refresh button
refresh_button = ttk.Button(inventory_frame, text="Refresh", command=refreshInventory)
refresh_button.grid(row=1, column=0, padx=10, pady=5)

# Main loop
window.mainloop()

# Close DB connection
connection.close()