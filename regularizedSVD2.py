# Daniel Alabi and Cody Wang

import math
import random

class SvdMatrix:
    def __init__(self, trainfile, nusers, nmovies, r):
        self.M = [[None]*nmovies]*nusers
        self.U = [[1/math.sqrt(r)]*nusers]*r
        self.V = [[1/math.sqrt(r)]*nmovies]*r
        self.r = r
        self.lrate = 0.001
        self.regularizer = 0.015
        self.nusers = nusers
        self.nmovies = nmovies
        self.maxepochs = 120
        self.minimprov = 0.0001

        # fill in utility matrix
        # None for absent
        # rating for present
        f = open(trainfile)
        
        for line in f:
            newline = [int(each) for each in line.split("\t")]
            userid, movieid, rating = newline[0], newline[1], newline[2]
            self.M[userid-1][movieid-1] = rating

    def predict(self, i, j, k, cacheEntry):
        return cacheEntry + rVector[i] * cVector[j]

    # iteratively train each feature on the entire dataset
    # once sufficient progress has been made, move on
    def train(self):
        nusers = self.nusers
        nmovies = self.nmovies

        cache = [[0.0]*nmovies]*nusers

        for k in range(self.r):
            
            for epoch in range(self.maxepochs):
                rmselast = float("inf")
                
                for i in range(nusers):
                    for j in range(nmovies):
                        # ignore empty entries
                        if self.M[i][j] == None: continue
                                                
                        prediction = self.predict(i, j, k, cache[i][j])
                                    
                                               
if __name__ == "__main__":
    f = open("ua.base")

    svd = SvdMatrix("ua.base", 943, 1682, 20)
    svd.train()




