class Dbscan:
    def __init__(self, data, min_pts, eps):
        self.min_pts = min_pts
        self.eps = eps
        self.data = data
        self.core_points = []
        self.border_points = []
        self.noise_points = []
        self.labels = [None for _ in range(len(data))]
        # None unlabeled
        # 'noise' noise point
        # int some cluster label
        self.index = 0
        self.state = 0
        self.cluster_label = 0
        self.seed_set = set()
        self.seed_list = []
        self.seed_index = 0
        
    def distance(self, v1, v2):
        distance = 0
        for i in range(len(v1)):
            distance += pow((abs(v1[i] - v2[i])), 2)
        return sqrt(distance)
        
    def labeled_all_points(self):
        return len(self.data) == 0    
    
    def label_points(self):
        pass
        
    def show_points(self):
        for i, p in enumerate(self.data):
            if self.labels[i] is None:
                fill(255)
                stroke(0)
            elif self.labels[i] == 'noise':
                noStroke()
                fill(0)
            else:
                noStroke()
                fill((self.labels[i]) * 100, 255, 255)
            ellipse(p[0], p[1], 5, 5)
            
    def neighbors(self, p):
        neighbors = []
        for i, q in enumerate(self.data):
            if q == p:
                continue
            if self.distance(p, q) < self.eps:
                neighbors.append(i)
        return neighbors
            
