import sys
from PyQt5.QtWidgets import *


class RegistrationForm(QDialog):
    def __init__(self):
        super(RegistrationForm, self).__init__()

        self.setWindowTitle("User Registration")
        self.setGeometry(100, 100, 300, 400)

        # new group box
        self.formGroupBox = QGroupBox("Registration Form")

        # create the line edit
        self.lineEditUsername = QLineEdit()

        self.lineEditPassword = QLineEdit()
        self.lineEditPassword.setEchoMode(QLineEdit.Password)

        self.lineEditName = QLineEdit()
        self.lineEditSurname = QLineEdit()
        self.lineEditBirthDate = QLineEdit()

        self.radioButtonGenderFemale = QRadioButton("Female")
        self.radioButtonGenderMale = QRadioButton("Male")

        self.lineEditEmail = QLineEdit()

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

    # getting the info method which is called when the form gets accepted
    def getInfo(self):
        # print the information on the form
        print("Username: {0}".format(self.lineEditUsername.text()))
        gender = "Female" if self.radioButtonGenderFemale.isChecked() else "Male"
        print("Name: {0}".format(self.lineEditName.text()))
        print("Surname: {0}".format(self.lineEditSurname.text()))
        print("Birth Date: {0}".format(self.lineEditBirthDate.text()))
        print("Gender: {0}".format(gender))
        print("Email: {0}".format(self.lineEditEmail.text()))

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

        self.formGroupBox.setLayout(layout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())