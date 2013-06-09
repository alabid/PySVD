# Daniel Alabi and Cody Wang
# Recommendation Systems -- User-based 

import math
import heapq
import time
from shared import *

# fills predicted ratings for every
# movie that id1 hasn't seen
# using a user-based collaborative filtering
# userssim: stores similarities between any 2 users
# userssim[id1][id2] should give (sim, lenshared) of id1 and id2
# th -> threshold for nearest neighbor
# n -> number of nearest neighbors to consider
def userbased(users, mtopredict, userssim, id1, th=10, n=25):
    predictions = {}
    # heap to put possible items to be recommended
    # every item has a heap for users that has seen it
    heaps = {}

    # stores sum of rating for each item id1 doens't have
    items = {}
    # stores total number of people who have an item that
    # id1 doesn't have
    simsums = {}
    nn = 0

    for item in mtopredict:
        items[item] = 0.0
        simsums[item] = 0.0
        heaps.setdefault(item, [])

    for id2 in users:
        # skip myself
        if id1 == id2: continue
        (sim, lenshared) = userssim[id1][id2]
        if lenshared < th: continue
        
        for item in users[id2]:
            if item in items:
                heapq.heappush(heaps[item], (-sim, id2))
    
    for item in items:            
        nn = 0
        # make sure heap has enough items to pop
        while len(heaps[item]) > 0 and nn < n:
            (sim, id2) = heapq.heappop(heaps[item])
            sim = -sim
            # user with id2 has to have rated item to
            # be considered as a nearest neighbor
            if item in users[id2]:
                items[item] += users[id2][item]*sim
                simsums[item] += sim
                nn += 1
   
    # compute the predicted rating for each movie as
    # a weighted average
    for item in items:
         predictions[item] = items[item] / simsums[item] if simsums[item] > 0 else 0

    return predictions


if __name__ == "__main__":
    # read in training data set
    f1 = open("ua.base")
    users = readratings(f1)
    f1.close()

    # read in test data set
    f2 = open("ua.test")
    rated = readratings(f2)

    # normalize user ratings
    avgs = normalize(users)

    # stores movie predictions in form (movie, rmse, estimates used)
    mpredictions = {}
    init = time.time()
    totalrmse = 0.0
    total = 0
    userssim = computesims(users)
    for userid in rated:
        predictions = userbased(users, rated[userid].keys(), userssim, userid)
        for movieid in predictions:
            totalrmse += (predictions[movieid]+avgs[userid]-rated[userid][movieid])**2                
            mpredictions.setdefault(movieid, (movieid, 0.0, 0))
            movieid, crmse, nest = mpredictions[movieid]
            mpredictions[movieid] =  (movieid, crmse+(predictions[movieid]+avgs[userid]-rated[userid][movieid])**2, nest+1)        
            total += 1

    print "user-based totalrmse: ", math.sqrt(totalrmse/total)
    print "time taken: ", time.time()-init
   

