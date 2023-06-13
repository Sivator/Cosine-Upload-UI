import coscine
from datetime import datetime
import tkinter as tk


def upload_notification():
    notify_window = tk.Tk()
    notify_window.title("Notification")
    notify_window.geometry("300x200")
    tk.Label(notify_window,text ="Upload Complete!").pack()

def upload_coscine(token, path, project_name, resource_name, m_title,m_name,m_date,m_supervisor,m_reviewer,m_course, m_project, m_location, m_institute, m_degree, m_archivist,m_groups, m_organism, m_molecules, m_methodology, m_partners,m_abstract):
    
    client = coscine.Client(token)
    form = client.project_form()
    project = client.project(project_name)
    resource = project.resource(resource_name)

    metadata = resource.metadata_form()
    metadata["Title"] = m_title
    metadata["Name"] = m_name
    metadata["Final Date"] = datetime.combine(m_date, datetime.min.time())
    metadata["Supervisor, direct"] = m_supervisor
    metadata["Reviewer(s)"] = m_reviewer
    metadata["Study Course Field"] = m_course
    metadata["Project"] = m_project
    metadata["Files Location"] = m_location
    #optional
    metadata["Institute"] = m_institute
    metadata["Degree"] = m_degree
    metadata["Name of the archivist"] = m_archivist
    metadata["Sub-working group(s)"] = m_groups
    metadata["Organism"] = m_organism
    metadata["Target Molecules"] = m_molecules
    metadata["Methodology"] = m_methodology
    metadata["Project partners"] = m_partners
    metadata["Abstract"] = m_abstract

    filename = m_title + ".pdf"
    resource.upload(filename, path, metadata, callback= upload_notification())