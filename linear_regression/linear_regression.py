import random

import pandas as pd
import numpy

import sklearn
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

#  this model is used to fetch the data
def getData(location="../data/carprices.csv"):
    dataset = pd.read_csv(location, ',')
    labels = dataset.iloc[:, 0].values
    features = dataset.iloc[:, 1:].values
    return features, labels

def preprocess_data(X,Y):
    # check for missing values
    # we need to handle the categorical data by encoding them 
    le = sklearn.preprocessing.LabelEncoder()
    le.fit(['Diesel','Petrol','CNG'])
    X[: , 2] = le.transform(X[:,2]) # encoding the fuel type
    #  we have 1436 features so we split into 500 for training and validation and 436 for testing
    train_x = X[0:500, ]
    train_y = [x for x in Y[0:500]]
    valid_x = X[500:1000, ]
    valid_y = [x for x in Y[500:1000]]
    test_x = X[1000:, ]   # we do not touch these variables until the we get the best model
    test_y = [ x for x in Y[1000:]]   # we do not touch these variables until the we get the best model
    return train_x, train_y, valid_x, valid_y, test_x, test_y

def linear_regression(train_x, train_y, valid_x, valid_y):
    # Create the linear model
    model = LinearRegression(normalize=True)
    # Train the model using the training data
    model.fit(train_x, train_y)
    # Validate the model using validation data
    predict_price = model.predict(valid_x)
    # The coefficients
    print('Coefficients: \n', model.coef_)
    # Show The mean squared error
    print("Mean squared error: %.2f"
        % mean_squared_error(valid_y, predict_price))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % r2_score(valid_y, predict_price)) 
        
    # Visualize results of test
    true_price = plt.scatter(valid_x[:,3], valid_y,  marker='^', label='True price')
    predicted = plt.scatter(valid_x[:,3], predict_price, marker='*', label='Predicted Price')
    plt.legend(handles=[true_price, predicted])
    plt.xlabel('HorsePower')
    plt.ylabel('Price')
    plt.xticks(())
    plt.yticks(())
    plt.title('A scatter plot of the Predicted Results and Features')
    plt.savefig("./images/Visualized_features.png")
    return model
    
def test_model(model, test_x, test_y):
    # pick a random sample from our test_x
    random_value = random.randint(1,435)
    prediction = model.predict(test_x)
    
    print "Chosen sample has these features : \n", test_x[random_value]
    print "\nFor this sample, our model predicted the car to cost $", round(prediction[random_value],2)
    print "\nAnd the car truly cost $", test_y[random_value]

# now we fetch the dataset
features, labels = getData()
# then we preprocess the data
train_x, train_y, valid_x, valid_y, test_x, test_y = preprocess_data(features, labels)
# call the linear regression function
linear_model = linear_regression(train_x, train_y, valid_x, valid_y)
# now we test our model with the test data
test_model( linear_model, test_x, test_y)