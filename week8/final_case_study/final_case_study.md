## Linear Regression Case Study

__intro__
Much of what you will be doing today you have seen before! For your final in-class assignment, we want you to analyze the Violent Crimes dataset, creating insights from the data. Make sure to explore the data, graphing appropriately and being able to interpret the graphs. 

__data__
Today we will be looking at the Violent Crimes dataset. This dataset you should be trying to answer the question: 


__exercises__
1.	Look at the data. How are missing values recorded? How can we deal with these when reading in our data?

__reading the data__
  - pandas `read_csv()` default is to read .csv 
  - make sure to import data with a missing value parameter
  - use the provided parsing script provided to parse through column names

__model exercises__
1. What does the distribution of the outcome (Violent Crimes per Population) look like? Create a histogram AND boxplot and write down your thoughts on the distribution.
2.	Does it make sense to transform the outcome some how to make it look more `normal`? If so, try that transformation and plot again to visualize your outcome.
3.  Get some basic info, descriptive statistics, and shape of your dataset.
4.  Does it make sense to make a scatter_matrix? 
- If yes, using Pandas or a pairplot using Seaborn do that and look at the relationships between all the variables, are there any specific variables that stick out? Which variables look more correlated with each other? Which variables look the most normally distributed?
- If no, pick a few variables based on their names that you might think are important or could be related to the outcome of interest create scatterplots looking at each variable on the x-axis and the outcome on the y-axis.
5.	Create the X matrix and y variable and run a linear regression on all the variables. What is the score for this model?
6.	Now, using `from sklearn.model_selection import train_test_split`, split the data into a test and train set, overwriting the default to split into an 80/20 split and run the linear regression on all the variables. How does the score for this model compare to the score from question 5?
7.	We are using R^2 for this, what are some other metrics that we can use for linear regression? Do you think one is better than the other in this case? What are the units of each of these metrics?
8.  What do the residuals look like for the train_test model?
9. Try removing a few columns that might not make sense to keep in, and run the model again using a train test split. 
10. What was the model that returned the best score?


__extra credit__ 
Try to scale all your features and look at your coefficients to see which feature might be the most important! (code provided if needed)
