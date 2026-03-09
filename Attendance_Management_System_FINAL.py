from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="butterfly",
    database="attendance_system"
)
cursor = mydb.cursor()


root = Tk()
root.title("Attendance Management System")
root.geometry("650x500")
root.configure(bg="#f2f2f2")

Label(root, text="Attendance Management System",
      font=("Arial", 18, "bold"),
      bg="#f2f2f2").pack(pady=20)


def add_student():
    win = Toplevel(root)
    win.title("Add Student")
    win.geometry("350x300")

    Label(win, text="Student Name").pack(pady=5)
    name_entry = Entry(win)
    name_entry.pack()

    Label(win, text="Department").pack(pady=5)
    dept_entry = Entry(win)
    dept_entry.pack()

    Label(win, text="Year (1/2/3)").pack(pady=5)
    year_entry = Entry(win)
    year_entry.pack()

    def save():
        name = name_entry.get()
        dept = dept_entry.get()
        year = year_entry.get()

        if not name or not dept or not year:
            messagebox.showerror("Error", "All fields required!")
            return

        cursor.execute(
            "INSERT INTO student (name, department, year) VALUES (%s,%s,%s)",
            (name, dept, year)
        )
        mydb.commit()
        messagebox.showinfo("Success", "Student Added!")
        win.destroy()

    Button(win, text="Save", command=save).pack(pady=15)


def mark_attendance():
    win = Toplevel(root)
    win.title("Mark Attendance")
    win.geometry("400x400")

    
    Label(win, text="Select Student").pack(pady=5)
    cursor.execute("SELECT student_id, name FROM student")
    students = cursor.fetchall()
    student_dict = {f"{row[1]} (ID:{row[0]})": row[0] for row in students}
    student_combo = ttk.Combobox(win, values=list(student_dict.keys()), state="readonly")
    student_combo.pack()

    
    Label(win, text="Select Subject").pack(pady=5)
    cursor.execute("SELECT subject_id, subject_name FROM subject")
    subjects = cursor.fetchall()
    subject_dict = {f"{row[1]} (ID:{row[0]})": row[0] for row in subjects}
    subject_combo = ttk.Combobox(win, values=list(subject_dict.keys()), state="readonly")
    subject_combo.pack()

    Label(win, text="Date (YYYY-MM-DD)").pack(pady=5)
    date_entry = Entry(win)
    date_entry.pack()

    Label(win, text="Status").pack(pady=5)
    status_combo = ttk.Combobox(win, values=["Present", "Absent"], state="readonly")
    status_combo.pack()

    def save():
        if not student_combo.get() or not subject_combo.get() or not date_entry.get() or not status_combo.get():
            messagebox.showerror("Error", "All fields required!")
            return

        student_id = student_dict[student_combo.get()]
        subject_id = subject_dict[subject_combo.get()]
        date = date_entry.get()
        status = status_combo.get()

        
        cursor.execute("""
            SELECT * FROM attendance
            WHERE student_id=%s AND subject_id=%s AND date=%s
        """, (student_id, subject_id, date))

        if cursor.fetchone():
            messagebox.showerror("Error", "Attendance already marked!")
            return

        cursor.execute("""
            INSERT INTO attendance (student_id, subject_id, date, status)
            VALUES (%s,%s,%s,%s)
        """, (student_id, subject_id, date, status))
        mydb.commit()

        messagebox.showinfo("Success", "Attendance Marked!")
        win.destroy()

    Button(win, text="Save", command=save).pack(pady=20)


def view_students():
    win = Toplevel(root)
    win.title("Student Records")
    win.geometry("600x400")

    tree = ttk.Treeview(win, columns=("ID","Name","Dept","Year"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Dept", text="Department")
    tree.heading("Year", text="Year")

    cursor.execute("SELECT * FROM student")
    for row in cursor.fetchall():
        tree.insert("", END, values=row)

    tree.pack(fill=BOTH, expand=True)


def view_attendance():
    win = Toplevel(root)
    win.title("Attendance Records")
    win.geometry("800x400")

    tree = ttk.Treeview(win, columns=("Name","Subject","Date","Status"), show="headings")
    tree.heading("Name", text="Student Name")
    tree.heading("Subject", text="Subject")
    tree.heading("Date", text="Date")
    tree.heading("Status", text="Status")

    cursor.execute("""
        SELECT s.name, sub.subject_name, a.date, a.status
        FROM attendance a
        JOIN student s ON a.student_id = s.student_id
        JOIN subject sub ON a.subject_id = sub.subject_id
    """)

    for row in cursor.fetchall():
        tree.insert("", END, values=row)

    tree.pack(fill=BOTH, expand=True)


def search_attendance():
    win = Toplevel(root)
    win.title("Search Attendance")
    win.geometry("500x400")

    Label(win, text="Enter Student ID").pack(pady=5)
    entry = Entry(win)
    entry.pack()

    tree = ttk.Treeview(win, columns=("Subject","Date","Status"), show="headings")
    tree.heading("Subject", text="Subject")
    tree.heading("Date", text="Date")
    tree.heading("Status", text="Status")
    tree.pack(fill=BOTH, expand=True)

    def search():
        tree.delete(*tree.get_children())
        cursor.execute("""
            SELECT sub.subject_name, a.date, a.status
            FROM attendance a
            JOIN subject sub ON a.subject_id = sub.subject_id
            WHERE a.student_id=%s
        """, (entry.get(),))
        for row in cursor.fetchall():
            tree.insert("", END, values=row)

    Button(win, text="Search", command=search).pack(pady=10)

def report_summary():
    win = Toplevel(root)
    win.title("Report Summary")
    win.geometry("400x300")

    Label(win, text="Enter Student ID").pack(pady=5)
    entry = Entry(win)
    entry.pack()

    def generate():
        student_id = entry.get()

        cursor.execute("""
            SELECT COUNT(*) FROM attendance
            WHERE student_id=%s
        """, (student_id,))
        total = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*) FROM attendance
            WHERE student_id=%s AND status='Present'
        """, (student_id,))
        present = cursor.fetchone()[0]

        percentage = (present / total * 100) if total > 0 else 0

        messagebox.showinfo("Report",
                            f"Total Classes: {total}\n"
                            f"Present: {present}\n"
                            f"Attendance %: {percentage:.2f}%")

    Button(win, text="Generate Report", command=generate).pack(pady=15)


Button(root, text="Add Student", width=25, height=2, command=add_student).pack(pady=5)
Button(root, text="Mark Attendance", width=25, height=2, command=mark_attendance).pack(pady=5)
Button(root, text="View Students", width=25, height=2, command=view_students).pack(pady=5)
Button(root, text="View Attendance", width=25, height=2, command=view_attendance).pack(pady=5)
Button(root, text="Search Attendance", width=25, height=2, command=search_attendance).pack(pady=5)
Button(root, text="Report Summary", width=25, height=2, command=report_summary).pack(pady=5)
Button(root, text="Exit", width=25, height=2, command=root.destroy).pack(pady=15)

root.mainloop()
