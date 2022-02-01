import numpy as np

def C_circle(radius):
    ''' input radius of a circle (unit does not matter, just use your SI brain) 
        output the circumference of the circle

        Parameters:
        -----------
        radius : float
                circle radius

        Returns
        -------
        cir : float
            the cirle's circumference
    '''
    cir = 2*np.pi*radius 

    return cir

#def test.S_circle(radius):
#''' input radius of a circle (unit does not matter, just use your SI brain) 
#    output the circumference of the circle
#    
#    Parameters:
#    -----------
#    radius : float
#            circle radius
#    
#    Returns
#    -------
#    sur : float
#        the cirle's circumference
#'''
#    sur = np.pi*radius**2 #pir^2
#    
#    return sur



