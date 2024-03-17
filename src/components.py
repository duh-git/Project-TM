import pymysql as sql
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import colorama

class App(tk.Tk):
  def __init__(self) -> None:
    super().__init__()
    self.title("Task Manager")
    self.iconphoto(False, tk.PhotoImage(file="./public/mospolytech-logo-white.png"))
    self.geometry(f"800x650+100+50")
    self.resizable(False, False)
    self.config(bg="#3A3A54")

    self.Form()
    self.Worker_Table(self.sql_query("SELECT * FROM task"))
    
    
  def Form(self):
    
    # Title
    new_task_label = tk.Label(self, text="New Task", font=("Arial", 24, "bold"), fg="white", bg="#3A3A54")
    new_task_label.place(x=40, y=30)
    
    # Label"s
    labels = ["Name", "Speciality", "Deadline", "Description"]
    for i, label_text in enumerate(labels):
        label = tk.Label(self, text=label_text, font=("Arial", 20), fg="white", bg="#3A3A54")
        label.place(x=60, y=85 + 55*i)
    
    # Entry"s
    self.task_name = tk.Text(self, height=1, width=12, font=("Arial", 16))
    self.task_name.place(x=220, y=85)
    
    self.speciality = "Frontend\n"
    speciality_options = ["Frontend", "Backend", "Team Leader", "Designer"]
    speciality_var = tk.StringVar(self)
    speciality_var.set(speciality_options[0])
    speciality_menu = tk.OptionMenu(self, speciality_var, *speciality_options, command=self.select_speciality)
    speciality_menu.config(font=("Arial", 16), bg="#3A3A54", fg="white")
    speciality_menu.place(x=220, y=140)
    
    self.deadline_entry = tk.Text(self, height=1, width=12, font=("Arial", 16))
    self.deadline_entry.place(x=220, y=200)
    self.deadline_calendar = Calendar(self, date_pattern="y-mm-dd",)
    self.deadline_calendar.place(x=395, y=60)
    
    self.description_entry = tk.Text(self, height=5, width=35, font=("Arial", 16))
    self.description_entry.place(x=220, y=248)
    
    # Button"s
    reset_button = tk.Button(self, text="Set", font=("Arial", 18), fg="black", width=6, command=self.select_date)
    reset_button.place(x=666, y=60)
    
    # reset_button = tk.Button(self, text="Reset", font=("Arial", 18), fg="black", bg="#E37979", width=6)
    # reset_button.place(x=666, y=260)

    submit_button = tk.Button(self, text="Submit", font=("Arial", 18), fg="black", bg="#66EA63", width=6, command=self.submit)
    submit_button.place(x=666, y=325)
    
    # Line
    line = tk.Canvas(self, width=720, height=2, bg="white", highlightthickness=0)
    line.place(x=40, y=410)

  def select_date(self):
    date = self.deadline_calendar.get_date()
    self.deadline_entry.delete(0.1, tk.END)
    self.deadline_entry.insert(0.1, date)
    
  def select_speciality(self, selection):
    self.speciality = selection + "\n"
    
  def submit(self):
    temp_obj = {
      "title": self.task_name.get(0.1, tk.END),
      "speciality": self.speciality,
      "daedline": self.deadline_entry.get(0.1, tk.END),
      "description": self.description_entry.get(0.1, tk.END),
    }
    
    for key, value in temp_obj.items():
      print(key, value[:-1])
    print()
    
    ### use SQL (temp_obj)
    
    temp_obj = {}


  def Worker_Table(self, cash):

    # Title
    current_task_label = tk.Label(self, text="Current Task", font=("Arial", 24, "bold"), fg="white", bg="#3A3A54")
    current_task_label.place(x=40, y=420)
    
    # Table
    worker_columns = ("TID", "Task", "Worker", "Speciality", "Daedline")
    self.worker_tree = ttk.Treeview(self, columns=worker_columns, show="headings", height=5)
    self.worker_tree.place(x=40, y=480)
    for i, col_name in enumerate(worker_columns):
      self.worker_tree.heading(f"#{i+1}", text=col_name)
      
    col_width = (35, 120, 200, 100, 150)
    for i, width in enumerate(col_width):
      self.worker_tree.column(f"#{i+1}", width=width, anchor='center')
    
    ### use SQL (download data)
    ### item examle: ['1', 'A', 'Dima', 'Back', '10.11.2024']
    
    for item in cash:
      self.worker_tree.insert("", tk.END, values=list(item.values()))
    
    # with open("./contacts.csv", newline="") as f:
    #   for item in csv.reader(f):
    #     item = item[0].split(";")
    #     print(item)
    #     self.worker_tree.insert("", tk.END, values=item)
    #     self.cash.append(item)

    # Button
    delete_button = tk.Button(self, text="Delete", font=("Arial", 18), fg="black", bg="#E37979", width=6, command=self.delete_item)
    delete_button.place(x=666, y=480)
    
  #   scroll = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.worker_tree.yview)
  #   self.worker_tree.configure(yscroll=scroll.set)
  #   scroll.place(x=720, y=500)
  # 
  #   self.task_description = tk.Text(self, height=5, width=35, font=("Arial", 16))
  #   self.task_description.place(x=40, y=640)
  # 
  # 
  #   with open("./contacts.csv", newline="") as f:
  #     for contact in csv.reader(f):
  #       contact = contact[0].split(";")
  #       self.worker_tree.insert("", tk.END, values=contact)
  # 
  #   self.worker_tree.bind("<<TreeviewSelect>>", self.print_selection)
  # 
  # def print_selection(self, event):
  #   for selection in self.worker_tree.selection():
  #     item = self.worker_tree.item(selection)
  #     ###
  #     TID, Task, Worker, Speciality, Deadline = item["values"]
  #     print(TID, Task, Worker, Speciality, Deadline)

  def delete_item(self):
    item_treeID = self.worker_tree.selection()
    item = self.worker_tree.item(item_treeID)["values"]
    
    self.worker_tree.delete(self.worker_tree.selection())
    
    ### SQL (use item)
    
    
  def sql_query(self, query):
    answer = ''
    try:
      connection = sql.connect(
        host="localhost",
        user="root",
        password='root',
        database="Project TM",
        cursorclass=sql.cursors.DictCursor
      )
      print(colorama.Back.GREEN + colorama.Fore.BLACK + '{:-^40}'.format('Connection SUCCESFUL'))

      try:
        with connection.cursor() as cursor:
          cursor.execute(query)
          answer = cursor.fetchall()
          
          print(colorama.Back.WHITE + colorama.Fore.BLACK + '{:-<30}'.format('Total received values:') + f'{len(answer):->10}')

      except Exception as error:
        print(colorama.Back.YELLOW + colorama.Fore.BLACK + '{:-^40}'.format('Connection INTERRAPTED'), error, sep='\n')

      finally:
        connection.close()
        print(colorama.Back.GREEN + colorama.Fore.BLACK + '{:-^40}'.format('Connection CLOSED'))

    except Exception as error:
      print(colorama.Back.RED + colorama.Fore.BLACK + '{:-^40}'.format('Connection FAILED'))
      print(error)
    return answer

  def render(self):
    self.Worker_Table(self.sql_query("SELECT * FROM task"))


if __name__ == "__main__":
  colorama.init(autoreset=True)
  app = App()
  app.mainloop()