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

class HistoryDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Order history")
        self.history_display = QTextEdit(self)
        self.history_display.setReadOnly(True)
        layout = QVBoxLayout(self)
        layout.addWidget(self.history_display)


class OrderingBooks(QDialog):
    def __init__(self):
        super().__init__()
        self.conn_params = conn_params
        self.order_history = []
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
        self.confirm_button.clicked.connect(self.confirm_and_show_history)
        self.button_layout.addWidget(self.confirm_button)

        #uzsakymo atsaukimas
        self.cancel_button = QPushButton('Atsaukti uzsakyma', self)
        self.cancel_button.clicked.connect(self.order_cancellation)
        # self.cancel_button.clicked.connect(self.reset_progress)
        self.button_layout.addWidget(self.cancel_button)

        # uzsakymu istorija
        self.order_history_button = QPushButton('Uzsakymu istorija', self)
        self.order_history_button.clicked.connect(self.show_order_info)
        self.history_dialog = HistoryDialog(self)
        self.button_layout.addWidget(self.order_history_button)

        self.author_surname_checkbox = QCheckBox("Filtruoti pagal autoriaus pavarde", self)
        self.date_checkbox = QCheckBox('Filtruoti pagal isleidimo metus', self)
        self.genre_checkbox = QCheckBox('Filtruoti pagal zanra', self)
        self.layout.addWidget(self.author_surname_checkbox)
        self.layout.addWidget(self.date_checkbox)
        self.layout.addWidget(self.genre_checkbox)
        # self.progress_bar = QProgressBar()
        # self.progress_bar.setFormat('Uzsakymo busena: %p%')
        # self.progress_bar.setValue(0)
        # self.layout.addWidget(self.progress_bar)

        self.setLayout(self.layout)
        self.setWindowTitle('Knygu uzsakymo puslapis')


    def search_books(self):
        try:
            search_term = self.search_field.text()
            connection = psycopg2.connect(**self.conn_params)
            cursor = connection.cursor()

            # atrinkti pagal paieskos laukelyje ivedama teksta
            query = "SELECT * FROM books2 WHERE book_title ILIKE %s"
            params = [f"{search_term}%"]

            if self.author_surname_checkbox.isChecked():
                query += " OR author_last_name ILIKE %s"
                params.append(f"{search_term}%")
            if self.date_checkbox.isChecked():
                query += " OR publish_date ILIKE %s"
                params.append(f"{search_term}%")
            if self.genre_checkbox.isChecked():
                query += " OR genre ILIKE %s"
                params.append(f"{search_term}")

            cursor.execute(query, params)
            # fetch all the matching rows
            results = cursor.fetchall()
            # print(f"Search results: {results}") # Print the results to the console
            cursor.close()
            connection.close()

            return results
        except Exception as e:
            print(f"Error from search_books: {e}")

    def display_search_results(self, results):
        # pirmiausia istrinam paieskos rezultatus
        self.search_results.clear()

        try:
            # pridedam kiekviena rezultata i QListWidget
            for book in results:
                item_text = f"{book[1]} {book[2]}, {book[3]}, {book[4]}, {book[6]}"  # [3] indeksas 'book_title'
                item = QListWidgetItem(item_text)
                self.search_results.addItem(item)
        except Exception as e:
            print(f"Error from display_search_results: {e}")

    def search_button_clicked(self):
        try:
            results = self.search_books()
            self.display_search_results(results)
        except Exception as e:
            print(f"Error from search_button_clicked: {e}")

    def add_to_cart(self):
        selected_books = self.search_results.selectedItems()
        for book in selected_books:
            self.uzsakymo_krepselis.addItem(book.text())
            self.search_results.takeItem(self.search_results.row(book))

    # def order_confirmation(self):  # kazkodel neveikia connection
    #     if self.uzsakymo_krepselis.count() == 0:
    #         QMessageBox.warning(self, 'Klaida', 'Nepridejote nei vienos knygos')
    #     else:
    #         for index in range(self.uzsakymo_krepselis.count()):
    #             book = self.uzsakymo_krepselis.item(index).text()
    #
    #             connection = psycopg2.connect(**self.conn_params)
    #             cursor = connection.cursor()
    #             cursor.execute(f"INSERT INTO orders(reader_id, book_id, order_time) VALUES ('reader_id', '{book}', CURRENT_TIMESTAMP);")
    #
    #             QMessageBox.information(self, 'Information', 'Jusu uzsakymas sekmingai patvirtintas!')
    #             self.uzsakymo_krepselis.clear()
    #             # self.update_item_count()
    #             # self.progress_bar.setValue(100)
    #             # self.show_order()
    #
    #             cursor.close()
    #             connection.close()

    def order_confirmation(self):
        try:
            if self.uzsakymo_krepselis.count() == 0:
                QMessageBox.warning(self, 'Klaida', 'Nepridejote nei vienos knygos')
            else:
                order_info = ""
                for index in range(self.uzsakymo_krepselis.count()):
                    book = self.uzsakymo_krepselis.item(index).text()
                    order_info += f"Book: {book}\n"

                    self.order_history.append(order_info)
                    QMessageBox.information(self, 'Information', 'Jusu uzsakymas sekmingai patvirtintas!')
                    # self.uzsakymo_krepselis.clear()
        except Exception as e:
            print(f"Error from order_confirmation: {e}")
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
    def show_order_info(self):
        try:
            if self.uzsakymo_krepselis.count() == 0:
                QMessageBox.warning(self, "Klaida", "Uzsakymo krepselyje nera nei vienos knygos")
            else:
                order_info = ""
                for index in range(self.uzsakymo_krepselis.count()):
                    book = self.uzsakymo_krepselis.item(index).text()
                    order_info += f"Book: {book}\n"

                    #pridedam order_info i order_history list
                self.order_history.append(order_info)

                QMessageBox.information(self, 'Order Information', order_info)
        except Exception as e:
            print(f"Error from show_order_info: {e}")

    def show_order_history(self):
        try:
            if len(self.order_history) == 0:
                QMessageBox.warning(self, "Klaida", "Nėra jokios užsakymo istorijos")
            else:
                order_info = "\n".join(f'Order: {order}' for order in self.order_history)
                self.history_dialog.history_display.setPlainText(order_info)  # Display the history in the QTextEdit widget
                self.history_dialog.show()
        except Exception as e:
            (
                print(f"Error from show_order_history: {e}"))

    def confirm_and_show_history(self):
        self.order_confirmation()
        self.show_order_history()

    def confirm_and_show_history(self):
        self.order_confirmation()
        self.show_order_history()

    def delete_item(self):
        try:
            for item in self.uzsakymo_krepselis.selectedItems():
                self.uzsakymo_krepselis.takeItem(self.uzsakymo_krepselis.row(item))
        except Exception as e:
            print(f"Error: {e}")

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
        # connection = psycopg2.connect(**self.conn_params)
        # cursor = connection.cursor()
        #
        # # istrinam vartotojo konkrecios datos ir laiko uzsakyma
        # cursor.execute("DELETE FROM orders WHERE reader_id = %s AND order_time = %s", (self.logged_in_user_id, specific_order_time)) #You’ll need to replace specific_order_time with the actual date and time of the order you want to delete
        # connection.commit()
        # cursor.close()
        # connection.close()

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
