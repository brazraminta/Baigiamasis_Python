import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QKeySequence, QFont
from PyQt5.QtCore import Qt, QSize, QTimer, QTime, QDate
from loginForm import LoginForm
from registrationForm import RegistrationForm
from knyguUzsakymas import OrderingBooks
from knyguUzsakymas import OrderingBooks, HistoryDialog

conn_params = {
    "host": "localhost",
    "database": "baigiamasis",  #pakeisti
    "user": "postgres",
    "password": "riko789",
    "port": "5432"
}


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.conn_params = conn_params

        self.setWindowTitle("Bibliotekos Inventoriaus Valdymo Sistema")
        self.setGeometry(300, 300, 1200, 750)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.vLayout = QVBoxLayout(self.central_widget) # vertikalus isdestymas
        self.hLayout = QHBoxLayout() # horizontalus isdestymas

        self.gridLayout = QGridLayout() # gardeliu isdestymas
        self.gridLayout.setSpacing(0)

        self.setStyleSheet("background-image: url(C:/Users/Raminta/Documents/Programavimas su python 2023-12-18/baigiamasis darbas/book-3033196_1280.jpg);")

        # nustatom datos rodyma
        self.date_label = QLabel()
        self.date_label.setStyleSheet("background-color: white;")
        self.date_label.setStyleSheet("QLabel{font-size: 14pt;}")
        # self.date_label.setFixedSize(150, 50)
        self.vLayout.addWidget(self.date_label)
        self.date_timer = QTimer(self)
        self.date_timer.timeout.connect(self.showDate)
        self.date_timer.start(1000)

        # nustatom laiko rodyma
        font = QFont('Times New Roman', 14, QFont.Bold)
        self.timer_label = QLabel()
        self.timer_label.setAlignment(Qt.AlignLeft)
        self.timer_label.setFont(font)
        self.vLayout.addWidget(self.timer_label)
        self.setLayout(self.vLayout)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

        # centruojam gardeles su stretch'u is abieju pusiu
        self.hLayout.addStretch(1)
        self.hLayout.addLayout(self.gridLayout)
        self.hLayout.addStretch(1)

        self.vLayout.addLayout(self.hLayout)
        # gardeles pastumiam i lango virsu
        # self.vLayout.addStretch(1)

        self.central_widget.setStyleSheet("background-color: pink;")
        # self.vLayout.addStretch(1)

        # sukuriam knygu paieskos (ir detalios) lango nuoroda/mygtuka
        self.search_title = QLabel()
        self.search_title.setAlignment(Qt.AlignLeft)
        self.search_title.setStyleSheet("QLabel{font-size: 12pt;}")
        self.gridLayout.addWidget(self.search_title, 0, 3)
        self.search_title.setAlignment(Qt.AlignLeft)

        self.search_button = QPushButton("Knygu paieska ir uzsakymas", self)
        self.search_button.setFixedSize(300, 100)
        self.search_button.setStyleSheet("background-color: green; font-size: 20px;")
        # self.hLayout.addWidget(self.search_button)
        self.gridLayout.addWidget(self.search_button, 4, 1)
        self.search_button.clicked.connect(self.open_book_search)

        self.book_search = OrderingBooks() # sukuriame 'self.book_search' egzempliorių pagrindinio lango konstruktoriuje, kurį naudosime 'open_book_search' metode.

        # # paieskos laukelio centravimo pabaiga
        self.vLayout.addStretch(1)

        # sukuriame toolbar su mygtukais ir meniu juosta
        self.toolbar = QToolBar()
        self.toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(self.toolbar)

        self.pradzia_button = QAction(QIcon("C:/Users/Raminta/PycharmProjects/baigiamasisProjektas/fugue-icons-3.5.6/icons/application-home.png"), "&Pradinis puslapis", self)
        self.pradzia_button.setStatusTip("Eiti i pagrindini puslapi")
        self.pradzia_button.triggered.connect(self.onMyToolBarButtonClick)
        self.pradzia_button.setCheckable(True)
        self.pradzia_button.setShortcut(QKeySequence("Ctrl+m"))
        self.toolbar.addAction(self.pradzia_button)

        self.uzsakymas_info_button = QAction(QIcon("C:/Users/Raminta/PycharmProjects/baigiamasisProjektas/fugue-icons-3.5.6/icons/address-book--plus.png"), "&Knygu uzsakymas", self)
        self.uzsakymas_info_button.setStatusTip("Perziureti uzsakyma")
        self.uzsakymas_info_button.triggered.connect(self.onMyToolBarButtonClick)
        self.uzsakymas_info_button.setCheckable(True)
        self.uzsakymas_info_button.setShortcut(QKeySequence("Ctrl+o"))
        self.toolbar.addAction(self.uzsakymas_info_button)

        self.toolbar.addSeparator()

        self.returnRemind_button = QAction(QIcon("C:/Users/Raminta/PycharmProjects/baigiamasisProjektas/fugue-icons-3.5.6/icons/alarm-clock--exclamation.png"), "&Artejantys grazinimai", self)
        self.returnRemind_button.setStatusTip("Artejantys uzsakytu knygu grazinimai")
        self.returnRemind_button.triggered.connect(self.onMyToolBarButtonClick)
        self.returnRemind_button.setCheckable(True)
        self.returnRemind_button.setShortcut(QKeySequence("Ctrl+g"))
        self.toolbar.addAction(self.returnRemind_button)

        # Create a spacer action
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolbar.addWidget(spacer)

        self.negalia_button = QAction(QIcon("C:/Users/Raminta/PycharmProjects/baigiamasisProjektas/fugue-icons-3.5.6/icons/script-binary.png"), "&Versija turintiems negalia", self)
        self.negalia_button.setStatusTip("Versija turintiems negalia")
        self.negalia_button.triggered.connect(self.onMyToolBarButtonClick)
        self.negalia_button.setCheckable(True)
        self.negalia_button.setShortcut(QKeySequence("Ctrl+n"))
        self.toolbar.addAction(self.negalia_button)

        self.duk_button = QAction(QIcon("C:/Users/Raminta/PycharmProjects/baigiamasisProjektas/fugue-icons-3.5.6/icons/document-attribute-q.png"), "&DUK", self)
        self.duk_button.setStatusTip("Dazniausiai uzduodami klausimai")
        self.duk_button.triggered.connect(self.onMyToolBarButtonClick)
        self.duk_button.setCheckable(True)
        self.duk_button.setShortcut(QKeySequence("Ctrl+q"))
        self.toolbar.addAction(self.duk_button)

        self.request_button = QAction(QIcon("C:/Users/Raminta/PycharmProjects/baigiamasisProjektas/fugue-icons-3.5.6/icons/balloon-smiley.png"), "&Siusti uzklausa", self)
        self.request_button.setStatusTip("Siusti uzklausa bibliotekininkui")
        self.request_button.triggered.connect(self.onMyToolBarButtonClick)
        self.request_button.setCheckable(True)
        self.request_button.setShortcut(QKeySequence("Ctrl+u"))
        self.toolbar.addAction(self.request_button)

        # pridedam prisijungimo ir registracijos mygtukus
        self.login_button = QPushButton('Prisijungti prie paskyros', self)
        self.login_button.setFixedSize(150, 50)
        self.login_button.setStyleSheet("background-color: white;")
        # self.gridLayout.addWidget(self.login_button, 5, 0) # pridedam mygtuką į pirmą eilutę ir pirmą stulpelį
        self.vLayout.addWidget(self.login_button)
        self.login_button.clicked.connect(self.open_login_form)

        self.register_button = QPushButton('Sukurti paskyra', self)
        self.register_button.setFixedSize(150, 50)
        self.register_button.setStyleSheet("background-color: white;")
        # self.gridLayout.addWidget(self.register_button, 5, 1) # pridedam mygtuką į antrą eilutę ir pirmą stulpelį)
        self.vLayout.addWidget(self.register_button)
        self.register_button.clicked.connect(self.open_registration_form)

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(self.uzsakymas_info_button)

        file_menu.addSeparator()

        file_submenu = file_menu.addMenu("Submeniu")
        file_submenu.addAction(self.returnRemind_button)

    def onMyToolBarButtonClick(self, s):
        print("click", s)

    ## dialogBox
    # def button_clicked(self, s):
    #     print("clicked", s)
    #
    #     dlg = CustomDialog()  # subklase
    #     if dlg.exec():
    #         print("Success!")
    #     else:
    #         print("Cancel!")

    def open_login_form(self):
        self.login_form = LoginForm()
        self.login_form.show()

    def open_registration_form(self):
        self.registration_form = RegistrationForm()
        self.registration_form.setModal(True)
        self.registration_form.show()

    def open_book_search(self):
        try:
            self.book_search.setModal(True)
            self.book_search.show()
        except Exception as e:
            print(f"Error: {e}")

    def showTime(self):
        current_time = QTime.currentTime()
        time_text = current_time.toString('hh:mm:ss')
        self.timer_label.setText(time_text)

    def showDate(self):
        current_date = QDate.currentDate()
        date_text = current_date.toString('yyyy.MM.dd')
        self.date_label.setText(date_text)

# class CustomDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         self.setWindowTitle("Hello! Let's start the dialog")
#
#         QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
#
#         self.buttonBox = QDialogButtonBox(QBtn)
#         self.buttonBox.accepted.connect(self.accept)
#         self.buttonBox.rejected.connect(self.reject)
#
#         self.layout = QVBoxLayout()
#         message = QLabel("Something happened, is that OK?")
#         self.layout.addWidget(message)
#         self.layout.addWidget(self.buttonBox)
#         self.setLayout(self.layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
