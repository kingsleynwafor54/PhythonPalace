import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
import seaborn as sns

fruits = pd.read_table("C:\\Users\\USCHIP\\Downloads\\fruit_data_with_colors.txt")
print(fruits.head(10))

print(fruits.shape)
print(fruits['fruit_name'].unique())
print(len(fruits['fruit_name'].unique()))
print(fruits.groupby("fruit_name").size())
sns.countplot(fruits['fruit_name'], label="Count")
plt.show()
# box-plot helps in visualization of your data
fruits.drop('fruit_label', axis=1).plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False,
                                        figsize=(9, 9),
                                        title='Box Plot for each input variable')

plt.savefig('fruits_box')
plt.show()
# Let's plot histogram
fruits.drop('fruit_label', axis=1).hist(bins=30, figsize=(9, 9))
pl.suptitle("Histogram for each numeric input variable")
plt.savefig('fruits_hist')
plt.show()
# dividing your dataset into target and predictor variables
feature_names = ['mass', 'width', 'height', 'color_score']
X = fruits[feature_names]
y = fruits['fruit_label']
# data splicing, it is splitting your data into training and testing
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
# scaler (MinMaxScaler()) is used for normalizing you datatypes from the variables
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Here we are going to build our models
# Importing Linear regression
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(X_train, y_train)
print("Accuracy of logistic regression classifier on training set: {:.2f}".format(logreg.score(X_train, y_train)))
print("Accuracy of logistic regression classifier on test set: {:.2f}".format(logreg.score(X_test, y_test)))

# Decision tree
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier().fit(X_train, y_train) 
print("Accuracy of Decision tree classifier on training set: {:.2f}".format(clf.score(X_train, y_train)))
print("Accuracy of Decision tree classifier on test set: {:.2f}".format(clf.score(X_test, y_test)))

# KNN Classifier
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
print("Accuracy of K-NN classifier on training set:{:.2f}".format(knn.score(X_train, y_train)))
print("Accuracy of K-NN classifier on training set:{:.2f}".format(knn.score(X_test, y_test)))

# NaiveBayes
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
gnb.fit(X_train, y_train)
print("Accuracy of NaiveBayes classifier on training set:{:.2f}".format(gnb.score(X_train, y_train)))
print("Accuracy of Naivebayes classifier on training set:{:.2f}".format(gnb.score(X_test, y_test)))

# Support Vector Machine Classifier
from sklearn.svm import SVC

svm = SVC()
svm.fit(X_train, y_train)
print("Accuracy of SVM classifier on training set:{:.2f}"
      .format(svm.score(X_train, y_train)))
print("Accuracy of SVM classifier on training set:{:.2f}"
      .format(svm.score(X_test, y_test)))


gamma='auto'
# Confusion matrix
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

pred=knn.predict(X_test)
print(confusion_matrix(y_test,pred))
print(classification_report(y_test,pred))





