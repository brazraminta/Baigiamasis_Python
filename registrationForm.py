import sys
from PyQt5.QtWidgets import *
import psycopg2


class RegistrationForm(QDialog):
    def __init__(self):
        super(RegistrationForm, self).__init__()

        self.setWindowTitle("User Registration Form")
        self.setGeometry(100, 100, 300, 400)

        # new group box
        self.formGroupBox = QGroupBox("Registration Form")

        # create the line edit for registration data
        self.lineEditEmail = QLineEdit()
        self.lineEditEmail.setStyleSheet("background-color: white;")

        self.lineEditPassword = QLineEdit()
        self.lineEditPassword.setEchoMode(QLineEdit.Password)  # papildomai sukurti 'confirm password' laukelius
        self.lineEditPassword.setStyleSheet("background-color: white;")

        self.lineEditName = QLineEdit()
        self.lineEditName.setStyleSheet("background-color: white;")
        self.lineEditSurname = QLineEdit()
        self.lineEditSurname.setStyleSheet("background-color: white;")
        self.lineEditBirthDate = QLineEdit()
        self.lineEditBirthDate.setStyleSheet("background-color: white;")

        self.radioButtonGenderFemale = QRadioButton("Female")
        self.radioButtonGenderMale = QRadioButton("Male")

        self.checkBoxTaisykles = QCheckBox()

        # self.confirm_button = QPushButton("Register")
        # self.confirm_button.clicked.connect(self.register)

        # # a new combo box for user category
        # self.comboBoxCategory = QComboBox()
        #
        # # add the items into the combo box
        # self.comboBoxCategory.addItems(["Studentas", "Destytojas", "Darbuotojas"])

        # call the function which will be helping to create the form
        self.creatingForm()

        # creating a new dialog button for the actions ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        # # add the action to the buttons, when the form gets accepted
        # self.buttonBox.accepted.connect(self.register_login)
        self.buttonBox.accepted.connect(self.getInfo)
        # add the action to the button, when the form gets rejected
        self.buttonBox.rejected.connect(self.reject)

        # creating new vertical layout
        layoutMain = QVBoxLayout()
        # add the form group box to the main layout
        layoutMain.addWidget(self.formGroupBox)
        #add the button box to the main layout
        layoutMain.addWidget(self.buttonBox)

        self.setLayout(layoutMain)

    # getting the user info (method which is called when the form gets accepted)
    def getInfo(self):
        username = self.lineEditEmail.text()
        password = self.lineEditPassword.text()
        name = self.lineEditName.text()
        surname = self.lineEditSurname.text()
        birth_date = self.lineEditBirthDate.text()
        gender = "Female" if self.radioButtonGenderFemale.isChecked() else "Male"

        # connection = psycopg2.connect(**self.conn_params)
        # cursor = connection.cursor()

        # # itraukti nauja skaitytoja i readers lentele
        # cursor.execute(
        #     "INSERT INTO readers(username, password, name, surname, birth_date, gender) VALUES (%s, %s, %s, %s, %s, %s)",
        # (username, password, name, surname, birth_date, gender)
        # )
        # connection.commit()
        # cursor.close()
        # connection.close()

        # patikrinam, ar visi laukeliai pazymeti
        if not username or not password or not name or not surname or not birth_date:
            # print the information on the form
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Warning")
            msgBox.setText("All fields must be filled!")
            msgBox.exec_()
        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("User Inforamtion")
            msgBox.setText(f"Informacija apie skaitytoja:\nUsername (email): {username}\nName: {name}\nSurname: {surname}\nBirth Date: {birth_date}\nGender: {gender}")
            msgBox.exec_()

        # self.close()

    def creatingForm(self):
        layout = QFormLayout()  # Define the main layout

        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.radioButtonGenderFemale)
        gender_layout.addWidget(self.radioButtonGenderMale)
        layout.addRow(QLabel("Gender"), gender_layout)

        # add rows for names, category and birth date
        layout.addRow(QLabel("Email"), self.lineEditEmail)
        layout.addRow(QLabel("Password"), self.lineEditPassword)
        layout.addRow(QLabel("Name"), self.lineEditName)
        layout.addRow(QLabel("Surname"), self.lineEditSurname)
        layout.addRow(QLabel("Birth Date (YYYY-MM-DD)"), self.lineEditBirthDate)

        layout.addRow(QLabel(f"Su naudojimosi \ntaisyklemis bei \nprivatumo politika \nsusipazinau"), self.checkBoxTaisykles)
        self.checkBoxTaisykles.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        # self.checkBoxTaisykles.setStyleSheet("background-color: lightgreen;")

        # sukurti mygtuka "Uzregistruoti"

        self.formGroupBox.setLayout(layout)
        self.formGroupBox.setStyleSheet("background-color: lightgreen;")

    # #def register_login(self, username, password):
    #     connection = psycopg2.connect(**self.conn_params)
    #     cursor = connection.cursor()
    #
    #     cursor.execute("INSERT INTO readers(username, password) VALUES (%s, %s)", (username, password))
    #
    #     connection.commit()
    #     cursor.close()
    #     connection.close()
    #     print("Jusu registracija buvo sekminga")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())




