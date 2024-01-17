import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt, QSize

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bibliotekos Inventoriaus Valdymo Sistema")
        self.setGeometry(300, 300, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.central_widget.setStyleSheet("background-color: lightgreen;")

        # self.label = QLabel("Knygu paieska")
        # self.label.setAlignment(Qt.AlignCenter)
        # self.label.setStyleSheet("background-color: lightgreen;")

        # sukuriame toolbar su mygtukais ir meniu juosta
        self.toolbar = QToolBar()
        self.toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(self.toolbar)

        self.pradzia_button = QAction(QIcon("C:/Users/Raminta/PycharmProjects/baigiamasisProjektas/fugue-icons-3.5.6/icons/application-home.png"), "&Pradinis puslapis", self)
        self.pradzia_button.setStatusTip("Eiti i pagrindini puslapi")
        self.pradzia_button.triggered.connect(self.onMyToolBarButtonClick)
        self.pradzia_button.setCheckable(True)
        self.pradzia_button.setShortcut(QKeySequence("Ctrl+p"))
        self.toolbar.addAction(self.pradzia_button)

        self.uzsakymas_button = QAction(QIcon("C:/Users/Raminta/PycharmProjects/baigiamasisProjektas/fugue-icons-3.5.6/icons/address-book--plus.png"), "&Knygu uzsakymas", self)
        self.uzsakymas_button.setStatusTip("Knygu uzsakymas")
        self.uzsakymas_button.triggered.connect(self.onMyToolBarButtonClick)
        self.uzsakymas_button.setCheckable(True)
        self.uzsakymas_button.setShortcut(QKeySequence("Ctrl+p"))
        self.toolbar.addAction(self.uzsakymas_button)

        self.toolbar.addSeparator()

        self.returnRemind_button = QAction(QIcon("C:/Users/Raminta/PycharmProjects/baigiamasisProjektas/fugue-icons-3.5.6/icons/alarm-clock--exclamation.png"), "&Artejantys grazinimai", self)
        self.returnRemind_button.setStatusTip("Artejantys uzsakytu knygu grazinimai")
        self.returnRemind_button.triggered.connect(self.onMyToolBarButtonClick)
        self.returnRemind_button.setCheckable(True)
        self.returnRemind_button.setShortcut(QKeySequence("Ctrl+o"))
        self.toolbar.addAction(self.returnRemind_button)

        # Create a spacer action
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolbar.addWidget(spacer)

        self.negalia_button = QAction(QIcon("C:/Users/Raminta/PycharmProjects/baigiamasisProjektas/fugue-icons-3.5.6/icons/script-binary.png"), "&Versija turintiems negalia", self)
        self.negalia_button.setStatusTip("Versija turintiems negalia")
        self.negalia_button.triggered.connect(self.onMyToolBarButtonClick)
        self.negalia_button.setCheckable(True)
        self.negalia_button.setShortcut(QKeySequence("Ctrl+o"))
        self.toolbar.addAction(self.negalia_button)

        self.duk_button = QAction(QIcon("C:/Users/Raminta/PycharmProjects/baigiamasisProjektas/fugue-icons-3.5.6/icons/document-attribute-q.png"), "&DUK", self)
        self.duk_button.setStatusTip("Dazniausiai uzduodami klausimai")
        self.duk_button.triggered.connect(self.onMyToolBarButtonClick)
        self.duk_button.setCheckable(True)
        self.duk_button.setShortcut(QKeySequence("Ctrl+o"))
        self.toolbar.addAction(self.duk_button)

        self.request_button = QAction(QIcon("C:/Users/Raminta/PycharmProjects/baigiamasisProjektas/fugue-icons-3.5.6/icons/balloon-smiley.png"), "&Siusti uzklausa", self)
        self.request_button.setStatusTip("Siusti uzklausa bibliotekininkui")
        self.request_button.triggered.connect(self.onMyToolBarButtonClick)
        self.request_button.setCheckable(True)
        self.request_button.setShortcut(QKeySequence("Ctrl+o"))
        self.toolbar.addAction(self.request_button)

        # self.toolbar.addWidget(QLabel("Hello"))
        # self.toolbar.addWidget(QCheckBox())

        # pridedam dialogo langa
        self.dialog_button = QPushButton("Press me for a dialog!")
        self.dialog_button.setStyleSheet("background-color: yellow;")
        self.dialog_button.clicked.connect(self.button_clicked)
        self.layout.addWidget(self.dialog_button)


        self.setStatusBar(QStatusBar(self))

        # menu = self.menuBar()
        #
        # file_menu = menu.addMenu("&File")
        # file_menu.addAction(self.uzsakymas_button)
        #
        # file_menu.addSeparator()
        #
        # file_submenu = file_menu.addMenu("Submeniu")
        # file_submenu.addAction(self.returnRemind_button)

    def onMyToolBarButtonClick(selfself, s):
        print("click", s)

    def button_clicked(self, s):
        print("clicked", s)

        dlg = CustomDialog()
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")



class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Hello! Let's start the dialog")

        self.setWindowTitle("HELLO!")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
