import numpy as np
import random
from matplotlib import pyplot as plt

# Experiment 1

ar_A = []
ar_B = []
ar_C = []
ar_X = []

av_A = []
av_B = []
av_C = []
av_X = []
vr_X = []

# Populate the given arrays.
for i in range(30000):
    a = random.random()
    if (a < 1 / 6):
       a = 1
    elif (a < 2 / 6):
        a = 2
    elif (a < 3 / 6):
        a = 3
    elif (a < 4 / 6):
        a = 4
    elif (a < 5 / 6):
        a = 5
    else:
        a = 6
    
    ar_A.append(a)


    b = random.random()
    if (b < 1/4):
        b = 1
    elif(b < 2/4):
        b = 2
    elif(b < 3/4):
        b = 3
    else:
        b = 4
    
    ar_B.append(b)

    c = random.random()
    if(c < 1/2):
        c = -1
    else:
        c = 1
    ar_C.append(c)

    X = a + (b*c)
    ar_X.append(X)

total_A = 0
for i in range(len(ar_A)):
    total_A += ar_A[i]
    average_A = total_A / (i+1)
    av_A.append(average_A)

total_B = 0
for i in range(len(ar_B)):
    total_B += ar_B[i]
    average_B = total_B / (i+1)
    av_B.append(average_B)

total_C = 0
for i in range(len(ar_C)):
    total_C += ar_C[i]
    average_C = total_C / (i+1)
    av_C.append(average_C)

total_X = 0
for i in range(len(ar_X)):
    total_X += ar_X[i]
    average_X = total_X / (i+1)
    av_X.append(average_X)

total_var_X = 0
for j in range(len(ar_X)):
    if (j==0):
        var_X = 0 #to prevent 0/0
    else:
        total_var_X += (ar_X[j] - av_X[j])**2
        var_X = total_var_X / j
    vr_X.append(var_X)

# Inspect the following plots.
plt.figure()
plt.hist(ar_A,6,range=(1,7),align='left',density=True, rwidth=0.8)
plt.figure()
plt.hist(ar_B,4,range=(1,5),align='left',density=True, rwidth=0.8)
plt.figure()
plt.hist(ar_C,3,range=(-1,2),align='left',density=True, rwidth=0.8)
plt.figure()
plt.hist(ar_X,14,range=(-3,11),align='left',density=True, rwidth=0.8)

# Plot the average and variance values.
av_A_Xvalue = [x for x in range(len(av_A))]
av_B_Xvalue = [x for x in range(len(av_B))]
av_C_Xvalue = [x for x in range(len(av_C))]
av_X_Xvalue = [x for x in range(len(av_X))]
vr_X_Xvalue = [x for x in range(len(vr_X))]


plt.figure()
plt.plot(av_A_Xvalue,av_A)
plt.figure()
plt.plot(av_B_Xvalue,av_B)
plt.figure()
plt.plot(av_C_Xvalue,av_C)
plt.figure()
plt.plot(av_X_Xvalue,av_X)
plt.figure()
plt.plot(vr_X_Xvalue,vr_X)


# Experiment 2

# Part a (Inverse Transform Method)
U = []
Xa = []
av_Xa = []
vr_Xa = []

# Populate the given arrays.
for i in range(30000):
    u = random.random()
    x = u ** (1 / 2)
    U.append(u)
    Xa.append(x)

total_Xa = 0
for i in range(len(Xa)):
    total_Xa += Xa[i]
    average_Xa = total_Xa / (i+1)
    av_Xa.append(average_Xa)

total_var_Xa = 0
for j in range(len(Xa)):
    if ((j==0)):
        var_Xa = 0 #to prevent 0/0
    else:
        total_var_Xa += (Xa[j] - av_Xa[j])**2
        var_Xa = total_var_Xa / j
    vr_Xa.append(var_Xa)

# Inspect the following plots.
plt.figure()
for i in range(len(Xa)):
    plt.plot([Xa[i],U[i]],[1,1.2])
plt.figure()
hU = plt.hist(U,100,alpha=0.5,density=True)
hXa = plt.hist(Xa,100,alpha=0.5,density=True)
plt.figure()
plt.plot(np.cumsum(hU[0]))
plt.plot(np.cumsum(hXa[0]))

# Plot the average and variance values.
av_Xa_Xvalue = [x for x in range(len(av_Xa))]
vr_Xa_Xvalue = [x for x in range(len(vr_Xa))]


plt.figure()
plt.plot(av_Xa_Xvalue,av_Xa)
plt.figure()
plt.plot(vr_Xa_Xvalue,vr_Xa)


# Part b (Rejection Method)
Xb = []
av_Xb = []
vr_Xb = []

# Populate the given arrays.
A = 0
B = 1
C = 2 #f(1) derivative of x^2 = 2x 

for i in range(30000):
    u = random.random()
    v = random.random()
    X1 = A + (B - A) * u
    Y = C * v
    while Y > 2*X1 :
        u = random.random()
        v = random.random()
        X1 = A + (B - A) * u
        Y = C * v
    Xb.append(X1)


total_Xb = 0
for i in range(len(Xb)):
    total_Xb += Xb[i]
    average_Xb = total_Xb / (i+1)
    av_Xb.append(average_Xb)

total_var_Xb = 0
for j in range(len(Xb)):
    if (j==0):
        var_Xb = 0 #to prevent 0/0
    else:
        total_var_Xb += (Xb[j] - av_Xb[j])**2
        var_Xb = total_var_Xb / j
    vr_Xb.append(var_Xb)

# Inspect the following plots.
plt.figure()
hXb = plt.hist(Xb,100,density=True)
plt.figure()
plt.plot(np.cumsum(hXb[0]))

# Plot the average and variance values.
av_Xb_Xvalue = [x for x in range(len(av_Xb))]
vr_Xb_Xvaule = [x for x in range(len(vr_Xb))]


plt.figure()
plt.plot(av_Xb_Xvalue,av_Xb)
plt.figure()
plt.plot(vr_Xb_Xvaule,vr_Xb)

plt.show()
plt.close()