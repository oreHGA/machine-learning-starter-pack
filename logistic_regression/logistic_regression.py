import random

import pandas as pd
import numpy

import sklearn
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

import matplotlib.pyplot as plt

#  this model is used to fetch the data
def getData(location="../data/breastcancerdataset.csv"):
    dataset = pd.read_csv(location, ',')
    labels = dataset.iloc[:, 1].values
    count = 0
    temp = []
    for i in labels:
        if i == 'M':
            temp.append('0')
        else:
            temp.append('1')
        count = count + 1
    features = dataset.iloc[:, 2:].values
    return features,labels,temp 

def preprocess_data(X,Y):
    feat = sklearn.preprocessing.normalize(X, 'l1')
    train_x = feat[0:235, ]
    train_y = [map(int, x) for x in Y[0:235]]
    valid_x = feat[235:470, ]
    valid_y = [map(int, x) for x in Y[235:470]]
    test_x = feat[470:, ]   # we do not touch these variables until the we get the best model
    test_y = [map(int, x) for x in Y[470:]]   # we do not touch these variables until the we get the best model
    return train_x, train_y, valid_x, valid_y, test_x, test_y,feat

def plotfeatures(xsample, ysample):
    count = 0
    for i in ysample:
        if i == 'M':
            malignant, = plt.plot(xsample[count, 1], xsample[count, 2], 'ro')
        elif i == 'B':
            benign, = plt.plot(xsample[count, 1], xsample[count, 2], 'bo')
        plt.hold(True)
        count += 1
    plt.xlabel('texture_mean')
    plt.ylabel('radius_mean')
    plt.legend(handles=[malignant, benign], labels=['Malignant', 'Benign'])
    plt.title('A scatter plot of the Dataset considering 2 features, radius_mean and texture_mean')
    plt.savefig("./images/Visualized_features.png")

def logistic_regression(train_x, train_y, valid_x, valid_y):
    # Define possible models
    # this is just plain Ordinary Least Squares
    class_names = ['Malignant','Benign']
    model = LogisticRegression(C=1e6, solver='liblinear');
    #  now we fit the model with the training data 
    model.fit( train_x, train_y );
    #  now we use our validation data to give us a prediction to see how well the model is performing
    predictions = model.predict( valid_x );
    accuracy = metrics.accuracy_score( valid_y, predictions ); 
    confusion_matrix = metrics.confusion_matrix(valid_y, predictions)
    classification_report = metrics.classification_report(numpy.asarray(valid_y), numpy.asarray(predictions))
    print "For the vaildation data, your model had an accuracy of : ", accuracy
    print "Classification Report for Logistic Regression Model :\n", classification_report
    print "Confusion Matrix :\n", confusion_matrix

    return model;

def test_model(model, test_x, test_y):
    # pick a random sample from our test_x
    random_value = random.randint(1,100)
    prediciton = model.predict(test_x)
    predicted_breastcancer_type = ''
    true_breastcancer_type = ''
    if (test_y[random_value] == '0'):
        true_breastcancer_type = 'Malignant' 
    else:
        true_breastcancer_type = 'Benign'
    if (prediciton[random_value] == 0):
        predicted_breastcancer_type = 'Malignant' 
    else: 
        predicted_breastcancer_type = 'Benign'

    print "Chosen sample has these features : \n", test_x[random_value]
    print "\nFor this sample, our model predicted the breast cancer to be ", predicted_breastcancer_type
    print "\n And the sample truly had a breast cancer type of", true_breastcancer_type


# now we fetch the dataset
features, labels, temp = getData()

# then we preprocess the data
train_x, train_y, valid_x, valid_y, test_x, test_y, features = preprocess_data(features, temp)

# afterwards, we visualize the data we have
plotfeatures(xsample=features, ysample=labels)

# now we are going to test our model on a single sample in our dataset
logistic_model = logistic_regression( train_x, train_y, valid_x, valid_y)

# now testing the model
test_model( logistic_model, test_x, test_y)