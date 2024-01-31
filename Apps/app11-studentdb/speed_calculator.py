from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QComboBox, QGridLayout, QLineEdit, QPushButton
import sys
from datetime import datetime

class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        distance_label = QLabel("Distance")
        self.distance_label_edit = QLineEdit()

        time_label = QLabel("Time (hours)")
        self.time_label_edit = QLineEdit()

        self.measure = QComboBox()
        self.measure.addItems(["Metric (km)", "Imperial (miles)"])

        calculate_button = QPushButton("Calculate speed")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_label_edit, 0, 1)
        grid.addWidget(self.measure, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_label_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)
        

        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.distance_label_edit.text())
        time = float(self.time_label_edit.text())

        if self.measure.currentText() == "Imperial (miles)":
            miles = distance * 1.609
            result = miles * time 
        else:
            result = distance * time

        self.output_label.setText(f"Average speed: {result}")

app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())

