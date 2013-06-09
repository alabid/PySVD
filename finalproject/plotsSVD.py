# Daniel Alabi and Cody Wang
# Separate code for plotting since matplotlib runs slow under Python
# The first part plots the results obtained from the smaller dataset
# The second part plots the results obtained from the larger dataset
# Run only one main function at a time by commenting and uncommenting

# =============Code to plot for smaller-sized datasets=============#
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

if __name__ == "__main__":
    
    # ========= Code to Plot time against k ========= #
    f = open("data/ranktime2")
    kvalues = range(1, 51)
    lines = f.readlines()
    line1 = lines[0].split('\t')
    times = [float(line1[i]) for i in range(0, len(line1)-1)]
    
    xdata = np.array(kvalues)
    ydata = np.array(times)    
    

    plt.xlabel("rank")
    plt.ylabel("time used")

    xnew = np.linspace(xdata.min(), xdata.max(), len(kvalues)*1)
    ysmooth = spline(xdata, ydata, xnew)
    
    plt.plot(xnew, ysmooth)
    plt.show()
    # ==================================================================#
    
    # ========= Code to Plot time against regularizers ========= #
    f = open("data/regularizertime2")
    regularizers = [i*0.001 for i in range(1, 51)]
    lines = f.readlines()
    line1 = lines[0].split('\t')
    times = [float(line1[i]) for i in range(0, len(line1)-1)]
    
    xdata = np.array(regularizers)
    ydata = np.array(times)    
    

    plt.xlabel("regularizers")
    plt.ylabel("time used")

    xnew = np.linspace(xdata.min(), xdata.max(), len(regularizers)*1)
    ysmooth = spline(xdata, ydata, xnew)
    
    plt.plot(xnew, ysmooth)
    plt.show()
    # ==================================================================#
    
    # ========= Code to Plot time against lrates ========= #
    f2 = open("data/lratetime2")
    lrate = [i*0.005 for i in range(1, 51)]
    lines = f2.readlines()
    line1 = lines[0].split('\t')
    times = [float(line1[i]) for i in range(0, len(line1)-1)]
    
    xdata = np.array(lrate)
    ydata = np.array(times)    
    

    plt.xlabel("learning rate")
    plt.ylabel("time used")

    xnew = np.linspace(xdata.min(), xdata.max(), len(lrate)*1)
    ysmooth = spline(xdata, ydata, xnew)
    
    plt.plot(xnew, ysmooth)
    plt.show()
    # ==================================================================#

    # ========= Code to Plot rmse against k ========= #
    f3 = open("data/ranktest2")
    kvalues = range(1, 51)
    lines = f3.readlines()
    line1 = lines[0].split('\t')
    rmsetrain = [float(line1[i]) for i in range(0, len(line1)-1)]
    line2 = lines[1].split('\t')
    rmsetest = [float(line2[i]) for i in range(0, len(line2)-1)]
    
    xdata = np.array(kvalues)
    y1data = np.array(rmsetrain)    
    y2data = np.array(rmsetest)

    plt.xlabel("rank")
    plt.ylabel("rmse of data (red: trainingset; blue: testset)")

    xnew = np.linspace(xdata.min(), xdata.max(), len(kvalues)*1)
    ysmooth = spline(xdata, y1data, xnew)
    y2smooth = spline(xdata, y2data, xnew)
    
    plt.plot(xnew, ysmooth, 'r--', xnew, y2smooth, 'bs')
    plt.show()
    # ==================================================================#
   

    # ========= Code to Plot rmse against regularizers ========= #
    f2 = open("data/regularizertest2")
    regularizers = [i*0.001 for i in range(1, 51)]
    lines = f2.readlines()
    line1 = lines[0].split('\t')
    rmsetrain = [float(line1[i]) for i in range(0, len(line1)-1)]
    line2 = lines[1].split('\t')
    rmsetest = [float(line2[i]) for i in range(0, len(line2)-1)]

   
    xdata = np.array(regularizers)
    y1data = np.array(rmsetrain)    
    y2data = np.array(rmsetest)

    plt.xlabel("regularizers")
    plt.ylabel("rmse of data (red: trainingset; blue: testset)")

    xnew = np.linspace(xdata.min(), xdata.max(), len(regularizers)*1)
    ysmooth = spline(xdata, y1data, xnew)
    y2smooth = spline(xdata, y2data, xnew)
    
    plt.plot(xnew, ysmooth, 'r--', xnew, y2smooth, 'bs')
    plt.show()
    # ==================================================================#
    

    # ========= Code to Plot rmse against lrate ========= # 
    f3 = open("data/lratetest2")
    lrate = [i*0.005 for i in range(1, 51)]
    lines = f3.readlines()
    line1 = lines[0].split('\t')
    rmsetrain = [float(line1[i]) for i in range(0, len(line1)-1)]
    line2 = lines[1].split('\t')
    rmsetest = [float(line2[i]) for i in range(0, len(line2)-1)]
   
    xdata = np.array(lrate)
    y1data = np.array(rmsetrain)
    y2data = np.array(rmsetest)

    plt.xlabel("lrate")
    plt.ylabel("rmse of data (red: trainingset; blue: testset)")

    xnew = np.linspace(xdata.min(), xdata.max(), len(lrate)*1)
    ysmooth = spline(xdata, y1data, xnew)
    y2smooth = spline(xdata, y2data, xnew)
    
    plt.plot(xnew, ysmooth, 'r--', xnew, y2smooth, 'bs')
    plt.show()
    # ==================================================================#


