# Linear Modeling Assignment

## Instructions

For your assignment tonight you're going to be calling the shots. Similar to the final part of `day10-intro_to_pandas`, you're going to be taking a data set and using it to create a model. You're welcome to use the data set you worked with during that assignment. If, however, you worked with the iris data set, you should pick a new one. Here's a list of links to other data sets (some of which are the same as before), along with the type of target that is in the data:

* [Forest Fires](http://archive.ics.uci.edu/ml/datasets/Forest+Fires) - continuous
* [Abalone](http://archive.ics.uci.edu/ml/datasets/Abalone) - multi-class
* [Adult Income](http://archive.ics.uci.edu/ml/datasets/Adult) - multi-class
* [Glass Identification](http://archive.ics.uci.edu/ml/datasets/Glass+Identification) - multi-class
* [Concrete Strength](http://archive.ics.uci.edu/ml/datasets/Concrete+Compressive+Strength) - continuous

All of these data sets are linked from the University of California, Irvine data sets archive. You're welcome to look at the [full list](http://archive.ics.uci.edu/ml/datasets/Glass+Identification) of data sets available there if you'd like; don't look too long, though! Also, keep in mind that we mainly want you to get used to the Python portion of this modeling endeavor. As such, the data set doesn't matter too much - we just want you to get practice working with data in Python.

Two of the data sets above have a continuous target (suitable for a regression model), and three have a multi-class target. You should aim to make a model for one of both types tonight. Now, we have a little advice in getting this done.

## Advice

You're going to want to do some EDA on the data before you model. This is a very important step. It allows you to get a feel for the data. It turns out that it's actually pretty easy to "make" a model out of some data, but relatively hard to get the data in a format that your model can use successfully. Getting data into a format that your model can use successfully requires you to know it well, and well enough to realize that maybe one of the inputs should be [transformed](https://en.wikipedia.org/wiki/Data_transformation_(statistics)). Or maybe the product of the values in two features happens to be very predictive. You will never know this if you don't do EDA!

If you just take the raw values in the data set and put them directly into a model, you're probably not going to get as good of a model as is possible. So part of this modeling process is going to be like the programming process that we have learned about in this course - it's going to be iterative. This being said, it's usually worth it to see how good of a model you can make with the data straight out of the box. We saw that the iris data set did pretty well without doing anything to it. Often times, though, you'll notice when you look at your data that some of it might not be numeric, and it turns out that linear models can only handle numbers for inputs. So, you're going to have to think about which features in your data can be used to make your first model.

Whatever score comes out of your first model is going to be your baseline for that data set (make sure that this score is from out-of-sample observations, and to set the `random_state` on `train_test_split()` as you saw in the lecture. This will allow you to compare the same split of your data each time, so the scores you get back later will be comparable). This is not the end, though. Learn from the EDA that your doing/going to do, and talk to an instructor about what you find. This way, you can try to figure out how to make your features more predictive, or get some information from your non-numeric features. When you want to test what you've found, make and score a new model with the same `train_test_split()` (guaranteed with the same `random_state`). If the score goes up, there's a good chance you found some more information in your data!
