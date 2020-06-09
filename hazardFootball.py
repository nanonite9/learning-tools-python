# a function that returns a triple with the drag force, 
# gravity force, and the ratio between the two 
# (drag force: gravity force)

def hazardFootball(V):
    m = 0.43                #given mass of the object
    g = 9.81                #acceleration 
    FG = m*g                #force of gravity
    p = 1.2                 #given density
    a = 0.11                #given radius of object
    A = 3.14*(a**2)         #cross-sectional area (normal to the velocity direction), assume pi=3.14
    C = 0.2                 #drag coefficient
    D = 0.5*C*p*A*(V**2)    #drag force
    R = D/FG                #ratio between drag force and force of gravity
    return (D, FG, R)

'''
Test Case:
>>> hazardFootball(5)
(0.113982, 4.2183, 0.027020837778251903)
'''
