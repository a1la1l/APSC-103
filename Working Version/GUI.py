from LOAN import process_loan, get_equipment_list_with_stock
from LOGIN import verifyLogin
from RETURN import get_open_loans, process_return
from tkinter import ttk
from DATA import get_table_data
from LOGIN import hash
from ADMIN import (add_equipment, remove_equipment, get_all_equipment,
                   add_icon, remove_icon, get_icon_usernames,
                   get_all_records, update_record, delete_record)

import tkinter as tk
from datetime import datetime


LARGE_FONT= ("Verdana", 12)


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.current_user = None

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (generateMainUI, adminLogin, iConLogin, iConMainUI, adminMainUI, loanUI, returnUI, dataAnalysisUI, addEquipmentUI, removeEquipmentUI, addiConUI, removeiConUI, changeAdminPasswordUI, editRecordsUI):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        self.geometry("1920x1080")
        self.show_frame(generateMainUI)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class generateMainUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Admin login",
                            command=lambda: controller.show_frame(adminLogin))
        button.pack(padx=150, pady=150)

        button2 = tk.Button(self, text="iCon login",
                            command=lambda: controller.show_frame(iConLogin))
        button2.pack()


class adminLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Admin login", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        label2 = tk.Label(self, text="Enter your admin username", font=LARGE_FONT)
        label2.place(x=100,y=200,)

        self.username_entry = tk.Entry(self)
        self.username_entry.place(x=400, y=205)

        label3 = tk.Label(self, text="Enter your admin password", font=LARGE_FONT)
        label3.place(x=100,y=300,)

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.place(x=400, y=305)

        self.error_label = tk.Label(self, text="", fg="red", font=LARGE_FONT)
        self.error_label.place(x=100, y=350)

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame(generateMainUI))
        button1.place(x=25,y=25)

        button2 = tk.Button(self, text="Login",
                            command=self.check_admin_login)
        button2.place(x=100,y=400)

    def check_admin_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if verifyLogin(username, password, False):
            self.error_label.config(text="")
            self.controller.show_frame(adminMainUI)
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            self.error_label.config(text="Invalid username or password")


class iConLogin(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="iCon login", font=LARGE_FONT)
        label1.pack(pady=10,padx=10)

        label2 = tk.Label(self, text="Enter your iCons username", font=LARGE_FONT)
        label2.place(x=100,y=200,)

        self.username_entry = tk.Entry(self)
        self.username_entry.place(x=400, y=205)

        label3 = tk.Label(self, text="Enter your iCons password", font=LARGE_FONT)
        label3.place(x=100,y=300,)

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.place(x=400, y=305)

        self.error_label = tk.Label(self, text="", fg="red", font=LARGE_FONT)
        self.error_label.place(x=100, y=350)

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame(generateMainUI))
        button1.place(x=25,y=25)

        button2 = tk.Button(self, text="Login",
                            command=self.check_login)
        button2.place(x=100,y=400)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if verifyLogin(username, password, True):
            self.error_label.config(text="")
            self.controller.current_user = username
            self.controller.show_frame(iConMainUI)
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            self.error_label.config(text="Invalid username or password")


class iConMainUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label1 = tk.Label(self, text="iCon Main UI", font=LARGE_FONT)
        label1.pack(pady=10,padx=10)
        

        button1 = tk.Button(self, text="Loan",
                            command=lambda: controller.show_frame(loanUI))
        button1.place(x=100,y=200,)

        button2 = tk.Button(self, text="Return",
                            command=lambda: controller.show_frame(returnUI))
        button2.place(x=900,y=200,)

        button3 = tk.Button(self, text="Data analysis",
                            command=lambda: controller.show_frame(dataAnalysisUI))
        button3.place(x=500,y=200,)

        button4 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame(iConLogin))
        button4.place(x=25,y=25)


class loanUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Loan UI", font=LARGE_FONT)
        label1.pack(pady=10, padx=10)

        label2 = tk.Label(self, text="Student first name", font=LARGE_FONT)
        label2.place(x=100, y=200)
        self.student_first_name_entry = tk.Entry(self)
        self.student_first_name_entry.place(x=100, y=230)

        label3 = tk.Label(self, text="Student last name", font=LARGE_FONT)
        label3.place(x=300, y=200)
        self.student_last_name_entry = tk.Entry(self)
        self.student_last_name_entry.place(x=300, y=230)

        self.student_card_var = tk.BooleanVar()
        self.student_card_checkbox = tk.Checkbutton(
            self, text="Student card taken", variable=self.student_card_var
        )
        self.student_card_checkbox.place(x=100, y=270)

        label4 = tk.Label(self, text="Equipment loaned", font=LARGE_FONT)
        label4.place(x=100, y=310)
        self.equipment_var = tk.StringVar(value="    ")
        self.equipment_combobox = tk.OptionMenu(self, self.equipment_var, "    ")
        self.equipment_combobox.place(x=300, y=310)

        label5 = tk.Label(self, text="Amount", font=LARGE_FONT)
        label5.place(x=100, y=360)
        # No upper limit — to=99999 effectively unlimited
        self.amount_spinbox = tk.Spinbox(self, from_=1, to=99999)
        self.amount_spinbox.place(x=300, y=360)

        self.status_label = tk.Label(self, text="", font=LARGE_FONT)
        self.status_label.place(x=100, y=410)

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame(iConMainUI))
        button1.place(x=25, y=25)
        button2 = tk.Button(self, text="Submit", command=self.submit_loan)
        button2.place(x=100, y=450)

        # --- Out of stock panel ---
        label6 = tk.Label(self, text="Out of stock", font=LARGE_FONT, fg="red")
        label6.place(x=700, y=200)
        self.out_of_stock_listbox = tk.Listbox(
            self, fg="red", font=LARGE_FONT,
            width=30, height=10,
            selectmode=tk.NONE  # display only, not selectable
        )
        self.out_of_stock_listbox.place(x=700, y=230)

    def tkraise(self, *args, **kwargs):
        self._refresh_equipment()
        super().tkraise(*args, **kwargs)

    def _refresh_equipment(self):
        in_stock, out_of_stock = get_equipment_list_with_stock()

        # Rebuild dropdown
        menu = self.equipment_combobox["menu"]
        menu.delete(0, "end")
        if in_stock:
            for item in in_stock:
                menu.add_command(label=item,
                                 command=lambda v=item: self.equipment_var.set(v))
        else:
            menu.add_command(label="No stock available", command=lambda: None)
        self.equipment_var.set("    ")

        # Rebuild out-of-stock listbox
        self.out_of_stock_listbox.delete(0, tk.END)
        for item in out_of_stock:
            self.out_of_stock_listbox.insert(tk.END, item)

    def submit_loan(self):
        first_name = self.student_first_name_entry.get()
        last_name = self.student_last_name_entry.get()
        student_card_taken = self.student_card_var.get()
        equipment = self.equipment_var.get()
        amount = self.amount_spinbox.get()

        if first_name and last_name and equipment not in ("    ", "No stock available"):
            try:
                process_loan({
                    "icon_name": self.controller.current_user,
                    "first_name": first_name,
                    "last_name": last_name,
                    "student_card_taken": student_card_taken,
                    "equipment": equipment,
                    "amount": int(amount)
                })
                self.status_label.config(text="Submitted successfully", fg="green")
                self._refresh_equipment()  # update stock lists after loan
            except Exception as e:
                self.status_label.config(text=f"Error: {e}", fg="red")
        else:
            self.status_label.config(text="Please fill in all fields", fg="red")

        self.student_first_name_entry.delete(0, tk.END)
        self.student_last_name_entry.delete(0, tk.END)
        self.student_card_var.set(False)
        self.equipment_var.set("    ")
        self.amount_spinbox.delete(0, tk.END)
        self.amount_spinbox.insert(0, "1")


        
class returnUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="Return UI", font=LARGE_FONT)
        label1.pack(pady=10, padx=10)

        label2 = tk.Label(self, text="List of Loans", font=LARGE_FONT)
        label2.pack(pady=10, padx=10)

        self.list_of_loans_var = tk.StringVar(value="    ")
        self.list_of_loans_combobox = tk.OptionMenu(self, self.list_of_loans_var, "    ")
        self.list_of_loans_combobox.pack(pady=10, padx=10)

        self.student_card_var = tk.BooleanVar()
        self.student_card_checkbox = tk.Checkbutton(
            self, text="Student card returned", variable=self.student_card_var
        )
        self.student_card_checkbox.pack(pady=10, padx=10)

        label3 = tk.Label(self, text="Additional comments", font=LARGE_FONT)
        label3.pack(pady=10, padx=10)

        self.comments_entry = tk.Entry(self)
        self.comments_entry.pack(pady=10, padx=10)

        self.status_label = tk.Label(self, text="", font=LARGE_FONT)
        self.status_label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame(iConMainUI))
        button1.place(x=25, y=25)

        button2 = tk.Button(self, text="Submit return",
                            command=self.submit_return)
        button2.pack(pady=10, padx=10)

    def tkraise(self, *args, **kwargs):
        # Refresh the dropdown every time this screen is shown
        self._refresh_loans()
        super().tkraise(*args, **kwargs)

    def _refresh_loans(self):
        loans = get_open_loans()
        menu = self.list_of_loans_combobox["menu"]
        menu.delete(0, "end")
        if loans:
            for loan in loans:
                menu.add_command(label=loan,
                                 command=lambda v=loan: self.list_of_loans_var.set(v))
            self.list_of_loans_var.set("    ")
        else:
            menu.add_command(label="No open loans", command=lambda: None)
            self.list_of_loans_var.set("No open loans")

    def submit_return(self):
        selected_loan = self.list_of_loans_var.get()
        card_returned = self.student_card_var.get()
        comments = self.comments_entry.get()

        if selected_loan in ("    ", "No open loans"):
            self.status_label.config(text="Please select a loan", fg="red")
            return

        try:
            process_return(selected_loan, card_returned, comments)
            self.status_label.config(text="Return submitted successfully", fg="green")
            self.comments_entry.delete(0, tk.END)
            self.student_card_var.set(False)
            self._refresh_loans()  # update dropdown immediately after return
        except Exception as e:
            self.status_label.config(text=f"Error: {e}", fg="red")
            
            

class dataAnalysisUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="Data Analysis", font=LARGE_FONT)
        label1.pack(pady=10, padx=10)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Chart: Borrow Count",
                  command=self.show_borrow_chart).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Chart: Out of Stock",
                  command=self.show_oos_chart).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Refresh",
                  command=self._refresh_table).pack(side=tk.LEFT, padx=10)

        # Table headers
        cols = ("Item", "Borrow Count", "Total Loaned", "Currently On Loan", "Out of Stock Events")
        self.tree = tk.ttk.Treeview(self, columns=cols, show="headings", height=20)
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=200, anchor="center")
        self.tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(iConMainUI)).place(x=25, y=25)

    def tkraise(self, *args, **kwargs):
        self._refresh_table()
        super().tkraise(*args, **kwargs)

    def _refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for entry in get_table_data():
            self.tree.insert("", tk.END, values=(
                entry["item"],
                entry["borrow_count"],
                entry["total_loaned"],
                entry["currently_on_loan"],
                entry["out_of_stock"],
            ))

    def show_borrow_chart(self):
        import matplotlib.pyplot as plt
        data = sorted(get_table_data(), key=lambda x: x["borrow_count"], reverse=True)
        if not data:
            return
        items  = [d["item"] for d in data]
        counts = [d["borrow_count"] for d in data]
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(items, counts, color="steelblue")
        ax.set_title("Borrow Count by Item (most to least)")
        ax.set_xlabel("Item")
        ax.set_ylabel("Number of Loans")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    def show_oos_chart(self):
        import matplotlib.pyplot as plt
        data = sorted(get_table_data(), key=lambda x: x["out_of_stock"], reverse=True)
        data = [d for d in data if d["out_of_stock"] > 0]
        if not data:
            import tkinter.messagebox as mb
            mb.showinfo("No Data", "No out-of-stock events have been recorded yet.")
            return
        items  = [d["item"] for d in data]
        counts = [d["out_of_stock"] for d in data]
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(items, counts, color="crimson")
        ax.set_title("Out of Stock Events by Item")
        ax.set_xlabel("Item")
        ax.set_ylabel("Times Hit Zero Stock")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()




class adminMainUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label1 = tk.Label(self, text="Admin Main UI", font=LARGE_FONT)
        label1.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Add Equipment",
                            command=lambda: controller.show_frame(addEquipmentUI))
        button1.place(x=100,y=200,)

        button2 = tk.Button(self, text="Remove Equipment",
                            command=lambda: controller.show_frame(removeEquipmentUI))
        button2.place(x=900,y=200,)

        button3 = tk.Button(self, text="Add iCon",
                            command=lambda: controller.show_frame(addiConUI))
        button3.place(x=100,y=300,)

        button4 = tk.Button(self, text="Remove iCon",
                            command=lambda: controller.show_frame(removeiConUI))
        button4.place(x=900,y=300,)

        button5 = tk.Button(self, text="Change Admin Password",
                            command=lambda: controller.show_frame(changeAdminPasswordUI))
        button5.place(x=500,y=400,)

        button6 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame(adminLogin))
        button6.place(x=25,y=25)

        button7 = tk.Button(self, text="Edit Records",
                    command=lambda: controller.show_frame(editRecordsUI))
        button7.place(x=500, y=300)



class addEquipmentUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Add Equipment", font=LARGE_FONT)
        label1.pack(pady=10, padx=10)

        tk.Label(self, text="Equipment name", font=LARGE_FONT).pack(pady=5)
        self.equipment_name_entry = tk.Entry(self)
        self.equipment_name_entry.pack(pady=5)

        tk.Label(self, text="Quantity", font=LARGE_FONT).pack(pady=5)
        self.quantity_spinbox = tk.Spinbox(self, from_=1, to=10000)
        self.quantity_spinbox.pack(pady=5)

        self.status_label = tk.Label(self, text="", font=LARGE_FONT)
        self.status_label.pack(pady=10)

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(adminMainUI)).place(x=25, y=25)
        tk.Button(self, text="Add", command=self.add_equipment).pack(pady=5)

    def add_equipment(self):
        name = self.equipment_name_entry.get().strip()
        qty  = self.quantity_spinbox.get()

        if name and qty.isdigit() and int(qty) > 0:
            try:
                add_equipment(name, int(qty))
                self.status_label.config(text="Equipment added successfully", fg="green")
                self.equipment_name_entry.delete(0, tk.END)
                self.quantity_spinbox.delete(0, tk.END)
                self.quantity_spinbox.insert(0, "1")
            except Exception as e:
                self.status_label.config(text=f"Error: {e}", fg="red")
        else:
            self.status_label.config(text="Invalid name or quantity", fg="red")


class removeEquipmentUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Remove Equipment", font=LARGE_FONT).pack(pady=10)
        tk.Label(self, text="Select equipment", font=LARGE_FONT).pack(pady=5)

        self.equipment_var = tk.StringVar(value="    ")
        self.equipment_combobox = tk.OptionMenu(self, self.equipment_var, "    ")
        self.equipment_combobox.pack(pady=5)

        self.status_label = tk.Label(self, text="", font=LARGE_FONT)
        self.status_label.pack(pady=10)

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(adminMainUI)).place(x=25, y=25)
        tk.Button(self, text="Remove", command=self.remove_equipment).pack(pady=5)

    def tkraise(self, *args, **kwargs):
        self._refresh_equipment()
        super().tkraise(*args, **kwargs)

    def _refresh_equipment(self):
        items = get_all_equipment()
        menu  = self.equipment_combobox["menu"]
        menu.delete(0, "end")
        if items:
            for name, qty in items:
                label = f"{name}  (stock: {qty})"
                menu.add_command(label=label,
                                 command=lambda v=name: self.equipment_var.set(v))
        else:
            menu.add_command(label="No equipment", command=lambda: None)
        self.equipment_var.set("    ")

    def remove_equipment(self):
        name = self.equipment_var.get()
        if name in ("    ", "No equipment"):
            self.status_label.config(text="Please select an item", fg="red")
            return
        try:
            remove_equipment(name)
            self.status_label.config(text=f"'{name}' removed", fg="green")
            self._refresh_equipment()
        except Exception as e:
            self.status_label.config(text=f"Error: {e}", fg="red")


class addiConUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Add iCon", font=LARGE_FONT).pack(pady=10)

        tk.Label(self, text="iCon username", font=LARGE_FONT).pack(pady=5)
        self.icon_username_entry = tk.Entry(self)
        self.icon_username_entry.pack(pady=5)

        tk.Label(self, text="iCon password", font=LARGE_FONT).pack(pady=5)
        self.icon_password_entry = tk.Entry(self, show="*")
        self.icon_password_entry.pack(pady=5)

        self.status_label = tk.Label(self, text="", font=LARGE_FONT)
        self.status_label.pack(pady=10)

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(adminMainUI)).place(x=25, y=25)
        tk.Button(self, text="Add", command=self.add_icon).pack(pady=5)

    def add_icon(self):
        username = self.icon_username_entry.get().strip()
        password = self.icon_password_entry.get()
        if username and password:
            try:
                add_icon(username, password)
                self.status_label.config(text="iCon added successfully", fg="green")
                self.icon_username_entry.delete(0, tk.END)
                self.icon_password_entry.delete(0, tk.END)
            except Exception as e:
                self.status_label.config(text=f"Error: {e}", fg="red")
        else:
            self.status_label.config(text="Username and password required", fg="red")


class removeiConUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Remove iCon", font=LARGE_FONT).pack(pady=10)
        tk.Label(self, text="iCon username", font=LARGE_FONT).pack(pady=5)

        self.icon_username_var = tk.StringVar(value="    ")
        self.icon_username_combobox = tk.OptionMenu(self, self.icon_username_var, "    ")
        self.icon_username_combobox.pack(pady=5)

        self.status_label = tk.Label(self, text="", font=LARGE_FONT)
        self.status_label.pack(pady=10)

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(adminMainUI)).place(x=25, y=25)
        tk.Button(self, text="Remove", command=self.remove_icon).pack(pady=5)

    def tkraise(self, *args, **kwargs):
        self._refresh_icons()
        super().tkraise(*args, **kwargs)

    def _refresh_icons(self):
        usernames = get_icon_usernames()
        menu = self.icon_username_combobox["menu"]
        menu.delete(0, "end")
        if usernames:
            for u in usernames:
                menu.add_command(label=u, command=lambda v=u: self.icon_username_var.set(v))
        else:
            menu.add_command(label="No iCons", command=lambda: None)
        self.icon_username_var.set("    ")

    def remove_icon(self):
        username = self.icon_username_var.get()
        if username in ("    ", "No iCons"):
            self.status_label.config(text="Please select an iCon", fg="red")
            return
        try:
            remove_icon(username)
            self.status_label.config(text=f"'{username}' removed", fg="green")
            self._refresh_icons()
        except Exception as e:
            self.status_label.config(text=f"Error: {e}", fg="red")


class editRecordsUI(tk.Frame):

    BOOL_FIELDS = {"Student Card Taken", "Student Card Returned", "Signed Out", "Signed In"}
    FIELDS = ["iCon Name", "Date", "First Name", "Last Name", "Equipment",
              "Amount", "Student Card Taken", "Student Card Returned",
              "Signed Out", "Signed In", "Comments"]

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Edit Records", font=LARGE_FONT).pack(pady=10)

        tk.Button(self, text="Back",
                  command=lambda: controller.show_frame(adminMainUI)).place(x=25, y=25)
        tk.Button(self, text="Refresh",
                  command=self._refresh_table).place(x=120, y=25)

        cols = ("Row", "iCon", "Date", "First", "Last", "Equipment",
                "Qty", "Card Taken", "Card Returned", "Signed Out", "Signed In", "Comments")
        self.tree = ttk.Treeview(self, columns=cols, show="headings", height=22)
        col_widths = [50, 100, 150, 90, 90, 120, 50, 100, 120, 100, 90, 200]
        for col, w in zip(cols, col_widths):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=w, anchor="center")
        self.tree.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
        self.tree.bind("<<TreeviewSelect>>", self._on_select)

        # Edit panel
        edit_frame = tk.Frame(self)
        edit_frame.pack(pady=5)

        tk.Label(edit_frame, text="Field:", font=LARGE_FONT).grid(row=0, column=0, padx=5)
        self.field_var = tk.StringVar(value=self.FIELDS[0])
        tk.OptionMenu(edit_frame, self.field_var, *self.FIELDS).grid(row=0, column=1, padx=5)

        tk.Label(edit_frame, text="New value:", font=LARGE_FONT).grid(row=0, column=2, padx=5)
        self.new_value_entry = tk.Entry(edit_frame, width=25)
        self.new_value_entry.grid(row=0, column=3, padx=5)

        tk.Button(edit_frame, text="Update field",
                  command=self.update_field).grid(row=0, column=4, padx=5)
        tk.Button(edit_frame, text="Delete record",
                  command=self.delete_record, fg="red").grid(row=0, column=5, padx=5)

        self.status_label = tk.Label(self, text="", font=LARGE_FONT)
        self.status_label.pack(pady=5)

        self._records = []
        self._selected_row = None

    def tkraise(self, *args, **kwargs):
        self._refresh_table()
        super().tkraise(*args, **kwargs)

    def _refresh_table(self):
        self._selected_row = None
        for item in self.tree.get_children():
            self.tree.delete(item)
        self._records = get_all_records()
        for r in self._records:
            self.tree.insert("", tk.END, values=(
                r["row_number"], r["icon_name"], r["date"],
                r["first_name"], r["last_name"], r["equipment"],
                r["amount"], r["card_taken"], r["card_returned"],
                r["signed_out"], r["signed_in"], r["comments"]
            ))

    def _on_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0], "values")
        self._selected_row = int(values[0])

    def update_field(self):
        if self._selected_row is None:
            self.status_label.config(text="Select a record first", fg="red")
            return
        field     = self.field_var.get()
        raw_value = self.new_value_entry.get().strip()

        # Convert value type appropriately
        if field == "Amount":
            try:
                value = int(raw_value)
            except ValueError:
                self.status_label.config(text="Amount must be a whole number", fg="red")
                return
        elif field in self.BOOL_FIELDS:
            if raw_value.lower() in ("true", "yes", "1"):
                value = True
            elif raw_value.lower() in ("false", "no", "0"):
                value = False
            else:
                self.status_label.config(text="Boolean fields: enter true or false", fg="red")
                return
        else:
            value = raw_value

        try:
            update_record(self._selected_row, field, value)
            self.status_label.config(text="Record updated successfully", fg="green")
            self.new_value_entry.delete(0, tk.END)
            self._refresh_table()
        except Exception as e:
            self.status_label.config(text=f"Error: {e}", fg="red")

    def delete_record(self):
        if self._selected_row is None:
            self.status_label.config(text="Select a record first", fg="red")
            return
        import tkinter.messagebox as mb
        if mb.askyesno("Confirm", f"Delete row {self._selected_row}? This cannot be undone."):
            try:
                delete_record(self._selected_row)
                self.status_label.config(text="Record deleted", fg="green")
                self._selected_row = None
                self._refresh_table()
            except Exception as e:
                self.status_label.config(text=f"Error: {e}", fg="red")


class changeAdminPasswordUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label1 = tk.Label(self, text="Change Admin Password", font=LARGE_FONT)
        label1.pack(pady=10,padx=10)

        label2 = tk.Label(self, text="New password", font=LARGE_FONT)
        label2.pack(pady=10,padx=10)

        self.new_password_entry = tk.Entry(self)
        self.new_password_entry.pack(pady=10,padx=10)

        label3 = tk.Label(self, text="Confirm new password", font=LARGE_FONT)
        label3.pack(pady=10,padx=10)

        self.confirm_password_entry = tk.Entry(self)
        self.confirm_password_entry.pack(pady=10,padx=10)

        label4 = tk.Label(self, text="Current admin password", font=LARGE_FONT)
        label4.pack(pady=10,padx=10)

        self.current_password_entry = tk.Entry(self)
        self.current_password_entry.pack(pady=10,padx=10)

        self.status_label = tk.Label(self, text="", font=LARGE_FONT)
        self.status_label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame(adminMainUI))
        button1.place(x=25,y=25)

        button2 = tk.Button(self, text="Change Password",
                            command=self.change_password)
        button2.pack(pady=10,padx=10)

    def change_password(self):
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        current_password = self.current_password_entry.get()

        username = "Efstathios"  # ⚠️ TEMP (we'll improve this later)

        # Step 1: verify current password
        if not verifyLogin(username, current_password, False):
            self.status_label.config(
                text="Current password is incorrect",
                fg="red"
            )
            return

        # Step 2: validate new password
        if new_password != confirm_password or not new_password:
            self.status_label.config(
                text="New passwords do not match or are empty",
                fg="red"
            )
            return

        # Step 3: update file
        try:
            filepath = "aData.txt"

            new_hashed = hash(new_password)

            lines = []
            with open(filepath, "r") as file:
                for line in file:
                    user, pw = line.strip().split(",")

                    if user == username:
                        lines.append(f"{user},{new_hashed}\n")
                    else:
                        lines.append(line)

            with open(filepath, "w") as file:
                file.writelines(lines)

            self.status_label.config(
                text="Password changed successfully",
                fg="green"
            )

            # Clear fields
            self.new_password_entry.delete(0, tk.END)
            self.confirm_password_entry.delete(0, tk.END)
            self.current_password_entry.delete(0, tk.END)

        except Exception as e:
            self.status_label.config(
                text=f"Error: {e}",
                fg="red"
            )

app = App()
app.mainloop()
