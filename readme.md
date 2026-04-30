# Deep Learning Lab Works 

Welcome to the **Deep Learning Lab Works** repository! This repository contains a series of practical, hands-on laboratory exercises focusing on various Deep Learning concepts. The labs cover everything from basic neural networks to advanced architectures, transfer learning, natural language processing, and explainable AI.

---

## Table of Contents

- [Overview](#-overview)
- [Lab Breakdown](#-lab-breakdown)
- [Tech Stack](#-tech-stack)

---

## Overview

This repository serves as a structured learning path for Deep Learning. It transitions from fundamental concepts like artificial neural networks (ANNs) using MNIST, to convolutional neural networks (CNNs), recurrent neural networks (RNNs) for NLP, transfer learning with VGG16, and interpretability using LIME. It also features an AI Assistant web application integrated with the Gemini API.

---

## Lab Breakdown

| Lab | Topic | Dataset | Key Concepts | File Location |
| :---: | :--- | :--- | :--- | :--- |
| **Lab 1** | **Introduction to Neural Networks** | MNIST | Implementing foundational Multilayer Perceptron (MLP) architectures using TensorFlow/Keras. Covers data flattening, building sequential dense models, compiling with optimizers, and evaluating classification accuracy. | [`dl_lab1.ipynb`](./dl_lab1.ipynb) |
| **Lab 2** | **Regularization & Optimization** | MNIST | Addressing model overfitting through advanced techniques: applying Dropout layers, implementing Batch Normalization to stabilize learning, and utilizing L2 Regularization to constrain model weights. | [`dl_lab2.ipynb`](./dl_lab2.ipynb) |
| **Lab 3** | **Advanced Training Techniques** | MNIST | Enhancing training loops using Custom Callbacks to dynamically monitor performance, and implementing Learning Rate Scheduling to adjust step sizes across epochs for optimal convergence. | [`dl_lab3.ipynb`](./dl_lab3.ipynb) |
| **Lab 4** | **Convolutional Neural Networks (CNN)** | CIFAR-10 | Constructing CNNs for spatial feature extraction. Concepts include 2D Convolutions, MaxPooling for downsampling, flatten operations, and plotting training graphs for loss and accuracy. | [`dl_lab4.ipynb`](./dl_lab4.ipynb) |
| **Lab 5** | **Transfer Learning with VGG16** | CIFAR-10 | Utilizing a pre-trained VGG16 model. Covers freezing base layers for rapid feature extraction, replacing the classifier head, and fine-tuning by unfreezing final layers with a reduced learning rate. | [`dl_lab5.ipynb`](./dl_lab5.ipynb) |
| **Lab 6** | **Natural Language Processing (NLP)** | IMDb Reviews | Text classification for sentiment analysis. Includes tokenization, sequence padding for uniform length, word embeddings, and training sequential models using Recurrent Neural Networks (LSTM/RNN). | [`dl_lab6.ipynb`](./dl_lab6.ipynb) |

---



