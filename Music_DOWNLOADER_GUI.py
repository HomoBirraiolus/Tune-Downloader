import sys
from PyQt5.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QFileDialog,
    QWidget,
)
from pytubefix import YouTube 
import os



class YT_music(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube Music downloader")
        self.setGeometry(200, 200, 600, 400)

        # Create layout
        layout = QVBoxLayout()

        # Input label and text field
        self.label1 = QLabel("YT url:")
        self.url_input = QLineEdit()
        
        self.label2 = QLabel("dest path:")
        self.dst_folder = QLineEdit()
        self.dst_folder.setText(r"C:\Users\Utente\Downloads")
        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.download_file)
        
        """
        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert_file)
        """
        # Output text area
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)

        # Add widgets to layout
        layout.addWidget(self.label1)
        layout.addWidget(self.url_input)
        layout.addWidget(self.label2)
        layout.addWidget(self.dst_folder)
        layout.addWidget(self.download_button)
        #layout.addWidget(self.convert_button)
        layout.addWidget(self.output_text)

        self.setLayout(layout)

    def download_file(self):
        # Open a file dialog to select a PDF file
        # url input from user 
        yt = YouTube( 
            self.url_input.text())
            #str(input("Enter the URL of the video you want to download: \n>> "))) 

        # extract only audio 
        video = yt.streams.filter(only_audio=True).first() 

        # check for destination to save file 
        #print("Enter the destination (leave blank for current directory)") 
        destination = self.dst_folder.text() or '.'

        # download the file 
        out_file = video.download(output_path=destination) 

        # save the file 
        base, ext = os.path.splitext(out_file) 
        new_file = base + '.mp3'
        os.rename(out_file, new_file) 

        # result of success 
        self.output_text.setPlainText( yt.title + " has been successfully downloaded.\n")
       
"""
    def convert_file(self):
        # Get the file path from the input field
        file_path = self.pdf_input.text()
        if not file_path:
            self.output_text.setPlainText("Please select a file.")
            return

        # Initialize OCR model
        model = ocr_predictor(pretrained=True)

        try:
            # Check if the file is a PDF or JPG
            if file_path.lower().endswith(".pdf"):
                # Convert PDF to images
                pages = convert_from_path(file_path)
                extracted_text = ""

                # Perform OCR on each page of the PDF
                for page in pages:
                    img_array = np.array(page)
                    result = model([img_array])
                    for p in result.export()["pages"]:
                        for block in p.get("blocks", []):
                            for line in block.get("lines", []):
                                for word in line.get("words", []):
                                    extracted_text += word["value"] + " "
                        extracted_text += "\n"

            elif file_path.lower().endswith((".jpg", ".jpeg")):
                # Process the JPG image directly
                img = Image.open(file_path)
                img_array = np.array(img)
                extracted_text = ""

                # Perform OCR on the image
                result = model([img_array])
                for p in result.export()["pages"]:
                    for block in p.get("blocks", []):
                        for line in block.get("lines", []):
                            for word in line.get("words", []):
                                extracted_text += word["value"] + " "
                    extracted_text += "\n"
            else:
                self.output_text.setPlainText("Unsupported file type. Please select a PDF or JPG file.")
                return

            # Display extracted text in the output area
            self.output_text.setPlainText(extracted_text)

        except Exception as e:
            self.output_text.setPlainText(f"Error: {e}")

"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YT_music()
    window.show()
    sys.exit(app.exec())
