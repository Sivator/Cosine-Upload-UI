import coscine
from datetime import datetime
import tkinter as tk


def upload_notification():
    notify_window = tk.Tk()
    notify_window.title("Notification")
    notify_window.title("New Window")
    notify_window.geometry("200x200")
    # A Label widget to show in toplevel
    tk.Label(notify_window,text ="Upload Complete!").pack()

def upload_coscine(token, path, project_name, resource_name, m_title,m_name,m_date,m_supervisor,m_reviewer,m_course, m_project, m_location, m_institute, m_degree, m_archivist):
    
    client = coscine.Client(token)
    form = client.project_form()
    #Project name Should be Configurable
    project = client.project(project_name)
    #Same as Project name
    resource = project.resource(resource_name)

    metadata = resource.metadata_form()
    metadata["Title"] = m_title
    metadata["Name"] = m_name
    metadata["Final Date"] = datetime.now()#m_date possibly doesnt work
    metadata["Supervisor, direct"] = m_supervisor
    metadata["Reviewer(s)"] = m_reviewer
    metadata["Study Course Field"] = m_course
    metadata["Project"] = m_project
    metadata["Files Location"] = m_location
    metadata["Institute"] = m_institute
    metadata["Degree"] = 'B.Sc.' # defenitly doesnt work
    metadata["Name of the archivist"] = m_archivist
    filename = m_title + ".pdf"
    resource.upload(filename, path, metadata, callback= upload_notification())