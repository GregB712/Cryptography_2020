import numpy as np
import math

def create_table(elements):
    return np.reshape(elements, (int(math.sqrt(len(elements))),int(math.sqrt(len(elements)))))

def entropy(table):
    # Calculate pX and pY
    pX = [sum(i) for i in zip(*table)] #add columns
    pY =[sum(i) for i in table] #add rows
    
    # Calculate HX and HY
    HX = -sum([x*math.log(x,2) for x in pX])
    HY = -sum([x*math.log(x,2) for x in pY])
    
    return HX, HY, pX, pY

def mutual_entropy(table):
    temp = np.reshape(table, (len(table)**2)) # flatten table (easier to iterate)
    temp = [i for i in temp if i != 0] # remove 0 from list (log(0) is undefined)
    
    HX_Y = -sum([x*math.log(x,2) for x in temp])
    
    return HX_Y

def committed_entropy(table):
    HX, HY, pX, pY = entropy(table)
    
    temp= []
    for i in range(len(table)):
        for j in range(len(table)):
            temp.append(table[j][i] / pX[i])
    
    temp = [i if i != 0 else 1 for i in temp] # replace 0 from list (log(0) is undefined) 
                                              #log(1) = 0 so it will not affect our results
    
    pY_X = create_table(temp)
    
    HY_X_table = []
    for row in pY_X:
        HY_X_table.append(-sum([x*math.log(x,2) for x in row]))
    
    HY_X = sum([pX[i] * HY_X_table[i] for i in range(len(pX))])
    
    # Mutual Information: I(X,Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)
    HX_Y = -(HY - HY_X - HX)
        
    return HX_Y, HY_X

def mutual_information(table):
    HX, _, _, _ = entropy(table)
    HX_Y, _ = committed_entropy(table)
    
    IX_Y = HX - HX_Y
    
    return IX_Y

elements = [1/7,1/7,1/7,0,1/7,1/7,2/7,0,0]
table = create_table(elements)


HX, HY, _, _ = entropy(table)
print("Entropy: ")
print(HX, HY)
print()
print("Mutual Entropy: ")
print(mutual_entropy(table))
print()
print("Committed Entropy: ")
print(committed_entropy(table))
print()
print("Mutual Information: ")
print(mutual_information(table))