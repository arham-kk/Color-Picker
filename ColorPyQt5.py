import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from pynput import mouse
from PIL import ImageGrab

class ColorPicker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Picker")
        self.setGeometry(100, 100, 400, 400)
        self.setFixedSize(400, 400)
        self.setStyleSheet("background-color: #212121; color: white; border-radius: 10px;")
        self.create_widgets()

    def create_widgets(self):
        # Create canvas to display color
        self.canvas = QLabel(self)
        self.canvas.setGeometry(50, 50, 300, 300)
        self.canvas.setStyleSheet("background-color: white; border-radius: 5px;")

        # Create color information label
        self.color_label = QLabel("Click anywhere to check color", self)
        self.color_label.setGeometry(20, 360, 360, 30)
        self.color_label.setStyleSheet("font: 14pt Helvetica")

        # Create mouse listeners
        self.mlstnr = mouse.Listener(on_click=self.onClick)

    def getHex(self, rgb):
        return '%02X%02X%02X' % rgb

    def checkColor(self, x, y):
        bbox = (x, y, x + 1, y + 1)
        im = ImageGrab.grab(bbox=bbox)
        rgbim = im.convert('RGB')
        r, g, b = rgbim.getpixel((0, 0))
        color_hex = f'#{self.getHex((r, g, b))}'
        self.color_label.setText(f'COLOR: rgb({r}, {g}, {b}) | HEX {color_hex}')
        self.canvas.setStyleSheet(f"background-color: {color_hex}; border-radius: 5px;")

    def onClick(self, x, y, button, pressed):
        if pressed and button == mouse.Button.left:
            self.checkColor(x, y)

    def run(self):
        self.mlstnr.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    color_picker = ColorPicker()
    color_picker.show()
    color_picker.run()
    sys.exit(app.exec_())