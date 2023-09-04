# CNN-Dog-Breed-Classification-
by JengShiuan Ma
![Upload your doggy here](https://xvgnrrrxjup83pmyz5s4jg.streamlit.app/)

# The Dataset
The Stanford Dogs dataset has images of 120 dog breeds from around the world.

The contents of the dataset are:
- ***Number of Categories*** = 120
- ***Total Number of images*** = 20,580

The number of images per dog breed is low to train a neural network from scratch.
Hence it would be beneficial to use transfer learning. 
The dataset is imported from tensorflow data.
The data can be found at https://www.tensorflow.org/datasets/catalog/stanford_dogs

More information about the dataset can be found at http://vision.stanford.edu/aditya86/ImageNetDogs/
![example images](https://i.imgur.com/Mp2Te2Y.png)


# Xception
Xception is a convolutional neural network that is 71 layers deep. You can load a pretrained version of the network trained on more than a million images from the ImageNet database . The pretrained network can classify images into 1000 object categories, such as keyboard, mouse, pencil, and many animals. As a result, the network has learned rich feature representations for a wide range of images.
The network is shown below.
![InceptionV3](Xception.png)


# Challenges The network might face
The dataset contains dog breeds which are visually similar to each other.
This might cause challenges for the network.

As you can see Swiss mountain dogs and Bernese Mountain dogs are very similar

![Swiss mountain dog and Bernese mountain dog](https://i.imgur.com/Cwzthgx.jpg)



# Overview of the entire network

1. Input to Inceptionv3 (non trainable)
2. Average Pooling 2D layer
3. Flattening layer
4. Dropout layer 
5. Dense layer (240 units)
6. Dropout layer
7. Dense layer (240 units)
8. Dropout layer
9. Softmax layer (120 units)

The network uses data augmentation and dropout to reduce overfitting and is implemented in a google colab environment


# Training and Testing accuracy
After training with 80%-20% training and testing split respectively the results are as follows.
- ***Training accuracy*** = 78%
- ***Testing accuracy*** = 72%

***Note*** - The trained weights have been provided in the repo. Importing them has been described in the instructions below.

# Instructions

1. Download the code from the repository to your computer
2. Open the ***Dog_classifier.ipynb*** file from the repository in the browser.
3. After opening click on the 'Open in Colab' button. This will redirect you to a google colab environment.
4. Download the files named ***'checkpoint', 'cp.ckpt.data-00000-of-00001', 'cp.ckpt.index' and 'kaggle.json'***.
5. Run the code cells of the notebook.
6. Ignore the code cells under headings labeled ***(*skip)*** if you only want to test the network without training.
7. Upload the files ***'checkpoint', 'cp.ckpt.data-00000-of-00001' and 'cp.ckpt.index'*** when asked by the notebook. This will import the weights.
8. Run the subsequent cells to upload your own images to test the network. Further instructions are given in the notebook
