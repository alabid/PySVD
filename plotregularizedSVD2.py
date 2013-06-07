import time
from regularizedSVD2 import *

if __name__ == "__main__":
    # timeused = []
    # rmsetrain = []
    # rmsetest = []
    init = time.time()
    
    svd = SvdMatrix("ratings.dat", 6040, 3952, 30)
    svd.trainratings()
    print "took: ", time.time()-init
    
    print svd.calcrmse(svd.M)
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
    
    '''
