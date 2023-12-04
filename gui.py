# third party library for gui
import PySimpleGUI as sg
import functions as fn

font_style = ("Ubuntu", 15)
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=fn.get_todo(), key="todos", 
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("To-do App", 
                   layout=[[label],
                   [input_box, add_button],
                   [list_box, edit_button, complete_button],
                   [exit_button]],
                   font=font_style)

while True:
    event, values = window.read()
    print (1, event)
    print (2, values)

    match event:
        case "Add":
            todos = fn.get_todo()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            fn.write_todo(todos)
            window["todos"].update(values=todos)

        case "Edit":
            
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = fn.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            fn.write_todo(todos)
            window["todos"].update(values=todos)

        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = fn.get_todo()
            todos.remove(todo_to_complete)
            fn.write_todo(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case "Exit":
            break

        case "todos":
            window["todo"].update(value=values["todos"][0])

        # WIN_CLOSED è la variabile che indica la chiusura della finestra
        case sg.WIN_CLOSED:
            break
window.close()


