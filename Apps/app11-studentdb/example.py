from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
import sys
from datetime import datetime

# desktop app sample with PyQt6
# one class for each window

class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__() # returns the parent class init method
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        # create widgets
        name_label = QLabel("Name :")
        self.name_line_edit = QLineEdit()

        date_label = QLabel("Date of birth DD/MM/YYYY :")
        self.date_birth_line_edit = QLineEdit() # instance variable

        calculate_button = QPushButton("Calculate age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        # add widgets to grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_label, 1, 0)
        grid.addWidget(self.date_birth_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2) # span across 1 rows and take 2 columns
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year 
        date_of_birth = self.date_birth_line_edit.text() # extract the user year
        year_of_birth = datetime.strptime(date_of_birth, "%d/%m/%Y").date().year
        age = current_year - year_of_birth
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old")

app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())