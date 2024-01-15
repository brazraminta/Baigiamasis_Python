import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, \
    QMainWindow, QAction, qApp, \
    QTabWidget, QMessageBox, QProgressBar, QGroupBox, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt, QTimer


class Vartotojas():
    def __init__(self, name, last_name, category, birth_date, gender, email):
        self.name = name
        self.last_name = last_name
        self.category = category
        self.birth_date = birth_date
        self.gender = gender
        self.email = email

class Administratorius(Vartotojas):
    def __init__(self, name, last_name, email):
        super().__init__(name, last_name)

    def suteikti_teises_vartotojui(self):
