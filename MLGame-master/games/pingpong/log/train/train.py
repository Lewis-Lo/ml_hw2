import pickle
import os 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn import ensemble, preprocessing, metrics
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier

files = ['', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '', 
         '', '', '', '', '', '', '', '', '', '']

for index in range(0, 200):
    files[index] = ("features{}.pickle".format(str(index+1)))

data = pickle.load(open(files[0], 'rb'))

for index in files[0:200]:
    temp = pickle.load(open(index, 'rb'))
    data = np.hstack((data, temp))

data = data.T
dataX = data[:, 0:9]
dataYP1 = data[:, 9]
dataYP2 = data[:, 10]

X_trainP1, X_testP1, Y_trainP1, Y_testP1 = train_test_split(dataX, dataYP1, test_size = 0.3)
X_trainP2, X_testP2, Y_trainP2, Y_testP2 = train_test_split(dataX, dataYP2, test_size = 0.3)

# knn = KNeighborsClassifier(n_neighbors=2)
# knn.fit(X_trainP1, Y_trainP1)

# print(knn.predict(X_testP1))
# print(Y_testP1)
# print(knn.score(X_testP1, Y_testP1))

# pickle.dump(knn, open('model_s5.pickle', 'wb'))

dtc = tree = DecisionTreeClassifier(criterion = 'entropy', max_depth=50, random_state=3)
dtc.fit(X_trainP1, Y_trainP1)
print(dtc.score(X_testP1, Y_testP1))
pickle.dump(dtc, open('dtcP1.pickle', 'wb'))

dtc = tree = DecisionTreeClassifier(criterion = 'entropy', max_depth=50, random_state=3)
dtc.fit(X_trainP2, Y_trainP2)
print(dtc.score(X_testP2, Y_testP2))
pickle.dump(dtc, open('dtcP2.pickle', 'wb'))

# rf = RandomForestClassifier(n_estimators=1000, random_state=42)
# rf.fit(X_trainP1, Y_trainP1)
# print(rf.score(X_testP1, Y_testP1))
# pickle.dump(rf, open('rfP1.pickle', 'wb'))

# rf = RandomForestClassifier(n_estimators=1000, random_state=42)
# rf.fit(X_trainP2, Y_trainP2)
# print(rf.score(X_testP2, Y_testP2))
# pickle.dump(rf, open('rfP2.pickle', 'wb'))