'''
# =============Code to plot for larger-sized datasets=============#

# Daniel Alabi and Cody Wang
# Separate code for plotting since matplotlib runs slow under Python

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

if __name__ == "__main__":
    
    # ========= Code to Plot time against k ========= #
    f = open("data/ranktime3")
    kvalues = range(10, 31)
    lines = f.readlines()
    line1 = lines[0].split('\t')
    times = [float(line1[i]) for i in range(0, len(line1)-1)]
    
    xdata = np.array(kvalues)
    ydata = np.array(times)    
    

    plt.xlabel("rank")
    plt.ylabel("time used")

    xnew = np.linspace(xdata.min(), xdata.max(), len(kvalues)*1)
    ysmooth = spline(xdata, ydata, xnew)
    
    plt.plot(xnew, ysmooth)
    plt.show()
    # ==================================================================#
    
    # ========= Code to Plot time against regularizers ========= #
    f = open("data/regularizertime3")
    regularizers = [i*0.001 for i in range(1, 21)]
    lines = f.readlines()
    line1 = lines[0].split('\t')
    times = [float(line1[i]) for i in range(0, len(line1)-1)]
    
    xdata = np.array(regularizers)
    ydata = np.array(times)    
    

    plt.xlabel("regularizers")
    plt.ylabel("time used")

    xnew = np.linspace(xdata.min(), xdata.max(), len(regularizers)*1)
    ysmooth = spline(xdata, ydata, xnew)
    
    plt.plot(xnew, ysmooth)
    plt.show()
    # ==================================================================#
    
    # ========= Code to Plot time against lrates ========= #
    f2 = open("data/lratetime3")
    lrate = [i*0.005 for i in range(1, 21)]
    lines = f2.readlines()
    line1 = lines[0].split('\t')
    times = [float(line1[i]) for i in range(0, len(line1)-1)]
    
    xdata = np.array(lrate)
    ydata = np.array(times)    
    

    plt.xlabel("learning rate")
    plt.ylabel("time used")

    xnew = np.linspace(xdata.min(), xdata.max(), len(lrate)*1)
    ysmooth = spline(xdata, ydata, xnew)
    
    plt.plot(xnew, ysmooth)
    plt.show()
    # ==================================================================#

    # ========= Code to Plot rmse against k ========= #
    f3 = open("data/ranktest3")
    kvalues = range(10, 31)
    lines = f3.readlines()
    line1 = lines[0].split('\t')
    rmsetrain = [float(line1[i]) for i in range(0, len(line1)-1)]
    
    xdata = np.array(kvalues)
    y1data = np.array(rmsetrain)    
    
    plt.xlabel("rank")
    plt.ylabel("rmse of data")

    xnew = np.linspace(xdata.min(), xdata.max(), len(kvalues)*1)
    ysmooth = spline(xdata, y1data, xnew)
    
    plt.plot(xnew, ysmooth)
    plt.show()
    # ==================================================================#
   

    # ========= Code to Plot rmse against regularizers ========= #
    f2 = open("data/regularizertest3")
    regularizers = [i*0.001 for i in range(1, 21)]
    lines = f2.readlines()
    line1 = lines[0].split('\t')
    rmsetrain = [float(line1[i]) for i in range(0, len(line1)-1)]

   
    xdata = np.array(regularizers)
    y1data = np.array(rmsetrain)    

    plt.xlabel("regularizers")
    plt.ylabel("rmse of data")
    
    xnew = np.linspace(xdata.min(), xdata.max(), len(regularizers)*1)
    ysmooth = spline(xdata, y1data, xnew)

    plt.plot(xnew, ysmooth)
    plt.show()
    # ==================================================================#
    

    # ========= Code to Plot rmse against lrate ========= # 
    f3 = open("data/lratetest3")
    lrate = [i*0.005 for i in range(1, 21)]
    lines = f3.readlines()
    line1 = lines[0].split('\t')
    rmsetrain = [float(line1[i]) for i in range(0, len(line1)-1)]

    xdata = np.array(lrate)
    y1data = np.array(rmsetrain)

    plt.xlabel("lrate")
    plt.ylabel("rmse of data")

    xnew = np.linspace(xdata.min(), xdata.max(), len(lrate)*1)
    ysmooth = spline(xdata, y1data, xnew)

    plt.plot(xnew, ysmooth)
    plt.show()
    # ==================================================================#
'''
