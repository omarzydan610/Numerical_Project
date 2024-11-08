from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontMetrics

from GUI.matrix_screen import clear_layout


class Solve(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        # Set up the window
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        main_layout = QVBoxLayout()
        
        # Container layout for fields
        container_layout = QVBoxLayout()

        # Method label, centered horizontally
        self.method_label = QLabel("Method:")
        self.method_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        container_layout.addWidget(self.method_label)
        container_layout.addWidget(QLabel(" "))

        # Execution time label and field in an HBox, centered
        execution_time_layout = QHBoxLayout()
        self.execution_time_label = QLabel('Execution Time:')
        self.execution_time_field = QLineEdit()
        self.execution_time_field.setReadOnly(True)
        self.execution_time_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        execution_time_layout.addWidget(self.execution_time_label)
        execution_time_layout.addWidget(self.execution_time_field)
        
        font_metrics = QFontMetrics(self.execution_time_field.font())
        text_width = font_metrics.horizontalAdvance(self.execution_time_field.text()) + 30  # Adding padding
        self.execution_time_field.setFixedWidth(text_width)
        
        container_layout.addLayout(execution_time_layout)
        container_layout.addWidget(QLabel(" "))

        # Iterations label and field in an HBox, centered
        iterations_layout = QHBoxLayout()
        self.iterations_label = QLabel('Number of Iterations:')
        self.iterations_field = QLineEdit()
        self.iterations_field.setReadOnly(True)
        self.iterations_field.setAlignment(Qt.AlignmentFlag.AlignCenter)

        iterations_layout.addWidget(self.iterations_label)
        iterations_layout.addWidget(self.iterations_field)
        font_metrics = QFontMetrics(self.iterations_field.font())
        text_width = font_metrics.horizontalAdvance(self.iterations_field.text()) + 30  # Adding padding
        self.iterations_field.setFixedWidth(text_width)
        container_layout.addLayout(iterations_layout)
        self.iterations_space=QLabel("")
        container_layout.addWidget(self.iterations_space)

        # Solution label (optional)
        self.solve_label = QLabel('Solution is:')
        self.solve_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        container_layout.addWidget(self.solve_label)
        container_layout.addWidget(QLabel(" "))
        
        self.solution_layout=QHBoxLayout()
        self.solution_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        container_layout.addLayout(self.solution_layout)
        
        

        # Wrap the container layout in a widget to enable horizontal centering
        container_widget = QWidget()
        container_widget.setLayout(container_layout)

        # Add the container widget to the main layout, centered horizontally
        main_layout.addWidget(container_widget, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Spacer item to push content towards the top
        main_layout.addStretch()

        # Home button, center-aligned
        self.Home_button = QPushButton('Home screen')
        self.Home_button.clicked.connect(self.home)
        main_layout.addWidget(self.Home_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Set main layout as the layout for the widget
        self.setLayout(main_layout)

        # Apply the stylesheet
        self.setStyleSheet("""
            QWidget{
                font-size: 20px;
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
                min-width: fit-content;
            }
            QPushButton{
                background-color: #439A97;
                color: #F3F7EC;
                border-radius: 5px;
                padding: 10px;
                margin: 15px 0;
                font-size: 20px;
            }
            QPushButton:hover{
                background-color: #62B6B7;
            }
        """)


        
    def setSolution(self, solution):
        if solution == "error":
            return
        self.execution_time_field.setText(f"{round(solution[2], 9)}")
        font_metrics = QFontMetrics(self.execution_time_field.font())
        text_width = font_metrics.horizontalAdvance(f"{round(solution[2], 9)}") + 30  # Adding padding
        self.execution_time_field.setFixedWidth(text_width)
        
        self.method_label.setText(f"Selected method : {solution[0]}")
        
        clear_layout(self.solution_layout)
        sol = solution[1]
        for i in range(len(sol)):
            temp = QVBoxLayout()
            temp.setAlignment(Qt.AlignmentFlag.AlignCenter)
            temp2 = QLabel(f"X{i+1}")
            temp2.setAlignment(Qt.AlignmentFlag.AlignCenter)
            temp2.setStyleSheet("font-size:14px")
            temp.addWidget(temp2)
            res = QLineEdit(f"{sol[i]}")
            res.setReadOnly(True)
            res.setStyleSheet("""
                QLineEdit {
                    background-color: #fff;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                    padding: 5px;
                    min-width: fit-content;
                }
            """)

            # Calculate the width of the content and set the width of the QLineEdit
            res.setFixedWidth(150)

            temp.addWidget(res)
            self.solution_layout.addLayout(temp)
            if (solution[0] == "Gauss" or solution[0] == "Gauss Jordan" ):
                self.iterations_label.setVisible(False)
                self.iterations_field.setVisible(False)
                self.iterations_space.setVisible(False)


    def home(self):
        self.stacked_widget.setCurrentIndex(0)
