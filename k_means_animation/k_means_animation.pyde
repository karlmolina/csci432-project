import random
from operator import add

size(600, 600)
pixelDensity(2)
# noFill()
background(0)
stroke(255)
noStroke()
colorMode(HSB)

class KMeans:
    def __init__(self, data, k, min_change):
        self.data = data
        self.k = k
        self.change = 0
        self.centroids = []
        self.centroid_assignments = {}
        self.min_change = min_change
        
    def distance(self, v1, v2):
        """
        Finds euclidean distance between two vectors.
        
        :param v1: Vector 1
        :param v2: Vector 2
        :return: The distance between the two vectors
        """
        distance = 0
        for i in range(len(v1)):
            distance += pow((abs(v1[i] - v2[i])), 2)
        return sqrt(distance)
    
    def initialize_centroids(self):
        # Generates the initial centroids and saves them
        for i in range(self.k):
            self.centroids.append(random.choice(self.data))
    
    def assign_data(self):
        # centroids is the dictionary that contains all of the vectors that are assigned to a centroid in u
        self.centroid_assignments = {}  # centroid: list of vectors
        for x in self.data:
            minDistance = None
            closest_centroid_index = None
            # Finds the closest centroid for all points in the data
            for i, centroid in enumerate(self.centroids):
                d = self.distance(x, centroid)
                if minDistance == None:
                    minDistance = d
                    closest_centroid_index = i
                elif d < minDistance:
                    minDistance = d
                    closest_centroid_index = i
                    
            # Catches cases where the centroid a was not already assigned points
            try:
                self.centroid_assignments[closest_centroid_index].append(x)
            except:
                self.centroid_assignments.setdefault(closest_centroid_index, [])
                self.centroid_assignments[closest_centroid_index].append(x)
    
    def move_centroids(self):
        # Moves the centroid point to the new mean of the assigned data
        max_change = 0
        for i, centroid in enumerate(self.centroids):
            # temp is the list of points assigned to a given centroid
            temp = self.centroid_assignments[i]
            
            # calculates the mean values of the vectors
            total = temp[0]
            for j in temp[1:]:
                total = map(add, total, j)
            mean = [x / len(temp) for x in total]
            change = self.distance(mean, centroid)
            if change > max_change:
                max_change = change
            print('change', i, change)
            self.centroids[i] = mean
            ellipse(mean[0], mean[1], 30, 30)
            # print(mean)
        self.change = max_change

    def k_means(self):
        """
        Creates centroid points at random, assigns the closest points in the data,
            then re-determines the new centoid point based on the mean of the datapoints assigned to the old centroid.
            This will repeat until the centroids converge to the true means.
            
        :param data: The input data that will be clustered
        :param k: How many clusters are predetermined to be in the data
        :return: Returns the centroids of each cluster
        """
        self.initialize_centroids()
        
        iteration = 0
        while True:
            iteration += 1
            print('iteration', iteration)
            self.assign_data()
            self.move_centroids()
            
            print('self.change', self.change)
            if self.change <= self.min_change:
                break

def load_data(filename):
    data = []
    for line in loadStrings(filename):
        x = line.split(',')
        x = [int(a) for a in x]
        data.append(x)
    
    return data
    
def main():
    data = load_data('../generate_convex_clusters/data/without_noise.csv')
    k_means = KMeans(data, 3, 0.01)
    
    # for x in data:
    #     ellipse(x[0], x[1], 5, 5)
    
    # print(data)
        
    k_means.k_means()
    
    for centroid_index, points in k_means.centroid_assignments.items():
        fill(centroid_index * 100, 255, 255)
        for p in points:
            ellipse(p[0], p[1], 5, 5)
    
    for i, x in enumerate(k_means.centroids):
        fill(i* 100, 255, 255)
        ellipse(x[0], x[1], 30, 30)
    
    print(k_means.centroids)
    
    
main()