class RegistrationFormOfLibrarian(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Register User (for librarians)")
        self.setGeometry(150, 150, 400, 500)

        # new group box
        self.formGroupBox = QGroupBox("Readers Registration Form") # groups related widgets together in a frame with a title on top

        # create the line edit for registration data
        self.lineEditEmail = QLineEdit()
        self.lineEditEmail.setStyleSheet("background-color: white;")

        self.lineEditPassword = QLineEdit()
        self.lineEditPassword.setEchoMode(QLineEdit.Password)  # papildomai sukurti 'confirm password' laukelius
        self.lineEditPassword.setStyleSheet("background-color: white;")

        self.lineEditName = QLineEdit()
        self.lineEditName.setStyleSheet("background-color: white;")

        self.lineEditSurname = QLineEdit()
        self.lineEditSurname.setStyleSheet("background-color: white;")

        self.lineEditBirthDate = QLineEdit()
        self.lineEditBirthDate.setStyleSheet("background-color: white;")

        self.radioButtonGenderFemale = QRadioButton("Female")
        self.radioButtonGenderMale = QRadioButton("Male")

        self.checkBoxStudentas = QCheckBox("Studentas")
        self.checkBoxMokytojas = QCheckBox("Mokytojas")

        self.checkBoxTaisykles = QCheckBox()

        # call the function which will be helping to create the form
        self.creatingForm()

        # creating a new dialog button for the actions ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        # # add the action to the buttons, when the form gets accepted
        # self.buttonBox.accepted.connect(self.register_login)
        self.buttonBox.accepted.connect(self.getInfo)
        # add the action to the button, when the form gets rejected
        self.buttonBox.rejected.connect(self.reject)

        # creating new vertical layout
        layoutMain = QVBoxLayout()
        # add the form group box to the main layout
        layoutMain.addWidget(self.formGroupBox)
        # add the button box to the main layout
        layoutMain.addWidget(self.buttonBox)

        self.setLayout(layoutMain)


    # getting the user info (method which is called when the form gets accepted)
    def getInfo(self):
        username = self.lineEditEmail.text()
        password = self.lineEditPassword.text()
        name = self.lineEditName.text()
        surname = self.lineEditSurname.text()
        birth_date = self.lineEditBirthDate.text()
        gender = "Female" if self.radioButtonGenderFemale.isChecked() else "Male"

        # print the information on the form
        msgBox = QMessageBox()
        msgBox.setWindowTitle("User Inforamtion")
        msgBox.setText(f"Informacija apie skaitytoja:\nUsername (email): {username}\nName: {name}\nSurname: {surname}\nBirth Date: {birth_date}\nGender: {gender}")
        msgBox.exec_()

        self.close()

    def creatingForm(self):
        layout = QFormLayout()  # the main layout

        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.radioButtonGenderFemale)
        gender_layout.addWidget(self.radioButtonGenderMale)
        layout.addRow(QLabel("Gender"), gender_layout)

        # add rows for names, category and birth date
        layout.addRow(QLabel("Email"), self.lineEditEmail)
        layout.addRow(QLabel("Password"), self.lineEditPassword)
        layout.addRow(QLabel("Name"), self.lineEditName)
        layout.addRow(QLabel("Surname"), self.lineEditSurname)
        layout.addRow(QLabel("Birth Date (YYYY-MM-DD)"), self.lineEditBirthDate)

        categories_layout = QHBoxLayout()
        categories_layout.addWidget(self.checkBoxStudentas)
        categories_layout.addWidget(self.checkBoxMokytojas)
        layout.addRow(QLabel("Users' Category"), categories_layout)

        layout.addRow(QLabel(f"Su naudojimosi \ntaisyklemis bei \nprivatumo politika \nsusipazinau"), self.checkBoxTaisykles)
        self.checkBoxTaisykles.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.formGroupBox.setLayout(layout)
        self.formGroupBox.setStyleSheet("background-color: lightgreen;")


    # def register_login(self, username, password):
    #     connection = psycopg2.connect(**self.conn_params)
    #     cursor = connection.cursor()
    #
    #     cursor.execute("INSERT INTO readers(username, password) VALUES (%s, %s)", (username, password))
    #
    #     connection.commit()
    #     cursor.close()
    #     connection.close()
    #     print("Jusu registracija buvo sekminga")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrationFormOfLibrarian()
    window.show()
    sys.exit(app.exec_())