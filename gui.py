# third party library for gui
import PySimpleGUI as sg
import functions as fn

font_style = ("Ubuntu", 15)
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
#exit_button = sg.Button("Exit")

window = sg.Window("To-do App", 
                   layout=[[label],
                   [input_box, add_button]],
                  # [exit_button]],
                   font=font_style)

while True:
    event, values = window.read()
    if event == "Add":
        print(event)
        print(values)

    match event:
        case "Add":
            todos = fn.get_todo()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            fn.write_todo(todos)
        # WIN_CLOSED è la variabile che indica la chiusura della finestra
        case sg.WIN_CLOSED:
            break
window.close()


