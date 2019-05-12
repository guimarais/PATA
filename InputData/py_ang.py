import numpy as np

def py_ang(v1, v2):
    """Returns the angle in radians between vectors 'v1' and 'v2'    
    Parameters
    -----------
    v1: ndarray of floats
        First input vector
    v2: ndarray of floats
        Second input vector. Must be the same dimension as 'v1'        
    
    Returns
    -----------
    angle: float
        The angle between v1 and v2    
    """
    cosang = np.dot(v1, v2)
    sinang = np.linalg.norm(np.cross(v1, v2))
    angle = np.arctan2(sinang, cosang) 
    return angle

def py_ang_deg(v1, v2):
    """Returns the angle in degrees between vectors 'v1' and 'v2'    
    Parameters
    -----------
    v1: ndarray of floats
        First input vector
    v2: ndarray of floats
        Second input vector. Must be the same dimension as 'v1'        
    
    Returns
    -----------
    angle: float
        The angle between v1 and v2, in degrees
    """
    angle = py_ang(v1, v2)
    return angle*180.0/np.pi


