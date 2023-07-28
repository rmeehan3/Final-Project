# ... (Existing code)

# View visual inventory
def viewVisual():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Visual")
    data = cursor.fetchall()

    if view_audio_button.cget("text") == "View Inventory":

        inventory_frame.grid(row=1, column=0, padx=20, pady=25)
        view_audio_button.config(text="Close Inventory")

        # Clears existing data from the table
        inventory_tree.delete(*inventory_tree.get_children())
        for item in data:
            inventory_tree.insert("", "end", values=item)
    else:
        inventory_frame.grid_forget()
        view_audio_button.config(text="View Inventory")

# ... (Existing code)

# Add visual inventory
def addNewVisual():
    cursor = connection.cursor()
    VisualID = int(item_id_entry.get())
    VisualName = item_name_entry.get()
    VisualAmount = int(item_count_spinbox.get())
    cursor.execute("""INSERT INTO Visual(VisualID, VisualName, VisualAmount) VALUES (?,?,?)""", (VisualID, VisualName, VisualAmount))
    connection.commit()

# Edit visual inventory
def editVisualAmount():
    cursor = connection.cursor()
    VisualID = int(item_id_entry.get())
    VisualAmount = int(item_count_spinbox.get())
    cursor.execute("""UPDATE Visual SET VisualAmount = ? WHERE VisualID = ?""", (VisualAmount, VisualID))
    connection.commit()

# Remove visual inventory
def removeVisual():
    cursor = connection.cursor()
    del_id = int(item_id_entry.get())
    cursor.execute("""DELETE FROM Visual WHERE VisualID = ?""", (del_id,))
    connection.commit()

# ... (Existing code)

# View visual inventory frame and button
view_visual_button = ttk.Button(frame, text="View Visual Inventory", command=viewVisual)
view_visual_button.grid(row=0, column=1, sticky="news", padx=15, pady=15)

# Add visual item button
add_visual_button = ttk.Button(item_info_frame, text="Add New Visual Item", command=addNewVisual)
add_visual_button.grid(row=4, column=3, sticky="news", padx=15, pady=10)

# Change visual item amount button
edit_visual_button = ttk.Button(item_info_frame, text="Change Visual Amount", command=editVisualAmount)
edit_visual_button.grid(row=4, column=4, sticky="news", padx=15, pady=10)

# Delete visual item button
del_visual_button = ttk.Button(item_info_frame, text="Delete Visual", command=removeVisual)
del_visual_button.grid(row=4, column=5, sticky="news", padx=15, pady=10)

# ... (Existing code)

# Main loop
window.mainloop()

# Close DB connection
connection.close()
