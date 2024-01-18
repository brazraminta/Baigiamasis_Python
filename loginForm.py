import sys
from PyQt5.QtWidgets import *
import psycopg2
from registrationForm import RegistrationForm

conn_params = {
    "host": "localhost",
    "database": "baigiamasis",  #pakeisti
    "user": "postgres",
    "password": "riko789",
    "port": "5432"
}

class LoginForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.conn_params = conn_params

        self.setWindowTitle('Login Form')
        self.setGeometry(100, 100, 300, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        form_layout = QFormLayout()  # arranges the widgets

        # QLabel and QLineEdit widgets for username
        username_label = QLabel("Username:")
        self.username_field = QLineEdit()
        self.username_field.setFixedSize(200, 25)

        # QLabel and QLineEdit widgets for password
        password_label = QLabel("Password:")
        self.password_field = QLineEdit()
        self.password_field.setEchoMode(QLineEdit.Password)

        vartotojas_label = QLabel("Jungiates kaip:")
        self.vartotojo_teises = QComboBox()
        self.vartotojo_teises.addItem("Skaitytojas")
        self.vartotojo_teises.addItem("Darbuotojas")
        self.vartotojo_teises.addItem("Administratorius")
        self.vartotojo_teises.currentIndexChanged.connect(self.index_changed)
        self.vartotojo_teises.currentTextChanged.connect(self.text_changed)

        # button for login
        login_button = QPushButton("Jungtis")
        login_button.setFixedSize(300, 40)
        login_button.clicked.connect(self.login)

        # jei naujas vartotojas, nuoroda i registracija
        registration_button_label = QLabel("Neturite paskyros? Registruotis>")
        self.register_button = QPushButton("Registruotis")
        self.register_button.setFixedSize(100, 30)
        self.register_button.clicked.connect(self.registration)

        # add widgets to the form layout
        form_layout.addRow(username_label, self.username_field)
        form_layout.addRow(password_label, self.password_field)
        form_layout.addRow(vartotojas_label, self.vartotojo_teises)
        form_layout.addRow(login_button)
        form_layout.addRow(registration_button_label, self.register_button)

        # set the layout for the central widget
        central_widget.setLayout(form_layout)

    def login(self):
        # Retrieve the username and password entered by the user
        username = self.username_field.text()
        password = self.password_field.text()
        role_selected = self.vartotojo_teises.currentText()  # get the selected role from the QComboBox

        connection = psycopg2.connect(**self.conn_params)
        cursor = connection.cursor()

        # Check if the username and password are valid for the selected role
        cursor.execute(f"SELECT * FROM {role_selected} WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user is not None:
            QMessageBox.information(self, "Login Successful", "Welcome, " + username + "!")
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password. Please try again.")

    def index_changed(selfself, i): # i is an int
        print(i)

    def text_changed(self, t): # t is a str
        print(t)

    def registration(self):
        self.register = RegistrationForm()
        self.register.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginForm()
    window.show()
    sys.exit(app.exec_())






