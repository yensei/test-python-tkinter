from tkinter import END, Button, Canvas, E, Entry, Frame, Label, Listbox, Tk, W

import psycopg2

root = Tk()

root.title("Python & PostgreSQL")


def save_new_student(name, age, address):
    conn = psycopg2.connect(
        dbname="tuto_flask_db",
        user="usr_julio",
        password="123",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    query = '''INSERT INTO STUDENTS(name,age, address) VALUES (%s,%s,%s)'''
    cursor.execute(query, (name, age, address))
    print("saved!")
    conn.commit()

    conn.close()
    # refresh list
    display_students()


def display_students():
    conn = psycopg2.connect(
        dbname="tuto_flask_db",
        user="usr_julio",
        password="123",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    query = '''SELECT * FROM students'''
    cursor.execute(query)
    row = cursor.fetchall()
    listbox = Listbox(frame, width=20, height=10)
    listbox.grid(row=10, columnspan=4, sticky=W + E)

    for x in row:
        listbox.insert(END, x)

    conn.close()


def search(id):
    conn = psycopg2.connect(
        dbname="tuto_flask_db",
        user="usr_julio",
        password="123",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    query = '''SELECT * FROM students WHERE id= %s'''
    cursor.execute(query, (id))
    row = cursor.fetchone()
    display_search_result(row)
    conn.close()


def display_search_result(r):
    lb_search = Listbox(frame, width=20, height=2)
    lb_search.grid(row=9, columnspan=4, sticky=W + E)
    lb_search.insert(END, r)


canvas = Canvas(root, height=500, width=400)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text='Add a Student')
label.grid(row=0, column=1)

# Nombre
label = Label(frame, text='Name')
label.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

# Edad
label = Label(frame, text='Age')
label.grid(row=2, column=0)

entry_age = Entry(frame)
entry_age.grid(row=2, column=1)

# Address
label = Label(frame, text='Address')
label.grid(row=3, column=0)

entry_address = Entry(frame)
entry_address.grid(row=3, column=1)


button = Button(frame, text="Add", command=lambda: save_new_student(
    entry_name.get(),
    entry_age.get(),
    entry_address.get()
))
button.grid(row=4, column=1, sticky=W + E)


# Search
label = Label(frame, text="SEARCH DATA")
label.grid(row=5, column=1, sticky=W + E)

label = Label(frame, text="Search by ID")
label.grid(row=6, column=0)

id_search = Entry(frame)
id_search.grid(row=6, column=1)

btn_search = Button(
    frame,
    text="Search",
    command=lambda: search(id_search.get()))
btn_search.grid(row=6, column=2)

display_students()

root.mainloop()
