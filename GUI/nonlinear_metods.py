from pathlib import Path
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

class NonLinearMethods(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        self.main_layout = QVBoxLayout()

        # Back button layout
        self.backButton_latout = QHBoxLayout()
        pixmap = QPixmap(str(Path("Numerical_lab/images/back_icon.png").resolve())).scaled(24, 24)  # Resize to 24x24 pixels
        icon = QIcon(pixmap)

        back_button = QPushButton(self)
        back_button.setIcon(icon)  # Set the icon
        back_button.setIconSize(back_button.sizeHint())  # Adjust icon size if needed
        back_button.setFixedSize(24, 24)

        # Custom style for back button
        back_button.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: transparent;
                min-width: 30px;
                min-height: 30px;
                padding: 0;
                margin: 0;
            }
            QPushButton:hover {
                background-color: #E0F7FA;  # Optional hover effect for the back button
            }
        """)  # Apply the custom style sheet

        back_button.clicked.connect(self.go_back)
        self.backButton_latout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.main_layout.addLayout(self.backButton_latout)

        # Label for method selection
        label = QLabel("Choose Method")
        label.setStyleSheet("font-size:50px; font-weight:bold; color:#439A97;")
        self.main_layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)

        # List of method buttons
        button_texts = ["Bisection", "False-Position", "Fixed point", "Original Newton-Raphson", "Modified Newton-Raphson", "Secant Method"]

        for text in button_texts:
            btn = QPushButton(text, self)
            btn.clicked.connect(lambda checked, method=text: self.show_matrix_screen(method))
            self.main_layout.addWidget(btn)

        self.setLayout(self.main_layout)
        self.setStyleSheet("""
            QPushButton {
                min-width: 600px;
                height: 50px;
                background-color: #439A97;
                color: #F3F7EC;
                border-radius: 5px;
                padding: 7px;
                margin: 10px 0;
                font-size: 40px;
            }
            QPushButton:hover {
                background-color: #62B6B7;
            }
        """)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def show_matrix_screen(self, method):
        self.stacked_widget.setCurrentIndex(3)


    def go_back(self):
        print("Back button clicked")  # Debugging line
        self.stacked_widget.setCurrentIndex(0)
