# Daniel Alabi and Cody Wang

import math
import random
import time

# remember to normalize by subtracting out averages

class SvdMatrix:
    def __init__(self, trainfile, nusers, nmovies, r=10, lrate=0.001, regularizer=0.015):
        self.M = [[None]*nmovies for i in range(nusers)]
        self.Mtest = [[None]*nmovies for i in range(nusers)]

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

        avg = self.averagerating()
        initval = math.sqrt(avg/r)

        self.U = [[initval]*r for i in range(nusers)]
        self.V = [[initval]*r for i in range(nmovies)]
        self.r = r
        self.lrate = lrate
        self.regularizer = regularizer
        self.minimprov = 0.001
        self.maxepochs = 30            

    def dotproduct(self, v1, v2):
        return sum([v1[i]*v2[i] for i in range(len(v1))])

    def calcrating(self, uid, mid):
        p = self.dotproduct(self.U[uid], self.V[mid])
        if p > 5:
            p = 5
        elif p < 1:
            p = 1
        return p

    def averagerating(self):
        avg = 0
        n = 0
        for i in range(self.nusers):
            for j in range(self.nmovies):
                if self.M[i][j] == None: continue
                avg += self.M[i][j]
                n += 1
        return float(avg)/n

    def predict(self, i, j):
        return self.calcrating(i, j)
    """
    def probe(self):
        sse = 0.0
        n = 0
        for i in range(self.nusers):
            for j in range(self.nmovies):
                if self.M[i][j] == None: continue
                prediction = self.predict(i, j)
                err = self.M[i][j] - prediction
                sse += err**2
                n += 1
        return math.sqrt(sse/n)
    """
    def train(self):
        sse = 0.0
        n = 0
        for i in range(self.nusers):
            for j in range(self.nmovies):
                if self.M[i][j] == None: continue
                err = self.M[i][j] - self.predict(i, j)
                sse += err**2
                n += 1
                for k in range(self.r):
                    uTemp = self.U[i][k]
                    vTemp = self.V[j][k]
                    self.U[i][k] += self.lrate * (err*vTemp - self.regularizer*uTemp)
                    self.V[j][k] += self.lrate * (err*uTemp - self.regularizer*vTemp)
        return math.sqrt(sse/n)

    def trainratings(self):        
        # set old probe error to large value
        # oldprobeerr = 100000.0
        oldtrainerr = 1000000.0
        for epoch in range(self.maxepochs):
            trainerr = self.train()
            # probeerr = self.probe()
            if abs(oldtrainerr-trainerr) < self.minimprov:
                break
            oldtrainerr = trainerr
            print "epoch=", epoch, "; trainerr=", trainerr

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
    timeused = []
    rmsetrain = []
    rmsetest = []
    # init = time.time()
    # svd = SvdMatrix("ua.base", 943, 1682, 40)
    # svd.trainratings()
    # print "took: ", time.time()-init

    # print svd.calcrmse(svd.M)
    # svd.test("ua.test")
    # print svd.calcrmse(svd.Mtest)

    '''

    # ==============Varying learning rate=============== #
    lrate = [i*0.0005 for i in range(1, 51)]
    for l in lrate:
        init = time.time()
        svd = SvdMatrix("ua.base", 943, 1682, 13, l)
        svd.trainratings()
        rmsetrain.append(svd.calcrmse(svd.M))
        svd.test("ua.test")
        rmsetest.append(svd.calcrmse(svd.Mtest))
        timeused.append(time.time()-init)
    
    f = open("lratetest2", 'w')
    for item in rmsetrain:
        f.writelines("%s\t" % item)
    f.writelines('\n')
    for item in rmsetest:
        f.writelines("%s\t" % item)
    f.close()
    
    f2 = open("lratetime2", 'w')
    for item in timeused:
        f2.writelines("%s\t" % item)
    f2.close()

    # ================================================== #
    
    # ==============Varying regularizer================= #
    regularizers = [i*0.001 for i in range(1, 51)]
    for reg in regularizers:
        init = time.time()
        svd = SvdMatrix("ua.base", 943, 1682, 13, 0.001, reg)
        svd.trainratings()
        rmsetrain.append(svd.calcrmse(svd.M))
        svd.test("ua.test")
        rmsetest.append(svd.calcrmse(svd.Mtest))
        timeused.append(time.time()-init)
    
    f = open("regularizertest2", 'w')
    for item in rmsetrain:
        f.writelines("%s\t" % item)
    f.writelines('\n')
    for item in rmsetest:
        f.writelines("%s\t" % item)
    f.close()
    
    f2 = open("regularizertime2", 'w')
    for item in timeused:
        f2.writelines("%s\t" % item)
    f2.close()
    # ================================================== #
    
    '''

    # ==============Varying rank================= #
    kvalues = range(5, 56)
    for k in kvalues:
        init = time.time()
        svd = SvdMatrix("ua.base", 943, 1682, k)
        svd.trainratings()
        rmsetrain.append(svd.calcrmse(svd.M))
        svd.test("ua.test")
        rmsetest.append(svd.calcrmse(svd.Mtest))
        timeused.append(time.time()-init)
    
    f = open("ranktest2", 'w')
    for item in rmsetrain:
        f.writelines("%s\t" % item)
    f.writelines('\n')
    for item in rmsetest:
        f.writelines("%s\t" % item)
    f.close()
    
    f2 = open("ranktime2", 'w')
    for item in timeused:
        f2.writelines("%s\t" % item)
    f2.close()
