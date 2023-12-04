# third party library for gui
import PySimpleGUI as sg
import zip_creator as zc

# 1st line
label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
button1 = sg.FilesBrowse("Choose", key="files")

# 2nd line
label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose", key="destination")

#3rd line
label3 = sg.Text("Write the name of the zip file")
input3 = sg.Input(size = (15, 10), key = "filename")

firstRow = [label1, input1, button1]
secondRow = [label2, input2, button2]
thirdRow = [label3, input3]

compressButton = sg.Button("Compress")
output_label = sg.Text(key="output", text_color = "green")

window = sg.Window("File Zipper", layout = [firstRow,
                                            secondRow,
                                            thirdRow,
                                            [compressButton, output_label]])

while True:
    event, values = window.read()
    #print(event, values)
    
    filepaths = values["files"].split(";")
    destinationPath = values["destination"] 
    nameZipFile = values["filename"]
    zc.make_archive(filepaths, destinationPath, nameZipFile)
    window["output"].update(value = "Compression completed")

    if event == sg.WIN_CLOSED:
        break

window.close()

