# third party library for gui
import PySimpleGUI as sg

# 1st line
label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
button1 = sg.FilesBrowse("Choose")

# 2nd line
label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose")

firstRow = [label1, input1, button1]
secondRow = [label2, input2, button2]

compressButton = sg.Button("Compress")

window = sg.Window("File Zipper", layout = [firstRow,
                                            secondRow,
                                            [compressButton]])

window.read()
window.close()

print("test")