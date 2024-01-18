import psycopg2
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QKeySequence, QFont
from PyQt5.QtCore import Qt, QSize, QTimer, QTime, Qt

conn_params = {
    "host": "localhost",
    "database": "baigiamasis",  #pakeisti
    "user": "postgres",
    "password": "riko789",
    "port": "5432"
}

class OrderingBooks(QWidget):
    def __init__(self):
        super().__init__()
        self.conn_params = conn_params
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.layout.addLayout(self.button_layout)

        # knygu paieskos laukelio pavadinimas
        self.title = QLabel("Leidinio paieska")
        self.title.setAlignment(Qt.AlignLeft)
        self.title.setStyleSheet("QLabel{font-size: 14pt;}")
        self.layout.addWidget(self.title)

        # knygu pasieskos laukelis
        self.search_field = QLineEdit(self)
        self.search_field.setPlaceholderText('Irasykite knygos pavadinima')
        self.search_field.setFixedSize(500, 50)
        self.search_field.setStyleSheet("background-color: white;")
        self.search_field.returnPressed.connect(self.search_button_clicked)
        self.layout.addWidget(self.search_field)

        # # knygu skaiciaus pavadinimas
        # self.item_count_label = QLabel(self)
        # self.layout.addWidget(self.item_count_label)

        # # mygtukas knygos pridejimui
        # self.add_button = QPushButton('Prideti knyga', self)
        # self.add_button.clicked.connect(self.add_item)
        # self.add_button.clicked.connect(self.increase_progress)
        # self.layout.addWidget(self.add_button)

        # resultatu rodymo laukelis su galimybe pasirinkti
        self.results_field = QLabel("Paieskos rezultatai:", self)
        self.layout.addWidget(self.results_field)

        self.search_results = QListWidget(self)
        self.search_results.setSelectionMode(QAbstractItemView.MultiSelection)
        self.layout.addWidget(self.search_results)

        # self.list_widget = QListWidget(self)
        # self.layout.addWidget(self.list_widget)

        # krepselio sukurimas
        self.cart_title = QLabel("Uzsakymo krepselis", self)
        self.layout.addWidget(self.cart_title)

        self.uzsakymo_krepselis = QListWidget(self)
        self.layout.addWidget(self.uzsakymo_krepselis)

        # mygtukas prideti pasirinktas knygas i krepseli
        self.add_to_uzsakymo_krepselis = QPushButton("Ideti prie uzsakymo", self)
        self.add_to_uzsakymo_krepselis.clicked.connect(self.add_to_cart)
        self.button_layout.addWidget(self.add_to_uzsakymo_krepselis)

        # knygos isemimas
        self.delete_from_uzsakymo_krepselis = QPushButton('Isimti knyga', self)
        self.delete_from_uzsakymo_krepselis.clicked.connect(self.delete_item)
        # self.delete_from_uzsakymo_krepselis.clicked.connect(self.decrease_progress)
        self.button_layout.addWidget(self.delete_from_uzsakymo_krepselis)

        # uzsakymo patvirtinimo mygtukas
        self.confirm_button = QPushButton("Patvirtinti uzsakyma", self)
        self.confirm_button.clicked.connect(self.order_confirmation)
        # self.confirm_button.clicked.connect(self.progress_full)

        # #uzsakymo patvirtinimas
        # self.confirm_button = QPushButton('Patvirtinti uzsakyma', self)
        # self.confirm_button.clicked.connect(self.order_confirmation)
        # # self.confirm_button.clicked.connect(self.progress_full)
        self.button_layout.addWidget(self.confirm_button)

        #uzsakymo atsaukimas
        self.cancel_button = QPushButton('Atsaukti uzsakyma', self)
        self.cancel_button.clicked.connect(self.order_cancellation)
        # self.cancel_button.clicked.connect(self.reset_progress)
        self.button_layout.addWidget(self.cancel_button)

        # self.progress_bar = QProgressBar()
        # self.progress_bar.setFormat('Uzsakymo busena: %p%')
        # self.progress_bar.setValue(0)
        # self.layout.addWidget(self.progress_bar)

        self.setLayout(self.layout)
        self.setWindowTitle('Knygu uzsakymo puslapis')


    def search_books(self):
        search_term = self.search_field.text()
        connection = psycopg2.connect(**self.conn_params)
        cursor = connection.cursor()

        # atrinkti pagal paieskos laukelyje ivedama teksta
        cursor.execute("SELECT * FROM books2 WHERE book_title ILIKE %s", (f"%{search_term}%",))

        # fetch all the matching rows
        results = cursor.fetchall()
        # print(f"Search results: {results}") # Print the results to the console
        cursor.close()
        connection.close()

        return results

    def display_search_results(self, results):
        # pirmiausia istrinam QListWIdget
        self.search_results.clear()

        # pridedam kiekviena rezultata i QListWidget
        for book in results:
            item = QListWidgetItem(str(book[3]))
            self.search_results.addItem(item)

    def search_button_clicked(self):
        results = self.search_books()
        self.display_search_results(results)

    def add_to_cart(self):
        selected_books = self.search_results.selectedItems()
        for book in selected_books:
            self.uzsakymo_krepselis.addItem(book.text())
            self.search_results.takeItem(self.search_results.row(book))

    def order_confirmation(self):
        if self.uzsakymo_krepselis.count() == 0:
            QMessageBox.warning(self, 'Klaida', 'Nepridejote nei vienos knygos')
        else:
            for index in range(self.uzsakymo_krepselis.count()):
                book = self.uzsakymo_krepselis.item(index).text()

                connection = psycopg2.connect(**self.conn_params)
                cursor = connection.cursor()
                cursor.execute(f"INSERT INTO orders(reader_id, book_id, order_time) VALUES ('reader_id', '{book}', CURRENT_TIMESTAMP);")

                QMessageBox.information(self, 'Information', 'Jusu uzsakymas sekmingai patvirtintas!')
                self.uzsakymo_krepselis.clear()
                # self.update_item_count()
                # self.progress_bar.setValue(100)
                # self.show_order()

                cursor.close()
                connection.close()

    # def add_item(self):
    #     item_text = self.item_input.text()
    #     if item_text:
    #         item = QListWidgetItem(item_text)
    #         item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
    #         self.list_widget.addItem(item)
    #         self.item_input.clear()
    #         self.update_item_count()
    #     else:
    #         QMessageBox.warning(self, 'Klaida', 'Irasykite knygos pavadinima')

    def delete_item(self):
        for item in self.uzsakymo_krepselis.selectedItems():
            self.uzsakymo_krepselis.takeItem(self.uzsakymo_krepselis.row(item))

        # self.update_item_count()

    # def order_confirmation(self):
    #     if self.list_widget.count() == 0:
    #         QMessageBox.warning(self, 'Klaida', 'Nepridejote nei vienos knygos')
    #     else:
    #         for index in range(self.list_widget.count()):
    #             item = self.list_widget.item(index)
    #             self.order.append(item.text())
    #
    #         QMessageBox.information(self, 'Information', 'Jusu uzsakymas sekmingai patvirtintas!')
    #
    #         self.list_widget.clear()
    #         self.update_item_count()
    #         # self.progress_bar.setValue(100)
    #         self.show_order()

    def order_cancellation(self):
        connection = psycopg2.connect(**self.conn_params)
        cursor = connection.cursor()

        # istrinam vartotojo konkrecios datos ir laiko uzsakyma
        cursor.execute("DELETE FROM orders WHERE reader_id = %s AND order_time = %s", (self.logged_in_user_id, specific_order_time)) #You’ll need to replace specific_order_time with the actual date and time of the order you want to delete
        connection.commit()
        cursor.close()
        connection.close()

        self.uzsakymo_krepselis.clear()
        QMessageBox.information(self, 'Information', 'Jusu uzsakymas sekmingai atsauktas!')
    #
    # def increase_progress(self):
    #     current_value = self.progress_bar.value()
    #     if current_value < 100:
    #         self.progress_bar.setValue(current_value + 33)
    #
    # def decrease_progress(self):
    #     current_value = self.progress_bar.value()
    #     if current_value > 0:
    #         self.progress_bar.setValue(current_value - 33)
    #
    # def progress_full(self):
    #     current_value = self.progress_bar.value()
    #     if current_value == 99:
    #         self.progress_bar.setValue(100)
    #
    # def reset_progress(self):
    #     QMessageBox.warning(self, 'Warning', 'Uzsakymo busena atstatyta')
    #     self.progress_bar.setValue(0)

    def update_item_count(self):
        item_count = self.list_widget.count()
        self.item_count_label.setText(f'Pasirinkta knygu: {item_count}')

    # def show_order(self):
    #     order_count = self.update_item_count()
    #     print(f'Jus uzsakete {order_count} knygu: ')
    #
    #     for book in self.order:
    #         print(book.item_text)
    #
    #     self.order_window = OrderWindow(self.order)
    #     self.order_window.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OrderingBooks()
    window.show()
    sys.exit(app.exec_())
