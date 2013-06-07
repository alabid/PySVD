# Daniel Alabi and Cody Wang
# ======================================
# SvdMatrix:
# generates matrices U and V such that
# U * V^T closely approximates
# the original matrix (in this case, the utility
# matrix M)
# =======================================


import math
import random
import time



class SvdMatrix:
    """
    trainfile -> name of file to train data against
    nusers -> number of users in dataset
    nmovies -> number of movies in dataset
    r -> rank of approximation (for U and V)
    lrate -> learning rate
    regularizer -> regularizer
    typefile -> 0 if for smaller MovieLens dataset
                1 if for medium or larger MovieLens dataset
    """
    def __init__(self, trainfile, nusers, nmovies, r=10, lrate=0.001, regularizer=0.015, typefile=1):
        self.M = [[None]*nmovies for i in range(nusers)]
        self.Mtest = [[None]*nmovies for i in range(nusers)]
                
        self.nusers = nusers
        self.nmovies = nmovies

        if typefile == 0:
            self.readtrainsmaller(trainfile)
        elif typefile == 1:
            self.readtrainlarger(trainfile)

        # get average rating
        avg = self.averagerating()
        # set initial values in U, V using square root
        # of average/rank
        initval = math.sqrt(avg/r)
        
        # U matrix
        self.U = [[initval]*r for i in range(nusers)]
        # V matrix -- easier to store and compute than V^T
        self.V = [[initval]*r for i in range(nmovies)]

        self.r = r
        self.lrate = lrate
        self.regularizer = regularizer
        self.minimprov = 0.001
        self.maxepochs = 30            

    """
    Returns the dot product of v1 and v2
    """
    def dotproduct(self, v1, v2):
        return sum([v1[i]*v2[i] for i in range(len(v1))])

    """
    Returns the estimated rating corresponding to userid for movieid
    Ensures returns rating is in range [1,5]
    """
    def calcrating(self, uid, mid):
        p = self.dotproduct(self.U[uid], self.V[mid])
        if p > 5:
            p = 5
        elif p < 1:
            p = 1
        return p

    """
    Returns the average rating of the entire dataset
    """
    def averagerating(self):
        avg = 0
        n = 0
        for i in range(self.nusers):
            for j in range(self.nmovies):
                if self.M[i][j] == None: continue
                avg += self.M[i][j]
                n += 1
        return float(avg)/n

    """
    Predicts the estimated rating for user with id i
    for movie with id j
    """
    def predict(self, i, j):
        return self.calcrating(i, j)

    """
    Trains the kth column in U and the kth row in
    V^T
    See docs for more details.
    """
    def train(self, k):
        sse = 0.0
        n = 0
        for i in range(self.nusers):
            for j in range(self.nmovies):
                if self.M[i][j] == None: continue
                err = self.M[i][j] - self.predict(i, j)

                sse += err**2
                n += 1

                uTemp = self.U[i][k]
                vTemp = self.V[j][k]

                self.U[i][k] += self.lrate * (err*vTemp - self.regularizer*uTemp)
                self.V[j][k] += self.lrate * (err*uTemp - self.regularizer*vTemp)
        return math.sqrt(sse/n)

    """
    Trains the entire U matrix and the entire V (and V^T) matrix
    """
    def trainratings(self):        
        # stub -- initial train error
        oldtrainerr = 1000000.0
       
        for k in range(self.r):
            for epoch in range(self.maxepochs):
                trainerr = self.train(k)
                
                # check if train error is still changing
                if abs(oldtrainerr-trainerr) < self.minimprov:
                    break
                oldtrainerr = trainerr
                print "epoch=", epoch, "; trainerr=", trainerr
                
    """
    Calculates the RMSE using between arr
    and the estimated values in (U * V^T)
    """
    def calcrmse(self, arr):
        nusers = self.nusers
        nmovies = self.nmovies
        sse = 0.0
        total = 0
        for i in range(nusers):
            for j in range(nmovies):
                if arr[i][j] == None: continue
                sse += (arr[i][j] - self.calcrating(i, j))**2
                total += 1
        return math.sqrt(sse/total)

    """
    Read in the ratings from fname and put in arr
    Use splitter as delimiter in fname
    """
    def readinratings(self, fname, arr, splitter="\t"):
        f = open(fname)

        for line in f:
            newline = [int(each) for each in line.split(splitter)]
            userid, movieid, rating = newline[0], newline[1], newline[2]
            arr[userid-1][movieid-1] = rating    
        
    """
    Read in the smaller train dataset
    """
    def readtrainsmaller(self, fname):
        self.readinratings(fname, self.M, splitter="\t")
        
    """
    Read in the large train dataset
    """
    def readtrainlarger(self, fname):
        self.readinratings(fname, self.M, splitter="::")
        
    """
    Read in the smaller test dataset
    """
    def readtestsmaller(self, fname):
        self.readinratings(fname, self.Mtest, splitter="\t")
                
    """
    Read in the larger test dataset
    """
    def readtestlarger(self, fname):
        self.readinratings(fname, self.Mtest, splitter="::")

                           
