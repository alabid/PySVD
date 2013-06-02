# Daniel Alabi and Cody Wang

import math
import random
import time

class SvdMatrix:
    def __init__(self, trainfile, nusers, nmovies, r):
        self.M = [[None]*nmovies for i in range(nusers)]
        self.Mtest = [[None]*nmovies for i in range(nusers)]

        self.Up = None
        self.Vp = None
        self.r = r
        self.lrate = 0.001
        self.regularizer = 0.015
        self.nusers = nusers
        self.nmovies = nmovies

        # fill in utility matrix
        # None for absent
        # rating for present
        f = open(trainfile)
        
        for line in f:
            newline = [int(each) for each in line.split("\t")]
            userid, movieid, rating = newline[0], newline[1], newline[2]
            self.M[userid-1][movieid-1] = rating
            
    def predict(self, i, j, rVector, cVector, cacheEntry):
        p = cacheEntry + rVector[i] * cVector[j]
        if p > 5: 
            p = 5
        elif p < 1:
            p = 1
        return p

    def relDiff(self, x, y):
        return abs(x-y)/(abs(x)+abs(y))

    def train(self, eps, rmseimprov, maxepoch=1000):
        nusers = self.nusers
        nmovies = self.nmovies
        # number of entries in matrix
        nEntries = nusers * nmovies

        cache = [[0.0]*nmovies]*nusers

        rVectors = [None]*self.r
        cVectors = [None]*self.r

        for k in range(self.r):
            rVector = [1/math.sqrt(self.r)]*nusers
            cVector = [1/math.sqrt(self.r)]*nmovies

            rmselast = float("inf") # stores last rmse
            for epoch in range(maxepoch):
                sse = 0.0
                for i in range(nusers):
                    for j in range(nmovies):
                        # ignore empty entries
                        if self.M[i][j] == None: continue                        

                        prediction = self.predict(i, j, rVector, cVector, cache[i][j])
                        error = self.M[i][j] - prediction
                        sse += error * error
                        
                        # get current row, column
                        cRow = rVector[i]
                        cColumn = cVector[j]

                        rVector[i] += self.lrate * (error * cColumn - self.regularizer * cRow)
                        cVector[j] += self.lrate * (error * cRow - self.regularizer * cColumn)

                rmse = math.sqrt(sse/nEntries)
                print "epoch=", epoch, "; rmse=", rmse, "; relDiff=", self.relDiff(rmse, rmselast)
                if self.relDiff(rmse, rmselast) < eps or rmse < rmseimprov:
                    print "Converged in epoch=", epoch, "; rmse=", rmse, \
                        "; relative difference=", self.relDiff(rmse, rmselast)
                    break
                rmselast = rmse
            print "order k=", k, "; rmse=", rmselast
            rVectors[k] = rVector
            cVectors[k] = cVector

            for i in range(nusers):
                for j in range(nmovies):
                    cache[i][j] = self.predict(i, j, rVector, cVector, cache[i][j])

        self.Up = rVectors
        self.Vp = cVectors

    def calcrating(self, uid, mid):
        p = sum([self.Up[i][uid]*self.Vp[i][mid] for i in range(self.r)])
        if p > 5:
            p = 5
        elif p < 1:
            p = 1
        return p

    def calcrmse(self, arr):
        nusers = self.nusers
        nmovies = self.nmovies
        sse = 0.0
        total = 0
        for i in range(nusers):
            for j in range(nmovies):
                if arr[i][j] == None: continue
                total += 1
                sse += (arr[i][j] - self.calcrating(i, j))**2
        return math.sqrt(sse/total)

    def test(self, fname):
        nusers = self.nusers
        nmovies = self.nmovies

        # for i in range(nusers):
        #   for j in range(nmovies):
        #     self.Mtest[i][j] = self.M[i][j]

        f = open(fname)

        for line in f:
            newline = [int(each) for each in line.split("\t")]
            userid, movieid, rating = newline[0], newline[1], newline[2]
            self.Mtest[userid-1][movieid-1] = rating                    
        
                                               
if __name__ == "__main__":
    init = time.time()
    svd = SvdMatrix("ua.base", 943, 1682, 10)
    svd.train(.001, 0.01)
    print "took: ", time.time()-init

    print svd.calcrmse(svd.M)
    svd.test("ua.test")
    print svd.calcrmse(svd.Mtest)

# 2.76364392142
# 2.7689925966
