import sys
sys.path.append('../')

import pandas as pd
import numpy as np
from utils.plot_highDim_data import plot_data
from sklearn.model_selection import train_test_split
import scikitplot as skplt

from sklearn.feature_selection import SelectKBest, mutual_info_classif, f_classif, f_regression, RFECV, VarianceThreshold
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC, SVR
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

#df = pd.read_csv('../data/machining_drive_load.csv', header=0)
df = pd.read_csv('../data/axis_xyz_load.csv', header=0)

df2 = pd.read_csv('../data/prod_measurements2.csv', header=0, sep=';')
df2 = df2.set_index('trace:id')
df = df.set_index('trace:id')

df_join = df2['status']

df_all = df.join(df_join,how='inner')
df_all = df_all.dropna()
y = df_all.pop('status')
df_all = df_all.drop('qr', axis=1)

print(y)
print(len(df_all))
# plot high dim data
plot_data(df_all, y, 'TSNE', 2)
#print(df_all.columns)
pipe = make_pipeline(SelectFromModel(estimator=RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)), LogisticRegression(solver='lbfgs', multi_class='auto', max_iter=5000))
lr = LogisticRegression(solver='lbfgs', multi_class='auto', max_iter=5000, class_weight='balanced')
#rf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
rf = RandomForestClassifier(n_estimators=500, max_depth=5, random_state=0, class_weight={'nok':4, 'ok':1})
print(cross_val_score(lr, df_all, y, scoring='accuracy', cv=5).mean())
print(cross_val_score(rf, df_all, y, scoring='accuracy', cv=5).mean())
print(cross_val_score(pipe, df_all, y, scoring='accuracy', cv=5).mean())


X_train, X_test, Y_train, Y_test = train_test_split(df_all, y, test_size=0.2, random_state=420)

clf = SVC(gamma='scale', class_weight={'nok':4, 'ok':1}, kernel='sigmoid')
#clf = SVC(gamma='scale', class_weight='balanced', kernel='rbf')
#clf = SVR(gamma="scale", kernel="linear")
y_fac = pd.factorize(y)
#print(y_fac[0])
clf.fit(X_train, Y_train)  
Y_pred_svm = clf.predict(X_test)
#Y_pred_svm = clf.score(df_all, y)
print("SVM:\n%s\n" % (
    metrics.classification_report(Y_test, Y_pred_svm)))

print(Y_pred_svm)
print(cross_val_score(clf, X_test, Y_test, scoring='accuracy', cv=5).mean())


rf = RandomForestClassifier(n_estimators=500, max_depth=5, random_state=0, class_weight='balanced')
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
print(cross_val_score(est, X_test, Y_test, scoring='accuracy', cv=5).mean())



#skplt.metrics.plot_roc(Y_test, Y_proba)
#plt.show()
"""
fpr, tpr, thresholds = metrics.roc_curve(Y_test, Y_pred, pos_label=0)
plt.plot(fpr, tpr)
plt.show()
auc = np.trapz(tpr, fpr)
print('AUC:', auc)

#print(df2[df2.status=='nok'].manual_measure1,df2[df2.status=='nok'].manual_measure2, df2[df2.status=='nok'].manual_measure3)

#logistic = linear_model.LogisticRegression(solver='lbfgs', max_iter=10000, multi_class='multinomial')
rbm = BernoulliRBM(random_state=0, verbose=True)
#rbm.cv = 5
rbm.learning_rate = 0.5
rbm.n_iter = 25
rbm.n_components = 200

#logistic.C = 6000

rbm_features_classifier = Pipeline(steps=[('rbm', rbm), ('clf', clf)])
# cross validation to get n_iter and learning_rate parameters
#get_rbm_params(rbm_features_classifier, X_train, Y_train)

# Training RBM-Logistic Pipeline
rbm_features_classifier.fit(df_all, y)

# Predicting test set
Y_pred = rbm_features_classifier.predict(df_all)

print("Logistic regression using RBM features:\n%s\n" % (
    metrics.classification_report(y, Y_pred)))
"""