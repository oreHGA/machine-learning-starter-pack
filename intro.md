# Introduction to Machine Learning 

## What's all the buzz about?
If you're a dev, i'm sure by now you've heard alot about machine learning.
Everyone's talking about it, but not much people know what it really means. For most people, all they know is that, machine learning is what makes most of our apps today do cool stuff.<br>
Ever wondered how snapchat always gets those dog filters to come on your face ( placing the crown well on your head)? <br/>
Ever wondered how Netflix gets the idea that ' Because you watched ' "Agents of S.H.I.E.L.D" you'd like to watch "Luke Cage"?<br/>
or how Amazon knows to show you "Macbook Pro Cases" after looking-up/buying a "Macbook Pro" from their website? <br/>

It's all MACHINE LEARNING. <br />
In this introduction, we are going to be looking at the basics of Machine Learning, types of learning, advantages of machine learning, and how we can leverage machine learning by using APIs.

## What is Machine Learning
Officially,

"Machine Learning is a field of study that gives the computer the ability to learn without being explicitly programmed" <p style="float:right"> Arthur Samuel (1959) </p>

<div style="clear:both"></div>
In the most basic of terms, machine learning is the ability of the computer to predict future events based off of data it has collected of past events. Obviously machine learning is not just about generating
predictions, machine learning also involves the understanding of data samples and categorizing them into clusters i.e grouping them and making sense off of what we have.
<br>Before we continue, I want to make this clear : <br>
The 👏🏾 output 👏🏾  of 👏🏾  your 👏🏾  model 👏🏾  is 👏🏾  highly 👏🏾  dependent 👏🏾  on 👏🏾  the 👏🏾  data 👏🏾  you 👏🏾 train 👏🏾  the 👏🏾 model 👏🏾  with!

## Types of Learning
Generally learning algorithms can be broadly classified into two categories.
 
### Supervised Learning
With Supervised Learning, the dataset you are going to train your model off has labels i.e you know what is 'a' and what is 'b'. <br>
For example : 
<br>
Say we are trying to predict wether an object is a car or not. We could have a dataset which has as features such as the 'weight', 'length', 'number of tyres' as part of the attributes. and we also have a field telling us where the object is a car or not. A sample dataset is shown below:

<!-- insert sample dataset here -->
<table>
    <thead>
        <th>No</th>
        <th>Weight(kg)</th>
        <th>Length(m)</th>
        <th>Number of Tyres</th>
        <th>isCar</th>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>2.5</td>
            <td>1.5</td>
            <td>1</td>
            <td>0</td>
        </tr>
        <tr>
            <td>2</td>
            <td>80</td>
            <td>2</td>
            <td>4</td>
            <td>1</td>
        </tr>
        <tr>
            <td>3</td>
            <td>75</td>
            <td>3</td>
            <td>4</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

Looking at the table above, we can observe that when we already have the labels (i.e isCar) present before we start anything. This means that when we are making an machine learning application that leveraages this dataset we are most likely going to be using it to <strong>predict</strong> whether an object is a car or not.

### Unsupervised Learning

With Unsupervised Learning, things are a little different. Here, we are more concerned wiith making sense of the data set and then categorizing the data into smaller clusters and our training data has only unmlabeled features. 
So an example dataset we could have is:

<table>
    <thead>
        <th>No</th>
        <th>Weight(kg)</th>
        <th>Length(m)</th>
        <th>Number of Tyres</th>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>2.5</td>
            <td>1.5</td>
            <td>1</td>
        </tr>
        <tr>
            <td>2</td>
            <td>80</td>
            <td>2</td>
            <td>4</td>
        </tr>
        <tr>
            <td>3</td>
            <td>75</td>
            <td>3</td>
            <td>4</td>
        </tr>
    </tbody>
</table>

Notice how in the table above, the label <strong>isCar</strong> is left out here. In this case, our job would then be to cluster the dataset and group related samples.

## Advantages of Machine Learning
- Fraud Detection
- Stock Price Prediction
- House Price Prediction
- Disease Prediction
- Snap Chat adaptive filters 😂

## Examples of Machine Learning Models

We have alot of machine learning models that have been developed over the years : linearn regression, logisitic regressiom, neural networks, support vector machines, KMeans etc.

In this starter pack we are going to explore these machine learning models in-depth one after the other 😇

## Machine Learning APIs
Lucky for us, companies are already riding the wave of machine learning and have publicly accessible APIs for use. So if you just want to get to using their APIs, here are some listed below:
- [Tensorflow](https://www.tensorflow.org)
- [Scikit Learn](http://scikit-learn.org/stable/)
- [Kairos API](http://kairos.com)
- [Microsoft's API](https://azure.microsoft.com/en-us/services/cognitive-services/)
