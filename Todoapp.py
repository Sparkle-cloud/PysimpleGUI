
import PySimpleGUI as sg

def add_task(values):
    task = values['taskname']
    todolist.append(task)
    window.FindElement('taskname').Update(value="")
    window.FindElement('todolist').Update(values=todolist)
    window.FindElement('add_save').Update('Add')

def edit_tasks(values):
    edit_val = values['todolist'][0]
    window.FindElement('taskname').Update(value=edit_val)
    todolist.remove(edit_val)
    window.FindElement('add_save').Update('Save')

def delete_tasks(values):
    delete_val = values['todolist'][0]
    todolist.remove(delete_val)
    window.FindElement('todolist').Update(values=todolist)

layout = [
    [sg.Text("Enter the task", font=("Arial", 14)), sg.InputText("", font=("Arial", 14), size=(20,1),key="taskname"),
     sg.Button("Add", font=("Arial", 14), key="add_save")],
    [sg.Listbox(values=[], size=(40, 10), font=("Arial", 14), key='todolist'), sg.Button("Edit", font=("Arial", 14)),
     sg.Button("Delete", font=("Arial", 14))]
]
todolist = []

window = sg.Window("Week1", layout)
while True:
    event, values = window.Read()
    if event == 'add_save':
        add_task(values)
    elif event =='Edit':
        edit_tasks(values)
    elif event == 'Delete':
        delete_tasks(values)
    else:
        break
window.Close()