# README

Credit to the [Data Science Working Group](http://datascience.codeforsanfrancisco.org) for this template. To complete this project, delete all template text (save for the headers) and fill in your own information.

Begin reading `instructions.md` to get started.

## Project Intro/Objective
The purpose of this project is to analyze stock data stored in a Python file ("stock_data.py") by implementing various methods. This includes handling data initialization, loading, and addressing missing data points. The main goal is to perform a calculations in solving the metrics such as finding the average , median and standard deviation. 
### Methods Used
* Inferential Statistics
* Machine Learning
* Data Visualization
* Predictive Modeling
* etc.

### Technologies
* R 
* Python
* D3
* PostGres, MySql
* Pandas, jupyter
* HTML
* JavaScript
* etc. 

## Project Description
In this project, we are supposed to analyze stock data in the "stock_data.py" file. For each method, we require an initialization method where our data is initially set to "None," and in the other methods, we need to load the data. Within our dataset, there are three tasks we need to complete, which involve finding missing data points, calculating the average, median, and standard deviation. For each of these tasks, we need to create a data structure to process the values.

During this project, we encountered an issue in figuring out how to handle missing values. To address this, we were able to create a new row in the dataset using the following code: "new_row = [float(val) for val in row[1:] if val != "" and val != " "]. This solution allowed us to overcome the problem we were facing.
