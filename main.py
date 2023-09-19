from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QProgressBar, QLabel
from PyQt5.QtCore import Qt
from pytube import YouTube
import sys

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText('Zadejte URL videa...')
        layout.addWidget(self.url_input)

        self.download_button = QPushButton('Stáhnout video', self)
        self.download_button.clicked.connect(self.download_video)
        layout.addWidget(self.download_button)

        self.progress_bar = QProgressBar(self)
        layout.addWidget(self.progress_bar)

        self.status_label = QLabel('Čeká se na stahování...')
        layout.addWidget(self.status_label)

        self.setLayout(layout)
        self.setWindowTitle('YouTube Downloader')
        self.show()

    def download_video(self):
        url = self.url_input.text()
        if not url:
            self.status_label.setText('https://www.youtube.com/watch?v=ZhG18g4XNO8&list=RDGMEMWO-g6DgCWEqKlDtKbJA1GwVMZhG18g4XNO8&start_radio=1')
            return

        try:
            yt = YouTube(url)
            yt.register_on_progress_callback(self.progress_callback)
            video = yt.streams.get_highest_resolution()
            video.download()
            self.status_label.setText(f"Video '{yt.title}' bylo úspěšně staženo.")
        except Exception as e:
            self.status_label.setText(f"Nastala chyba: {e}")

    def progress_callback(self, stream, chunk, bytes_remaining):
        size = stream.filesize
        progress = (float(abs(bytes_remaining - size) / size)) * float(100)
        self.progress_bar.setValue(int(progress))
        self.status_label.setText(f"Stahování: {int(progress)}%")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
