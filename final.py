import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as a

# ------------------- DATABASE CONNECTION -------------------
try:
    con = a.connect(host="localhost", user="root", passwd=os.getenv("DB_PASSWORD"), database="school")
except a.Error as e:
    messagebox.showerror("Database Error", f"Connection failed: {e}")
    exit()


# ------------------- STUDENT MANAGEMENT -------------------
def add_student():
    def submit():
        n = entry_name.get()
        c = entry_class.get()
        r = entry_roll.get()
        a_ = entry_address.get()
        p = entry_phone.get()

        if not all([n, c, r, a_, p]):
            messagebox.showerror("Error", "All fields are required")
            return

        data = (n, c, r, a_, p)
        sql = 'INSERT INTO student (name,class,roll_no,address,phone) VALUES(%s,%s,%s,%s,%s)'
        cursor = con.cursor()
        cursor.execute(sql, data)
        con.commit()
        messagebox.showinfo("Success", "Student added successfully!")
        add_student_window.destroy()

    add_student_window = tk.Toplevel()
    add_student_window.title("Add Student")

    labels = ["Name:", "Class:", "Roll No:", "Address:", "Phone No:"]
    entries = []
    for i, text in enumerate(labels):
        tk.Label(add_student_window, text=text).grid(row=i, column=0)
        e = tk.Entry(add_student_window)
        e.grid(row=i, column=1)
        entries.append(e)

    entry_name, entry_class, entry_roll, entry_address, entry_phone = entries
    tk.Button(add_student_window, text="Submit", command=submit).grid(row=5, column=1)


def remove_student():
    def submit():
        n = entry_name.get()
        r = entry_roll.get()
        if not n or not r:
            messagebox.showerror("Error", "Enter valid student details")
            return
        data = (n, r)
        sql = 'DELETE FROM student WHERE name=%s AND roll_no=%s'
        cursor = con.cursor()
        cursor.execute(sql, data)
        con.commit()
        messagebox.showinfo("Success", "Student removed successfully!")
        remove_student_window.destroy()

    remove_student_window = tk.Toplevel()
    remove_student_window.title("Remove Student")

    tk.Label(remove_student_window, text="Name:").grid(row=0, column=0)
    tk.Label(remove_student_window, text="Roll No:").grid(row=1, column=0)

    entry_name = tk.Entry(remove_student_window)
    entry_roll = tk.Entry(remove_student_window)
    entry_name.grid(row=0, column=1)
    entry_roll.grid(row=1, column=1)

    tk.Button(remove_student_window, text="Submit", command=submit).grid(row=2, column=1)


