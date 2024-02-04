from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, \
QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QComboBox
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
import sys
import sqlite3

class MainWindow(QMainWindow): # this module offers more flexibility
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management system")

        # adding items in the menu bar
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")

        # adding sub-items
        add_student_action = QAction("Add Student", self)
        add_student_action.triggered.connect(self.insert)      

        about_action = QAction("About", self)
        search_action = QAction("Search", self)
        search_action.triggered.connect(self.search)

        file_menu_item.addAction(add_student_action)
        help_menu_item.addAction(about_action)
        edit_menu_item.addAction(search_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False) # it hides the number of row
        self.setCentralWidget(self.table)
        

    def load_data(self):
        connection = sqlite3.connect("database.db")
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
        
        layout.addWidget(self.student_name)
        layout.addWidget(self.course_name)
        layout.addWidget(self.mobile_phone)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile_phone.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, phone) \
                        VALUES (?, ?, ?)",
                       (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        student_table.load_data()

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
        connection = sqlite3.connect("database.db")
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