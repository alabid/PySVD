# Daniel Alabi and Cody Wang

class SvdMatrix:
    def __init__(self, trainfile, nusers, nmovies, r):
        self.M = [[None]*nmovies]*nusers
        self.Up = [[None]*r]*nusers
        self.Vp = [[None]*r]*nmovies
        self.r = r
        self.lrate = 0.001
        self.regularizer = 0.02
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

    def dotproduct(self):
        return sum([self.Up[i][k]*self.Vp[j][k] for k in range(self.r)])
            
    def train(self, maxrmse):
        nusers = self.nusers
        nmovies = self.nmovies
        for k in range(self.r):
            for i in range(nusers):
                self.Up[i][k] = 1
            for j in range(nmovies):
                self.Vp[j][k] = 1
            error = float("inf")
            while error > maxrmse:
                for i in range(nusers):
                    for j in range(nmovies):
                        # ignore empty entries
                        if self.M[i][j] == None: continue                        

                        error = self.M[i][j] - self.dotproduct(k)
                        uTemp = self.Up[i][k]
                        vTemp = self.Vp[j][k]
                        self.Up[i][k] += self.lrate * (error * vTemp - self.regularizer * uTemp)
                        self.Vp[j][k] += self.lrate * (error * uTemp - self.regularizer * vTemp)


if __name__ == "__main__":
    f = open("ua.base")

    svd = SvdMatrix("ua.base", 943, 1682, 20)
    svd.train(.002)




