import time
from regularizedSVD3 import *

if __name__ == "__main__":
    timeusedr = []
    rmsetrainr = []
    timeusedl = []
    rmsetrainl = []
    timeusedreg = []
    rmsetrainreg = []
    rmsetestl = []
    rmsetestreg = []
    rmsetestr = []
    # init = time.time()
    
    # svd = SvdMatrix("ratings.dat", 6040, 3952, 30)
    # svd.trainratings()
    # print "took: ", time.time()-init
    
    # print svd.calcrmse(svd.trainrats)
    # svd.test("ua.test")
    # print svd.calcrmse(svd.testrats)
    
    # ==============Varying learning rate=============== #
    lrate = [i*0.0005 for i in range(50, 101)]
    for l in lrate:
        init = time.time()
        svd = SvdMatrix("ua.base", 943, 1682, 20, l)
        svd.trainratings()
        rmsetrainl.append(svd.calcrmse(svd.trainrats))
        svd.readtestsmaller("ua.test")
        rmsetestl.append(svd.calcrmse(svd.testrats))
        timeusedl.append(time.time()-init)
    
    f = open("lratetest2", 'w')
    for item in rmsetrainl:
        f.writelines("%s\t" % item)
    f.writelines('\n')
    for item in rmsetestl:
        f.writelines("%s\t" % item)
    f.close()
    
    f2 = open("lratetime2", 'w')
    for item in timeusedl:
        f2.writelines("%s\t" % item)
    f2.close()

    # ================================================== #
    
    # ==============Varying regularizer================= #
    regularizers = [i*0.001 for i in range(50, 101)]
    for reg in regularizers:
        init = time.time()
        svd = SvdMatrix("ua.base", 943, 1682, 20, 0.001, reg)
        svd.trainratings()
        rmsetrainreg.append(svd.calcrmse(svd.trainrats))
        svd.readtestsmaller("ua.test")
        rmsetestreg.append(svd.calcrmse(svd.testrats))
        timeusedreg.append(time.time()-init)
    
    f = open("regularizertest2", 'w')
    for item in rmsetrainreg:
        f.writelines("%s\t" % item)
    f.writelines('\n')
    for item in rmsetestreg:
        f.writelines("%s\t" % item)
    f.close()
    
    f2 = open("regularizertime2", 'w')
    for item in timeusedreg:
        f2.writelines("%s\t" % item)
    f2.close()
    # ================================================== #
    
    
    
    # ==============Varying rank================= #
    kvalues = range(5, 56)
    for k in kvalues:
        init = time.time()
        svd = SvdMatrix("ua.base", 943, 1682, k)
        svd.trainratings()
        rmsetrainr.append(svd.calcrmse(svd.trainrats))
        svd.readtestsmaller("ua.test")
        rmsetestr.append(svd.calcrmse(svd.testrats))
        timeusedr.append(time.time()-init)
    
    f = open("ranktest2", 'w')
    for item in rmsetrainr:
        f.writelines("%s\t" % item)
    f.writelines('\n')
    for item in rmsetestr:
        f.writelines("%s\t" % item)
    f.close()
    
    f2 = open("ranktime2", 'w')
    for item in timeusedr:
        f2.writelines("%s\t" % item)
    f2.close()

'''
import time
from regularizedSVD3 import *

if __name__ == "__main__":
    timeusedr = []
    rmsetrainr = []
    timeusedl = []
    rmsetrainl = []
    timeusedreg = []
    rmsetrainreg = []
    # rmsetest = []
    # init = time.time()
    
    # svd = SvdMatrix("ratings.dat", 6040, 3952, 30)
    # svd.trainratings()
    # print "took: ", time.time()-init
    
    # print svd.calcrmse(svd.trainrats)
    # svd.test("ua.test")
    # print svd.calcrmse(svd.testrats)
    
    # ==============Varying learning rate=============== #
    lrate = [i*0.0005 for i in range(5, 26)]
    for l in lrate:
        init = time.time()
        svd = SvdMatrix("ratings.dat", 6040, 3952, 20, l)
        svd.trainratings()
        rmsetrainl.append(svd.calcrmse(svd.trainrats))
        # svd.test("ua.test")
        # rmsetest.append(svd.calcrmse(svd.testrats))
        timeusedl.append(time.time()-init)
    
    f = open("lratetest3", 'w')
    for item in rmsetrainl:
        f.writelines("%s\t" % item)
    f.writelines('\n')
    # for item in rmsetest:
    #    f.writelines("%s\t" % item)
    f.close()
    
    f2 = open("lratetime3", 'w')
    for item in timeusedl:
        f2.writelines("%s\t" % item)
    f2.close()

    # ================================================== #
    
    # ==============Varying regularizer================= #
    regularizers = [i*0.001 for i in range(10, 31)]
    for reg in regularizers:
        init = time.time()
        svd = SvdMatrix("ratings.dat", 6040, 3952, 20, 0.001, reg)
        svd.trainratings()
        rmsetrainreg.append(svd.calcrmse(svd.trainrats))
        # svd.test("ua.test")
        # rmsetest.append(svd.calcrmse(svd.testrats))
        timeusedreg.append(time.time()-init)
    
    f = open("regularizertest3", 'w')
    for item in rmsetrainreg:
        f.writelines("%s\t" % item)
    f.writelines('\n')
    # for item in rmsetest:
    #    f.writelines("%s\t" % item)
    f.close()
    
    f2 = open("regularizertime3", 'w')
    for item in timeusedreg:
        f2.writelines("%s\t" % item)
    f2.close()
    # ================================================== #
    
    
    
    # ==============Varying rank================= #
    kvalues = range(10, 31)
    for k in kvalues:
        init = time.time()
        svd = SvdMatrix("ratings.dat", 6040, 3952, k)
        svd.trainratings()
        rmsetrainr.append(svd.calcrmse(svd.trainrats))
        # svd.test("ua.test")
        # rmsetest.append(svd.calcrmse(svd.testrats))
        timeusedr.append(time.time()-init)
    
    f = open("ranktest3", 'w')
    for item in rmsetrainr:
        f.writelines("%s\t" % item)
    f.writelines('\n')
    # for item in rmsetest:
    #    f.writelines("%s\t" % item)
    f.close()
    
    f2 = open("ranktime3", 'w')
    for item in timeusedr:
        f2.writelines("%s\t" % item)
    f2.close()
'''


