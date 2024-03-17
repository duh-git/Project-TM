import pymysql as sql
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import colorama

class App(tk.Tk):
  def __init__(self) -> None:
    super().__init__()
    self.title("Task Manager")
    self.iconphoto(False, tk.PhotoImage(file="../public/mospolytech-logo-white.png"))
    self.geometry(f"800x650+400+50")
    self.resizable(False, False)
    self.config(bg="#3A3A54")

    self.Form()
    self.Worker_Table(self.sql_query("SELECT * FROM task"))
    
    
  def Form(self):
    
    # Title
    new_task_label = tk.Label(self, text="New Task", font=("Arial", 24, "bold"), fg="white", bg="#3A3A54")
    new_task_label.place(x=40, y=30)
    
    # Label"s
    labels = ["Name", "Speciality", "Deadline", "Worker"]
    for i, label_text in enumerate(labels):
        label = tk.Label(self, text=label_text, font=("Arial", 20), fg="white", bg="#3A3A54")
        label.place(x=60, y=85 + 55*i)
    
    # Entry"s
    self.task_name = tk.Text(self, height=1, width=12, font=("Arial", 16))
    self.task_name.place(x=220, y=85)
    
    self.speciality = "Frontend"
    speciality_options = ["Frontend", "Backend", "TeamLeader", "Designer"]
    speciality_var = tk.StringVar(self)
    speciality_var.set(speciality_options[0])
    speciality_menu = tk.OptionMenu(self, speciality_var, *speciality_options, command=self.select_speciality)
    speciality_menu.config(font=("Arial", 16), bg="#3A3A54", fg="white")
    speciality_menu.place(x=220, y=140)
    
    self.deadline_entry = tk.Text(self, height=1, width=12, font=("Arial", 16))
    self.deadline_entry.place(x=220, y=200)
    self.deadline_calendar = Calendar(self, date_pattern="y-mm-dd",)
    self.deadline_calendar.place(x=395, y=60)
    
    self.worker_name = tk.Text(self, height=5, width=35, font=("Arial", 16))
    self.worker_name.place(x=220, y=248)
    
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
    self.speciality = selection
    
  def submit(self):
    temp_obj = {
      "title": self.task_name.get(0.1, tk.END)[:-1],
      "speciality": self.speciality,
      "deadline": self.deadline_entry.get(0.1, tk.END)[:-1],
      "worker": self.worker_name.get(0.1, tk.END)[:-1],
    }
    
    ### use SQL (temp_obj)
    id = self.sql_query(f"INSERT INTO task (name, speciality, deadline, worker) VALUES ('{temp_obj['title']}', '{temp_obj['speciality']}', '{temp_obj['deadline']}', '{temp_obj['worker']}');")
    temp_list = [id[0]['id'], temp_obj["title"], temp_obj["worker"], temp_obj["speciality"], temp_obj["deadline"]]
    self.worker_tree.insert("", tk.END, values=temp_list)

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
      self.worker_tree.column(f"#{i+1}", width=width, anchor="center")
    
    for item in cash:
      self.worker_tree.insert("", tk.END, values=list(item.values()))

    # Button
    delete_button = tk.Button(self, text="Delete", font=("Arial", 18), fg="black", bg="#E37979", width=6, command=self.delete_item)
    delete_button.place(x=666, y=480)
    
    # refresh_button = tk.Button(self, text="Refresh", font=("Arial", 18), fg="black", width=6, command=self.refresh)
    # refresh_button.place(x=666, y=560)
    
  def delete_item(self):
    item_treeID = self.worker_tree.selection()
    item = self.worker_tree.item(item_treeID)["values"]
    if item_treeID:
      self.worker_tree.delete(self.worker_tree.selection())
    
    ### SQL (use item)
    self.sql_query(f"DELETE FROM `task` WHERE `id` = {item[0]} LIMIT 1;")
    
    
  def sql_query(self, query):
    answer = ""
    try:
      connection = sql.connect(
        host="localhost",
        user="root",
        password="root",
        database="Project TM",
        cursorclass=sql.cursors.DictCursor
      )
      print(colorama.Back.GREEN + colorama.Fore.BLACK + "{:-^40}".format("Connection SUCCESFUL"))

      try:
        with connection.cursor() as cursor:
          cursor.execute(query)
          if "INSERT" in query:
            connection.commit()
            task_name = query.split('\'')[1]
            cursor.execute(f"SELECT id FROM task WHERE name = '{task_name}';")
          
          if "DELETE" in query:
            connection.commit()
          
          answer = cursor.fetchall()
          print(colorama.Back.WHITE + colorama.Fore.BLACK + "{:-<30}".format("Total received values:") + f"{len(answer):->10}")

      except Exception as error:
        print(colorama.Back.YELLOW + colorama.Fore.BLACK + "{:-^40}".format("Connection INTERRAPTED"), error, sep="\n")

      finally:
        connection.close()
        print(colorama.Back.GREEN + colorama.Fore.BLACK + "{:-^40}".format("Connection CLOSED"))

    except Exception as error:
      print(colorama.Back.RED + colorama.Fore.BLACK + "{:-^40}".format("Connection FAILED"))
      print(error)
    print()
    
    return answer


if __name__ == "__main__":
  colorama.init(autoreset=True)
  app = App()
  app.mainloop()