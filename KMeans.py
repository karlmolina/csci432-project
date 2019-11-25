import random
from operator import add

class KMeans:
    def __init__(self):
        pass

    def minkowskiDistance(v1, v2, p):
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

    def processData(self):
        pass

    def kMeans(self, data, k):
        u = []
        change = 1
        for i in range(k):
            u.append(random.choice(data))
        while change > .01:
            centroids = {}
            for x in data:
                minDistance = None
                min = None
                for m in u:
                    dist = self.minkowskiDistance(x, m, 'inf')
                    if minDistance == None:
                        minDistance = dist
                        min = m
                    elif dist < minDistance:
                        minDistance = dist
                        min = m
                a = u.index(min)
                try:
                    centroids[a].append(x)
                except:
                    centroids.setdefault(a, [])
                    centroids[a].append(x)
            for i in u:
                a = u.index(i)
                try:
                    temp = centroids[a]
                except:
                    del u[u.index(i)]
                total = temp[0]
                count = 1
                for j in temp[1:]:
                    total = list(map(add, total, j))
                    count += 1
                # print(total)
                mean = [x / float(count) for x in total]
                oldU = u
                try:
                    u[u.index(i)] = mean
                except:
                    mean = mean
            comb = 0
            countC = 0
            for i in range(len(u)):
                comb += self.minkowskiDistance(u[i], oldU[i], 'inf')
                countC += 1
            change = comb / float(countC)
        return u

