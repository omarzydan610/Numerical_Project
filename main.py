import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QPushButton
from PyQt6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

from GUI.methods_screen import Methods
from GUI.LU_screen import LU
from GUI.matrix_screen import Matrix
from GUI.solve_screen import Solve 



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.setStyleSheet("background-color:white")
        self.setWindowTitle("numerical methods")
        self.setGeometry(100, 100, 800, 600)

        # Create QStackedWidget to manage multiple pages
        self.stacked_widget = QStackedWidget(self)

        # Create two pages
        self.methods_page = Methods(self.stacked_widget)
        self.LU_page = LU(self.stacked_widget)
        self.matrix_screen_page = Matrix(self.stacked_widget)
        self.solve_page = Solve(self.stacked_widget)

        # Add pages to QStackedWidget
        self.stacked_widget.addWidget(self.methods_page)
        self.stacked_widget.addWidget(self.LU_page)
        self.stacked_widget.addWidget(self.matrix_screen_page)
        self.stacked_widget.addWidget(self.solve_page)

        # Set the layout of the main window
        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)
        self.setStyleSheet("background-color:#CBEDD5")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
