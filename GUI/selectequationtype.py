from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt

class SelectEquationType(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        self.main_layout = QVBoxLayout()

        # Add a vertical spacer to push content to the middle
        self.main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.label = QLabel("Select Equation Type")
        self.label.setStyleSheet("font-size:50px; font-weight:bold; color:#439A97;")
        self.main_layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Create buttons for Linear and Nonlinear Equations
        button_texts = ["Linear Equation", "Nonlinear Equation"]
        self.buttons_layout = QVBoxLayout()
        for text in button_texts:
            btn = QPushButton(text, self)
            # Connect buttons to appropriate methods
            btn.clicked.connect(lambda checked, equation_type=text: self.show_equation_screen(equation_type))
            self.buttons_layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)
            btn.setStyleSheet("""
                QPushButton {
                    min-width: 600px;
                    height: 50px;
                    background-color: #439A97;
                    color: white;
                    border-radius: 5px;
                    padding: 10px;
                    margin: 15px 0;
                    font-size: 40px;
                }
                QPushButton:hover {
                    background-color: #62B6B7;
                }
            """)

        self.main_layout.addLayout(self.buttons_layout)
        self.main_layout.setAlignment(self.buttons_layout, Qt.AlignmentFlag.AlignCenter)

        # Add another vertical spacer to push content to the middle
        self.main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.setLayout(self.main_layout)

    def show_equation_screen(self, equation_type):
        if equation_type == "Linear Equation":
            self.stacked_widget.setCurrentIndex(1)
        elif equation_type == "Nonlinear Equation":
            self.stacked_widget.setCurrentIndex(5)

# Example usage:
# if __name__ == "__main__":
#     import sys
#     from PyQt6.QtWidgets import QApplication, QStackedWidget
#     app = QApplication(sys.argv)
#     stacked_widget = QStackedWidget()
#     select_equation_type = SelectEquationType(stacked_widget)
#     stacked_widget.addWidget(select_equation_type)
#     stacked_widget.show()
#     sys.exit(app.exec())
