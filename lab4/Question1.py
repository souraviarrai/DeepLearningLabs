import numpy as np
def activation(y): 
    if y <= 0:
        return 0 
    else:
        return 1 #AND Gate
def and_gate(x1,x2,x3): 
    x=np.array([x1,x2,x3])
    w=np.array([0.5,0.5,0.5]) 
    b=-1
    
    y=np.sum(w*x)+ b 
    return activation(y)
def or_gate(x1,x2,x3): 
    x=np.array([x1,x2,x3]) 
    w=np.array([0.5,0.5,0.5]) 
    b=-0.2
    y=np.sum(w*x)+ b 
    return activation(y)


arrays=[ [0,0,0],[0,0,1],[0,1,1],[1,1,1],[1,0,0],[1,1,0],[0,1,0],[1,0,1]
]

print("AND GATE") 
for x1,x2,x3 in arrays:
    print('input: ',x1,x2,x3,'output' , and_gate(x1,x2,x3))
print("") 
print("") 
print("")
print("")
print("OR GATE")
for x1,x2,x3 in arrays:
    print('input: ',x1,x2,x3,'output' , or_gate(x1,x2,x3))