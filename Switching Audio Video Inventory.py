import tkinter
from tkinter import ttk
import sv_ttk
import sqlite3

# ... (existing code up to the inventory_display_frame)

# Inventory display frame for video
video_inventory_frame = ttk.LabelFrame(frame, text="Video Inventory")
video_inventory_frame.grid(row=1, column=0, padx=20, pady=25)

video_inventory_tree = ttk.Treeview(video_inventory_frame, columns=("ID", "Name", "Amount"), show="headings", height=10)
video_inventory_tree.grid(row=0, column=0, padx=10, pady=10)

video_inventory_tree.heading("ID", text="ID")
video_inventory_tree.heading("Name", text="Name")
video_inventory_tree.heading("Amount", text="Amount")

video_inventory_scrollbar = ttk.Scrollbar(video_inventory_frame, orient=tkinter.VERTICAL, command=video_inventory_tree.yview)
video_inventory_scrollbar.grid(row=0, column=1, sticky="ns")
video_inventory_tree.config(yscrollcommand=video_inventory_scrollbar.set)

# View video inventory
def viewVideo():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Video")
    data = cursor.fetchall()

    if view_video_button.cget("text") == "View Video Inventory":
        hideAudioInventory()
        video_inventory_frame.grid(row=1, column=0, padx=20, pady=25)
        view_video_button.config(text="Close Video Inventory")

        # Clears existing data from the video inventory table
        video_inventory_tree.delete(*video_inventory_tree.get_children())
        for item in data:
            video_inventory_tree.insert("", "end", values=item)
    else:
        video_inventory_frame.grid_forget()
        view_video_button.config(text="View Video Inventory")

# Hide video inventory on start
def hideVideoInventory():
    video_inventory_frame.grid_remove()

# Refresh video inventory to display new data
def refreshVideoInventory():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Video")
    data = cursor.fetchall()

    # Clear existing data from the video inventory display
    video_inventory_tree.delete(*video_inventory_tree.get_children())
    for item in data:
        video_inventory_tree.insert("", "end", values=item)

# ... (existing code up to the main loop)

# View video inventory frame and button
view_inv_frame = ttk.LabelFrame(frame, text="Inventory")
view_inv_frame.grid(row=0, column=1)
view_video_button = ttk.Button(frame, text="View Video Inventory", command=viewVideo)
view_video_button.grid(row=0, column=1, sticky="news", padx=15, pady=15)

# ... (existing code up to the main loop)

# Refresh video button
refresh_video_button = ttk.Button(video_inventory_frame, text="Refresh", command=refreshVideoInventory)
refresh_video_button.grid(row=1, column=0, padx=10, pady=5)

# ... (existing code up to the main loop)

# Main loop
window.mainloop()

# Close DB connection
connection.close()
