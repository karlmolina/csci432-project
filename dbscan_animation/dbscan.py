def load_data(filename):
    data = []
    for line in loadStrings(filename):
        x = line.split(',')
        x = [int(a) for a in x]
        data.append(x)
    
    return data

class Dbscan:
    def __init__(self, filename, min_pts, eps, process_amount, colors):
        self.min_pts = min_pts
        self.eps = eps
        self.process_amount = process_amount
        self.data = load_data(filename)
        self.labels = [None for _ in range(len(self.data))]
        # None unlabeled
        # 'noise' noise point
        # int some cluster label
        self.index = 0
        self.state = 0
        self.cluster_label = 0
        self.seed_list = []
        self.seed_index = 0
        self.time = 0
        self.colors = colors
    
    def distance(self, v1, v2):
        distance = 0
        for i in range(len(v1)):
            distance += pow((abs(v1[i] - v2[i])), 2)
        return sqrt(distance)
        
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
                fill(self.colors[self.labels[i]], 255, 255)
            ellipse(p[0], p[1], 5, 5)
    
    def show(self):
        self.show_points()
        noStroke()
        fill(255)
        rect(192, 16, 373, 20)
        fill(0)
        text('DBSCAN  eps={}, min_pts={}'.format(self.eps, self.min_pts), 10, 20)
            
    def neighbors(self, p):
        neighbors = []
        for i, q in enumerate(self.data):
            if q == p:
                continue
            if self.distance(p, q) < self.eps:
                neighbors.append(i)
        return neighbors
            
    def run(self):
        if self.state == 2:
            if self.time < 100:
                self.time += 1
                return False
            else:
                return True
        for _ in range(self.process_amount):
            if self.index == len(self.data):
                self.state = 2
                return False
            
            if self.state == 0:
                if self.labels[self.index] is not None:
                    while self.labels[self.index] is not None:
                        self.index += 1
                        if self.index == len(self.data):
                            return False
                    continue
                neighbors = self.neighbors(self.data[self.index])
                if len(neighbors) < self.min_pts:
                    self.labels[self.index] = 'noise'
                    self.index += 1
                    continue
                self.cluster_label += 1
                self.labels[self.index] = self.cluster_label
                self.seed_list = neighbors
                self.state = 1
                self.index += 1
            elif self.state == 1:
                if self.seed_index == len(self.seed_list):
                    self.seed_index = 0
                    self.state = 0
                    continue
                index = self.seed_list[self.seed_index]
                if self.labels[index] == 'noise':
                    self.labels[index] = self.cluster_label
                    continue
                if self.labels[index] is not None:
                    self.seed_index += 1
                    continue
                self.labels[index] = self.cluster_label
                neighbors = self.neighbors(self.data[index])
                if len(neighbors) >= self.min_pts:
                    s = set(neighbors)
                    seed_set = set(self.seed_list)
                    for x in s:
                        if x not in seed_set:
                            self.seed_list.append(x)
                self.seed_index += 1
        return False
