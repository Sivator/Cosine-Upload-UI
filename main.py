import tkinter as tk
import subprocess
import threading
from tkinter import filedialog
from coscine_upload import upload_coscine
from tkcalendar import DateEntry
import os

token = ""
file_path =""

def upload_call():
    print("test")
    upload_coscine(token,file_path, project_name_entry.get(), resource_entry.get(), title_entry.get(),name_entry.get(),cal.get_date(), supervisor_entry.get(), reviewer_entry.get(), studycoursefield_entry.get(), project_entry.get(), location_entry.get(), institute_entry.get(), degree_entry.get(),archivist_entry.get())


def read_token():
    file = filedialog.askopenfile(mode='r', filetypes=[("Text files","*.txt")])
    if file:
        file_path = os.path.abspath(file.name)
        fd = open(file_path, "rt")
        global token
        token = fd.read()
        fd.close()
    
def find_file():
    global file_path
    file_path= filedialog.askopenfilename(title = "Select A File", filetypes =[("PDF Files","*.pdf")])


root = tk.Tk()
root.title("Coscine Uploader")
root.geometry("600x800")

#All the neccesary labels and entry widgets
title_var = tk.StringVar()
title_label = tk.Label(root, text="Title:")
title_label.pack()
title_entry = tk.Entry(root, textvariable= title_var)
title_entry.pack()

project_name_label = tk.Label(root, text="Project Name:")
project_name_label.pack()
project_name_entry = tk.Entry(root)
project_name_entry.pack()
project_name_entry.insert(-1, "iAMB-Theses & Reports")

resource_label = tk.Label(root, text= "Recource Window:")
resource_label.pack()
resource_entry = tk.Entry(root)
resource_entry.pack()
resource_entry.insert(-1, "Thesis and Reports")
#saving the token file location has yet to be implemented
token_button = tk.Button(root, text="Token Location", command=read_token)
token_button.pack()

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

supervisor_label = tk.Label(root, text="Supervisor, direct:")
supervisor_label.pack()
supervisor_entry = tk.Entry(root)
supervisor_entry.pack()

reviewer_label = tk.Label(root, text="Reviewer(s):")
reviewer_label.pack()
reviewer_entry = tk.Entry(root)
reviewer_entry.pack()

studycoursefield_label =tk.Label(root, text="Study Course Field:")
studycoursefield_label.pack()
studycoursefield_entry = tk.Entry(root)
studycoursefield_entry.pack()

project_label =tk.Label(root, text="Project:")
project_label.pack()
project_entry = tk.Entry(root)
project_entry.pack()

location_label = tk.Label(root, text="File Location:")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

institute_label = tk.Label(root, text="Institute:")
institute_label.pack()
institute_entry = tk.Entry(root)
institute_entry.pack()

degree_label = tk.Label(root, text="Degree:")
degree_label.pack()
degree_entry = tk.Entry(root)
degree_entry.pack()

archivist_label = tk.Label(root, text=" Archivist:")
archivist_label.pack()
archivist_entry = tk.Entry(root)
archivist_entry.pack()

cal_label =tk.Label(root, text="Choose Date:")
cal_label.pack()
cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2) #yyyy-mm-dd
cal.pack(padx=10, pady=10)

file_button = tk.Button(root, text="File Location", command=find_file)
file_button.pack()

#this button executes the metadata_fill funktion inside coscine_upload
upload_button = tk.Button(root, text="Upload", command=upload_call)
upload_button.pack()

root.mainloop()