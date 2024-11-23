import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QTextEdit, QVBoxLayout, QPushButton

class StepsDisplay(QDialog):
    def __init__(self, steps="No available solutions"):
        super().__init__()
        self.setWindowTitle("Steps of Solution")
        self.setFixedSize(600, 400) 
        self.setStyleSheet("background-color:#CBEDD5")
        layout = QVBoxLayout()


        self.title_label = QLabel("Solution Steps:")
        self.title_label.setStyleSheet("color:black;font-size:15px;")
        layout.addWidget(self.title_label)

        self.text_display = QTextEdit(self)
        self.text_display.setReadOnly(True)
        self.text_display.setText(steps)
        self.text_display.setStyleSheet("color:black;background-color:white")
        layout.addWidget(self.text_display)

        self.close_button = QPushButton("Close", self)
        self.close_button.setStyleSheet("""
            QPushButton {
                background-color: #439A97;
                color: white;
                border-radius: 10px;
                padding: 15px 30px;
                font-size: 18px;
                font-weight: bold;
                max-width: 100px;
                margin: 0 auto;
            }
            QPushButton:hover {
                background-color: #62B6B7;
            }
        """)

        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)
