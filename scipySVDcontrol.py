# Daniel Alabi and Cody Wang

import math
from scipy.linalg import *
import numpy as np
import time

np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)

class SvdMatrix:
    def __init__(self, trainfile, nusers, nmovies):
        self.M = [[None]*nmovies for i in range(nusers)]
        self.Mtest = [[None]*nmovies for i in range(nusers)]
        self.Ahat = None

        self.U = None
        self.S = None
        self.Vt = None
        self.nusers = nusers
        self.nmovies = nmovies

        # fill in utility matrix
        # rating for present
        # average for absent
        f = open(trainfile)
        for line in f:
            newline = line.split("\t")
            userid, movieid, rating = int(newline[0]), int(newline[1]), int(newline[2])
            self.M[userid-1][movieid-1] = rating
        for userid in range(nusers):
            avg = 0.0
            nm = 0
            missmovies = []
            for movieid in range(nmovies):
                if self.M[userid][movieid] == None: 
                    missmovies.append(movieid)
                    continue
                avg += self.M[userid][movieid] 
                nm += 1
            avg = float(avg)/nm
            for movieid in missmovies:
                self.M[userid][movieid] = avg
            
        self.M = np.matrix(self.M)

    def test(self, fname):
        nusers = self.nusers
        nmovies = self.nmovies

        f = open(fname)

        for line in f:
            newline = [int(each) for each in line.split("\t")]
            userid, movieid, rating = newline[0], newline[1], newline[2]
            self.Mtest[userid-1][movieid-1] = rating             

    def train(self):
        (U, Sd, Vt) = svd(self.M, False)
        
        # remove 20% of energy of Sd
        energy = np.sum(Sd)
        e80 = energy * 0.8
        e = 0
        c = 0
        while e < e80:
            e += Sd[c]
            c += 1

        Uhat =  np.matrix(np.copy(U)[:, 0:c])
        Sdhat = np.copy(Sd)[0:c]
        Vthat = np.matrix(np.copy(Vt)[0:c, :])
        
        self.Ahat = Uhat * np.diag(Sdhat) * Vthat        
    

    def calcrmsetest(self, arr):
        nusers = self.nusers
        nmovies = self.nmovies
        sse = 0.0
        total = 0
        for i in range(nusers):
            for j in range(nmovies):
                if arr[i][j] == None: continue
                total += 1
                sse += (arr[i][j] - self.Ahat[i, j])**2
        return math.sqrt(sse/total)

    def calcrmsetrain(self):
        nusers = self.nusers
        nmovies = self.nmovies
        sse = 0.0
        total = 0
        for i in range(nusers):
            for j in range(nmovies):
                total += 1
                sse += (self.M[i, j] - self.Ahat[i, j])**2
        return math.sqrt(sse/total)
                                               
if __name__ == "__main__":
    init = time.time()
    svdM = SvdMatrix("ua.base", 943, 1682)
    svdM.train()
    print "rmse of trainset: ", svdM.calcrmsetrain()
    svdM.test("ua.test")
    print "rmse of testset: ", svdM.calcrmsetest(svdM.Mtest)
    print "time used: ", time.time()-init



