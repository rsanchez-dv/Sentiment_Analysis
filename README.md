# Sentiment Analysis on Yelp's Dataset

> Author: Roberto Sanchez, Talent Path: D1 Group

## Table of Contents

[TOC]

## Overview

This capstone project is centered around the data processing, elementary data analysis, and training of a model to predict user reviews sentiment.

### Business Goals

Create a model to be able to be used in generating sentiments on reviews or comments found in external websites to give insights on what people are talking about outside of Yelp.

This could give the company insights not easily available on sites where ratings are required or for internal use to determine sentiment on blogs or comments.

## Model Deployment

> Show demo of model

Link: <Pending Link>

Currently the LogisticRegression model is a viable candidate to be used in production for analyzing reviews of services or food. 

Current Stats: 

**Classification Report:**

![Classification Report](2million_classificationReport_linReg.PNG)



## Technology Stack

I'll be using these technologies for this project:

* [Jupyter Notebook](https://jupyter.org/) - **Version 6.3.0**
  * Used for most of the data processing, EDA, and model training.
* [Python](https://www.python.org/) - **Version 3.8.8**
  * The main language this project will be done in.
* [Tensorflow](https://www.tensorflow.org/) - **Version 2.5**
  * Using Keras to create and train our model.
* [Nvidia CUDA  Toolkit](https://developer.nvidia.com/cuda-toolkit) - **Version 11.2**
  * To enable TensorFlow to utilize the GPU to speed up training.
* [Scikit-learn](https://scikit-learn.org/stable/) - **Version 0.24**
  * Utilizing metrics reports
* [Postgres](https://www.postgresql.org/) - **Version 13**
  * Main database application used to store this data.
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - **Version 1.1.2**
  * Main backend technology to host a usable version of this project to the public.



## Data Processing

This capstone uses the Yelp dataset found on [Kaggle](https://www.kaggle.com/yelp-dataset/yelp-dataset/) which comprises of multiple files:

* Business Data
* Check-in Data
* Review Data
* Tips Data
* User Data

### Stage 1 - Read in From JSON files into Postgres

**Overview**

* Read in JSON files
* General observations on the features found in each file
* Modifying feature names to meet Postgres naming convention
* Normalized the data to prepare for import to Postgres
* Saved copies of each table as CSV file for backup incase Database goes down
* Exported data into Postgres

As stated above, Kaggle provided several JSON files with a large amount of data that needed to be stored in a location for easy access and provide a quick way to query data on the fly. As the files were read in Jupyter notebook a general observation was made to the feature names and amount each file contained to see what data I was dealing with along with the types associated with them. The business data contained a strange amount of attributes that had to be broken up into separate data frames to be normalized for Postgres. 

### Stage 2 -  Pre-Processing Data

**Overview**

* Read in data from Postgres
* IDing Null Values
* Removing Sparse features
* Saved data frame as a pickle to be used in model training

### Stage 3 - Cleaning Up Data

**Overview**

* Removed special characters, dates, emails, and URLs
* Removed stop_words
* Remove non-English reviews
* [IMPROVE] Replace contractions
* [IMPROVE] Remove newline and tab characters
* [IMPROVE] Balance Data with either SMOTE or Oversampling

## Elementary Data Analysis

### Analyzing Null Values in Dataset

Below is a visualization of the data provided by Kaggle showing which features have "NaN " values. Its is clear that the review ratings (review_stars) and reviews (text) are fully populated. Some of the business attributes are sparse but have enough values to be useful for other things. Note several other features were dropped in the Data Processing since they did not provide any insights for the scope of this project.

![Heatmap of several million rows of data.](null_heatmap.png)

### Looking Closer at the Ratings (review_stars)

This is a sample of 2 million rows from the original 8 million in the dataset. This distribution of ratings has a left skew on it where most of the reviews are 4 to 5 stars.

![A bar graph showing the distribution of ratings between 1 to 5. there is a significant amount of 5 stars compared to 1-3 combined.](ratings_distribution.png)

I simplified the ratings to better categorize the sentiment of the review by grouping 1 and 2 star reviews as 'negative', 3 star review as 'neutral', and 4 and 5 star reviews as 'positive'.

![Simplified Barchar showing just the negative, neutral, and positive ratings](ratings_distribution_simplified.png)

### Looking Closer at the Reviews (text)

In order to analyze the text I've calculated the length of each review in the sample and plotted a distribution graph showing them the number of characters of each review. The statistics were that the median review was approx. 606 characters with a range of 0 through 5000 characters.



![Showing a distribution chart of the length of the reviews. Clearly the distribution skews right with a median around 400 characters.](distribution_of_review_length.png)

A closer inspection on the range 0 - 2000 we can see that most of  the reviews are around this general area. 

![A zoomed in version of the same distribution chart now focusing on 0 - 2000 characters](distribution_of_review_length_trimmed.png)

In order to produce a viable word cloud I've had to process all of the text in the sample to remove special characters and stop words from NLTK to produce a viable string to be used in word cloud. Below is a visualization of all of the key words found in the positive reviews.

![Created a word cloud from the positive words after cleaning](wordCloud_positive.png)

As expected, words like "great", "amazing", "good", "love", and "best" came out on top.

![A word cloud showing all the words from the negative reviews](wordCloud_negative.png)

On the negative word cloud, words like "problem", "customer service", "least", "mean",  and "issue" are appearing on the word cloud. 

## Model Training

* The logistic regression model was built using a pipeline with TfidfVectorizer
* Was training using StratifiedKFold for cross-validator with 5 splits
* Final Results were as pictured above
* 

## Testing Model

After the model was trained, I fed it some reviews I found online to test out whether or not the model can properly detect the right sentiment. The following reviews are ordered as "Negative", "Neutral", and "Positive":

```python
new_test_data = [
    "This was the worst place I've ever eaten at. The staff was rude and did not take my order until after i pulled out my wallet.",
    "The food was alright, nothing special about this place. I would recommend going elsewhere.",
    "I had a pleasent time with kimberly at the granny shack. The food was amazing and very family friendly.",
]
res = model.prediction(new_test_data)
```

Below is the results of the prediction, notice that the neutral review has been labeled as negative. This makes sense since the model has a poor recall for neutral reviews as shown in the classification report.

<img src="results.PNG" alt="Results from the prediction" style="zoom:150%;" />



## End Notes

There are some improvements to be made such as the follow:

* Better text cleaning
* Balancing the data