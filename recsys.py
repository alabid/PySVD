# Daniel Alabi and Cody Wang
# Recommendation Systems

from heapq import *
import math
import numpypy as numpy
import time

# returns the list of movies that both user1 and user2 have rated
def shared(user1, user2):
    shared = []
    for movieid in user1:
        if movieid in user2:
            shared.append(movieid)
    
    if len(shared) == 0:
        return []

    else:
        return shared

# helper function for calculating the cosine distance
def sqrtsum(user):
    return math.sqrt(sum([math.pow(user[movieid], 2) for movieid in user]))

# calculates the cosine distance between two users
def cosinedist(user1, user2, shareditems):
    nominator = sum([user1[movieid]*user2[movieid] for movieid in shareditems])
    # denominator = 0, what to do
    denominator = sqrtsum(user1)*sqrtsum(user2)
    return nominator/denominator

# return a similarity value heap for the user
def similarityheap(users, user, threshold, movieid):
    simheap = []
    for otheruser in users:
        # exclude user himself
        if users[otheruser] == user:
            continue
        # check if the otheruser rated movie with movieid
        if movieid not in users[otheruser]:
            continue
        shareditems = shared(user, users[otheruser])
        # number of movies shared has to be larger than threshold
        if len(shareditems) >= threshold:
            # remember to check for 0s
            # push the tuple(cosinedist, otheruser's id)
            # larger the cosinedist value, smaller the distance
            heappush(simheap, (-cosinedist(user, users[otheruser], shareditems), otheruser))
    return simheap

# get the k-nearest neighbors from the similarity heap, chosen
# neighbors must have rated the movie with movieid
def knearest(users, user, threshold, k, movieid):
    simheap = similarityheap(users, user, threshold, movieid)
    nearests = []
    n = 0
    while n<k and len(simheap) != 0:
        nearests.append(heappop(simheap))
        n += 1
   
    return nearests
    
    
# normalize the ratings matrix                     
def normalize(users):
    for userid in users:
        avg = 0
        for movieid in users[userid]:
            avg += users[userid][movieid]
        avg = float(avg)/len(users[userid])
        for movieid in users[userid]:
            users[userid][movieid] -= avg
        # need to throw away all 0s

# evaluate the rating user would give to movieid
def evaluate(users, user, threshold, k, movieid):   
    neighbors = knearest(users, user, threshold, k, movieid)
    simsum = 0
    totalweight = 0
    # totalweight = -sum([-neighbors[i][0] for i in neighbors])
    for i in range(len(neighbors)):
        totalweight += -neighbors[i][0]
        simsum += -neighbors[i][0] * users[neighbors[i][1]][movieid]
    if totalweight == 0:
        return 0
    else:
        estimatedrating = simsum/totalweight
        return estimatedrating
            
        #neighborsavg = numpy.mean([users[neighbor][movieid] for neighbor in neighbors])
        #user[movieid] = useravg + neighborsavg
    #return user[movieid]
        
        

if __name__== "__main__":
    f1 = open("ua.base")
    users = {}
    for row in f1:
        line = row.split("\t")        
        userid, movieid, rating = int(line[0]), int(line[1]), int(line[2])
        users.setdefault(userid, {})
        users[userid][movieid] = rating
    avgratings = []

    
    # avgratings stores the average rating for each user
    for i in range(1, len(users)+1):
        avgratings.append(numpy.mean([users[i][movieid] for movieid in users[i]]))

    normalize(users)
    predictions1 = []
    
    f2 = open("ua.test")
    userstest = []
    for row in f2:
        line = row.split("\t")
        userid, movieid, rating = int(line[0]), int(line[1]), int(line[2])
        userstest.append((userid, movieid, rating))
    print userstest
    init = time.time()
    
    rmse = 0
    for item in userstest:
        userid = item[0]
        movieid = item[1]
        prediction = avgratings[userid-1] + evaluate(users, users[userid], 100, 25, movieid)
        rmse += math.pow(prediction-item[2], 2)
    rmse = rmse / float(len(userstest))
    print rmse
    
    print "time taken: ", time.time()-init
    '''
    for userid in userstest:
        users.setdefault(userid, {})
        for movieid in userstest[userid]:
            prediction = avgratings[userid] + evaluate(users, users[userid], 20, 10, movieid)
            users[userid][movieid] = prediction
            print (userid, movieid, prediction)
            '''

            
    # print shared(users[1], users[2])
    # normalizedrating = evaluate(users, users[2], 20, 10, 314)
    # print useravg + normalizedrating
    # rating = normalizedrating + useravg
    
    
    # do k-nearest neighbors
