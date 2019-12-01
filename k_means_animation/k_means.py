import random
from operator import add
from copy import deepcopy

def load_data(filename):
    data = []
    for line in loadStrings(filename):
        x = line.split(',')
        x = [int(a) for a in x]
        data.append(x)
    
    return data

class KMeans:
    def __init__(self, filename, k, min_change, centroid_lerp_value, random_seed):
        self.data = load_data(filename)
        self.k = k
        self.centroid_lerp_value = centroid_lerp_value
        self.change = float('inf')
        self.centroids = []
        self.centroid_assignments = {}
        self.min_change = min_change
        self.moving_centroids = False
        self.goal_centroids = [None for i in range(k)]
        self.iteration = 0
        self.random_seed = random_seed
        self.colors = [i * 200/k for i in range(k)]
        self.time = 0


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
    
    def is_converged(self):
        if self.change is None:
            return False
        return self.change < self.min_change
    
    def initialize(self):
        random.seed(self.random_seed)
        self.initialize_centroids()
        # self.assign_data()
    
    def initialize_centroids(self):
        # Generates the initial centroids and saves them
        for i in range(self.k):
            self.centroids.append(random.choice(self.data))
    
    def assign_data(self):
        # centroids is the dictionary that contains all of the vectors that are assigned to a centroid in u
        self.centroid_assignments = {i: [] for i in range(self.k)}  # centroid: list of vectors
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
        self.iteration += 1
        # Moves the centroid point to the new mean of the assigned data
        max_change = 0
        for i, centroid in enumerate(self.centroids):
            # temp is the list of points assigned to a given centroid
            temp = self.centroid_assignments[i]
            
            # calculates the mean values of the vectors
            if len(temp) != 0:
                total = temp[0]
                for j in temp[1:]:
                    total = map(add, total, j)
                    
                mean = [x / len(temp) for x in total]
                change = self.distance(mean, centroid)
                if change > max_change:
                    max_change = change
                # print('change', i, change)
                c = centroid
                # self.centroids[i] = [lerp(centroid[i], mean[i], 0.1) for i in range(len(mean))]
                self.goal_centroids[i] = mean
                # self.centroids[i] = mean

                # print(mean)
        self.change = max_change
        
    def update_centroids(self):
        for i in range(self.k):
            self.centroids[i] = [lerp(self.centroids[i][j], self.goal_centroids[i][j], self.centroid_lerp_value) for j in range(len(self.centroids[i]))]
            
        if self.distance(self.centroids[0], self.goal_centroids[0]) < 1:
            self.moving_centroids = False
            
    def show_points(self):
        noStroke()
        if len(self.centroid_assignments) == 0:
            for p in self.data:
                fill(255)
                stroke(0)
                strokeWeight(1)
                ellipse(p[0], p[1], 5, 5)
        else:
            for i, points in self.centroid_assignments.items():
                fill(self.colors[i], 255, 225)
                for p in points:
                    ellipse(p[0], p[1], 5, 5)
    
    def show_centroids(self):
        stroke(0)
        strokeWeight(2)
        for i, x in enumerate(self.centroids):
            fill(self.colors[i], 255, 255)
            rect(x[0], x[1], 10, 10)

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
    
    def run(self):
        self.time += 1
        if self.time < 100:
            return False
        elif self.time < 200:
            self.assign_data()
            return False
        if not self.is_converged():
            if not self.moving_centroids:
                self.assign_data()
            
                self.move_centroids()
                self.moving_centroids = True
            else:
                self.update_centroids()
            return False
        return True
                
    def show(self):
        self.show_points()
        self.show_centroids()
        fill(255)
        noStroke()
        rect(192, 16, 373, 20)
        fill(0)
        text('k-means  k={}, min_change={}, iteration={}, change={:.2f}'.format(self.k, self.min_change, self.iteration, self.change), 10, 20)
