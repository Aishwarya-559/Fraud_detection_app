# HEALTH INSURANCE CLAIM FRAUD DETECTION APP:
Problem statement: The main goal of this project to detect whether the claim made by a person is genuine of fake. This can help insurance company to save a lot of time and will give accurate results.

#DATASET:
The dataset has been received from a Hospital to check whether the claim is true or not.

# APPROACH :
Data is collected from hospital. All the required tasks to prepare the data for model buliding such as data cleaning, pre-processing, data exploration,visualisation were done.
##### 1.Data exploration: Exploring the dataset using pandas, numpy, matplotlib, plotly and seaborn.
##### 2.Exploratory Data Analysis : Plotted different graphs to get more insights about dependent and independent variables/features.
##### 3.Feature Engineering : There are numerical and categorical features are present. Scaling was performed on numerical data and encoding of categorical data is done.
##### 4.Feature Selection : There were multiple features in the dataset which were not contributing to the model building and were creating complex model. Feature selection was done by filter methods.
##### 5.Model Building : For model building, data was splitted into training and testing set.After splitting various algorithms were used to train our model.
 	⇥Decision Tree
 	⇥Random Forest
 	⇥Logistic regression
 	⇥Gradient Boosting
 	⇥Adaboost
##### 5.Model Selection : Tested all the models to check the accuracy.
##### 6.Pickle File : Selected model as per best precision score & recall and created pickle file using pickle library.
##### 7.Webpage &Deployment : Created a web application using streamlit API that takes all the necessary inputs from the user & shows the output. Then deployed project on the Heroku Platform.

# WEB INTERFACE :
#####INTERFACE
![alt tag](https://github.com/AishwaryaMate99/Fraud_detection_app/blob/main/Images/interface.jpg)
##### Prediction:
##### Fraud Claim prediction:
![alt tag](https://github.com/AishwaryaMate99/Fraud_detection_app/blob/main/Images/Fraud_Claim.jpg)
##### Genuine Claim prediction:
![alt tag](https://github.com/AishwaryaMate99/Fraud_detection_app/blob/main/Images/Genuine_claim.jpg)


# LIBRARIES USED :
1) Pandas
2) Numpy
3) Matplotlib, Seaborn, Plotly
4) Scikit-Learn
5) Streamlit 
6) HTML
7) CSS

# TECHNICAL ASPECTS:
1) Python 
2) Front-end : HTML
3) Back-end : Streamlit
4) Deployment : Heruko
