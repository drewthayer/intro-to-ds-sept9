Linear Regression Case Study

After going over XX dataset together, you should be able to explore the cars dataset (in the github repo) and 

1.	What does the distribution of the outcome (mpg) look like? Create a histogram AND boxplot and write down your thoughts on the distribution.
2.	Make a scatter_matrix using Pandas or a pairplot using Seaborn and look at the relationships between all the variables, are there any specific variables that stick out?
3.	Pick three variables and create 3 scatterplots looking at each variable on the x-axis and the outcome on the y-axis.
4.	Create the X matrix and y variable and run a linear regression on all the variables except the car name. What is the score for this model?
5.	Now, using `from sklearn.model_selection import train_test_split`, split the data into a test and train set and run the linear regression on all the variables. How does the score for this model compare to the core from question 4?
6.	We are using R^2 for this, what are some other metrics that we can use for linear regression? Do you think one is better than the other in this case?
7. Try removing a few columns that might not make sense to keep in, and run the model again using a train test split.
