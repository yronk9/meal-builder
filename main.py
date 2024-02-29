import tkinter as tk
import sqlite3

def create_database():
	conn = sqlite3.connect("names.db")
	c = conn.cursor()

	c. execute("""CREATE TABLE IF NOT EXISTS names (
		id INTEGER PRIMARY KEY,
		name TEXT
		)""")
	conn.commit()
	conn.close()

def on_submit():
	name = entry.get()
	conn = sqlite3.connect("names.db")
	c = conn.cursor()

	c.execute("INSERT INTO names (name) VALUES (?)", (name,))
	conn.commit()

	update_listbox()
	conn.close()

def clear_box():
	name = entry.get()
	conn = sqlite3.connect("names.db")
	c = conn.cursor()

	c.execute("DELETE FROM names")
	conn.commit()

	update_listbox()
	conn.close()

def update_listbox():
	conn = sqlite3.connect("names.db")
	c = conn.cursor()

	c.execute("SELECT * FROM names")
	rows = c.fetchall()

	listbox.delete(0, tk.END)
	for row in rows:
		listbox.insert(tk.END, row[1])

	conn.close()

create_database()

app = tk.Tk()
app.title("meal builder")
app.geometry("400x300")

label = tk.Label(app, text="enter some food item:")
label.pack()

entry = tk.Entry(app)
entry.pack()

submit_button = tk.Button(app, text="Submit", command=on_submit)
submit_button.pack()

listbox = tk.Listbox(app)
listbox.pack()

update_listbox()

clear = tk.Button(app, text="clear list", command=clear_box)
clear.pack()

# The following centres the app on open
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Calculate half the screen and window sizes
window_width = 400
window_height = 300
half_screen_width = int(screen_width / 2 - window_width / 2)
half_screen_height = int(screen_height / 2 - window_height / 2)

# Set the geometry with calculated coordinates
app.geometry(f"{window_width}x{window_height}+{half_screen_width}+{half_screen_height}")


app.mainloop()
