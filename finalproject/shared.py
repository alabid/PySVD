# Daniel Alabi and Cody Wang
# Recommendation Systems -- shared code for item and user-based
# This file contains the following functions:
# cosine_sim, computesims, transpose, normalize, and readratings
import math
import heapq


# util -> utility matrix. users -> movies -> rating
#         or movies -> users -> rating
# id1 -> first item being compared (user or movie)
# id2 -> second item being compared (user or movie)
# th -> threshold for number of shared items to consider
# returns the cosine similarity between util[id1] and
# util[id2] and the number of items shared by util[id1]
# and util[id2]
# ===========================================================
# Cosine distance is between -1 (oppposites) and +1 (closest)
# but since we want a weighted average,
# we needed to return a score between
# 0 and 1, so we scale the cosine distance
# appropriately
# ===========================================================
def cosine_sim(util, id1, id2, th=3):
    num = 0
        
    # get items util[id1] and util[id2] share in common
    shared = set(util[id1].keys()).intersection(util[id2].keys())

    # optimization to not compute similarity between items
    # that don't meet threshold
    if len(shared) < th:
        return (0.0, len(shared))
    firstmag = 0 
    secondmag = 0
    # calculate dot product and magnitudes of shared items
    for item in shared:
        num += util[id1][item] * util[id2][item]
        firstmag += util[id1][item]**2
        secondmag += util[id2][item]**2

    # prevent denom == 0
    firstmag = 1 if firstmag == 0 else firstmag
    secondmag = 1 if secondmag == 0 else secondmag
    # calculate magnitude of shared items in util[id2]
    denom = math.sqrt(firstmag) * math.sqrt(secondmag)

    return ((num/denom+1)/2, len(shared))


# should return (sim, lenshared) pairs
# where sim is the cosine similarity
def computesims(util):
    sims = {}
    for id1 in util:
        sims[id1] = {}
        for id2 in util:
            if id1 == id2: continue
            sims[id1][id2] = cosine_sim(util, id1, id2)
    return sims

# normalize the utility matrix
# and returns the subtracted averages
def normalize(util):
    # save average of each user
    avgs = {}
    for id1 in util:
        avg = 0.0
        for id2 in util[id1]:
            avg += util[id1][id2]
        avg = float(avg)/len(util[id1])
        for id2 in util[id1]:
            util[id1][id2] -= avg
        avgs[id1] = avg
    return avgs

# transpose the matrix
# e.g from movies -> users -> ratings
#     to users -> movies -> ratings
def transpose(util):
    transposed = {}
    for id1 in util:
        for id2 in util[id1]:
            transposed.setdefault(id2, {})
            # flip id1 and id2
            transposed[id2][id1] = util[id1][id2]
    return transposed

# read ratings file with entries (userid, movieid, rating)
def readratings(f):
    ratings = {}
    for row in f:
        line = row.split("\t")        
        userid, movieid, rating = int(line[0]), int(line[1]), int(line[2])
        ratings.setdefault(userid, {})
        ratings[userid][movieid] = rating
    return ratings
