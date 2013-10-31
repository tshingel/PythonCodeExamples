# function implements one-vs-all logistic regression
# to recognize hand-written digits 
# the system is trained on data in ex3data1.mat file  

import numpy as np
import scipy.optimize
import scipy.io

# sigmoid function
def sigmoid(mX, vBeta):
    return((np.exp(np.dot(mX, vBeta))/(1.0 + np.exp(np.dot(mX, vBeta)))))

# cost function
def lrCostFunction(vBeta, mX, vY, lmbda):
    m = vY.shape[0]
    unregJ = -1.0/m * (np.sum(vY*np.log(sigmoid(mX, vBeta)) + (1-vY)*(np.log(1-sigmoid(mX, vBeta)))))      
    J = unregJ  + lmbda/(2 * m) * np.dot(vBeta[1:], vBeta[1:]) 
    return(J)

# gradient of the cost function 
def likelihoodGrad(vBeta, mX, vY, lmbda):
    m = vY.shape[0]
    theta = np.empty_like(vBeta)
    theta[:] = vBeta
    theta[0] = 0.0
    grad = 1.0/m * np.dot(mX.T, (sigmoid(mX, vBeta) - vY)) + lmbda/m * theta    
    return(grad)

# Trains num_labels logisitc regression classifiers and returns each of these classifiers
# in a matrix all_vBeta, where the i-th row of all_vBeta corresponds to the classifier for label i
def onevsAll(mX, vY, num_labels, lmbda):
    all_vBeta = np.empty([num_labels, mX.shape[1]])
    for c in range(num_labels):
        x0 = np.zeros(mX.shape[1])
        optimBeta = scipy.optimize.fmin_bfgs(lrCostFunction, x0, fprime = likelihoodGrad, 
                                           args = (mX, np.array(vY == c,  dtype=int), lmbda), gtol = 1e-5)
        all_vBeta[c, :] = optimBeta
    return(all_vBeta)

# Predicts labels using learned logistic regression parameters all_vBeta
def predict(all_vBeta, mX):
    prod = np.dot(mX, all_vBeta.T)
    p = np.argmax(prod, axis = 1)
    return(p)

def main():
       
    # data set is pixel data (grey scale) for hand-written digits  
    mat = scipy.io.loadmat('ex3data1.mat')
    
    # regularization parameter 
    lmbda = 1.0
    # number of labels to classify 
    num_labels = 10

    vY = mat['y']

    for ind in range(len(vY)):
        if vY[ind] == 10:
            vY[ind] = 0 

    m = vY.shape[0]
    vY = vY.reshape(m)
    mX = mat['X']
    
    # add a column of 1s to matrix mX
    intercept = np.ones(mX.shape[0]).reshape(mX.shape[0], 1)
    mX = np.concatenate((intercept, mX), axis = 1) 
 
    all_vBeta = onevsAll(mX, vY, num_labels, lmbda)
    pred = predict(all_vBeta, mX)
    
    # compute the accuracy of the trained classifier on the training data
    score = np.mean(np.array(pred == vY, dtype=int))

    print("Accuracy of the trained classifier on the training data set is:  ", score) 
            
if __name__ == '__main__':
    main()                        