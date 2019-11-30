from dbscan import Dbscan
import time

background_color = 255

def setup():
    # random.seed(1)
    # random.seed(6)
    # random.seed(6)
    size(600, 600)
    pixelDensity(2)
    # noFill()
    background(background_color)
    stroke(255)
    noStroke()
    colorMode(HSB)
    
    data = load_data('../generate_clusters/data/with_noise.csv')
    global dbscan
    dbscan = Dbscan(data, 5, 20)
    print(len(data))
    print(len(dbscan.labels))
    
def draw():
    global dbscan
    
    background(255)
    dbscan.show_points()
    noFill()
    stroke(0)
    ellipse(mouseX, mouseY, dbscan.eps *2, dbscan.eps *2)
    noStroke()
    
    
    if dbscan.index == len(dbscan.data):
        dbscan.state = 2
        return
    
    if dbscan.state == 0:
        if dbscan.labels[dbscan.index] is not None:
            dbscan.index += 1
            return
        neighbors = dbscan.neighbors(dbscan.data[dbscan.index])
        if len(neighbors) < dbscan.min_pts:
            dbscan.labels[dbscan.index] = 'noise'
            dbscan.index += 1
            return
        dbscan.cluster_label += 1
        dbscan.labels[dbscan.index] = dbscan.cluster_label
        dbscan.seed_list = neighbors
        dbscan.state = 1
        dbscan.index += 1
    elif dbscan.state == 1:
        if dbscan.seed_index == len(dbscan.seed_list):
            dbscan.seed_index = 0
            dbscan.state = 0
            return
        index = dbscan.seed_list[dbscan.seed_index]
        if dbscan.labels[index] == 'noise':
            dbscan.labels[index] = dbscan.cluster_label
        if dbscan.labels[index] is not None:
            dbscan.seed_index += 1
            return
        dbscan.labels[index] = dbscan.cluster_label
        neighbors = dbscan.neighbors(dbscan.data[index])
        if len(neighbors) >= dbscan.min_pts:
            s = set(neighbors)
            for x in s:
                if x not in set(dbscan.seed_list):
                    dbscan.seed_list.append(x)
        dbscan.seed_index += 1
        
    
    
    
def load_data(filename):
    data = []
    for line in loadStrings(filename):
        x = line.split(',')
        x = [int(a) for a in x]
        data.append(x)
    
    return data