def display_students():
    display_window = tk.Toplevel()
    display_window.title("Students")

    canvas = tk.Canvas(display_window)
    scrollbar = tk.Scrollbar(display_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    cursor = con.cursor()
    cursor.execute("SELECT name, class, roll_no, address, phone FROM student")
    students = cursor.fetchall()

    headers = ["Name", "Class", "Roll No", "Address", "Phone"]
    for col, text in enumerate(headers):
        tk.Label(scrollable_frame, text=text, font=("Arial", 12, "bold")).grid(row=0, column=col)

    for index, student in enumerate(students, start=1):
        for col, value in enumerate(student):
            tk.Label(scrollable_frame, text=value).grid(row=index, column=col)

    con.commit()


# ------------------- TEACHER MANAGEMENT -------------------
def add_teacher():
    def submit():
        n = entry_name.get()
        p = entry_post.get()
        s = entry_salary.get()
        ph = entry_phone.get()
        tid = entry_tid.get()

        if not all([n, p, s, ph, tid]):
            messagebox.showerror("Error", "All fields are required")
            return

        data = (n, p, s, ph, tid)
        sql = 'INSERT INTO teacher (Name,Post,Salary,Phone,Teacher_ID) VALUES(%s,%s,%s,%s,%s)'
        cursor = con.cursor()
        cursor.execute(sql, data)
        con.commit()
        messagebox.showinfo("Success", "Teacher added successfully!")
        add_teacher_window.destroy()

    add_teacher_window = tk.Toplevel()
    add_teacher_window.title("Add Teacher")

    labels = ["Name:", "Post:", "Salary:", "Phone:", "Teacher ID:"]
    entries = []
    for i, text in enumerate(labels):
        tk.Label(add_teacher_window, text=text).grid(row=i, column=0)
        e = tk.Entry(add_teacher_window)
        e.grid(row=i, column=1)
        entries.append(e)

    entry_name, entry_post, entry_salary, entry_phone, entry_tid = entries
    tk.Button(add_teacher_window, text="Submit", command=submit).grid(row=5, column=1)


def remove_teacher():
    def submit():
        n = entry_name.get()
        tid = entry_tid.get()
        if not n or not tid:
            messagebox.showerror("Error", "Enter valid teacher details")
            return
        data = (n, tid)
        sql = 'DELETE FROM teacher WHERE Name=%s AND Teacher_ID=%s'
        cursor = con.cursor()
        cursor.execute(sql, data)
        con.commit()
        messagebox.showinfo("Success", "Teacher removed successfully!")
        remove_teacher_window.destroy()

    remove_teacher_window = tk.Toplevel()
    remove_teacher_window.title("Remove Teacher")

    tk.Label(remove_teacher_window, text="Name:").grid(row=0, column=0)
    tk.Label(remove_teacher_window, text="Teacher ID:").grid(row=1, column=0)

    entry_name = tk.Entry(remove_teacher_window)
    entry_tid = tk.Entry(remove_teacher_window)
    entry_name.grid(row=0, column=1)
    entry_tid.grid(row=1, column=1)

    tk.Button(remove_teacher_window, text="Submit", command=submit).grid(row=2, column=1)


def display_teachers():
    display_window = tk.Toplevel()
    display_window.title("Teachers")

    canvas = tk.Canvas(display_window)
    scrollbar = tk.Scrollbar(display_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    cursor = con.cursor()
    cursor.execute("SELECT Name, Post, Salary, Phone, Teacher_ID FROM teacher")
    teachers = cursor.fetchall()

    headers = ["Name", "Post", "Salary", "Phone", "Teacher ID"]
    for col, text in enumerate(headers):
        tk.Label(scrollable_frame, text=text, font=("Arial", 12, "bold")).grid(row=0, column=col)

    for index, teacher in enumerate(teachers, start=1):
        for col, value in enumerate(teacher):
            tk.Label(scrollable_frame, text=value).grid(row=index, column=col)

    con.commit()


# ------------------- FEES MANAGEMENT -------------------
def add_fees():
    def submit_fees():
        roll = entry_roll.get()
        fees_due = entry_fees_due.get()
        fees_paid = entry_fees_paid.get()

        if not all([roll, fees_due, fees_paid]):
            messagebox.showerror("Error", "All fields are required")
            return

        data = (fees_due, fees_paid, roll)
        sql = 'UPDATE student SET fees_due=%s, fees_paid=%s WHERE roll_no=%s'
        cursor = con.cursor()
        cursor.execute(sql, data)
        con.commit()
        messagebox.showinfo("Success", "Fees added successfully!")
        add_fees_window.destroy()

    add_fees_window = tk.Toplevel()
    add_fees_window.title("Add Fees")

    labels = ["Roll No:", "Total Fees Due:", "Fees Paid:"]
    entries = []
    for i, text in enumerate(labels):
        tk.Label(add_fees_window, text=text).grid(row=i, column=0)
        e = tk.Entry(add_fees_window)
        e.grid(row=i, column=1)
        entries.append(e)

    entry_roll, entry_fees_due, entry_fees_paid = entries
    tk.Button(add_fees_window, text="Submit", command=submit_fees).grid(row=3, column=1)


def view_fees():
    view_fees_window = tk.Toplevel()
    view_fees_window.title("View Fees")

    cursor = con.cursor()
    cursor.execute('SELECT roll_no, fees_due, fees_paid FROM student')
    fees_data = cursor.fetchall()

    headers = ["Roll No", "Fees Due", "Fees Paid"]
    for col, text in enumerate(headers):
        tk.Label(view_fees_window, text=text, font=("Arial", 12, "bold")).grid(row=0, column=col)

    for index, row in enumerate(fees_data, start=1):
        for col, value in enumerate(row):
            tk.Label(view_fees_window, text=value).grid(row=index, column=col)


def fees_management():
    fees_window = tk.Toplevel()
    fees_window.title("Fees Management")

    tk.Button(fees_window, text="Add Fees", command=add_fees, width=20).pack(pady=10)
    tk.Button(fees_window, text="View Fees", command=view_fees, width=20).pack(pady=10)


# ------------------- TRANSPORTATION MANAGEMENT -------------------
def add_transportation():
    def submit_transport():
        route_number = entry_route.get()
        bus_number = entry_bus.get()
        driver_name = entry_driver.get()
        stop_name = entry_stop.get()
        roll_no = entry_roll.get()

        if not all([route_number, bus_number, driver_name, stop_name, roll_no]):
            messagebox.showerror("Error", "All fields are required")
            return

        data = (route_number, bus_number, driver_name, stop_name, roll_no)
        sql = 'UPDATE student SET route_number=%s, bus_number=%s, driver_name=%s, stop_name=%s WHERE roll_no=%s'
        cursor = con.cursor()
        cursor.execute(sql, data)
        con.commit()
        messagebox.showinfo("Success", "Transportation route added successfully!")
        add_transport_window.destroy()

    add_transport_window = tk.Toplevel()
    add_transport_window.title("Add Transportation Route")

    labels = ["Route Number:", "Bus Number:", "Driver Name:", "Stop Name:", "Roll No:"]
    entries = []
    for i, text in enumerate(labels):
        tk.Label(add_transport_window, text=text).grid(row=i, column=0)
        e = tk.Entry(add_transport_window)
        e.grid(row=i, column=1)
        entries.append(e)

    entry_route, entry_bus, entry_driver, entry_stop, entry_roll = entries
    tk.Button(add_transport_window, text="Submit", command=submit_transport).grid(row=5, column=1)


def view_transportation():
    view_transport_window = tk.Toplevel()
    view_transport_window.title("View Transportation Routes")

    cursor = con.cursor()
    cursor.execute('SELECT route_number, bus_number, driver_name, stop_name, roll_no FROM student')
    transport_data = cursor.fetchall()

    headers = ["Route No", "Bus No", "Driver Name", "Stop Name", "Roll No"]
    for col, text in enumerate(headers):
        tk.Label(view_transport_window, text=text, font=("Arial", 12, "bold")).grid(row=0, column=col)

    for index, row in enumerate(transport_data, start=1):
        for col, value in enumerate(row):
            tk.Label(view_transport_window, text=value).grid(row=index, column=col)


def transportation_management():
    transport_window = tk.Toplevel()
    transport_window.title("Transportation Management")
    tk.Button(transport_window, text="Add Transportation", command=add_transportation, width=25).pack(pady=10)
    tk.Button(transport_window, text="View Transportation", command=view_transportation, width=25).pack(pady=10)


# ------------------- SEARCH STUDENT -------------------
def search_student():
    def submit_search():
        roll = entry_roll.get()
        if not roll:
            messagebox.showerror("Error", "Enter a valid Roll Number")
            return

        cursor = con.cursor()
        cursor.execute(
            'SELECT name, class, roll_no, address, phone, fees_due, fees_paid, route_number, bus_number, driver_name, stop_name FROM student WHERE roll_no=%s',
            (roll,))
        student_data = cursor.fetchone()

        if student_data:
            result_window = tk.Toplevel()
            result_window.title("Search Result")

            fields = ["Name", "Class", "Roll No", "Address", "Phone", "Fees Due", "Fees Paid", "Route No", "Bus No",
                      "Driver", "Stop Name"]
            for i, field in enumerate(fields):
                tk.Label(result_window, text=f"{field}:").grid(row=i, column=0, sticky="w", padx=10, pady=5)
                tk.Label(result_window, text=student_data[i]).grid(row=i, column=1, sticky="w", padx=10, pady=5)
        else:
            messagebox.showerror("Error", "Student not found!")

    search_window = tk.Toplevel()
    search_window.title("Search Student")
    tk.Label(search_window, text="Roll No:").grid(row=0, column=0)
    entry_roll = tk.Entry(search_window)
    entry_roll.grid(row=0, column=1)
    tk.Button(search_window, text="Search", command=submit_search).grid(row=1, column=1, pady=10)


# ------------------- MAIN GUI -------------------
def setup_window():
    root = tk.Tk()
    root.title("SRINIVASA PUBLIC SCHOOL")
    root.geometry("700x700")
    root.resizable(False, False)
    root.configure(bg="#f0f0f0")
    return root


def create_label_frame(parent):
    f = tk.LabelFrame(parent, text="SCHOOL MANAGEMENT SYSTEM", padx=20, pady=20, bg="#e0e0e0")
    f.grid(row=0, column=0, sticky="nsew")
    parent.grid_rowconfigure(0, weight=1)
    parent.grid_columnconfigure(0, weight=1)
    return f


def create_buttons(parent, button_options):
    button_frame = tk.Frame(parent, bg="#e0e0e0")
    button_frame.grid(row=1, column=0, pady=20, sticky="nsew")
    button_frame.grid_columnconfigure(0, weight=1)

    for i, (text, command) in enumerate(button_options.items()):
        btn = tk.Button(button_frame, text=text, command=command, width=25, bg="#007BFF", fg="white",
                        font=("Arial", 12))
        btn.grid(row=i, column=0, padx=10, pady=5, sticky="ew")


def main():
    button_options = {
        "Add Student": add_student,
        "Remove Student": remove_student,
        "Display Students": display_students,
        "Add Teacher": add_teacher,
        "Remove Teacher": remove_teacher,
        "Display Teachers": display_teachers,
        "Fees Management": fees_management,
        "Transportation Management": transportation_management,
        "Search Student": search_student,
    }

    root = setup_window()
    f = create_label_frame(root)

    # Load placeholder logo
    try:
        img = Image.open("logo.png")  
        t_img = img.resize((150, 150), Image.LANCZOS)
        logo_image = ImageTk.PhotoImage(t_img)
        label = tk.Label(f, image=logo_image, bg="#e0e0e0")
        label.image = logo_image
        label.grid(row=0, column=0, columnspan=2, pady=10)
    except Exception:
        tk.Label(f, text="School Logo", font=("Arial", 14, "bold"), bg="#e0e0e0").grid(row=0, column=0,
                                                                                       columnspan=2, pady=10)

    create_buttons(f, button_options)
    root.mainloop()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")
