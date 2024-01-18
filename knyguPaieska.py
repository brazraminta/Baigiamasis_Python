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

class KnyguPaieska(QWidget):
    def __init__(self, conn_params):
        super().__init__()
        self.conn_params = conn_params

        self.setWindowTitle('Ieskokite leidinio')
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        # knygu paieskos laukelio pavadinimas
        self.title = QLabel("Leidinio paieska")
        self.title.setAlignment(Qt.AlignLeft)
        self.title.setStyleSheet("QLabel{font-size: 18pt;}")
        self.layout.addWidget(self.title)

        # knygu pasieskos laukelis
        self.search_field = QLineEdit(self)  # reikia padaryti, kad vedant teksta i laukeli sitas tekstas issivalytu
        self.search_field.setFixedSize(500, 50)
        self.search_field.setStyleSheet("background-color: white;")
        self.search_field.returnPressed.connect(self.search_button_clicked)
        self.layout.addWidget(self.search_field)

        # resultatu rodymo laukelis su galimybe pasirinkti
        self.results_field = QLabel("Paieskos rezultatai:", self)
        self.layout.addWidget(self.results_field)

        self.search_results = QListWidget(self)
        self.search_results.setSelectionMode(QAbstractItemView.MultiSelection)
        self.layout.addWidget(self.search_results)

        # krepselio sukurimas
        self.uzsakymo_krepselis = QListWidget(self)

        # mygtukas prideti pasirinktas knygas i krepseli
        self.add_to_uzsakymo_krepselis = QPushButton("Ideti prie uzsakymo", self)
        self.add_to_uzsakymo_krepselis.clicked.connect(self.add_to_cart)

        # uzsakymo uzbaigimo mygtukas
        self.finish_order_button = QPushButton("Patvirtinti uzsakyma", self)
        self.finish_order_button.clicked.connect(self.finish_order)

    def search_books(self):
        search_term = self.search_field.text()
        connection = psycopg2.connect(**self.conn_params)
        cursor = connection.cursor()

        # atrinkti pagal paieskos laukelyje ivedama teksta
        cursor.execute("SELECT * FROM books2 WHERE book_title ILIKE %s", (f"%{search_term}%",))

        # fetch all the matching rows
        results = cursor.fetchall()
        print(f"Search results: {results}") # Print the results to the console
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

    def finish_order(self):
        for index in range(self.uzsakymo_krepselis.count()):
            book = self.uzsakymo_krepselis.item(index).text()
            connection = psycopg2.connect(**self.conn_params)
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO orders(reader_id, book_id) VALUES ('reader_id', '{book}');")
            self.uzsakymo_krepselis.clear()

            cursor.close()
            connection.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KnyguPaieska(conn_params)
    window.show()
    sys.exit(app.exec_())

