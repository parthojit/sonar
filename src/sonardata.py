import numpy as np
import matplotlib.pyplot as plt


class MakeSonarData(object):
    def __init__(self):
        np.random.seed(None)
        self.figure, self.axes = plt.subplots(1,figsize=(5,5))
        self.axes.set_facecolor('midnightblue')
        plt.axvline(x=0,color="white",linestyle="dashed")
        plt.axhline(y=0,color="white",linestyle="dashed")
        self.clr = {
            0: 'red',
            1: 'orange',
            2: 'yellow',
            3: 'lightgreen',
            4: 'green',
            5: 'blue',
            6: 'darkblue',
            7: 'indigo',
            8: 'darkviolet',
            9: 'black'
        }
    
    def plot_fish_loc(self,radius:int,angle:np.array,clr_index:int):
        x = radius*np.cos(angle)
        y = radius*np.sin(angle)
        plt.xlim(-1.1,1.1)
        plt.ylim(-1.1,1.1)
        self.axes.scatter(x,y,color=self.clr[clr_index],edgecolors="black")

    def make_scene(self,fish_number:int,loc_radius:float,zero_region:tuple,sparsity:float,frames:int):
        angle_choice = np.linspace(0,2*np.pi,360)
        P = np.linspace(0,1,360) # probability of angle
        P[zero_region[0]:zero_region[1]] = 0 # add bias here
        P = P/np.sum(P) # normalize to make P sum to 1
        for i in range(0,frames):
            loc_angle = np.random.choice(angle_choice,1,p=P)
            for _ in range(0,fish_number):
                self.plot_fish_loc(radius=loc_radius-abs(np.random.normal(0,sparsity))-0.1*i,angle=(loc_angle+np.random.normal(0,sparsity))[0],clr_index=i)

    def make_scene_array(self,fish_number:int,loc_radius:float,zero_region:tuple,sparsity:float,frames:int) ->np.array:
        angle_choice = np.linspace(0,2*np.pi,360)
        P = np.linspace(0,1,360) # probability of angle
        P[zero_region[0]:zero_region[1]] = 0 # add bias here
        P = P/np.sum(P) # normalize to make P sum to 1
        S = np.zeros((frames,fish_number))
        for i in range(0,frames):
            loc_angle = np.random.choice(angle_choice,1,p=P)
            for j in range(0,fish_number):
                r = loc_radius-abs(np.random.normal(0,sparsity))-0.1*i
                theta = (loc_angle+np.random.normal(0,sparsity))[0]*r
                S[i,j] = theta
        return S

    def make_sequence_from_array(self,S):
        S_ = np.zeros(shape=(1,np.size(S,0)*np.size(S,1)))
        for i in range(0,len(S)):
            S_[0,i*(len(S[i,:])):(i+1)*len(S[i,:])] = S[i,:]
        return S_
        
if __name__ == "__main__":  
    # S = ms.make_scene_array(fish_number=10,loc_radius=1,zero_region=(90,360),sparsity=0.1,frames=10)
    # S_ = ms.make_sequence_from_array(S)
    for i in range(0,10):
        ms = MakeSonarData()
        ms.make_scene(fish_number=10,loc_radius=1,zero_region=(90,360),sparsity=1,frames=10)
        plt.savefig("./png/"+str(i+1)+".png")
        plt.close()