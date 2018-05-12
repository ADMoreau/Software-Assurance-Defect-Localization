import pandas as pd
from sklearn.model_selection import train_test_split  
from sklearn.neural_network import MLPClassifier 
from sklearn.metrics import classification_report, confusion_matrix 
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn import svm
from sklearn.ensemble import ExtraTreesClassifier
'''
This program uses the array of floats listed below, the comparison made between the strings in the testcases and the filtered features, as 
data for ML processes.
The code directly below this is the final code used for the testing. The highest accuracy level found with this method was .92.
The other chunks of code below are other failed atempts used by the researchers which were left in for documentation purposes.
The final program uses a voter method with a random forest classifier, extra trees classifier and linear discriminant analysis as voters
with the hyperparameters listed.
To reproduce results simply open this file and hit run
'''
vals = [[0.9850746268656716, 0.9814814814814815, 0.9272727272727272, 0.9795918367346939, 1.0, 1.0, 0.993103448275862, 0.9923664122137404, 0.9702970297029703, 1.0, 0.8823529411764706, 0, 0.8066666666666666, 0.9763779527559056, 0.8976377952755905, 0.9913793103448276, 0.993006993006993, 1], [1.0, 0.9907407407407407, 0.9272727272727272, 0.9693877551020408, 1.0, 1.0, 0.9862068965517241, 1.0, 0.9801980198019802, 1.0, 0.8411764705882353, 0, 0.9, 0.984251968503937, 0.905511811023622, 0.9913793103448276, 0.993006993006993, 1], [0.9850746268656716, 0.9814814814814815, 0.9272727272727272, 0.9846938775510204, 1.0, 1.0, 0.993103448275862, 1.0, 0.9603960396039604, 1.0, 0.8705882352941177, 0, 0.8066666666666666, 0.9763779527559056, 0.905511811023622, 0.9913793103448276, 0.993006993006993, 1], [1.0, 0.9907407407407407, 0.9272727272727272, 0.9846938775510204, 1.0, 1.0, 0.993103448275862, 1.0, 0.9801980198019802, 1.0, 0.9235294117647059, 0, 0.8066666666666666, 0.984251968503937, 0.9291338582677166, 0.9913793103448276, 0.993006993006993, 1], [0.9925373134328358, 0.9907407407407407, 0.8636363636363636, 0.9693877551020408, 1.0, 1.0, 0.993103448275862, 0.9923664122137404, 0.9603960396039604, 1.0, 0.8764705882352941, 0, 0.8066666666666666, 0.984251968503937, 0.905511811023622, 0.9913793103448276, 0.993006993006993, 1], [0.9850746268656716, 0.9814814814814815, 0.9272727272727272, 0.9795918367346939, 1.0, 1.0, 0.993103448275862, 0.9923664122137404, 0.9702970297029703, 1.0, 0.8823529411764706, 0, 0.8066666666666666, 0.9763779527559056, 0.8976377952755905, 0.9913793103448276, 0.993006993006993, 0], [1.0, 0.9814814814814815, 0.9272727272727272, 0.9795918367346939, 1.0, 1.0, 0.993103448275862, 0.9923664122137404, 0.9702970297029703, 1.0, 0.7823529411764706, 0, 0.8266666666666667, 0.984251968503937, 0.8818897637795275, 0.9913793103448276, 0.986013986013986, 0], [0.9925373134328358, 0.9814814814814815, 0.9272727272727272, 0.9795918367346939, 0.9919354838709677, 1.0, 0.9862068965517241, 0.9923664122137404, 0.9603960396039604, 1.0, 0.8411764705882353, 0, 0.86, 0.984251968503937, 0.905511811023622, 0.9913793103448276, 0.993006993006993, 0], [1.0, 0.9814814814814815, 0.7545454545454545, 0.9846938775510204, 1.0, 1.0, 0.993103448275862, 1.0, 0.9801980198019802, 1.0, 0.9235294117647059, 0, 0.8, 0.9921259842519685, 0.8976377952755905, 0.9913793103448276, 0.993006993006993, 0], [1.0, 0.9814814814814815, 0.9272727272727272, 0.9795918367346939, 0.9919354838709677, 1.0, 0.993103448275862, 0.9923664122137404, 1.0, 1.0, 0.8058823529411765, 0, 0.8066666666666666, 0.984251968503937, 0.889763779527559, 0.9913793103448276, 0.993006993006993, 0],[0.9850746268656716, 0.9814814814814815, 0.8636363636363636, 0.9795918367346939, 1.0, 1.0, 0.9862068965517241, 0.9923664122137404, 0.9603960396039604, 1.0, 0.8647058823529412, 0, 0.8066666666666666, 0.984251968503937, 0.8976377952755905, 0.9913793103448276, 0.993006993006993, 1], [0.9850746268656716, 0.9814814814814815, 0.9272727272727272, 0.9744897959183674, 1.0, 1.0, 0.9862068965517241, 1.0, 0.9603960396039604, 1.0, 0.8705882352941177, 0, 0.8066666666666666, 0.9763779527559056, 0.905511811023622, 0.9913793103448276, 0.993006993006993, 1], [1.0, 0.9907407407407407, 0.9272727272727272, 0.9846938775510204, 1.0, 1.0, 0.993103448275862, 1.0, 0.9603960396039604, 1.0, 0.7941176470588235, 0, 0.9, 0.984251968503937, 0.9448818897637795, 0.9913793103448276, 0.986013986013986, 1], [0.9850746268656716, 0.9814814814814815, 0.9272727272727272, 0.9744897959183674, 1.0, 1.0, 0.9862068965517241, 1.0, 0.9603960396039604, 1.0, 0.8705882352941177, 0, 0.8066666666666666, 0.9763779527559056, 0.905511811023622, 0.9913793103448276, 0.993006993006993, 1], [0.9925373134328358, 0.9907407407407407, 0.9636363636363636, 0.9846938775510204, 1.0, 1.0, 0.993103448275862, 1.0, 0.9900990099009901, 1.0, 0.8647058823529412, 0, 0.9133333333333333, 0.984251968503937, 0.9448818897637795, 0.9913793103448276, 0.993006993006993, 1], [1.0, 0.9814814814814815, 0.7545454545454545, 0.9897959183673469, 1.0, 1.0, 0.9862068965517241, 1.0, 0.9801980198019802, 1.0, 0.9235294117647059, 0, 0.9, 0.984251968503937, 0.905511811023622, 0.9913793103448276, 0.993006993006993, 0], [1.0, 0.9907407407407407, 0.9636363636363636, 0.9846938775510204, 1.0, 1.0, 0.993103448275862, 0.9923664122137404, 0.9900990099009901, 1.0, 0.7823529411764706, 0, 0.7866666666666666, 0.9921259842519685, 0.9133858267716536, 0.9913793103448276, 0.9790209790209791, 0], [0.9925373134328358, 0.9907407407407407, 0.8636363636363636, 0.9693877551020408, 1.0, 1.0, 0.993103448275862, 1.0, 0.9900990099009901, 1.0, 0.8764705882352941, 0, 0.86, 0.984251968503937, 0.9291338582677166, 0.9913793103448276, 0.993006993006993, 0], [1.0, 0.9907407407407407, 0.8727272727272727, 0.9846938775510204, 1.0, 1.0, 0.993103448275862, 0.9847328244274809, 0.9801980198019802, 1.0, 0.8411764705882353, 0, 0.8133333333333334, 0.9921259842519685, 0.905511811023622, 0.9913793103448276, 0.993006993006993, 0], [1.0, 0.9907407407407407, 0.9636363636363636, 0.9846938775510204, 1.0, 1.0, 0.993103448275862, 0.9923664122137404, 0.9900990099009901, 1.0, 0.7823529411764706, 0, 0.7866666666666666, 0.9921259842519685, 0.9133858267716536, 0.9913793103448276, 0.9790209790209791, 0]]
vals = pd.DataFrame.from_records(vals)
X = vals.iloc[:, 0:16]
y = vals.iloc[:, 17]
#print(spam)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5)

