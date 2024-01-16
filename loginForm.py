import sys
from PyQt5.QtWidgets import *

class LoginForm(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Login Form')
        self.setGeometry(100, 100, 300, 150)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        form_layout = QFormLayout()  # arranges the widgets

        # QLabel and QLineEdit widgets for username
        username_label = QLabel("Username:")
        self.username_field = QLineEdit()

        # QLabel and QLineEdit widgets for password
        password_label = QLabel("Password:")
        self.password_field = QLineEdit()
        self.password_field.setEchoMode(QLineEdit.Password)

        # button for login
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.login)

        # add widgets to the form layout
        form_layout.addRow(username_label, self.username_field)
        form_layout.addRow(password_label, self.password_field)
        form_layout.addRow(login_button)

        # set the layout for the central widget
        central_widget.setLayout(form_layout)

    def login(self):
        # Retrieve the username and password entered by the user
        username = self.username_field.text()
        password = self.password_field.text()

        # Check if the username and password are valid (for demonstration purposes)
        if username == "admin" and password == "pass123$":
            QMessageBox.information(self, "Login Successful", "Welcome, " + username + "!")
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password. Please try again.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginForm()
    window.show()
    sys.exit(app.exec_())






