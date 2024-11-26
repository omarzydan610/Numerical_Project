import numpy as np

def gaussScale(system, n):

    system = np.array(system, dtype=float)

    A = system[:, :-1]  
    b = system[:, -1]   
    A = np.array(A, dtype=float)  
    b = np.array(b, dtype=float)

    scale = np.max(np.abs(A), axis=1)

    
    for k in range(n - 1):                                     # Forward Elimination
        pivot_row = np.argmax(np.abs(system[k:n, k]) / scale[k:n]) + k
        if pivot_row != k:
            system[[k, pivot_row]] = system[[pivot_row, k]]     # Swap rows
            scale[[k, pivot_row]] = scale[[pivot_row, k]]       # Swap scaling factors

        
        for i in range(k + 1, n):
            factor = system[i, k] / system[k, k]
            system[i, k:] -= factor * system[k, k:]

   
    x = np.zeros(n)                                              # Back Substitution
    for i in range(n - 1, -1, -1):
        x[i] = (system[i, -1] - np.dot(system[i, i + 1:n], x[i + 1:n])) / system[i, i]

    return x


def jordanScale(system, n):

    system = np.array(system, dtype=float)

    A = system[:, :-1]  
    b = system[:, -1]   
    A = np.array(A, dtype=float)  
    b = np.array(b, dtype=float)

    scale = np.max(np.abs(A), axis=1)

    
    for k in range(n - 1):                                     # Forward Elimination
        pivot_row = np.argmax(np.abs(system[k:n, k]) / scale[k:n]) + k
        if pivot_row != k:
            system[[k, pivot_row]] = system[[pivot_row, k]]     # Swap rows
            scale[[k, pivot_row]] = scale[[pivot_row, k]]       # Swap scaling factors

        
        for i in range(k + 1, n):
            factor = system[i, k] / system[k, k]
            system[i, k:] -= factor * system[k, k:]

    
    for i in range(n-1, -1, -1):                                        #backward elimination
            for j in range(i-1, -1, -1):
              factor = system[j][i]/system[i][i]
              system[j][i] -= system[i][i]*factor
              system[j][n] -= system[i][n]*factor


    x = np.zeros(n)     
    for i in range(n):
        x[i] = system[i][n]/system[i][i]


    return x



