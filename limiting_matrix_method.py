import numpy as np
from fractions import Fraction
def solve(m):

    a=np.array(m)
    n=len(a)
    terminal=[]
    non_terminal=[]
    summ=[]
    for x in range(len(a)):
        summ.append(sum(a[x]))
        if not summ[-1]:
            terminal.append(x)
        else:   
            non_terminal.append(x)
    
    
    R=[[a[x][y]/summ[x] for y in terminal ] for x in non_terminal]
    Q=[[a[x][y]/summ[x] for y in non_terminal ] for x in non_terminal]
    R=np.array(R)
    Q=np.array(Q)
    
    Q=np.eye(len(Q))-Q
    f=INV(Q,len(Q))

    y=np.dot(f,R)
    num,den=[],[]
    lcd=1
    for x in y[0]:
        fr = Fraction(x).limit_denominator()
        num.append(fr.numerator)
        den.append(fr.denominator)
        lcd=np.lcm(lcd,den[-1])
    final=[num[i]*int(lcd/den[i]) for i in range(len(num))]
    final.append(lcd)
    return final    
def INV(a,n):
    
    inv=[[0 for x in range(n)] for b in range(n)]
    for x in range(n):
        inv[x][x]=1
        
    for x in range(n):
        for y in range(x):
            
            if a[x][y]!=0:
                temp=a[x][y]
                for z in range(n):
                    a[x][z]=-(a[y][z]*temp-a[x][z])
                    inv[x][z]=-(inv[y][z]*temp-inv[x][z])

        if a[x][x]!=1:
            temp=a[x][x]
            for y in range(n):
                a[x][y]=a[x][y]/temp
                inv[x][y]=inv[x][y]/temp

        
    for x in range(n):
        for y in range(x+1,n):
            if a[x][y]!=0:
                temp=a[x][y]

                for z in range(n):
                    a[x][z]=-(a[y][z]*temp-a[x][z])
                    inv[x][z]=-(inv[y][z]*temp-inv[x][z])

    return  inv 
if __name__ == "__main__":
    a=[

    [0,1,0,0,0,1], # s0, the initial state, goes to s1 and s5 with equal probability

    [4,0,0,3,2,0], # s1 can become s0, s3, or s4, but with different probabilities

    [0,0,0,0,0,0], # s2 is terminal, and unreachable (never observed in practice)

    [0,0,0,0,0,0], # s3 is terminal

    [0,0,0,0,0,0], # s4 is terminal

    [0,0,0,0,0,0], # s5 is terminal

    ]
    # 4 terminal states
    print(solve(a))
    #output : [0, 3, 2, 9, 14]
    # 
    # output indexes from 0 to -2 are numerators of probability of each terminal states and index -1 is common denominator
    
    
