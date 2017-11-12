import numpy as np
def kalman_filter(data,Q,R,x0,P0):
    N = data.size
    K = np.zeros([N,1])
    X = np.zeros([N,1])
    P = np.zeros([N,1])
    
    X[0] = x0
    P[0] = P0
    
    for i in range(1,N):
        K[i] = P[i-1]/(P[i-1]+R)
        X[i] = X[i-1] + K[i]*(data[i] - X[i-1])
        P[i] = P[i-1] - K[i]* P[i-1] +Q
    return X


#上文是kalman filter的代码
#下文时test
data = [-59,-60,-55,-56,-56,-56,-57,-57,-59,-61,-57,-57,-57,-57,-57,-58,-57,-61,-57,-61,-59,-61,-60,-60,-59,-57,-56,-58,-58,-57,-57,-57,-57,-57,-60,-58,-61,-60,-60,-60,-57,-57,-57,-57,-58,-57,-58,-57,-58,-57,-58,-61,-58,-61,-62,-61,-61,-57,-57,-57,-57,-58,-57,-58,-57,-58,-61,-61,-60,-60,-58,-57,-57,-57,-57,-58,-58,-58,-58,-60,-61,-60,-57,-57,-57,-57,-57,-58,-58,-57,-57,-57,-60,-57,-60,-60,-59,-60,-57,-56]
data = np.array(data)
result = kalman_filter(data,1e-6,4e-4,-60,1)
import matplotlib.pyplot as plt
l = np.array(range(100))
plt.plot(l,result,'r',l,data,'b')
