import numpy as np
X = np.array(([2,9],[1,5],[3,6]),dtype=float)
y = np.array(([92],[86],[89]),dtype=float)
X = X/np.amax(X,axis=0)
y = y/100

def sigmoid(X):
    return 1/(1+np.exp(-X))

def derivative_sigmoid(X):
    return X*(1-X)

epoch = 5000
lr = 0.1
i_layer = 2
hi_layer = 3
out_layer = 1

wh = np.random.uniform(size=(i_layer,hi_layer))
bh = np.random.uniform(size=(1,hi_layer))
wout = np.random.uniform(size=(hi_layer,out_layer))
bout = np.random.uniform(size=(1,out_layer))

for i in range(epoch):
    hinp1 = np.dot(X,wh)
    hinp = hinp1 + bh
    hlayer_act = sigmoid(hinp)
    outinp1 = np.dot(hlayer_act,wout)
    outinp = outinp1 + bout
    output  = sigmoid(outinp)
    
    E0 = y - output
    outgrad = derivative_sigmoid(output)
    d_output = E0 * outgrad
    EH = d_output.dot(wout.T)
    
    hidden_grad = derivative_sigmoid(hlayer_act)
    d_hidden = EH * hidden_grad
    
wout+=hlayer_act.T.dot(d_output)*lr
wh+=X.T.dot(d_hidden)*lr

print("Input"+str(X))
print("Actual Output"+str(y))
print("Predicted Output",output)
