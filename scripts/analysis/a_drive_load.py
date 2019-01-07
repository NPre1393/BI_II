import sys
sys.path.append('../')

import pandas as pd
import numpy as np
from utils.plot_highDim_data import plot_data
from sklearn.model_selection import train_test_split
import scikitplot as skplt

from sklearn.feature_selection import SelectKBest, mutual_info_classif, f_classif, f_regression, RFECV, VarianceThreshold
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectFromModel
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn import metrics, linear_model
from sklearn.model_selection import StratifiedKFold
from sklearn.neural_network import BernoulliRBM

import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

df = pd.read_csv('../data/machining_drive_load.csv', header=0)
df2 = pd.read_csv('../data/prod_measurements2.csv', header=0, sep=';')

range1 = [4.500, 0.028, 0.040]
range2 = [19.20, -0.05, 0.00]
range3 = [15.15, 0.00, 0.05]
df2 = df2.set_index('trace:id')
df = df.set_index('trace:id')
#print(range1[0]+range1[1], range1[0]+range1[2])
mm1 = df2.manual_measure1.between(range1[0]+range1[1], range1[0]+range1[2])
a = df2[mm1]
mm2 = a.manual_measure2.between(range2[0]+range2[1], range2[0]+range2[2])
b = a[mm2]
mm3 = b.manual_measure3.between(range3[0]+range3[1], range3[0]+range3[2])
c = b[mm3]

print("Manual measures that indicate nok: ", len(df2)-len(c))
print("Status nok df2:", sum(df2.status=='nok'))
print("Status nok c:", sum(c.status=='nok'))
print(df2[-mm1].manual_measure1)
print(a[-mm2].manual_measure2)
print(b[-mm3].manual_measure3)
print(df2[-df2.manual_measure3.between(range3[0]+range3[1], range3[0]+range3[2])])

df_join = df2['status']
#print(df_join)
df_all = df.join(df_join,how='inner')
df_all = df_all.dropna()
y = df_all.pop('status')
df_all = df_all.drop('qr', axis=1)
print(df_all.columns)
pipe = make_pipeline(SelectFromModel(estimator=RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)), LogisticRegression(solver='lbfgs', multi_class='auto', max_iter=5000))
lr = LogisticRegression(solver='lbfgs', multi_class='auto', max_iter=5000, class_weight='balanced')
rf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
print(cross_val_score(lr, df_all, y, scoring='accuracy', cv=5).mean())
print(cross_val_score(rf, df_all, y, scoring='accuracy', cv=5).mean())
print(cross_val_score(pipe, df_all, y, scoring='accuracy', cv=5).mean())

X_train, X_test, Y_train, Y_test = train_test_split(df_all, y, test_size=0.5, random_state=420)
"""
rf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
rfecv = RFECV(estimator=rf, verbose=True, step=1, cv=StratifiedKFold(2), scoring="accuracy")
rfecv.fit(X_train, Y_train)
X_test = rfecv.transform(X_test)
print("Optimal number of features : %d" % rfecv.n_features_)
print("Feature ranking:", rfecv.ranking_)
est = rfecv.estimator_
Y_pred = est.predict(X_test)
Y_proba = est.predict_proba(X_test)
print(np.unique(Y_pred))
print("Random Forest with RFE feature selection:\n%s\n" % (
    metrics.classification_report(Y_test, Y_pred)))
"""
#skplt.metrics.plot_roc(Y_test, Y_proba)
#plt.show()
"""
fpr, tpr, thresholds = metrics.roc_curve(Y_test, Y_pred, pos_label=0)
plt.plot(fpr, tpr)
plt.show()
auc = np.trapz(tpr, fpr)
print('AUC:', auc)
"""
#print(df2[df2.status=='nok'].manual_measure1,df2[df2.status=='nok'].manual_measure2, df2[df2.status=='nok'].manual_measure3)

logistic = linear_model.LogisticRegression(solver='lbfgs', max_iter=10000, multi_class='multinomial')
rbm = BernoulliRBM(random_state=0, verbose=True)
#rbm.cv = 5
rbm.learning_rate = 0.1
rbm.n_iter = 25
rbm.n_components = 200

logistic.C = 6000

rbm_features_classifier = Pipeline(steps=[('rbm', rbm), ('logistic', logistic)])
# cross validation to get n_iter and learning_rate parameters
#get_rbm_params(rbm_features_classifier, X_train, Y_train)

# Training RBM-Logistic Pipeline
rbm_features_classifier.fit(df_all, y)

# Predicting test set
Y_pred = rbm_features_classifier.predict(df_all)

print("Logistic regression using RBM features:\n%s\n" % (
    metrics.classification_report(y, Y_pred)))