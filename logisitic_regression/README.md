# Getting Started 

## Install Dependencies
We are going to use

- scikit-learn package - main package going to be used for machine learning models
- [pandas](https://github.com/pandas-dev/pandas) - for preprocessing

To install `scikit` run the following command
```$
$ pip install -U scikit-learn
```

To install `pandas` run the following command
```$
$ pip install pandas
```

To run the logistic regression example, go to the `logistic_regression` folder, then run

```$
$ python logisitic_regression.py
```

Results could look like this,
```$
For the vaildation data, your model had an accuracy of :  0.923404255319
Classification Report for Logistic Regression Model :
             precision    recall  f1-score   support

          0       0.81      0.97      0.88        69
          1       0.99      0.90      0.94       166

avg / total       0.93      0.92      0.93       235

Confusion Matrix :
[[ 67   2]
 [ 16 150]]
Chosen sample has these features :
[  8.80400978e-03   1.24541194e-02   5.77250486e-02   3.37054132e-01
   8.32553098e-05   1.13536182e-04   3.29808596e-05   3.62481862e-05
   1.16817179e-04   4.95772383e-05   3.02535305e-04   7.99059583e-04
   2.17092663e-03   2.34933087e-02   3.60431239e-06   1.59196730e-05
   9.60375290e-06   8.50325168e-06   1.24131070e-05   2.25500219e-06
   1.02872940e-02   1.66578974e-02   6.78824698e-02   4.61185202e-01
   9.95235888e-05   2.02396529e-04   8.51692250e-05   7.49161080e-05
   1.76490320e-04   6.07873128e-05]

For this sample, our model predicted the breast cancer to be  Benign

And the sample truly had a breast cancer type of Benign
```

Your Visualized Dataset is also found [here](./images/Visualized_features.png)

<img src="./images/Visualized_features.png" height="400px">