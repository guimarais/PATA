import numpy as np
from DataGenerator import Particle
from DataGenerator import State
class GravPot():
    def __init__(self):
              
        self.G =6.67408e-11;
        
    def  getStatDev(self, p1, t, m1, listOfParticles):
        r = p1[:3]
        vel=p1[3:];
        acc=np.zeros(3);
        for par in listOfParticles:
            accThis = par.Mass*self.G;
            disp = -r+par.CurrentState.r;
            dist = (disp[0]**2+disp[1]**2+disp[2]**2);            
            acc2 = accThis*disp/dist
            acc=acc+acc2
        devState = State(vel, acc)
        
        return devState.statToVec();
   
        
        
