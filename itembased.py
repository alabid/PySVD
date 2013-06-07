# Daniel Alabi and Cody Wang
# Recommendation Systems -- Itembased

import math
import heapq
import time
from shared import *

# itembased collaborative filtering
# sim_movies: stores similarities between any 2 movies
# sim_movies[id1][id2] should give (sim, lenshared) of id1 and id2
# th -> threshold for nearest neighbor
# n -> number of nearest neighbors to consider
def itembased(users, mtopredict, moviessim, id1, th=10, n=25):
    items = {}
    simsums = {}
    predictions = {}

    for item in mtopredict:
        items[item] = 0.0
        simsums[item] = 0.0


    for item in items:
        # initialize heap for item
        h = []
        for item2 in users[id1]:
            if item == item2: continue
            # some movies like the one with id 1582
            # hasn't been rated by any user in ua.base
            if item not in moviessim or item2 not in moviessim[item]:
                predictions[item] = 0.0
                continue

            (sim, lenshared) = moviessim[item][item2]
            if lenshared < th: continue
            heapq.heappush(h, (-sim, item2))
        # get the nearest neightbors for item
        nn = 0
        while nn < n and len(h) > 0:
            (sim, item2) = heapq.heappop(h)
            sim = -sim
            items[item] += users[id1][item2]*sim
            simsums[item] += sim
            nn += 1
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
    movies = transpose(users)

    mpredictions = {}
    init = time.time()
    totalrmse = 0.0
    total = 0
    # computes similarities between all movies
    moviessim = computesims(movies)
    for userid in rated:
        predictions = itembased(users, rated[userid].keys(), moviessim, userid)
        for movieid in rated[userid]:
            if movieid in predictions:
                totalrmse += (predictions[movieid]+avgs[userid]-rated[userid][movieid])**2
                mpredictions.setdefault(movieid, (movieid, 0.0, 0))
                movieid, crmse, nest = mpredictions[movieid]
                mpredictions[movieid] =  (movieid, crmse+(predictions[movieid]+avgs[userid]-rated[userid][movieid])**2, nest+1)
                total += 1
    print "item-based totalrmse: ", math.sqrt(totalrmse/total)
    print "time taken: ", time.time()-init
