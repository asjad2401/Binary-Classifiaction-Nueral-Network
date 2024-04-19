import numpy as np
import copy
import h5py

#sigmoid function to calculate the sigmoid of a value
def sigmoid(x):
    s= 1 /(1+np.exp(-x))
    return s

#initialize the weights and bias to zeros
def initialize_with_zeros(dim):
    w = np.zeros((dim,1))
    b= 0.0
    return w, b #w is weights and b is bias intialized to arbitrary values i.e 0

#compute cost and gradients
def propagate(w, b, X, Y):

    '''
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of size (num_px * num_px * 3, number of examples)
    Y -- true "label" vector (containing 0, 1 depeding on true values ) of size (1, number of examples)
    '''
    
    m = X.shape[1] #number of examples

    #forward propagation
    #dw and db are the derivatives of cost function with respect to w and b
    #these are calculated using chain rule of partial differentiation
    A = sigmoid((np.dot(w.transpose(),X))+b)
    dZ = A - Y
    dw = (1/m)*np.dot(X,dZ.transpose())
    db = (1/m)*np.sum(dZ)

    #backward propagation
    #cost function is calculated using log likelihood function j = -1/m * sum(ylog(a) + (1-y)log(1-a))
    j = np.dot(Y,np.log(A).transpose()) + np.dot((1-Y),np.log(1-A).transpose())
    cost = (-1/m)*np.sum(j)

    cost = np.squeeze(np.array(cost))
    grads = {"dw": dw,
             "db": db}
    return grads, cost

#optimize the weights and bias using gradient descent
def optimize(w, b, X, Y, num_iterations=2000, learning_rate=0.5, print_cost=False):

    w = copy.deepcopy(w)
    b = copy.deepcopy(b)
    costs = []

    #run the forward and backward propagation for some number of iterations to update gradiend descent
    for i in range(num_iterations):
        #run the propogation
        grads,cost = propagate(w,b,X,Y)
        dw = grads["dw"]
        db = grads["db"]
        #these are values of d weights and d bias for for one loop of grad desc

        #update the weights and bias using learning rate and derivatives. this is gradient descent implemented
        w = w- learning_rate*dw
        b = b - learning_rate*db

        if i % 100 == 0:
            costs.append(cost)
        
            # Print the cost every 100 training iterations
            if print_cost:
                print ("Cost after iteration %i: %f" %(i, cost))
    
    #here the w and b has been learned from data.
    params = {"w": w,
              "b": b}
    
    grads = {"dw": dw,
             "db": db}
    
    return params, grads, costs

#predict the values of Y using learned weights and bias
def predict(w, b, X):
    '''
    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1) as learned earlier
    b -- bias, a scalar as learned earlier
    X -- data of size (num_px * num_px * 3, number of examples) test data
    '''
    #this method will be used to predict after the model has been trained
    m = X.shape[0]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)

    #using the w and b as learned from training data, we predict the values of Y i.e Y' = sigmoid(w.transpose()*X+b)
    A = sigmoid(np.dot(w.transpose(),X)+b)
    Y_prediction = A.round() #rounding the values to 0 or 1
    return Y_prediction

#model function to run the model
def model(X_train, Y_train, X_test, Y_test, num_iterations=2000, learning_rate=0.5, print_cost=False):
    '''
    Arguments:
    X_train -- training set represented by a numpy array of shape (num_px * num_px * 3, m_train)
    Y_train -- training labels represented by a numpy array (vector) of shape (1, m_train)
    X_test -- test set represented by a numpy array of shape (num_px * num_px * 3, m_test)
    Y_test -- test labels represented by a numpy array (vector) of shape (1, m_test)
    num_iterations -- hyperparameter representing the number of iterations to optimize the parameters
    learning_rate -- hyperparameter representing the learning rate used in the update rule of optimize()
    print_cost -- Set to True to print the cost every 100 iterations
    '''

    m = X_train.shape[0]
    w,b = initialize_with_zeros(m)
    params, grads, costs = optimize(w, b, X_train, Y_train, num_iterations, learning_rate, print_cost=False)
    w = params["w"]
    b = params["b"]

    #we run predictions on already known data in order to calculate success of model
    Y_prediction_test = predict(w,b,X_test)
    Y_prediction_train = predict(w,b,X_train)

    if print_cost:
        print("train accuracy:{}%".format(100 - np.mean(np.abs( Y_prediction_train - Y_train)) * 100))
        print("test accuracy:{}%".format(100 - np.mean(np.abs( Y_prediction_test - Y_test)) * 100))

    
    d = {"costs": costs,
         "gradients": grads,
         "Y_prediction_test": Y_prediction_test, 
         "Y_prediction_train" : Y_prediction_train, 
         "w" : w, 
         "b" : b,
         "learning_rate" : learning_rate,
         "num_iterations": num_iterations}
    
    return d

#load the dataset from a hdf5 file into numpy arrays of required shapes
def load_dataset():
    train_dataset = h5py.File('NeuralNetwork/datasets/trainset.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:]) #  train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:]) #  train set labels

    test_dataset = h5py.File('NeuralNetwork/datasets/testset.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:]) #  test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:]) #  test set labels

    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0])) #making it a column vector
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0])) #making it a column vector

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes

#main function to load, standardize and run the model
if __name__ == "__main__":

    train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()

    #flatten the image feature vectors
    train_set_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[0],-1).transpose()
    test_set_x_flatten = test_set_x_orig.reshape(test_set_x_orig.shape[0],-1).transpose()
    #standarize
    train_set_x = train_set_x_flatten / 255.
    test_set_x = test_set_x_flatten / 255.  

    logistic_regression_model = model(train_set_x, train_set_y, test_set_x, test_set_y, num_iterations=2000, learning_rate=0.005, print_cost=True)
    print(logistic_regression_model)

    w = logistic_regression_model["w"]
    b = logistic_regression_model["b"]

    #save the weights and biases into separate files
    np.save('weights.npy', w)
    np.save('bias.npy', b)