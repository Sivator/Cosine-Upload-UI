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
    upload_coscine(token,file_path, project_name_entry.get(), resource_entry.get(), title_entry.get(),name_entry.get(),cal.get_date(), supervisor_entry.get(), reviewer_entry.get(), studycoursefield_entry.get(), project_entry.get(), location_entry.get(), institute_entry.get(), degree_variable.get(), archivist_entry.get(), working_groups_entry.get(), organism_entry.get(),methodology_entry.get(), methodology_entry.get(), partners_entry.get(),abstract_text.get("1.0",'end-1c'))


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

def settings_window():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("250x200")
    global project_name_entry
    project_name_label = tk.Label(settings_window, text="Project Name:")
    project_name_label.grid(column=0, row=0,padx='5', pady='5', sticky='ew',columnspan=2)
    project_name_entry = tk.Entry(settings_window)
    project_name_entry.grid(column=0,row=1,padx='5', pady='5', sticky='ew',columnspan=2)
    project_name_entry.insert(-1, "iAMB-Theses & Reports")
    global resource_entry
    resource_label = tk.Label(settings_window, text= "Recource Name:")
    resource_label.grid(column=0,row=2,padx='5', pady='5', sticky='ew',columnspan=2)
    resource_entry = tk.Entry(settings_window)
    resource_entry.grid(column=0,row=3,padx='5', pady='5', sticky='ew',columnspan=2)
    resource_entry.insert(-1, "Thesis and Reports")
    #saving the token file location has yet to be implemented
    token_button = tk.Button(settings_window, text="Token Location", command=read_token)
    token_button.grid(column=0,row=4,padx='5', pady='5', sticky='ew',columnspan=2)

root = tk.Tk()
root.title("Coscine Uploader")
root.geometry("430x740")

#All the neccesary labels and entry widgets
title_var = tk.StringVar()
title_label = tk.Label(root, text="*Title:")
title_label.grid(column=0,row=0,padx='5', pady='5', sticky='ew')
title_entry = tk.Entry(root, textvariable= title_var)
title_entry.grid(column=0,row=1,padx='5', pady='5', sticky='ew')

name_label = tk.Label(root, text="*Name:")
name_label.grid(column=0,row=2,padx='5', pady='5', sticky='ew')
name_entry = tk.Entry(root)
name_entry.grid(column=0,row=3,padx='5', pady='5', sticky='ew')

supervisor_label = tk.Label(root, text="*Supervisor, direct:")
supervisor_label.grid(column=0,row=4,padx='5', pady='5', sticky='ew')
supervisor_entry = tk.Entry(root)
supervisor_entry.grid(column=0, row=5,padx='5', pady='5', sticky='ew')

reviewer_label = tk.Label(root, text="*Reviewer(s):")
reviewer_label.grid(column=0,row=6,padx='5', pady='5', sticky='ew')
reviewer_entry = tk.Entry(root)
reviewer_entry.grid(column=0, row=7,padx='5', pady='5', sticky='ew')

studycoursefield_label =tk.Label(root, text="*Study Course Field:")
studycoursefield_label.grid(column=0,row=8,padx='5', pady='5', sticky='ew')
studycoursefield_entry = tk.Entry(root)
studycoursefield_entry.grid(column=0,row=9,padx='5', pady='5', sticky='ew')

project_label =tk.Label(root, text="*Project:")
project_label.grid(column=0,row=10,padx='5', pady='5', sticky='ew')
project_entry = tk.Entry(root)
project_entry.grid(column=0, row=11,padx='5', pady='5', sticky='ew')

location_label = tk.Label(root, text="*File Location:")
location_label.grid(column=0, row=12,padx='5', pady='5', sticky='ew')
location_entry = tk.Entry(root)
location_entry.grid(column=0,row=13,padx='5', pady='5', sticky='ew')

institute_label = tk.Label(root, text="Institute:")
institute_label.grid(column=1,row=0,padx='5', pady='5', sticky='ew')
institute_entry = tk.Entry(root)
institute_entry.grid(column=1,row=1,padx='5', pady='5', sticky='ew')

degree_variable = tk.StringVar(root)
degree_variable.set("Research intern")
degree_label = tk.Label(root, text="Degree:")
degree_label.grid(column=0, row=14,padx='5', pady='5', sticky='ew')
degree_entry = tk.OptionMenu(root, degree_variable, "B.Sc.", "M.Sc.", "Research intern")
degree_entry.grid(column=0,row=15,padx='5', pady='5', sticky='ew')

archivist_label = tk.Label(root, text=" Archivist:")
archivist_label.grid(column=1, row=2,padx='5', pady='5', sticky='ew')
archivist_entry = tk.Entry(root)
archivist_entry.grid(column=1, row=3,padx='5', pady='5', sticky='ew')

working_groups_label = tk.Label(root, text="Sub-working group(s):")
working_groups_label.grid(column=1, row=4,padx='5', pady='5', sticky='ew')
working_groups_entry = tk.Entry(root)
working_groups_entry.grid(column=1, row=5,padx='5', pady='5', sticky='ew')#muss noch übergeben werden!

abstract_label = tk.Label(root, text="Abstract:")
abstract_label.grid(column=0, row=16,padx='5', pady='5', sticky='ew',columnspan=2)
abstract_text = tk.Text(root, height = 5, width = 52)
abstract_text.grid(column=0, row=17,padx='5', pady='5', sticky='ew',columnspan=2)#muss noch übergeben werden!

organism_label =tk.Label(root, text="Organism:")
organism_label.grid(column=1, row=6,padx='5', pady='5', sticky='ew')#muss noch übergeben werden!
organism_entry = tk.Entry(root)
organism_entry.grid(column=1, row=7,padx='5', pady='5', sticky='ew')

target_molecules_label = tk.Label(root, text="Target Molecules:")
target_molecules_label.grid(column=1, row=8,padx='5', pady='5', sticky='ew')
target_molecules_entry = tk.Entry(root)
target_molecules_entry.grid(column=1, row=9,padx='5', pady='5', sticky='ew')

methodology_label = tk.Label(root, text="Methodology:")
methodology_label.grid(column=1, row=10,padx='5', pady='5', sticky='ew')
methodology_entry = tk.Entry(root)
methodology_entry.grid(column=1, row=11,padx='5', pady='5', sticky='ew')

partners_label = tk.Label(root,text="Project Partners:")
partners_label.grid(column=1, row=12,padx='5', pady='5', sticky='ew')
partners_entry = tk.Entry(root)
partners_entry.grid(column=1, row=13,padx='5', pady='5', sticky='ew')

cal_label =tk.Label(root, text="*Choose Date:")
cal_label.grid(column=1, row=14,padx='5', pady='5', sticky='ew')
cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2) #yyyy-mm-dd
cal.grid(column=1, row=15,padx='5', pady='5', sticky='ew')

file_button = tk.Button(root, text="File Location", command=find_file)
file_button.grid(column=0,row=18,padx='5', pady='5', sticky='ew',columnspan=2)

#this button executes the metadata_fill funktion inside coscine_upload
upload_button = tk.Button(root, text="Upload", command=upload_call)
upload_button.grid(column=0,row=19,padx='5', pady='5', sticky='ew',columnspan=2)

settings_button = tk.Button(root, text="Coscine Settings", command=settings_window)
settings_button.grid(column=0,row=20,padx='5', pady='5', sticky='ew',columnspan=2)

root.mainloop()