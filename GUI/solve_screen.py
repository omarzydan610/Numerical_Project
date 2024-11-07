from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QFormLayout, QPushButton
from PyQt6.QtCore import Qt
class Solve(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        # Set up the window
        self.setWindowTitle('Solv Page')
        self.setGeometry(100, 100, 400, 200)

        # Create layout
        layout = QVBoxLayout()
        self.setGeometry(100, 100, 800, 600)
        # Create form layout
        form_layout = QFormLayout()

        # Execution time field
        self.execution_time_label = QLabel('Execution Time:')
        self.execution_time_field = QLineEdit()
        self.execution_time_field.setReadOnly(True)
        form_layout.addRow(self.execution_time_label, self.execution_time_field)

        # Solve field
        self.solve_label = QLabel('Solve:')
        self.solve_field = QLineEdit()
        self.solve_field.setReadOnly(True)
        form_layout.addRow(self.solve_label, self.solve_field)

        # Number of iterations field
        self.iterations_label = QLabel('Number of Iterations:')
        self.iterations_field = QLineEdit()
        self.iterations_field.setReadOnly(True)
        form_layout.addRow(self.iterations_label, self.iterations_field)

        layout.addLayout(form_layout)

        self.setLayout(layout)
        self.Home_button = QPushButton('Home screen')
        self.Home_button.clicked.connect(self.home)
        layout.addWidget(self.Home_button)
        layout.addWidget(self.Home_button, alignment=Qt.AlignmentFlag.AlignCenter)


        # Apply the stylesheet
        self.setStyleSheet("""
            QWidget{
                background-color: #f0f0f0;
                font-size: 14px;
                font-family: Arial, sans-serif;
            }
            QLabel{
                font-weight: bold;
                color: #333;
            }
            QLineEdit{
                background-color: #fff;
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 5px;
            }
            QPushButton{
                background-color: #007bff;
                color: #fff;
                border: none;
                border-radius: 4px;
                padding: 10px 20px;
                font-size: 14px;
            }
            QPushButton:hover{
                background-color: #0056b3;
            }
        """)


    def home(self):
        self.stacked_widget.setCurrentIndex(0)
