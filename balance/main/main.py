import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QPixmap

class MainWidget(QtWidgets.QWidget):
    """Main application widget.

    :param QtWidgets: Parent widget.
    :type QtWidgets: QWidget
    """
    def __init__(self):
        """Constructor for MyWidget."""
        super().__init__()
        self.setWindowTitle("Balance")
        title = self.create_title_banner()

    def create_title_banner(self):
        """Create the title banner for the application.

        :return: The layout containing the title banner widgets.
        :rtype: QVBoxLayout
        """

        # Create Title Text
        self.box_layout = QtWidgets.QVBoxLayout(self, alignment=QtCore.Qt.AlignTop)
        self.text = QtWidgets.QLabel("Balance",
                                     alignment=QtCore.Qt.AlignCenter)
        self.text.setStyleSheet("font-size: 48px; font-weight: bold; color: #333;")
        self.box_layout.addWidget(self.text)

        # Add Logo
        self.logo_label = QtWidgets.QLabel("LogoLabel", alignment=QtCore.Qt.AlignCenter)
        self.logo = QPixmap("resources/icons/scale.png")
        self.logo = QPixmap("resources/icons/scale.png")
        if self.logo.isNull():
            self.logo_label.setText("Logo not found")
        else:
            self.logo_label.setPixmap(self.logo)
            self.box_layout.addWidget(self.logo_label)
        return self.box_layout
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainWidget()
    widget.showFullScreen()
    widget.show()
    sys.exit(app.exec())