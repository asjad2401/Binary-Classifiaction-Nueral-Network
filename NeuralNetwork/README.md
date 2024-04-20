# Binary-Classification-Neural-Network

A simple neural network that implements logistic regression in order to perform binary classification.

This project uses logistic regression and gradient descent to build a neural network that performs binary classification of images.

## Project Structure

- **NeuralNetwork**
  - **datasets**
    - *here you put the train and test datasets*
  - **images**
    - *here you put the train and test images*
  - CreateTestset.py
    - *this file creates the test dataset provided labels and paths of test images*
  - CreateTrainset.py
    - *this file creates the train dataset provided labels and paths of train images*
  - NeuralNet.py
    - *this file contains all the functions for the neural network training. Run after creating datasets and placing them in the dataset folder*
  - predict.py
    - *you run this file to make a prediction provided values for w and b*
  - w.npy
    - *created after you run NeuralNet.py*
  - b.npy
    - *created after you run NeuralNet.py*

## How to Run the Program?

1. Place your desired images (all of the same dimensions) in the `images` folder.
2. Open `CreateTestset.py` and `CreateTrainset.py`. Write the image paths in the specified fields and also mention the labels (0 or 1) for each image in the specified place. 
3. After running these two files, you'll see two `.h5` files in your working directory. Place them in the `dataset` folder.
4. Run `NeuralNet.py`. It will create `w.npy` and `b.npy` files in your working directory.
5. Run `predict.py`. Insert an image (preferably of the same dimensions as training images) of your choice in the user interface.
6. Voila! The prediction is displayed at the bottom of the UI window.

