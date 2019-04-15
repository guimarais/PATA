import numpy as np
from scipy.integrate import  odeint
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
class State:    
    """
    A class representing a state - [x,y,z,px,py,px] - by its position and
    momentum components
    Attributes
    ----------
    self.r : np.array, size == 3
        the r - position - vector associated with this state
    self.p : np.array, size == 3
        the p - momentum - vector associated with this state
    """
    
    def __init__(self, r_=np.zeros(3), p_=np.zeros(3)):
        """
        The constructor for the State class        
        Parameters
        -----------
        r_: numpy.array, size == 3 -- default numpy.zeros(3)
            r vector ([x,y,z])
        p_: numpy.array, size == 3 -- default numpy.zeros(3)
            p vector ([px, py, pz])
        
        Example
        -----------
        pos = numpy.array([1.,1.,1.]) # a particle in x=1., y=1., z=1.
        momentum = numpy.array([0.,0.,0.]) # the particle is stoped
        st1 = State(pos,momentum)
        """
        self.r=r_
        self.p=p_
        
    def vetToState(self, stateVector):
        """
        Updates the current state object by the information within a state vector
        Parameters
        -----------
        stateVector : numpy.array, size == 6
            The state vector ([x,y,z,px,py,pz]) used to update the current state
        
        Example
        -----------
        st1 = State()  # initializes with the position and momentum equal to zero
        st1.vetToState([1.,1.,1.,0.,0.,0.])
        pos = st1.
        momentum = numpy.array([0.,0.,0.]) # the particle is stoped
        st1 = State(pos,momentum)
        st1.statToVec()
        # array([1.,1.,1.,0.,0.,0.])
        """
        if(stateVector.__class__.__name__=='ndarray' and stateVector.size==6):
            self.r = stateVector[:3]
            self.p = stateVector[3:]
            
    def statToVec(self):
        """
        Converts the current state to a state vector
        Returns
        -----------
        out : numpy.array, size == 6
            The state vector ([x,y,z,px,py,pz]) created by concatenating the 
            position and the momentum vectors
        
        Example
        -----------
        pos = numpy.array([1.,1.,1.]) # a particle in x=1., y=1., z=1.
        momentum = numpy.array([0.,0.,0.]) # the particle is stoped
        st1 = State(pos,momentum)
        st1.statToVec()
        # array([1.,1.,1.,0.,0.,0.])
        """
        newVector =np.concatenate((self.r, self.p), axis=0)        
        return newVector
    
    def 
    
        
    
    
class Particle:
    
    def __init__(self, state = State(), mass = 1):
        self.CurrentState = state;
        self.Mass = mass;
        self.Trajectory=[self.CurrentState];
        
    def SetTrajectory(self, trajectory):
        self.Trajectory=trajectory;
    
    def AddPointTrajectory(self, state):
        self.CurrentState= State(state[:3], state[3:])
        self.Trajectory.append(State(state[:3], state[3:]))
        
    
    def GetX(self):
        x = []
        for state in self.Trajectory:
            x.append(state.r[0])
        return np.array(x)
        
    def GetY(self):
        y = []
        for state in self.Trajectory:
            y.append(state.r[1])
        return np.array(y)
    
    def GetZ(self):
        z = []
        for state in self.Trajectory:
            z.append(state.r[2])
        return np.array(z)
     
    
    def SetInitialCondition(self, state):
        self.CurrentState=state;
        self.Trajectory = [self.CurrentState]
       #self.Potential = GravPot();
    
class DataGenerator:
    
    def GenerateInitialCondition(self, medianPos, covPos, medianMoment, covMoment):
        randomPosition1= np.random.multivariate_normal(medianPos, covPos, self.NumberParticles);
        randomMomento1= np.random.multivariate_normal(medianMoment, covMoment, self.NumberParticles);
        randomPosition2= np.random.multivariate_normal(medianPos, covPos, self.NumberParticles);
        randomMomento2= np.random.multivariate_normal(medianMoment, covMoment, self.NumberParticles);
        self.data1 = [];
        self.data2 = [];
        for i in range(self.NumberParticles):
            st1 = State(randomPosition1[i],randomMomento1[i] )
            part1 = Particle(st1, 10e18)
            st2 = State(randomPosition2[i],randomMomento2[i] )
            part2 = Particle(st2, 10e18)
            self.data1.append(part1)
            self.data2.append(part2)
        self.data1 = np.array(self.data1)
        self.data2 = np.array(self.data2)
    def PlotData(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        for i in range(self.NumberParticles):           
            ax.scatter(self.data1[i].CurrentState.r[0], self.data1[i].CurrentState.r[1], self.data1[i].CurrentState.r[2])
            ax.plot(self.data1[i].GetX(), self.data1[i].GetY(), self.data1[i].GetZ())
            ax.scatter(self.data2[i].CurrentState.r[0], self.data2[i].CurrentState.r[1], self.data2[i].CurrentState.r[2])
            ax.plot(self.data2[i].GetX(), self.data2[i].GetY(), self.data2[i].GetZ())
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        plt.show()
        
    def __init__(self, numberSamples):
        self.NumberParticles=numberSamples
        self.data1 =  np.array([]);
        self.data2 =  np.array([]);
        
    def SetPotential(self, potential):
        self.Potential = potential;
    def Propagate(self, t):
        for countTime in range(len(t)-1):
            timeInter= [t[countTime], t[countTime+1]];
            for i in range(self.NumberParticles):                
                y2 = odeint(self.Potential.getStatDev,self.data1[i].CurrentState.statToVec(), timeInter,args = (self.data1[i].Mass,  [self.data2[i] ], ))
                y3 = odeint(self.Potential.getStatDev,self.data2[i] .CurrentState.statToVec(), timeInter, args=(self.data2[i].Mass,  [self.data1[i] ], ))
                self.data1[i].AddPointTrajectory(y2[1])
                self.data2[i].AddPointTrajectory(y3[1])

