# third party library for gui
import PySimpleGUI as sg
import functions as fn
from datetime import datetime

sg.theme("Topanga")

actual_date = datetime.now()
actual_date = actual_date.strftime("%d-%m-%Y %H:%M:%S")
font_style = ("Ubuntu", 15)
clock = sg.Text(actual_date,key="date")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=fn.get_todo(), key="todos", 
                    enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
output_label = sg.Text(key="output", text_color = "red")

window = sg.Window("To-do App", 
                layout=[[clock],
                [label],
                [input_box, add_button],
                [list_box, edit_button, complete_button],
                [exit_button, output_label]],
                font=font_style)

while True:
        actual_date = datetime.now()
        actual_date = actual_date.strftime("%d-%m-%Y %H:%M:%S")
        event, values = window.read(timeout=1000)
        window["date"].update(value=actual_date)
        # print (1, event)
        # print (2, values)

        match event:
            case "Add":
                todos = fn.get_todo()
                new_todo = values["todo"] 
                # verifico che l'utente abbia scritto qualcosa prima di aggiungere il task
                if len(new_todo.strip()) == 0:
                    sg.popup("Please insert a todo task first!", font=("Helvetica", 18))
                else:
                    todos.append(new_todo + "\n")
                    fn.write_todo(todos)
                    window["todos"].update(values=todos)

            case "Edit":
                try:
                
                    todo_to_edit = values["todos"][0]
                    new_todo = values["todo"]
                    todos = fn.get_todo()
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo 
                    fn.write_todo(todos)
                    window["todos"].update(values=todos)

                except IndexError:
                    sg.popup("Please select an item first!", font=("Helvetica", 20))

            case "Complete":
                try:
                    todo_to_complete = values["todos"][0]
                    todos = fn.get_todo()
                    todos.remove(todo_to_complete)
                    fn.write_todo(todos)
                    window["todos"].update(values=todos)
                    window["todo"].update(value="")
                
                except IndexError:
                    sg.popup("Please select an item first!", font=("Helvetica", 20))

            case "Exit":
                break

            case "todos":
                window["todo"].update(value=values["todos"][0])

            # WIN_CLOSED è la variabile che indica la chiusura della finestra
            case sg.WIN_CLOSED:
                break


window.close()



