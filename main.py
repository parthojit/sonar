from src.trainingdata import MakeTrainingData

if __name__ == "__main__":
    mtd = MakeTrainingData()
    X,y = mtd.make_all(n_samples=100)
    print(X)