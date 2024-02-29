import PySimpleGUI as sg
import sqlite3

def create_database():
    conn = sqlite3.connect("names.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS names (
		id INTEGER PRIMARY KEY,
		name TEXT
		)""")
    conn.commit()
    conn.close()

def on_submit():
    name = input_field.get()
    conn = sqlite3.connect("names.db")
    c = conn.cursor()

    c.execute("INSERT INTO names (name) VALUES (?)", (name,))
    conn.commit()

    update_listbox()
    input_field.update('') # Clear the input field here
    conn.close()

def clear_box():
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

    listbox.Update(values=[row[1] for row in rows])

    conn.close()

create_database()

layout = [
    [sg.Text("Enter Food:"), input_field := sg.Input(key="-INPUT-")],
    [submit_button := sg.Button("Submit"), clear_button := sg.Button("Clear List")],
    [listbox := sg.Listbox(values=[], key="-LISTBOX-", size=(40, 10), font="Helvetica 16")]
]

# Build the Window
window = sg.Window("Meal Builder", layout, finalize=True)

# Load the listbox content initially
update_listbox()

while True:
    event, values = window.read()
    
    if event in (None, "Exit"):
        break
    elif event == "-INPUT-":
        pass
    elif event == "Submit":
        on_submit()
        input_field.set_focus() # Return focus to the Input field
    elif event == "Clear List":
        clear_box()

window.Close()
