from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget
from PyQt6.QtCore import Qt


class LU(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout()

        label = QLabel("Choose Method")
        label.setStyleSheet("font-size:50px; font-weight:bold; color:black; padding-left:100px")
        layout.addWidget(label)

        # Create and connect buttons dynamically in a loop
        button_texts = ["Doolittle", "Crout", "Cholesky"]
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
                background-color: lightblue;
                color: black;
                border-radius: 5px;
                padding: 10px;
                margin: 15px 0;
                font-size: 40px;
            }
            QPushButton:hover {
                background-color: #ddf3fa;
            }
        """)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def show_matrix_screen(self, method):
        # Pass the selected method to the second page
        self.stacked_widget.setCurrentIndex(2)
        # Get the second page widget and call its method to display the selected method
        self.stacked_widget.currentWidget().display_method(method)

