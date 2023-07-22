import tkinter
from tkinter import ttk
import sv_ttk
import sqlite3

window = tkinter.Tk()
window.title("Aux Inventory")
window.iconbitmap('C:/Users/ryder/python_final_project/companylogofavicon.ico')
window.resizable(width = False, height = False)

frame = tkinter.Frame(window)
frame.pack()

sv_ttk.set_theme("light")

connection = sqlite3.connect("inventoryList.db")

# View Audio Inventory WORKING ON
def viewAudio():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Audio")
    data = cursor.fetchall()
    connection.commit()
    print(data)

# Add Audio Inventory
def addNewAudio():
    cursor = connection.cursor()
    AudioID = int(item_id_entry.get())
    AudioName = item_name_entry.get()
    AudioAmount = int(item_count_spinbox.get())
    cursor.execute("""INSERT INTO Audio(AudioID, AudioName, AudioAmount) VALUES (?,?,?)""", (AudioID, AudioName, AudioAmount))
    connection.commit()

def editAudioAmount():
    cursor = connection.cursor()
    AudioID = int(item_id_entry.get())
    AudioAmount = int(item_count_spinbox.get())
    cursor.execute("""UPDATE Audio SET AudioAmount = ? WHERE AudioID = ?""", (AudioAmount, AudioID))
    connection.commit()

# Remove Audio Inventory
def removeAudio():
    cursor = connection.cursor()
    del_id = int(item_id_entry.get())
    cursor.execute("""DELETE FROM Audio WHERE AudioID = ?""", (del_id,))
    connection.commit()

# Working on this, view inventory function
view_inv_frame = ttk.LabelFrame(frame, text = "View Inventory")
view_inv_frame.grid(row = 0, column = 0, padx = 20, pady = 25)

view_audio_button = ttk.Button(view_inv_frame, text = "View Inventory", command = viewAudio)
view_audio_button.grid(row = 0, column = 0, padx = 15, pady = 15)

#view_audio_button = ttk.Combobox(view_inv_frame, values = ["Audio", "Visual", "Other"])
#view_audio_button.grid(row = 0, column = 0, padx = 15, pady = 15)

# Add Audio
inventory_audio_frame = ttk.LabelFrame(frame, text = "Audio Inventory")
inventory_audio_frame.grid(row = 2, column = 0, padx = 20, pady = 20)

item_info_frame = ttk.LabelFrame(frame, text = "Edit Inventory")
item_info_frame.grid(row = 2, column = 0, padx = 20, pady = 20)

# Product ID
item_id_label = ttk.Label(item_info_frame, text = "Product ID")
item_id_label.grid(row = 2, column = 0)
item_id_entry = ttk.Entry(item_info_frame)
item_id_entry.grid(row = 3, column = 0, padx = 15, pady = 5)

# Item Name
item_name_label = ttk.Label(item_info_frame, text = "Item Name")
item_name_label.grid(row = 2, column = 1)
item_name_entry = ttk.Entry(item_info_frame)
item_name_entry.grid(row = 3, column = 1, padx = 15, pady = 5)

# Item Amount
item_count_label = ttk.Label(item_info_frame, text = "Amount")
item_count_spinbox = ttk.Spinbox(item_info_frame, from_ = 1, to = 1000)
item_count_label.grid(row = 2, column = 2)
item_count_entry = ttk.Entry(item_info_frame)
item_count_spinbox.grid(row = 3, column = 2, padx = 15, pady = 5)

add_audio_button = ttk.Button(item_info_frame, text = "Add New Item", command = addNewAudio)
add_audio_button.grid(row = 4, column = 0, sticky = "news", padx = 15, pady = 10)

edit_audio_button = ttk.Button(item_info_frame, text = "Change Amount", command = editAudioAmount)
edit_audio_button.grid(row = 4, column = 1, sticky = "news", padx = 15, pady = 10)

add_audio_button = ttk.Button(item_info_frame, text = "Delete", command = removeAudio)
add_audio_button.grid(row = 4, column = 2, sticky = "news", padx = 15, pady = 10)

window.mainloop()

connection.close()