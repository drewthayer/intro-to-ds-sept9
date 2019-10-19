# Logistic Regression Problem Set

We've gone over the Credit Default dataset together and learned:
  - how to load a csv file and do some header name cleaning
  - how to fit an sklearn LogisticRegression model to classification data
  - how to evaluate the model's accuracy, recall, and precision
  - how to assess class balance
  - a basic technique to work with imbalanced classes

Now, you're going to apply these tactics (and any others you want) to the _fruit labels_ dataset

__data:__ https://github.com/susanli2016/Machine-Learning-with-Python/blob/master/fruit_data_with_colors.txt

__downloading the data__
  - you could clone the whole repository, OR you could just save this file's contents
  - click the button "RAW"
  - select all and copy (cmd+A, cmd+C)
  - open a new file in a text editor (VSCode, Atom, TextEdit, Notepad...)
  - paste (cmd+V)
  - take a look at the data...how is this file formatted?
~~~
fruit_label	fruit_name	fruit_subtype	mass	width	height	color_score
1	apple	granny_smith	192	8.4	7.3	0.55
1	apple	granny_smith	180	8.0	6.8	0.59
1	apple	granny_smith	176	7.4	7.2	0.60
2	mandarin	mandarin	86 	6.2	4.7	0.80
2	mandarin	mandarin	84 	6.0	4.6	0.79
2	mandarin	mandarin	80 	5.8	4.3	0.77
2	mandarin	mandarin	80 	5.9 	4.3	0.81
2	mandarin	mandarin	76	5.8	4.0	0.81
~~~

  - this is tabular data, separated by tabs (commas would be the common .csv)
  - Great! this is machine-readable. We call this tab-separated-values, or TSV
  - save as <some_name.tsv> in your data/ directory

__reading the data__
  - pandas `read_csv()` default is to read .csv (e.g. `delimiter=','`)
  - when you read this with pandas, pass the argument `delimiter=('\t')` to `pd.read_csv()`
    - '\t' is the character for tab

  - for this exercise, drop the 'fruit_subtype' category

__modeling exercise__
We're going to try to predict the type of fruit based on its mass, width, height, and color score.

1.	How many classes of fruit are there? How balanced are the classes? Find the % of the dataset for each class (e.g. apple: 32.2%).
  - There are multiple ways to do this, try using `dataframe.groupby(column)`. Remember you can add an aggregation function to the end of the `groupby()` call (.sum(), .mean(), .size(), .count(), .max(), etc...)
2.  What is the distribution of classes in the dataset? (try to plot this)
3.  Create a boxplot of the 4 numeric variables. Which is most closely distributed like a gaussian (normal) distribution?
4.  Make a scatter_matrix using Pandas or a pairplot using Seaborn and look at the relationships between all the variables, are there any specific variables that stick out? Which looks most normally distributed?
5.	Pick three variables and create 3 scatterplots looking at each variable on the x-axis and the outcome on the y-axis.
6.	Create the X matrix and y variable and split the data into train and test sets
7.  Fit a sklearn logistic regression model to the test set and predict the fruit type.
8.  Assess the training score and test score of the model (use `model.score(X_train, y_train)` and repeat for test set). Does it make sense that one is higher than the other?
  - It's often interesting to note the difference between train and test accuracy, because it gives you a sense of how _generalizeable_ the model might be, i.e. how it will perform on _unseen_ data (that's the whole point of holding a test set on the side when we train machine learning models).
  - If we're going to report one score, it's the test score.
9.  Assess the model's accuracy, precision, and recall. Think about what these three scores mean, and scenarios where you would want to optimize recall, or precision (remember that there is generally a tradeoff between the two... you can't increase both).
  - _NOTE: the recall_score() and precision_score() functions are set up with defaults for binary classification. There is a default parameter `average='binary'`. Since this is a multi-class problem, you will need to pass `average='weighted'` into these functions._
  - fruit-type prediction is obviously pretty trivial, but think about some classic examples, and WHY that metric is usually chosen:
    - high-precision email spam filter
    - high-recall skin cancer test
10.  Make a confusion matrix of the model's outputs (remember `sklearn.metrics.confusion_matrix`). Confusion matrices are a little more complex with more than two target classes, but remember that instance where the model predicted the True value are along the diagonal (ideal).
11. There is some class imbalance here, what could you do to try to get higher recall?
12. We've instantiated our LogisticRegression class with the default parameters, but there are many available parameters. Take a look at the 'class_weight' parameter in the docs: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
13. Try modeling again, passing `class_weight='balanced'` into LogisticRegression(). How does this affect your test accuracy, recall, and precision?
