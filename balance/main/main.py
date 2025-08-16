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

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.people_manager = PeopleManager()
        self.main_layout.addWidget(self.people_manager)  

class PeopleManager(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        master_container = QtWidgets.QHBoxLayout(self)
        master_container.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        
        user_panel = QtWidgets.QVBoxLayout(self)
        user_panel.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        master_container.addLayout(user_panel)

        self.details_layout = QtWidgets.QVBoxLayout(self)
        self.details_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.details_label_name = QtWidgets.QLabel("")
        self.details_layout.addWidget(self.details_label_name)

        master_container.addLayout(self.details_layout)
        
        new_person_dialog = QtWidgets.QHBoxLayout(self)
        user_panel.addLayout(new_person_dialog)

        self.person_list = QtWidgets.QVBoxLayout(self)
        user_panel.addLayout(self.person_list)

        input_dialog = QtWidgets.QLineEdit(placeholderText="Add New Person")
        input_dialog.setFixedHeight(50)
        input_dialog.setFixedWidth(150)
        new_person_dialog.addWidget(input_dialog)

        btn_add_person = QtWidgets.QPushButton("+")
        btn_add_person.setFixedHeight(50)
        btn_add_person.setFixedWidth(50)
        btn_add_person.clicked.connect(lambda: self.add_person(input_dialog.text()))
        new_person_dialog.addWidget(btn_add_person)
        
    def open_person_details(self, person : 'PersonWidget'):
        self.details_label_name.setText(person.name)
        pass
    
    def load_person(self, person : 'PersonWidget'):
        self.open_person_details(person)
        print(person.name)
    
    def add_person(self, name : str):
        person = PersonWidget(name)
        self.person_list.addWidget(person)
        person.btn_user.clicked.connect(lambda: self.load_person(person))
        person.btn_remove_person.clicked.connect(lambda: self.remove_person(person))
        return person
    
    def remove_person(self, widget : 'QtWidgets.QWidget'):
        self.widget = widget
        self.person_list.removeWidget(self.widget)
        widget.deleteLater()
    
class PersonDetails(QtWidgets.QWidget):
    def __init__(self, person : 'PersonWidget'):
        pass

class PersonWidget(QtWidgets.QWidget):
    def __init__(self, name : str): # will change this person arg to the person class later.
        super().__init__()
        
        self.name = name
        
        layout = QtWidgets.QHBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        
        self.btn_user = QtWidgets.QPushButton(name)
        self.btn_user.setMinimumWidth(100)

        self.btn_remove_person = QtWidgets.QPushButton("-")

        layout.addWidget(self.btn_user)
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