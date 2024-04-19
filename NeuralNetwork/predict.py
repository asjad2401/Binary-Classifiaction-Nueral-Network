#run this file after you have trained the model and you have the values of weights and bias

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QPixmap, QImage
import cv2
import numpy as np
from NeuralNetwork.NeuralNet import predict

# Load the weights and bias
w = np.load('weights.npy')
b = np.load('bias.npy')

#a user interface to select an image and run the prediction built using qt5
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Face Detection")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.initUI()

    def initUI(self):
        # Create widgets
        self.image_label = QLabel("")
        self.result_label = QLabel("")

        self.select_button = QPushButton("Select Image")
        self.select_button.clicked.connect(self.select_image)

        self.select_button.setStyleSheet("background-color: #4CAF50; color: white; border: none; padding: 10px; text-align: center; text-decoration: none; font-size: 16px; margin: 4px 2px; ")
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.result_label)
        layout.addWidget(self.select_button)

        self.central_widget.setLayout(layout)

    def select_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)")

        if file_path:
            # Read the image
            image = cv2.imread(file_path)
            if image is None:
                self.result_label.setText("Error: Unable to load image")
                return
 
            # Resize the image 
            resized_image = cv2.resize(image, (960, 960))
            #display the image
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            height, width, channel = image_rgb.shape
            bytes_per_line = channel * width
            q_image = QPixmap.fromImage(QImage(image_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888))
            self.image_label.setPixmap(q_image)

            #flatten and standarize the image
            flattened_image = resized_image.flatten() / 255.0

            # Make prediction
            prediction = predict(w, b, flattened_image)
            if prediction == 1:
                self.result_label.setText("Prediction: True")
            else:
                self.result_label.setText("Prediction: False")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    