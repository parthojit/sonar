from src.sonardata import MakeSonarData
import numpy as np


class MakeTrainingData(object):
    def __init__(self) -> None:
        self.ms = MakeSonarData()

    def make_one(self,sparsity:int):
        S = self.ms.make_scene_array(fish_number=10,loc_radius=1,zero_region=(90,360),sparsity=sparsity,frames=10)
        S_ = self.ms.make_sequence_from_array(S)
        return S_

    def make_all(self,n_samples:int):
        T = self.make_one(sparsity=0.1)
        X = np.zeros(shape=(2*n_samples,np.size(T,1)))
        y = np.zeros(shape=(2*n_samples,1))
        for n in range(0,n_samples):
            X[n,:] = self.make_one(sparsity=0.1)
            y[n] = 0

        for n in range(n_samples,2*n_samples):
            X[n,:] = self.make_one(sparsity=1)
            y[n] = 1
        # print(np.shape(X))
        # print(np.shape(y))
        return X,y

if __name__ == "__main__":
    mtd = MakeTrainingData()
    mtd.make_all(n_samples=100)