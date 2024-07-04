import sys

from decoders.affine import decode_aff
from decoders.atbash import find_atb
from decoders.b64 import decode_b64
from decoders.caesar import decode_cz

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import(
    QApplication, QMainWindow, QPushButton, QLabel,
    QLineEdit, QVBoxLayout, QWidget, QComboBox
)

class MainWindow(QMainWindow):

    def __init__(self, decoding_options):
        super().__init__()

        self.setWindowTitle("OCR Decoder")

        self.options = decoding_options

        # create the label whose text will change
        self.label = QLabel("Waiting for input")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        # connecting the signal of the lineedit changing to the label's text
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        self.input.returnPressed.connect(self.decode)
        
        # create the dropdown menu for decoder options
        self.dropdown = QComboBox()
        self.dropdown.addItems(self.options)

        # Connecting the signal of button press to a method
        self.button = QPushButton("Decode")
        self.button.clicked.connect(self.decode)

        # adding the above widgets into the layout
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.dropdown)
        layout.addWidget(self.button)
        # pack widgets into a container
        container = QWidget()
        container.setLayout(layout)

        self.setFixedSize(QSize(400, 300))

        # the container holds all the widgets and can itself be the central widget
        self.setCentralWidget(container)

    # the function our button will call on press
    def decode(self):
        try:
            if self.dropdown.currentIndex() == 0:
                self.label.setText(decode_aff(self.input.text()))
            elif self.dropdown.currentIndex() == 1:
                self.label.setText(find_atb(self.input.text()))
            elif self.dropdown.currentIndex() == 2:
                self.label.setText(decode_b64(self.input.text()))
            elif self.dropdown.currentIndex() == 3:
                self.label.setText(decode_cz(self.input.text()))
        
        except:
            self.label.setText(f"The input must not be encoded with {self.options[self.dropdown.currentIndex()]}")

app = QApplication(sys.argv)

window = MainWindow(decoding_options = ['Affine', 'Atbash', 'Base64', 'Caesar'])
window.show()

app.exec()