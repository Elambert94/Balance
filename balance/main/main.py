import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QColor
from base_classes import Person, PersonManager, Account

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

class WidgetHomepage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.people_manager = WidgetPeopleManager()
        self.main_layout.addWidget(self.people_manager)  

class WidgetItemPersonDetailsPanel(QtWidgets.QWidget):
    def __init__(self, person = Person):
        super().__init__()
        
        self.person = person
        self.main_layout = QtWidgets.QVBoxLayout(self)
        name_layout = QtWidgets.QHBoxLayout(self)
        label_name = QtWidgets.QLabel(self.person.get_name())
        self.label_name_val = QtWidgets.QLabel("")
        name_layout.addWidget(label_name)
        name_layout.addWidget(self.label_name_val)

        layout_account_details = QtWidgets.QVBoxLayout(self)
        layout_add_new_account = QtWidgets.QHBoxLayout(self)
        self.input_new_account = QtWidgets.QLineEdit(placeholderText="Enter Account Name")
        self.input_new_account.setFixedWidth(300)
        self.btn_new_account = QtWidgets.QPushButton("+")
        self.btn_new_account.setFixedSize(30, 30)
        self.btn_new_account.clicked.connect(lambda: self.create_account(self.input_new_account.text()))
        
        layout_add_new_account.addWidget(self.input_new_account)
        layout_add_new_account.addWidget(self.btn_new_account)
        layout_account_details.addLayout(layout_add_new_account)

        label_accounts = QtWidgets.QLabel("Accounts")
        self.layout_account_list = QtWidgets.QVBoxLayout(self)
        self.layout_account_list.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        
        layout_account_details.addWidget(label_accounts)
        layout_account_details.addLayout(self.layout_account_list)

        self.load_person()
        
        self.main_layout.addLayout(name_layout)
        self.main_layout.addLayout(layout_account_details)
    
    def create_account(self, account_name : str):
        new_account = self.person.create_account(account_name)
        new_widget = WidgetItemAccount(new_account)
        new_widget.btn_remove.clicked.connect(lambda: self.remove_account(self.remove_account(new_widget)))
        self.layout_account_list.addWidget(new_widget)

    def add_account_widget(self, account : Account):
        new_widget = WidgetItemAccount(account)
        new_widget.btn_remove.clicked.connect(lambda: self.remove_account(self.remove_account(new_widget)))
        self.layout_account_list.addWidget(new_widget)

    def load_person(self):
        for account in self.person.get_accounts():
            self.add_account_widget(account)

    def remove_account(self, widget_account : 'WidgetItemAccount'):
        # Delete account 
        self.layout_account_list.removeWidget(widget_account)
        widget_account.deleteLater()
   
class WidgetItemPersonPanel(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setFixedWidth(400)
        self.main_panel = QtWidgets.QVBoxLayout(self)
        self.main_panel.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        new_person_dialog = QtWidgets.QHBoxLayout(self)
        self.main_panel.addLayout(new_person_dialog)

        self.person_list = QtWidgets.QVBoxLayout(self)
        self.main_panel.addLayout(self.person_list)

        self.input_dialog = QtWidgets.QLineEdit(placeholderText="Add New Person")
        self.input_dialog.setFixedHeight(30)
        new_person_dialog.addWidget(self.input_dialog)

        self.btn_add_person = QtWidgets.QPushButton("+")
        self.btn_add_person.setFixedHeight(30)
        self.btn_add_person.setFixedWidth(60)
        
        new_person_dialog.addWidget(self.btn_add_person)

class WidgetPeopleManager(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.person_manager = PersonManager()

        self.master_container = QtWidgets.QHBoxLayout(self)
        
        self.user_panel = WidgetItemPersonPanel()
        self.user_panel.btn_add_person.clicked.connect(lambda : self.add_person(self.user_panel.input_dialog.text()))
        self.master_container.addWidget(self.user_panel)

        self.details : WidgetItemPersonDetailsPanel = None

        self.master_container.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.master_container.addStretch(1)
    
    def load_person(self, person : 'Person'):
        
        if self.details:
            self.master_container.removeWidget(self.details)
            self.details.deleteLater()
        
        self.details = WidgetItemPersonDetailsPanel(person)
        self.master_container.insertWidget(1, self.details)
        
    def add_person(self, name : str):
        
        new_person = self.person_manager.add_person_by_name(name)
        new_person_widget = WidgetItemPerson(new_person)
        
        self.user_panel.person_list.addWidget(new_person_widget)

        new_person_widget.btn.clicked.connect(lambda: self.load_person(new_person))
        new_person_widget.btn_remove.clicked.connect(lambda: self.remove_person(new_person_widget))

        return new_person_widget
    
    def remove_person(self, widget : 'WidgetItemPerson'):
        
        self.widget = widget
        self.person_manager.remove_person(widget.person)
        self.user_panel.person_list.removeWidget(self.widget)
        widget.deleteLater()

class WidgetItem(QtWidgets.QWidget):
    def __init__(self): 
        super().__init__()
        
        layout = QtWidgets.QHBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        
        self.btn = QtWidgets.QPushButton("")
        self.btn.setMinimumWidth(100)

        self.btn_remove = QtWidgets.QPushButton("-")

        layout.addWidget(self.btn)
        layout.addWidget(self.btn_remove)

class WidgetItemPerson(WidgetItem):
    def __init__(self, person : Person):
        super().__init__()

        self.person = person
        self.btn.setText(self.person.get_name())

class WidgetItemAccount(WidgetItem):
    def __init__(self, account : Account):
        super().__init__()

        self.account = account
        self.btn.setText(self.account.get_account_name())

class WidgetSettings(QtWidgets.QWidget):
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
        
        homepage = WidgetHomepage()
        toolbar_btn_homepage = toolbar.create_toolbar_button("Home")
        toolbar_btn_homepage.clicked.connect(lambda: content_stack.setCurrentIndex(0))
        content_stack.addWidget(homepage)
        
        settings = WidgetSettings()
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