# Just a quick back up to copy and paste incase anything goes wrong when changing a lot of thingd

import tkinter
import sqlite3

#Ignore this
#root = tkinter.Tk()
#style = ttk.Style(root)
#root.tk.call("source", "forest-light.tcl")
#style.theme_use("forest-light")

window = tkinter.Tk()
window.state('zoomed')
window.title("Aux Inventory")
window.iconbitmap('C:/Users/ryder/python_final_project/frenchlickresortlogofavicon.ico')

frame = tkinter.Frame(window)
frame.pack()

connection = sqlite3.connect("inventoryList.db")

cursor = connection.cursor()

# View Audio Inventory
def viewAudio():
    cursor.execute("""SELECT * FROM AUDIO""")
    connection.commit()
    connection.close()

# Add Audio Inventory
def addAudio():
    AudioID = int(item_id_entry.get())
    AudioName = item_name_entry.get()
    AudioAmount = int(item_count_spinbox.get())
    cursor.execute("""INSERT INTO Audio(AudioID, AudioName, AudioAmount) VALUES (?,?,?)""", (AudioID, AudioName, AudioAmount))
    connection.commit()
    connection.close()

# Remove Audio Inventory
def removeAudio():
    del_id = int(item_id_entry.get())
    cursor.execute("""DELETE FROM Audio WHERE AudioID = ?""", (del_id,))
    connection.commit()

view_inv_frame = tkinter.LabelFrame(frame, text = "View Inventory")
view_inv_frame.grid(row = 0, column = 0)

view_audio_button = tkinter.Button(frame, text = "View Inventory", command = viewAudio)
view_audio_button.grid(row = 1, column = 0, sticky = "news", padx = 15, pady = 15)

# Add Audio
inventory_audio_frame = tkinter.LabelFrame(frame, text = "Audio Inventory")
inventory_audio_frame.grid(row = 2, column = 0, padx = 20, pady = 20)

item_info_frame = tkinter.LabelFrame(frame, text = "Add Inventory")
item_info_frame.grid(row = 2, column = 0, padx = 20, pady = 20)

# Product ID
item_id_label = tkinter.Label(item_info_frame, text = "Product ID")
item_id_label.grid(row = 2, column = 0)
item_id_entry = tkinter.Entry(item_info_frame)
item_id_entry.grid(row = 3, column = 0)

# Item Name
item_name_label = tkinter.Label(item_info_frame, text = "Item Name")
item_name_label.grid(row = 2, column = 1)
item_name_entry = tkinter.Entry(item_info_frame)
item_name_entry.grid(row = 3, column = 1)

# Item Amount
item_count_label = tkinter.Label(item_info_frame, text = "Amount")
item_count_spinbox = tkinter.Spinbox(item_info_frame, from_ = 1, to = 1000)
item_count_label.grid(row = 2, column = 2)
item_count_entry = tkinter.Entry(item_info_frame)
item_count_spinbox.grid(row = 3, column = 2)

add_audio_button = tkinter.Button(frame, text = "Add", command = addAudio)
add_audio_button.grid(row = 4, column = 0, sticky = "news", padx = 15, pady = 15)

window.mainloop()