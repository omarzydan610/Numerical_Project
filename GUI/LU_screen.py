from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon,QPixmap
from pathlib import Path


class LU(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.main_layout = QVBoxLayout()
        
        self.backButton_latout=QHBoxLayout()
        pixmap = QPixmap(str(Path("images/back_icon.png").resolve())).scaled(24, 24)  # Resize to 24x24 pixels
        icon = QIcon(pixmap)

        back_button = QPushButton(self)
        back_button.setIcon(icon)  # Set the icon
        back_button.setIconSize(back_button.sizeHint())  # Adjust icon size if needed
        back_button.setFixedSize(30, 30)
        back_button.setStyleSheet("border:none")
        back_button.clicked.connect(self.go_back_to_methods)
        self.backButton_latout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.main_layout.addLayout(self.backButton_latout)


        label = QLabel("Choose LU Method")
        label.setStyleSheet("font-size:50px; font-weight:bold; color:#439A97;")
        self.main_layout.addWidget(label,alignment=Qt.AlignmentFlag.AlignCenter)

        # Create and connect buttons dynamically in a loop
        button_texts = ["Doolittle", "Crout", "Cholesky"]
        self.buttons_layout=QVBoxLayout()
        for text in button_texts:
            btn = QPushButton(text, self)
            btn.clicked.connect(lambda checked, method=text: self.show_matrix_screen(method))
            self.buttons_layout.addWidget(btn,alignment=Qt.AlignmentFlag.AlignCenter)
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
            

        # Set the layout for this widget
        self.main_layout.addLayout(self.buttons_layout)
        self.main_layout.addStretch()
        self.setLayout(self.main_layout)
        
        # self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def show_matrix_screen(self, method):
        # Pass the selected method to the second page
        self.stacked_widget.setCurrentIndex(2)
        # Get the second page widget and call its method to display the selected method
        self.stacked_widget.currentWidget().display_method(method)
        
    def go_back_to_methods(self):
        self.stacked_widget.setCurrentIndex(0)

