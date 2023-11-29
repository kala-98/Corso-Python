# third party library
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")

window = sg.Window("My App", layout=[[label, input_box]])
window.read()
window.close()