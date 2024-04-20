# 🧠 Binary Classification Neural Network

A simple neural network that implements logistic regression for binary classification of images.

## 📁 Project Structure

- **NeuralNetwork** 🧠
  - **datasets** 📊
    - *Place your train and test datasets here*
  - **images** 🖼️
    - *Place your train and test images here*
  - `CreateTestset.py` 🛠️
    - *Script to create the test dataset with provided labels and paths of test images*
  - `CreateTrainset.py` 🛠️
    - *Script to create the train dataset with provided labels and paths of train images*
  - `NeuralNet.py` 🖥️
    - *Contains functions for neural network training. Run after creating datasets and placing them in the dataset folder*
  - `predict.py` 🔄
    - *Run this script to make a prediction using the trained model*
  - `w.npy` 📦
    - *Stores the weights after running NeuralNet.py*
  - `b.npy` 📦
    - *Stores the biases after running NeuralNet.py* *created after you run NeuralNet.py*

## 💻 How to Run the Program?

1. Place your desired images (all of the same dimensions) in the `images` folder.
2. Open `CreateTestset.py` and `CreateTrainset.py`. Write the image paths in the specified fields and also mention the labels (0 or 1) for each image in the specified place.
    ```python
    paths = ["paths", "to", "images", "here"]
    labels =[] #labels here are 0 or 1
    ```
3. After running these two files, you'll see two `.h5` files in your working directory. Place them in the `dataset` folder.
4. Run `NeuralNet.py`. It will create `w.npy` and `b.npy` files in your working directory.  
5. Run `predict.py`. Insert an image (preferably of the same dimensions as training images) of your choice in the user interface.  
6. Voila! The prediction is displayed at the bottom of the UI window.