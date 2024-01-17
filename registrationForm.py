import sys
from PyQt5.QtWidgets import *


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
        # add the action to the buttons, when the form gets accepted
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
        # print the information on the form
        msgBox = QMessageBox()
        msgBox.setWindowTitle("User Inforamtion")

        print("Informacija apie vartotoja: ")
        print("Username (email): {0}".format(self.lineEditEmail.text()))
        print("Name: {0}".format(self.lineEditName.text()))
        print("Surname: {0}".format(self.lineEditSurname.text()))
        print("Birth Date: {0}".format(self.lineEditBirthDate.text()))
        gender = "Female" if self.radioButtonGenderFemale.isChecked() else "Male"
        print("Gender: {0}".format(gender))

        self.close()

    def creatingForm(self):
        layout = QFormLayout()  # Define the main layout

        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.radioButtonGenderFemale)
        gender_layout.addWidget(self.radioButtonGenderMale)
        layout.addRow(QLabel("Gender"), gender_layout)

        # add rows for names, category and birth date
        layout.addRow(QLabel("Username"), self.lineEditUsername)
        layout.addRow(QLabel("Password"), self.lineEditPassword)
        layout.addRow(QLabel("Name"), self.lineEditName)
        layout.addRow(QLabel("Surname"), self.lineEditSurname)
        layout.addRow(QLabel("Birth Date (YYYY-MM-DD)"), self.lineEditBirthDate)
        layout.addRow(QLabel("Email"), self.lineEditEmail)

        layout.addRow(QLabel(f"Su naudojimosi \ntaisyklemis bei \nprivatumo politika \nsusipazinau"), self.checkBoxTaisykles)
        self.checkBoxTaisykles.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        # self.checkBoxTaisykles.setStyleSheet("background-color: lightgreen;")

        # sukurti mygtuka "Uzregistruoti"

        self.formGroupBox.setLayout(layout)
        self.formGroupBox.setStyleSheet("background-color: lightgreen;")

    # def register(self):





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())