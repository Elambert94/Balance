import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QColor

class Toolbar(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

         # Attributes
        self.toolbar_layout = QtWidgets.QHBoxLayout(self)
        self.toolbar_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
    
    def create_toolbar_button(self, display_text : str) ->  QtWidgets.QPushButton:
        button = ToolbarButton(display_text)
        self.toolbar_layout.addWidget(button)
        return button
    
class ToolbarButton(QtWidgets.QPushButton):
    def __init__(self, text : str):
        """
        :param text: Text to be assigned to the button.
        :type text: str
        """
        super().__init__()
        self.text = text
        self.setText(text)

class Homepage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: lightblue;")

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        
        title = QtWidgets.QLabel("People")
        self.main_layout.addWidget(title)

        self.people_manager = PeopleManager()
        self.main_layout.addWidget(self.people_manager)

        self.create_people()
    
    def create_people(self):
        people = ["Elliott", "Vicky"]
        for person in people:
            self.people_manager.add_person(person)
        
class PeopleManager(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.container = QtWidgets.QVBoxLayout(self)
        self.create_add_new_user_widget()
        
        self.person_container = QtWidgets.QVBoxLayout(self)
        self.container.addLayout(self.person_container)
        self.container.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.container.addStretch(1)

        
    def create_add_new_user_widget(self):
        
        widget_width = 150
        widget_height = 30

        layout = QtWidgets.QHBoxLayout(self)
        
        button = QtWidgets.QPushButton("+")
        button.clicked.connect(lambda: self.add_person(input.toPlainText()))
        button.setFixedSize(widget_height, widget_height)

        input = QtWidgets.QTextEdit(placeholderText="Add new person")
        input.setFixedSize(widget_width, widget_height)

        layout.addWidget(input)
        layout.addWidget(button)
        
        self.container.addLayout(layout)


    def load_people(self):
        print("loading people")
    
    def add_person(self, name : str):
        person = PersonWidget(name)
        person.btn_remove_person.clicked.connect(lambda: self.remove_person(person))
        self.person_container.insertWidget(0, person)
        return person
    
    def remove_person(self, person : 'PersonWidget'):
        self.container.removeWidget(person)
        person.deleteLater()

class PersonWidget(QtWidgets.QWidget):
    def __init__(self, name : str): # will change this person arg to the person class later.
        super().__init__()
        
        self.name = name
        
        layout = QtWidgets.QHBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        
        text = QtWidgets.QLabel(name)
        text.setMinimumWidth(100)
        
        self.btn_remove_person = QtWidgets.QPushButton("-")

        layout.addWidget(text)
        layout.addWidget(self.btn_remove_person)
    
        
class Settings(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        title = QtWidgets.QLabel("Settings")
        layout.addWidget(title)        

class MainAppWidget(QtWidgets.QWidget):
    """Main application widget.

    :param QtWidgets: Parent widget.
    :type QtWidgets: QWidget
    """
    def __init__(self):
        """Constructor for MyWidget."""
        super().__init__()
        
        # Window settings
        self.setWindowTitle("Balance") 
        self.apply_minimum_dimensions()
        self.showFullScreen()

        # Interface creation.
        self.create_user_interface()
        

    def create_user_interface(self):
        """Creates the user interface elements for the application.

        """

        master_container = QtWidgets.QVBoxLayout(self)
        master_container.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        toolbar = Toolbar()
        master_container.addWidget(toolbar)

        content_stack = QtWidgets.QStackedWidget(self)
        master_container.addWidget(content_stack)
        
        homepage = Homepage()
        toolbar_btn_homepage = toolbar.create_toolbar_button("Home")
        toolbar_btn_homepage.clicked.connect(lambda: content_stack.setCurrentIndex(0))
        content_stack.addWidget(homepage)
        
        settings = Settings()
        toolbar_btn_settings = toolbar.create_toolbar_button("Settings")
        toolbar_btn_settings.clicked.connect(lambda: content_stack.setCurrentIndex(1))
        content_stack.addWidget(settings)
        
    
    def apply_minimum_dimensions(self, width : int = 1280, height : int = 720):
        """
        :param width: Minimum width to set, defaults to 1280
        :type width: int, optional
        :param height: Minimum height to set, defaults to 720
        :type height: int, optional
        """
        self.setMinimumWidth(width)
        self.setMinimumHeight(height)


    

    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainAppWidget()
    sys.exit(app.exec())