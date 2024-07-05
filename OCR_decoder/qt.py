import sys
import cv2
import numpy as np

from decoders.affine import decode_aff
from decoders.atbash import find_atb
from decoders.b64 import decode_b64
from decoders.caesar import decode_cz

from pytesseract import pytesseract as pt
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
        self.label = QLabel("Input directory and press return")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        # connecting the signal of the lineedit changing to the label's text
        self.input = QLineEdit("replace with path to image file")
        # self.input.textChanged.connect(self.label.setText)
        self.input.returnPressed.connect(self.getTessOutput)
        
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

    def decode(self):
        """
        This function handles the decoding operation based on the selection made in self.dropdown.
        """

        try:
            if self.dropdown.currentIndex() == 0:
                self.label.setText(decode_aff(self.label.text()))
            elif self.dropdown.currentIndex() == 1:
                self.label.setText(find_atb(self.label.text()))
            elif self.dropdown.currentIndex() == 2:
                self.label.setText(decode_b64(self.label.text()))
            elif self.dropdown.currentIndex() == 3:
                self.label.setText(decode_cz(self.label.text()))
        
        except:
            self.label.setText(f"The input must not be encoded with {self.options[self.dropdown.currentIndex()]}")

    def getTessOutput(self):
        """
        This function implements the PyTesseract framework to generate text from an input image
        file. It reads the filepath from the input box and uses cv2 to open and preprocess the
        image. It then renders the preprocessed image in a new window for preview before it is passed
        to Tesseract for final processing. Once this is done, the GUI label text is updated
        with the text Tesseract generated. 
        """

        # Need to tell pytesseract where the compiled tesseract binary is located
        pt.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

        img = cv2.imread(self.input.text())

        # Trying to apply some preprocessing to the image
        try:
            img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            kernel = np.ones((1,1), dtype=np.uint8)
            img = cv2.dilate(img, kernel, iterations=1)
            img = cv2.erode(img, kernel, iterations=1)
            img = cv2.medianBlur(img, 3)
            img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) [1]

            # Create a window to show the image being read before proceeding
            # Also wait for keypress to close
            cv2.imshow("Cipher Text Render - press any key to continue", img)
            k = cv2.waitKey(0)
            if k:
                # close the window on any buttonpress 
                cv2.destroyAllWindows()

            # Leverage pytesseract and assign what it returns to the 'text' var, then print
            text = pt.image_to_string(img)
            #text = text.replace(" ", "")
            text = text.strip()

            self.label.setText(text)

        except:
            self.label.setText("Can't open that image")
        
app = QApplication(sys.argv)

window = MainWindow(decoding_options = ['Affine', 'Atbash', 'Base64', 'Caesar'])
window.show()

app.exec()