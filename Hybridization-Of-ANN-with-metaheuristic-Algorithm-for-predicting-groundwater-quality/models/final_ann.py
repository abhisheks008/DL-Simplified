

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import mean_squared_error


data = pd.read_csv('../Ground Water .csv')



#data = data.fillna(data.mean())
# Fill NaN values only in numeric columns with median
numeric_columns = data.select_dtypes(include='number').columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].median())


# Select only numeric columns for quantile calculations
numeric_data = data.select_dtypes(include=[np.number])
data[numeric_data.columns] = numeric_data.clip(lower=numeric_data.quantile(0.01), upper=numeric_data.quantile(0.99), axis=1)

#data = data.clip(lower=data.quantile(0.01), upper=data.quantile(0.99), axis=1)

data = pd.get_dummies(data)

scaler = StandardScaler()
data[data.select_dtypes(include=['float64']).columns] = scaler.fit_transform(data.select_dtypes(include=['float64']))

data = data.drop(data.columns[[1, 2]], axis=1)
X = data.iloc[:,:-3]
y = data.iloc[:, -1]

#print("\nX: ",X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

#print("\nx: ")
#print("\nx:",X_train)
#print(X_train.shape())

from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

model = LinearRegression()

kf = KFold(n_splits=5, shuffle=True)


mse_scores = []
for train_index, test_index in kf.split(X_train):
    # Split the data into training and testing sets for this fold
    X_train_fold, X_test_fold = X_train.iloc[train_index], X_train.iloc[test_index]
    y_train_fold, y_test_fold = y_train.iloc[train_index], y_train.iloc[test_index]
    # Train the model on the training set and test it on the testing set
    model.fit(X_train_fold, y_train_fold)
    y_pred = model.predict(X_test_fold)
    mse = mean_squared_error(y_test_fold, y_pred)
    mse_scores.append(mse)
   
# Compute the average mean squared error across all folds
avg_mse = sum(mse_scores) / len(mse_scores)
print("\navgmse: ",avg_mse)

Y_train=np.unique(y_train_fold)
#y_train=y_train.reshape(-1,1)
print("\ny_train: ",y_train)
print("\ny_train shape: ",y_train.shape)

#neural Network
input_layer_size = X_train.shape[1]
print("\ninput_layer_shape: ",X_train.shape[1])
import numpy as np

