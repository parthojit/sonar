import numpy as np
import matplotlib.pyplot as plt


class Sonar(object):
    def __init__(self):
        np.random.seed(None)
        self.figure, self.axes = plt.subplots(1,figsize=(5,5))
        self.axes.set_facecolor('midnightblue')
        self.angle_length = 360
        plt.axvline(x=0,color="white",linestyle="dashed")
        plt.axhline(y=0,color="white",linestyle="dashed")
    
    def plot_circle(self,radius:int,angle:np.array):
        np.random.shuffle(angle)
        x = [radius*np.cos(ang) for ang in angle if ang>0]
        y = [radius*np.sin(ang) for ang in angle if ang>0]
        plt.xlim(-1.1,1.1)
        plt.ylim(-1.1,1.1)
        self.axes.scatter(x,y,color="white",edgecolors="black")
    
    def rand_angle(self,sample_size:int,p:np.array) -> np.array:
        self.angle = np.linspace(0,2*np.pi,self.angle_length)
        list_index = np.random.choice(np.arange(len(self.angle)),size=sample_size,p=p)
        out_angle = np.zeros(len(self.angle))
        for i in list_index:
            out_angle[i] = self.angle[i]
        return out_angle
    
    def make_P(self,thickness:int,offset:int) -> np.array:
        """
        thickness: 1 = sparse, >1 = dense
        offset: 0-359 degrees
        """
        P = np.zeros(self.angle_length)
        P[offset:offset+(self.angle_length//thickness)] = 1
        P = P*1/(np.count_nonzero(P==1))
        return P
    
    def make_angle_matrix(self,sample_size:int, max_steps:int) -> np.array:
        # thickness: 1 = sparse, >1 = dense
        # offset: 0-359 degrees
        U = np.zeros(self.angle_length)
        for _ in range(0,max_steps):
            thickness = np.random.randint(1,100)
            offset = np.random.randint(360)
            P = self.make_P(thickness=thickness,offset=offset)
            angle = s.rand_angle(sample_size=sample_size,p=P)
            U = np.vstack((U,angle))
        U = np.delete(U,0,0)
        return U
    
    # def make_noisy_matrix(self,U:np.array) -> np.array:
    #     N = np.random.normal(0,0.1, np.shape(U))
    #     return U+N

    def plot_angle_matrix(self, U:np.array, resolution:int):
        for i in range(0,len(U)):
            self.plot_circle(radius=i/(10*resolution),angle=U[i])


if __name__ == "__main__":  
    for i in range(0,10):
        s = Sonar()
        U = s.make_angle_matrix(sample_size=1,max_steps=10)
        s.plot_angle_matrix(U=U,resolution=1)
        plt.savefig("./png/img_" + str(i+1+10) + ".png",bbox_inches="tight")
        plt.close()

