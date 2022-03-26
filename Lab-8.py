from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
d = load_iris()
xtrain,xtest,ytrain,ytest = train_test_split(d.data,d.target,random_state=0)
print("XTRAIN :",*xtrain,"XTEST : ",*xtest,"YTRAIN :",ytrain,"YTEST :",ytest,sep="\n")
kn = KNeighborsClassifier(n_neighbors=5)
kn.fit(xtrain,ytrain)
x_new = np.asarray([[5,2.9,1,0.2]])
p = kn.predict(x_new)
print(d.target_names[p[0]])
print("{:<10} : {:<10}".format("Actual","Predict"))
for i in range(len(xtest)):
    x_new = np.asarray([xtest[i]])
    p = kn.predict(x_new)
    print("{:<10} : {:<10}".format(d.target_names[ytest[i]],d.target_names[p[0]]))
print("Accuracy is : {:.2f}%".format(kn.score(xtest,ytest)*100))
