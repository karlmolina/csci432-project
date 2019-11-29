from k_means import KMeans
import random

def setup():
    # random.seed(1)
    # random.seed(6)
    random.seed(6)
    size(600, 600)
    pixelDensity(2)
    # noFill()
    background(0)
    stroke(255)
    noStroke()
    colorMode(HSB)
    frameRate(1)
    
    data = load_data('../generate_convex_clusters/data/without_noise.csv')
    global k_means
    k_means = KMeans(data, 3, 0.01)
    k_means.initialize_centroids()
    
def draw():
    global k_means
    if not k_means.is_converged():
        background(0)
        k_means.assign_data()
        
        k_means.show_points()
        k_means.show_centroids()
    
        k_means.move_centroids()
        
    
    # print(k_means.centroids)
    
def load_data(filename):
    data = []
    for line in loadStrings(filename):
        x = line.split(',')
        x = [int(a) for a in x]
        data.append(x)
    
    return data
