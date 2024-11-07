from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget
from PyQt6.QtCore import Qt


class Methods(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        
        layout = QVBoxLayout()

        label = QLabel("Choose Method")
        label.setStyleSheet("font-size:50px; font-weight:bold; color:#439A97; padding-left:100px")
        layout.addWidget(label)

        # Create and connect buttons dynamically in a loop
        button_texts = ["Gauss", "Gauss Jordan", "LU Decomposition", "Jacobi", "Gauss Seidel"]
        for text in button_texts:
            btn = QPushButton(text, self)
            btn.clicked.connect(lambda checked, method=text: self.show_matrix_screen(method))
            layout.addWidget(btn)

        # Set the layout for this widget
        self.setLayout(layout)

        # Apply the stylesheet for the entire widget
        self.setStyleSheet("""
            QPushButton {
                min-width: 600px;
                height: 50px;
                background-color: #439A97;
                color: #F3F7EC;
                border-radius: 5px;
                padding: 10px;
                margin: 15px 0;
                font-size: 40px;
            }
            QPushButton:hover {
                background-color: #62B6B7;
            }
        """)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def show_matrix_screen(self, method):
        # Pass the selected method to the second page
        if(method == "LU Decomposition"):
            self.stacked_widget.setCurrentIndex(1)
        else:
            self.stacked_widget.setCurrentIndex(2)
            self.stacked_widget.currentWidget().display_method(method)
        # Get the second page widget and call its method to display the selected method

