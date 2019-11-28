import random
from operator import add


class KMeans:
    def __init__(self):
        pass

    def minkowskiDistance(self, v1, v2, p):
        """
        Finds the distance between two vectors utilizing a generalized minkowski distance formula
        :param v1: Vector 1
        :param v2: Vector 2
        :param p: the power of minkowski. If 2, it is euclidean distance and 'inf' is the maximum norm
        :return: The distance between the two vectors
        """
        if type(p) == str:
            maxDistance = 0
            for x in range(len(v1)):
                maxDistance = max(maxDistance, abs(v1[x] - v2[x]))
            return maxDistance
        else:
            distance = 0
            # assume: v1 and v2 are equal length
            for x in range(len(v1) - 1):
                distance += pow((abs(v1[x] - v2[x])), p)
            return pow(distance, 1.0 / p)

    def kMeans(self, data, k):
        """
        Creates centroid points at random, assigns the closest points in the data,
            then re-determines the new centoid point based on the mean of the datapoints assigned to the old centroid.
            This will repeat until the centroids converge to the true means.
        :param data: The input data that will be clustered
        :param k: How many clusters are predetermined to be in the data
        :return: Returns the centroids of each cluster
        """
        # u is the centroid vectors themselves
        u = []
        change = 1
        # Generates the initial centroids and saves them
        for i in range(k):
            u.append(random.choice(data))
        while change > .01:
            # centroids is the dictionary that contains all of the vectors that are assigned to a centroid in u
            centroids = {}  # centroid: list of vectors
            for x in data:
                minDistance = None
                min = None
                # Finds the closest centroid for all points in the data
                for m in u:
                    dist = self.minkowskiDistance(x, m, 2)
                    if minDistance == None:
                        minDistance = dist
                        min = m
                    elif dist < minDistance:
                        minDistance = dist
                        min = m
                # a is the closest centroid
                a = u.index(min)
                # Catches cases where the centroid a was not already assigned points
                try:
                    centroids[a].append(x)
                except:
                    centroids.setdefault(a, [])
                    centroids[a].append(x)
            # Moves the centroid point to the new mean of the assigned data
            for i in u:
                a = u.index(i)
                # check to see if any points were assigned to a given centroid, if not, then remove the centroid
                try:
                    #temp is the list of points assigned to a given centroid
                    temp = centroids[a]
                except:
                    del u[u.index(i)]
                #calculates the mean values of the vectors
                total = temp[0]
                count = 1
                for j in temp[1:]:
                    total = list(map(add, total, j))
                    count += 1
                mean = [x / float(count) for x in total]
                oldU = u
                #throwaway try and catch to prevent errors from insertion
                try:
                    u[u.index(i)] = mean
                except:
                    mean = mean
            #calculates the change of the centroids
            comb = 0
            countC = 0
            for i in range(len(u)):
                comb += self.minkowskiDistance(u[i], oldU[i], 2)
                countC += 1
            change = comb / float(countC)
        #returns centroid vectors u
        return u