class NeuralNetwork:
    def __init__(self,input_layer_size,hidden_layer_size,output_layer_size,X):
        self.input_layer_size = input_layer_size
        self.hidden_layer_size = hidden_layer_size
        self.output_layer_size = output_layer_size
       
        # Initialize the weights with random values
        self.W1 = np.random.randn(input_layer_size,hidden_layer_size)
        self.W2 = np.random.randn(hidden_layer_size,output_layer_size)
        print("\nW1: ",self.W1)
        print("\nw1_size: ",self.W1.shape)
        print("\nW2: ",self.W2)
        print("\nw2_size: ",self.W2.shape)
        # Initialize the biases with zeros
        self.b1 = np.random.randn(len(X),hidden_layer_size)#x_train
        self.b2 = np.random.randn(len(X),output_layer_size)#x_train
        print("\nB1:",self.b1)
        print("\nB2:",self.b2)
   
    def sigmoid(self, x):
        x = np.array(x, dtype=float)  # Ensure x is a NumPy array of floats
        if np.isnan(x).any():
            raise ValueError("Input contains NaN values.")
        return 1 / (1 + np.exp(-x))


       
    def forward_propagation(self, X):
        self.Z1 =np.dot(X,self.W1) + self.b1
        #print("\nZ1: ",self.Z1)
        #print("\nz1size: ",self.Z1.shape)
        self.A1 = self.sigmoid(self.Z1)
        #print("\nA1: ",self.A1)
        #print("\nA1size: ",self.A1.shape)
        self.Z2 = np.dot(self.A1,self.W2) + self.b2
        #print("\nZ2: ",self.Z2)
        #print("\nZ2size: ",self.Z2.shape)
        self.A2 = self.sigmoid(self.Z2)
        #print("\nA2: ",self.A2)
        #print("\n A2 shape",self.A2.shape)
        return self.A2
   
    def generate_wt(self,x, y):
        l =[]
        for i in range(len(x) * len(y)):
            l.append(np.random.randn())
        return(np.array(l).reshape(len(x),len(y)))

    def backward_propagation(self, X, Y, output,learning_rate):
        #print("\n Output",output)
        #print("\noutput: ",output.shape)
        Y=np.array(Y)
        Y=Y.reshape(-1,1)
        #print("\ny_shape: ",Y.shape)
        dZ2 = output - Y
        #print("\ndz2 ",dZ2.shape)
        #print(dZ2)
        #print("\n w2: ",self.W2)    
        dW2 = np.dot(self.A1.T,dZ2)
       
        #print("\ndw2: ",dW2)
        db2 = np.sum(dZ2, axis=1, keepdims=True)
       
        #print("\nw2 size:",self.W2.shape)
        #print("\ndw2 size:",dZ2.shape)
        dZ1=np.multiply((self.W2.dot((dZ2.T))).T,(np.multiply(self.A1, 1-self.A1)))
        #print('\ndz1:',dZ1)
        #dZ1 = np.dot(self.W2.T, dZ2) * (self.A1 * (1 - self.A1))
        dW1 = np.dot(X.T,dZ1)
        db1 = np.sum(dZ1, axis=1, keepdims=True)
        #print("\ndw1: ",dW1)
        #print("\ndb1: ",db1)
        #print("\ndw2: ",dW2)
        #print("\ndb2: ",db2)
        # Update the weights and biases
        self.W1 = self.W1.astype('float64')
        dW1 = dW1.astype('float64')

        self.W1 -= learning_rate*dW1
        self.b1 -= learning_rate*db1
        self.W2 -= learning_rate*dW2
        self.b2 -= learning_rate*db2
        #return self.W1,self.W2

    #1
   
    def loss(self,y_pred, y_true):
       y_true = y_true.values.reshape(-1, 1)
       #print("\n y_p:",y_pred)
       #print("\n y_t:",y_true)
       y_pred_binary = (y_pred >= 0.5).astype(int)
       y_true_binary = (y_true >= 0.5).astype(int)
       mse = np.mean((y_pred - y_true_binary)**2)
       print(f"\nMSE: {mse}")
       return mse

    def accuracy(self,y_pred,y_true):
       y_true = y_true.values.reshape(-1, 1)
       y_pred_binary = (y_pred >= 0.5).astype(int)
      
       y_true_binary = (y_true >= 0.5).astype(int)
       
       return (y_pred_binary == y_true_binary).mean() * 100
   
    def rmsee(self,y_pred,y_train):
        mse = mean_squared_error(y_train, y_pred)
        rmse = mean_squared_error(y_train, y_pred, squared=False)
        #print(f"MSE: {mse}")
        #print(f"RMSE: {rmse}")
        return rmse
   
    
    def train(self,x, Y,  epoch =10,alpha = 0.01):
        acc =[]
        losss =[]
        rm=[]
        for j in range(epoch):
            out = self.forward_propagation(x)
            self.backward_propagation(x, Y,out,alpha)
            #print("\n out: ",out)
            #print("\n Y:",Y)
            print("epochs:", j + 1, "======== acc:", self.accuracy(out, Y))  
            acc.append(self.accuracy(out,Y))
            losss.append(self.loss(out,Y))
            rm.append(self.rmsee(out,Y))
        #print("\n rm:",rm)
        return(acc, losss,rm)
   
    
    
    def predict(self,x):
        out = self.forward_propagation(x)
        #print("\n out: ",out)
        new_arr=[]
        for i in range(len(out)):
            if(out[i][0]<0.05):
                new_arr.append(0)
            else:
                new_arr.append(1)
        #print("\n new_arr: ",new_arr)
   

# Define your ANN architecture
input_layer_size = X_train.shape[1]
#print("\nils: ",X_train.shape[1])
hidden_layer_size = 10
output_layer_size = 1
#(len(y_train))
#print("\nols: ",output_layer_size)
weights = np.random.rand(input_layer_size*hidden_layer_size + hidden_layer_size*output_layer_size)

def fitness_function(weights):
    
    nn=NeuralNetwork(input_layer_size,hidden_layer_size,output_layer_size,X_train)
    
    return nn
   

    
   

ff=fitness_function(weights)
val=ff.forward_propagation( X_train)

acc,losss,rm=ff.train(X_train,y_train,10,0.01)
ac=acc[0]
# print("\ntrain: ",acc,losss)
# print("\n\n round: ",ff.predict(X_train))
print("rmse: ",rm[len(rm)-1])
print("Accuracy: ",ac)
print("Loss: ",losss[len(losss)-1])



import matplotlib.pyplot as plt1
 
# plotting accuracy
plt1.subplot(1, 3, 1)
plt1.plot(acc)
plt1.ylabel('Accuracy')
plt1.xlabel("Epochs:")
plt1.show()
 

# plotting Loss
plt1.subplot(1, 3, 2)
plt1.plot(losss)
plt1.ylabel('Loss')
plt1.xlabel("Epochs:")
plt1.show()

plt1.subplot(1, 3, 3)
plt1.plot(rm)
plt1.ylabel('RMSE value: ')
plt1.xlabel("Epochs:")
plt1.show()