clf1 = RandomForestClassifier(n_estimators = 20, max_depth = 500)
clf2 = ExtraTreesClassifier(criterion = 'entropy',n_estimators = 100, max_depth = 40)
clf3 = LinearDiscriminantAnalysis(solver = 'lsqr')

eclf1 = VotingClassifier(estimators = [('rfc', clf1) ,('etc', clf2),('lda',clf3)], voting='hard')

eclf1.fit(X_train, y_train.values.ravel())  

predictions = eclf1.predict(X_test)

print(confusion_matrix(y_test,predictions))  
print(classification_report(y_test,predictions)) 



#Neural Network
'''
mlp = MLPClassifier(hidden_layer_sizes=(20, 10), max_iter=10000)  
mlp.fit(X_train, y_train.values.ravel())  

predictions = mlp.predict(X_test)

print(confusion_matrix(y_test,predictions))  
print(classification_report(y_test,predictions)) 


#SVM

from sklearn.svm import SVC

SVM = SVC()
SVM.fit(X_train, y_train.values.ravel())

predictions = SVM.predict(X_test)

print(confusion_matrix(y_test,predictions))  
print(classification_report(y_test,predictions)) 

'''
'''
#Random Forest

RFC = RandomForestClassifier(max_depth=20, random_state=1)

RFC.fit(X_train, y_train.values.ravel())

predictions = RFC.predict(X_test)

print(confusion_matrix(y_test,predictions))  
print(classification_report(y_test,predictions)) 
'''
