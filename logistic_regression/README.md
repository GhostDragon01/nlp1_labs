# Introduction to Natural Language Processing 01
# Lab 03

## Description of the project

In this notebook, we have transformed the documents from the imdb dataset into vectors representing the following features:
- 1 if "no" appears in the document, 0 otherwise.
- The count of first and second pronouns in the document.
- 1 if "!" is in the document, 0 otherwise.
- Log(word count in the document).
- Number of words in the document which are in the positive lexicon.
- Number of words in the document which are in the negative lexicon.

Then , we implemented a classifier using logistic regression with Pythorch.
This allowed us to classify the documents in the dataset (positive or negative). We also compared the accuracies on different training splits. 
We also used another implementation from scikit-learn. 

## Project architecture

Our work can be found in the notebook named : logistic_regression.ipynb
