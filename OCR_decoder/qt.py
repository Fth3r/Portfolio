import sys
import cv2
import platform
import numpy as np

from decoders.affine import decode_aff
from decoders.atbash import find_atb
from decoders.b64 import decode_b64
from decoders.caesar import decode_cz
from decoders.binary import decode_bin

from pytesseract import pytesseract as pt
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import(
    QApplication, QMainWindow, QPushButton, QLabel,
    QVBoxLayout, QWidget, QComboBox, QFileDialog, QMessageBox
)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("OCR Decoder")

        self.options = ['Affine', 'Atbash', 'Base64', 'Binary', 'Caesar']

        # create the label whose text will change
        self.label = QLabel("Select an image for Tesseract to process")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        # create the open file button that calls the getOpenFileName widget
        self.fileButton = QPushButton("Select an image file")
        self.fileButton.clicked.connect(self.openFile)
        
        # create the dropdown menu for decoder options
        self.dropdown = QComboBox()
        self.dropdown.addItems(self.options)

        # Connecting the signal of button press to a method
        self.button = QPushButton("Decode")
        self.button.clicked.connect(self.decode)

        # adding the above widgets into the layout
        layout = QVBoxLayout()
        layout.addWidget(self.fileButton)
        layout.addWidget(self.label)
        layout.addWidget(self.dropdown)
        layout.addWidget(self.button)

        # pack widgets into a container
        container = QWidget()
        container.setLayout(layout)

        self.setFixedSize(QSize(400, 300))

        # the container holds all the widgets and can itself be the central widget
        self.setCentralWidget(container)

    def openFile(self):
        """
        This function handles the file open process and calls Tesseract to process the selected file.
        It was done this way in order to keep the function parameters and have it connected to a button press.
        """

        self.inFile = QFileDialog.getOpenFileName(self, caption="Open Image", filter="JPG files (*.jpg);; PNG files (*.png)")
        self.getTessOutput()

    def decode(self):
        """
        This function handles the decoding operation based on the selection made in self.dropdown.
        """

        try:
            match self.dropdown.currentIndex():
                case 0:
                    self.label.setText(decode_aff(self.label.text()))
                case 1:
                    self.label.setText(find_atb(self.label.text()))
                case 2:
                    self.label.setText(decode_b64(self.label.text()))
                case 3:
                    self.label.setText(decode_bin(self.label.text()))
                case 4:
                    self.label.setText(decode_cz(self.label.text()))

        except:
            # if a message is attempted to be decoded with the wrong cipher it may throw an error
            # here we handle those errors gracefully with a warning message rather than crashing the app
            QMessageBox.warning(self,
                                "Incorrect Encoding",
                                f"This message must not have been encoded with {self.options[self.dropdown.currentIndex()]}",
                                buttons=QMessageBox.StandardButton.Ok
            )

    def getTessOutput(self):
        """
        This function implements the PyTesseract framework to generate text from an input image
        file. It reads the filepath from file navigation window and uses cv2 to open and preprocess the
        image. It then renders the preprocessed image in a new window for preview before it is passed
        to Tesseract for final processing. Once this is done, the GUI label text is updated
        with the text Tesseract generated. 
        """

        if platform.system() == "Windows":
            # I have added C:\Program Files\Tesseract-OCR to my PATH, so just the executable works here
            pt.tesseract_cmd = 'tesseract.exe'
        # This may not work, needs more testing
        elif platform.system() == "Linux":
            pt.tesseract_cmd = "/home/fth3r/Downloads/tesseract-5.4.1-x86_64.AppImage"

        img = cv2.imread(self.inFile[0]) # getOpenFileName returns a tuple of the path and the file filter, get just the path

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
            text = text.strip()

            self.label.setText(text)

        except:
            self.label.setText("Can't open that image")
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()