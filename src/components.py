import tkinter as tk
from tkcalendar import Calendar

class Display(tk.Tk):
  def __init__(self) -> None:
    super().__init__()
    self.title("Task Manager")
    self.iconphoto(False, tk.PhotoImage(file="./public/mospolytech-logo-white.png"))
    self.geometry(f"800x600+100+100")
    self.resizable(False, False)
    self.config(bg="#3A3A54")

    self.Form()
    
  def Form(self):
    
    # Title
    new_task_label = tk.Label(self, text="New Task", font=("Arial", 24, "bold"), fg="white", bg="#3A3A54")
    new_task_label.place(x=40, y=30)
    
    # Label's
    labels = ["Name", "Speciality", "Deadline", "Decryption"]
    for i, label_text in enumerate(labels):
        label = tk.Label(self, text=label_text, font=("Arial", 20), fg="white", bg="#3A3A54")
        label.place(x=60, y=85 + 55*i)
    
    # Entry's
    self.task_name = tk.Text(self, height=1, width=12, font=("Arial", 16))
    self.task_name.place(x=220, y=85)
    
    self.speciality = "Frontend\n"
    speciality_options = ["Frontend", "Backend", "Team Leader", "Designer"]
    speciality_var = tk.StringVar(self)
    speciality_var.set(speciality_options[0])
    speciality_menu = tk.OptionMenu(self, speciality_var, *speciality_options, command=self.callback)
    speciality_menu.config(font=("Arial", 16), bg="#3A3A54", fg="white")
    speciality_menu.place(x=220, y=140)
    
    self.deadline_entry = tk.Text(self, height=1, width=12, font=("Arial", 16))
    self.deadline_entry.place(x=220, y=200)
    self.deadline_calendar = Calendar(self, date_pattern="dd.mm.y",)
    self.deadline_calendar.place(x=395, y=60)
    
    self.decryption_entry = tk.Text(self, height=5, width=35, font=("Arial", 16))
    self.decryption_entry.place(x=220, y=248)
    
    # Button's
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
    
  def callback(self, selection):
    self.speciality = selection + '\n'
    print(self.speciality)
    
  def submit(self):
    data = []
    data.append(self.task_name.get(0.1, tk.END))
    data.append(self.speciality)
    data.append(self.deadline_entry.get(0.1, tk.END))
    data.append(self.decryption_entry.get(0.1, tk.END))
    for prop in data:
      print(prop[:-1])



if __name__ == "__main__":
    d = Display()
    d.mainloop()
    