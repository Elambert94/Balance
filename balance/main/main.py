import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QColor

class Toolbar(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

         # Attributes
        toolbar_items = ["Home", "Settings"]
        toolbar_layout = QtWidgets.QHBoxLayout(self)
        toolbar_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.create_toolbar_items(toolbar_items, toolbar_layout)
    
    def create_toolbar_items(self, items : list[str], parent : QtWidgets.QLayout):
        for item in items:
            created_item = ToolbarButton(item)
            parent.addWidget(created_item, alignment=QtCore.Qt.AlignCenter)
    
    def create_toolbar_item(self, display_item : str) -> QtWidgets.QLabel:
        """Create a new toolbar item.

        :param display_item: Text value for the item. 
        :type display_item: str
        :return: The created item.
        :rtype: QtWidgets.QLabel
        """
        item = QtWidgets.QLabel(display_item)
        item.setPalette(QColor('Red'))
        item.setAutoFillBackground(True)
        return item
    
class ToolbarButton(QtWidgets.QPushButton):
    def __init__(self, text : str):
        """
        :param text: Text to be assigned to the button.
        :type text: str
        """
        super().__init__()
        self.text = text
        self.setText(text)

    
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
        self.main_container = self.create_main_container()
        self.create_user_interface()
        

    def create_user_interface(self):
        """Creates the user interface elements for the application.

        """
        toolbar = Toolbar()
        self.main_container.addWidget(toolbar)
        self.content_stack = QtWidgets.QStackedWidget(self)
        
    
    def create_main_container(self):
        """Creates the main container for app content.

        """
        container = QtWidgets.QVBoxLayout(self)
        container.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        return container
    
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