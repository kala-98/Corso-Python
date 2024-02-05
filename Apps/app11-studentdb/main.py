from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QToolBar, QMessageBox, \
QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QComboBox, QStatusBar
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
import sys
import sqlite3


# creating a connection with the database
class DatabaseConnection:
    def __init__(self, database_file = "database.db"):
        self.database_file = database_file

    def connect(self):
        connection = sqlite3.connect(self.database_file)
        return connection


class MainWindow(QMainWindow): # this module offers more flexibility
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management system")

        # adding items in the menu bar
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")

        # adding sub-items
        add_student_action = QAction(QIcon("icons/add.png"), "Add Student", self)
        add_student_action.triggered.connect(self.insert)      

        about_action = QAction("About", self)
        about_action.triggered.connect(self.about)
        search_action = QAction(QIcon("icons/search.png"),"Search", self)
        search_action.triggered.connect(self.search)

        file_menu_item.addAction(add_student_action)
        help_menu_item.addAction(about_action)
        edit_menu_item.addAction(search_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False) # it hides the number of row
        self.setCentralWidget(self.table)

        # creating a toolbar
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)

        # adding elements to toolbar
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        # create status bar and add status bar elements
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        # detect the cell click
        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        edit_button = QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete)

        # deleting previous pushbuttons if already exist
        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)

    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()

    def about(self):
        dialog = AboutDialog()
        dialog.exec()

    def load_data(self):
        connection = DatabaseConnection().connect()
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        connection.close()
        # self.table.resizeColumnsToContents()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        window = InsertSearch()
        window.exec()


class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        content = """Desktop App created during the Python course
                     on the platform Udemy"""
        self.setText(content)


class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Student Data")
        # self.setFixedWidth(300)
        # self.setFixedHeight(300)

        layout = QVBoxLayout()
        message = QLabel("Are you sure you want to delete the record?")
        index = student_table.table.currentRow()
        self.student_id = student_table.table.item(index, 0).text()
        button1 = QPushButton("Yes")
        button2 = QPushButton("No")

        button1.clicked.connect(self.delete_student)
        button2.clicked.connect(self.close_dialog)

        layout.addWidget(message)
        layout.addWidget(button1)
        layout.addWidget(button2)

        self.setLayout(layout)
    
    def delete_student(self):
        id = self.student_id
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students \
                        WHERE id = ?",
                       (id))
        connection.commit()
        cursor.close()
        connection.close()
        self.close()
        
        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle("Success")
        confirmation_widget.setText("The record was deleted successfully")
        confirmation_widget.exec()
    
    def close_dialog(self):
        self.close()


class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        # formatting the window layout
        layout = QVBoxLayout()

        # extract the student name from the selected cell
        index = student_table.table.currentRow()
        student_name = student_table.table.item(index, 1).text()

        # get id from selected row
        self.student_id = student_table.table.item(index, 0).text()

        self.student_name = QLineEdit(student_name)
        self.student_name.setPlaceholderText("Name")

        # extract the course name
        course_name = student_table.table.item(index, 2).text()
        self.course_name = QComboBox()
        courses = ["Biology", "History", "Math", "Physics"]
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(course_name)
        
        mobile = student_table.table.item(index, 3).text()
        self.mobile_phone = QLineEdit(mobile)
        self.mobile_phone.setPlaceholderText("Phone")

        button = QPushButton("Update")
        button.clicked.connect(self.update_student)
        
        layout.addWidget(self.student_name)
        layout.addWidget(self.course_name)
        layout.addWidget(self.mobile_phone)
        layout.addWidget(button)

        self.setLayout(layout)

    def update_student(self):
        id = self.student_id
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile_phone.text()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE students \
                        SET name = ?, course = ?, phone = ? \
                        WHERE id = ?",
                       (name, course, mobile, id))
        connection.commit()
        cursor.close()
        connection.close()
        student_table.load_data()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        # formatting the window layout
        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        
        self.course_name = QComboBox()
        courses = ["Biology", "History", "Math", "Physics"]
        self.course_name.addItems(courses)
        
        self.mobile_phone = QLineEdit()
        self.mobile_phone.setPlaceholderText("Phone")

        button = QPushButton("Insert")
        button.clicked.connect(self.add_student)

        button2 = QPushButton("Close")
        button2.clicked.connect(self.close_dialog)
        
        layout.addWidget(self.student_name)
        layout.addWidget(self.course_name)
        layout.addWidget(self.mobile_phone)
        layout.addWidget(button)
        layout.addWidget(button2)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile_phone.text()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, phone) \
                        VALUES (?, ?, ?)",
                       (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        student_table.load_data()

    def close_dialog(self):
        self.close()


class InsertSearch(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        # formatting the window layout
        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")

        button = QPushButton("Search")
        button.clicked.connect(self.search_student)

        layout.addWidget(self.student_name)
        layout.addWidget(button)

        self.setLayout(layout)

    def search_student(self):
        name = self.student_name.text()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        result = cursor.execute(f"SELECT * FROM students where name = ?", (name,))  
        rows = list(result)
        print(rows)

        # retrieving each value from column "name"            
        items = student_table.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            print(item)
            student_table.table.item(item.row(), 1).setSelected(True)

        cursor.close()
        connection.close()
       

app = QApplication(sys.argv)
student_table = MainWindow()
student_table.show()
student_table.load_data()
student_table.resize(500, 350)
sys.exit(app.exec())