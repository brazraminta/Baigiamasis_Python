import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, \
    QMainWindow, QAction, qApp, QGridLayout, \
    QTabWidget, QMessageBox, QProgressBar, QGroupBox, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt, QTimer, QSize


class OrderWindow(QWidget):
    def __init__(self, order):
        super().__init__()
        self.setWindowTitle('Jusu uzsakymo informacija')
        layout = QHBoxLayout()
        self.setLayout(layout)

        for book in order:
            layout.addWidget(QLabel(book))


class OrderingBooks(QWidget):
    def __init__(self):
        super().__init__()
        self.order = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Knygu uzsakymas')
        self.setGeometry(300, 300, 800, 600)
        layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        self.item_input = QLineEdit(self)
        self.item_input.setPlaceholderText('Irasykite knygos pavadinima')
        layout.addWidget(self.item_input)

        self.item_count_label = QLabel(self)
        layout.addWidget(self.item_count_label)

        self.add_button = QPushButton('Prideti knyga', self)
        self.add_button.clicked.connect(self.add_item)
        self.add_button.clicked.connect(self.increase_progress)
        layout.addWidget(self.add_button)

        self.list_widget = QListWidget(self)
        layout.addWidget(self.list_widget)

        self.delete_button = QPushButton('Isimti knyga', self)
        self.delete_button.clicked.connect(self.delete_item)
        self.delete_button.clicked.connect(self.decrease_progress)
        layout.addWidget(self.delete_button)

        self.confirm_button = QPushButton('Patvirtinti uzsakyma', self)
        self.confirm_button.clicked.connect(self.order_confirmation)
        # self.confirm_button.clicked.connect(self.progress_full)
        button_layout.addWidget(self.confirm_button)

        self.cancel_button = QPushButton('Atsaukti uzsakyma', self)
        self.cancel_button.clicked.connect(self.order_cancellation)
        self.cancel_button.clicked.connect(self.reset_progress)
        button_layout.addWidget(self.cancel_button)

        self.progress_bar = QProgressBar()
        self.progress_bar.setFormat('Uzsakymo busena: %p%')
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)
        self.setWindowTitle('Knygu uzsakymo puslapis')

    def add_item(self):
        item_text = self.item_input.text()
        if item_text:
            item = QListWidgetItem(item_text)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            self.list_widget.addItem(item)
            self.item_input.clear()
            self.update_item_count()
        else:
            QMessageBox.warning(self, 'Klaida', 'Irasykite knygos pavadinima')

    def delete_item(self):
        for item in self.list_widget.selectedItems():
            self.list_widget.takeItem(self.list_widget.row(item))

        self.update_item_count()

    def order_confirmation(self):
        if self.list_widget.count() == 0:
            QMessageBox.warning(self, 'Klaida', 'Nepridejote nei vienos knygos')
        else:
            for index in range(self.list_widget.count()):
                item = self.list_widget.item(index)
                self.order.append(item.text())

            QMessageBox.information(self, 'Information', 'Jusu uzsakymas sekmingai patvirtintas!')

            self.list_widget.clear()
            self.update_item_count()
            self.progress_bar.setValue(100)
            self.show_order()

    def order_cancellation(self):
        self.list_widget.clear()
        ################# turbut reikes is istorijos istrinti pridetas knygas
        QMessageBox.information(self, 'Information', 'Jusu uzsakymas sekmingai atsauktas!')

    def increase_progress(self):
        current_value = self.progress_bar.value()
        if current_value < 100:
            self.progress_bar.setValue(current_value + 33)

    def decrease_progress(self):
        current_value = self.progress_bar.value()
        if current_value > 0:
            self.progress_bar.setValue(current_value - 33)

    def progress_full(self):
        current_value = self.progress_bar.value()
        if current_value == 99:
            self.progress_bar.setValue(100)

    def reset_progress(self):
        QMessageBox.warning(self, 'Warning', 'Uzsakymo busena atstatyta')
        self.progress_bar.setValue(0)

    def update_item_count(self):
        item_count = self.list_widget.count()
        self.item_count_label.setText(f'Pasirinkta knygu: {item_count}')

    def show_order(self):
        order_count = self.update_item_count()
        print(f'Jus uzsakete {order_count} knygu: ')

        for book in self.order:
            print(book.item_text)

        self.order_window = OrderWindow(self.order)
        self.order_window.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OrderingBooks()
    window.show()
    sys.exit(app.exec_())
