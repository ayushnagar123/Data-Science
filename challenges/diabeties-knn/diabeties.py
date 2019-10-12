from math import sqrt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfx = pd.read_csv('Diabetes_XTrain.csv')
dfy = pd.read_csv('Diabetes_YTrain.csv')
dfz = pd.read_csv('Diabetes_Xtest.csv')
dfss = pd.read_csv('sample_submission.csv')
print(dfx.shape,dfy.shape)

print(dfx.columns)

print(dfx.head(n=5))

data =dfx.values
res = dfy.values
print(data.shape)
print(type(data))

testd = dfz.values
testy = dfss.values
x = data[:,1:]
y = res[:,0]
x_test = testd[:,1:]
y_test = testy[:,0]
split = int(1*x.shape[0])
print(split)

x_train = x[:,:]
y_train = y[:]

print(x_train.shape,y_train.shape)
print(x_test.shape,y_test.shape)

def dist(x1,x2):
    return np.sqrt(sum((x1-x2)**2))

def knn(x,y,queryPoint,k=17):
    vals = []
    m = x.shape[0]
    
    for i in range(m):
        d = dist(queryPoint,x[i])
        vals.append((d,y[i]))
    vals = sorted(vals)
    
    vals = vals[:k]
    vals = np.array(vals)
#     print(vals)
    
    new_vals = np.unique(vals[:,1],return_counts = True)
#     print(new_vals)
    index = new_vals[1].argmax()
    pred = new_vals[0][index]
    return pred
c=0
import csv
with open('people.csv', 'w') as writeFile:
    for i in range(len(x_test)):
        pred = knn(x_train,y_train,x_test[i])
        print(int(pred))
        if(y_test[i]==pred):
            c+=1
        writeFile.write(str(int(pred))+'\n')
writeFile.close()
print('accuracy=',c*100/len(x_test))